"""Unit tests for solarapi.py and solarfunc.py.

Run from the project directory with:

    python -m unittest -v test_solarapi_updated.py

The astronomy dependencies are mocked so the tests are deterministic.  The
coordinate-facing API contract tested here is:

* Moon requests return one angle in degrees.
* Planet requests return one angle in degrees per selected body.
* Jupiter-moon requests return one angle in degrees per selected body.
* strip_z() and sv_to_coord() only extract an (x, y) pair.
* rect2polar() converts that pair to an angular position in degrees.
"""

from __future__ import annotations

import importlib
import importlib.util
import math
import sys
import types
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, call, patch


TEST_DIR = Path(__file__).resolve().parent
if str(TEST_DIR) not in sys.path:
    sys.path.insert(0, str(TEST_DIR))


def _install_stub_if_missing(module_name: str) -> None:
    """Allow solarfunc to import when optional third-party packages are absent."""
    try:
        importlib.import_module(module_name)
    except ModuleNotFoundError:
        sys.modules[module_name] = types.ModuleType(module_name)


_install_stub_if_missing("solarsystem")
_install_stub_if_missing("astronomy")

# unittest.mock.patch requires each patched attribute to already exist.
_ss_module = sys.modules["solarsystem"]
for _name in ("Moon", "Heliocentric", "Sunriseset"):
    if not hasattr(_ss_module, _name):
        setattr(_ss_module, _name, None)

_astronomy_module = sys.modules["astronomy"]
if not hasattr(_astronomy_module, "Time"):
    _astronomy_module.Time = SimpleNamespace(Make=None)
for _name in ("JupiterMoons", "Seasons"):
    if not hasattr(_astronomy_module, _name):
        setattr(_astronomy_module, _name, None)


def _load_module(module_name: str, candidates: list[str]):
    """Load the first available candidate under a stable import name."""
    source_path = next(
        (TEST_DIR / candidate for candidate in candidates if (TEST_DIR / candidate).exists()),
        None,
    )
    if source_path is None:
        expected = ", ".join(candidates)
        raise FileNotFoundError(f"Expected one of these files beside the tests: {expected}")

    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {source_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


# Numbered filenames are preferred here so this suite can be run directly
# against the files uploaded in this conversation. Canonical project filenames
# remain supported when the test file is copied into the real project folder.
solarfunc = _load_module(
    "solarfunc",
    ["solarfunc(2).py", "solarfunc.py", "solarfunc(1).py"],
)
solarapi = _load_module(
    "solarapi",
    ["solarapi(1).py", "solarapi.py"],
)

Request = solarapi.Request
handle_request = solarapi.handle_request


def polar_degrees(x: float, y: float) -> float:
    """Return the standard polar-plane direction in degrees."""
    return math.degrees(math.atan2(y, x))


class RequestInitializationTests(unittest.TestCase):
    """Request construction with supplied and default values."""

    def test_typical_request_stores_all_supplied_values(self):
        req = Request("planets", 2026, 7, 16, 8, 30, "Mars")

        self.assertEqual(req.request, "planets")
        self.assertEqual(req.year, 2026)
        self.assertEqual(req.month, 7)
        self.assertEqual(req.day, 16)
        self.assertEqual(req.hour, 8)
        self.assertEqual(req.minute, 30)
        self.assertEqual(req.target, "Mars")
        self.assertEqual(req.response, 400)
        self.assertEqual(req.payload, [])

    def test_default_date_and_time_values(self):
        req = Request("equinox", 2026)

        self.assertEqual((req.month, req.day, req.hour, req.minute), (1, 1, 12, 0))
        self.assertIsNone(req.target)
        self.assertEqual(req.response, 400)
        self.assertEqual(req.payload, [])


class HandleRequestTypicalUseTests(unittest.TestCase):
    """Normal successful requests for every API operation."""

    def assert_success(self, result, expected_payload):
        self.assertEqual(result.response, 200)
        self.assertEqual(result.error, "None")
        self.assertEqual(result.payload, expected_payload)

    @patch("solarapi.sf.moonphase", return_value=["Waxing", "Crescent"])
    def test_moonphase_request_ignores_case_and_whitespace(self, mock_moonphase):
        req = Request("  MoonPhase  ", 2026, 7, 16, 9, 45)

        result = handle_request(req)

        self.assertIs(result, req)
        self.assert_success(result, ["Waxing", "Crescent"])
        mock_moonphase.assert_called_once_with(2026, 7, 16, 9, 45)

    @patch("solarapi.sf.moon", return_value=-72.5)
    def test_moon_request_returns_one_degree_angle(self, mock_moon):
        req = Request("moon", 2025, 12, 31, 23, 59)

        result = handle_request(req)

        self.assert_success(result, -72.5)
        self.assertIsInstance(result.payload, float)
        mock_moon.assert_called_once_with(2025, 12, 31, 23, 59)

    @patch(
        "solarapi.sf.rect2polar",
        side_effect=lambda coords: polar_degrees(coords[0], coords[1]),
    )
    @patch("solarapi.sf.strip_z", side_effect=lambda coords: (coords[0], coords[1]))
    @patch(
        "solarapi.sf.planets",
        return_value={
            "Mercury": (1, 2, 3),
            "Earth": (4, 5, 6),
            "Mars": (7, 8, 9),
        },
    )
    def test_planets_without_target_returns_degree_angle_for_each_body(
        self, mock_planets, mock_strip_z, mock_rect2polar
    ):
        req = Request("planets", 2026, 1, 2, 3, 4)

        result = handle_request(req)

        self.assert_success(
            result,
            {
                "Mercury": polar_degrees(1, 2),
                "Earth": polar_degrees(4, 5),
                "Mars": polar_degrees(7, 8),
            },
        )
        self.assertTrue(all(isinstance(angle, float) for angle in result.payload.values()))
        mock_planets.assert_called_once_with(2026, 1, 2, 3, 4)
        self.assertEqual(
            mock_strip_z.call_args_list,
            [call((1, 2, 3)), call((4, 5, 6)), call((7, 8, 9))],
        )
        self.assertEqual(
            mock_rect2polar.call_args_list,
            [call((1, 2)), call((4, 5)), call((7, 8))],
        )

    @patch("solarapi.sf.rect2polar", return_value=48.8140748343)
    @patch("solarapi.sf.strip_z", return_value=(7, 8))
    @patch("solarapi.sf.planets", return_value={"Mars": (7, 8, 9)})
    def test_planet_target_returns_only_degree_angle(
        self, mock_planets, mock_strip_z, mock_rect2polar
    ):
        req = Request("planets", 2026, 7, 16, target="  mArS  ")

        result = handle_request(req)

        self.assert_success(result, 48.8140748343)
        self.assertIsInstance(result.payload, float)
        mock_planets.assert_called_once_with(2026, 7, 16, 12, 0)
        mock_strip_z.assert_called_once_with((7, 8, 9))
        mock_rect2polar.assert_called_once_with((7, 8))

    @patch("solarapi.sf.sunriseSet", return_value=(5.25, 20.10))
    def test_sunrise_sunset_request(self, mock_sunrise_set):
        result = handle_request(Request("sunriseset", 2026, 7, 16))

        self.assert_success(result, (5.25, 20.10))
        mock_sunrise_set.assert_called_once_with(2026, 7, 16)

    @patch(
        "solarapi.sf.rect2polar",
        side_effect=lambda coords: polar_degrees(coords[0], coords[1]),
    )
    @patch("solarapi.sf.sv_to_coord", side_effect=lambda state: (state.x, state.y))
    @patch("solarapi.sf.JMoons")
    def test_jmoons_without_target_returns_degree_angle_for_each_moon(
        self, mock_jmoons, mock_sv_to_coord, mock_rect2polar
    ):
        moons = SimpleNamespace(
            io=SimpleNamespace(x=1, y=2),
            europa=SimpleNamespace(x=3, y=4),
            ganymede=SimpleNamespace(x=5, y=6),
            callisto=SimpleNamespace(x=7, y=8),
        )
        mock_jmoons.return_value = moons

        result = handle_request(Request("jmoons", 2026, 7, 16, 10, 15))

        self.assert_success(
            result,
            {
                "Io": polar_degrees(1, 2),
                "Europa": polar_degrees(3, 4),
                "Ganymede": polar_degrees(5, 6),
                "Callisto": polar_degrees(7, 8),
            },
        )
        self.assertTrue(all(isinstance(angle, float) for angle in result.payload.values()))
        mock_jmoons.assert_called_once_with(2026, 7, 16, 10, 15)
        self.assertEqual(
            mock_sv_to_coord.call_args_list,
            [call(moons.io), call(moons.europa), call(moons.ganymede), call(moons.callisto)],
        )
        self.assertEqual(
            mock_rect2polar.call_args_list,
            [call((1, 2)), call((3, 4)), call((5, 6)), call((7, 8))],
        )

    @patch("solarapi.sf.rect2polar", return_value=53.1301023542)
    @patch("solarapi.sf.sv_to_coord", return_value=(3, 4))
    @patch("solarapi.sf.JMoons")
    def test_jmoon_target_accepts_whitespace_and_mixed_case(
        self, mock_jmoons, mock_sv_to_coord, mock_rect2polar
    ):
        europa = SimpleNamespace(x=3, y=4)
        mock_jmoons.return_value = SimpleNamespace(europa=europa)

        result = handle_request(Request("jmoons", 2026, target="  EuRoPa  "))

        self.assert_success(result, 53.1301023542)
        self.assertIsInstance(result.payload, float)
        mock_sv_to_coord.assert_called_once_with(europa)
        mock_rect2polar.assert_called_once_with((3, 4))

    @patch("solarapi.sf.Equinox")
    def test_equinox_without_target_returns_all_four_events(self, mock_equinox):
        seasons = SimpleNamespace(
            mar_equinox="March result",
            jun_solstice="June result",
            sep_equinox="September result",
            dec_solstice="December result",
        )
        mock_equinox.return_value = seasons

        result = handle_request(Request("equinox", 2026))

        self.assert_success(
            result,
            {
                "March Equinox": "March result",
                "June Solstice": "June result",
                "September Equinox": "September result",
                "December Solstice": "December result",
            },
        )
        mock_equinox.assert_called_once_with(2026)

    @patch("solarapi.sf.Equinox")
    def test_each_valid_equinox_target_ignores_case_and_whitespace(self, mock_equinox):
        mock_equinox.return_value = SimpleNamespace(
            mar_equinox="MAR",
            jun_solstice="JUN",
            sep_equinox="SEP",
            dec_solstice="DEC",
        )
        cases = {
            " march ": "MAR",
            "JUNE": "JUN",
            " September ": "SEP",
            "december": "DEC",
        }

        for target, expected in cases.items():
            with self.subTest(target=target):
                result = handle_request(Request("equinox", 2026, target=target))
                self.assert_success(result, expected)


class HandleRequestAtypicalUseTests(unittest.TestCase):
    """Invalid inputs, missing targets, and dependency failures."""

    @patch("solarapi.sf.planets", return_value={"Earth": (1, 2, 3)})
    def test_unknown_planet_returns_404(self, _mock_planets):
        result = handle_request(Request("planets", 2026, target="Vulcan"))

        self.assertEqual(result.response, 404)
        self.assertEqual(result.error, "Planet not found")
        self.assertEqual(result.payload, [])

    @patch("solarapi.sf.JMoons", return_value=SimpleNamespace())
    def test_unknown_jupiter_moon_returns_404(self, _mock_jmoons):
        result = handle_request(Request("jmoons", 2026, target="Titan"))

        self.assertEqual(result.response, 404)
        self.assertEqual(result.error, "Jupiter moon not found")
        self.assertEqual(result.payload, [])

    @patch("solarapi.sf.Equinox", return_value=SimpleNamespace())
    def test_invalid_equinox_month_returns_404(self, _mock_equinox):
        result = handle_request(Request("equinox", 2026, target="January"))

        self.assertEqual(result.response, 404)
        self.assertEqual(result.error, "Invalid month")
        self.assertEqual(result.payload, [])

    def test_unknown_request_type_returns_404(self):
        result = handle_request(Request("asteroids", 2026))

        self.assertEqual(result.response, 404)
        self.assertEqual(result.error, "Unknown request type")
        self.assertEqual(result.payload, [])

    def test_empty_or_whitespace_request_returns_404(self):
        for request_type in ("", "   "):
            with self.subTest(request_type=request_type):
                result = handle_request(Request(request_type, 2026))
                self.assertEqual(result.response, 404)
                self.assertEqual(result.error, "Unknown request type")

    def test_non_string_request_is_converted_to_500_response(self):
        result = handle_request(Request(None, 2026))

        self.assertEqual(result.response, 500)
        self.assertIn("strip", result.error)
        self.assertEqual(result.payload, [])

    @patch("solarapi.sf.moon", side_effect=ValueError("invalid date"))
    def test_helper_exception_is_converted_to_500_response(self, _mock_moon):
        result = handle_request(Request("moon", 2026, 2, 30))

        self.assertEqual(result.response, 500)
        self.assertEqual(result.error, "invalid date")
        self.assertEqual(result.payload, [])

    @patch("solarapi.sf.JMoons")
    def test_non_string_jupiter_moon_target_returns_500(self, mock_jmoons):
        mock_jmoons.return_value = SimpleNamespace()

        result = handle_request(Request("jmoons", 2026, target=123))

        self.assertEqual(result.response, 500)
        self.assertIn("strip", result.error)
        self.assertEqual(result.payload, [])


class SolarFuncCoordinateHelperTests(unittest.TestCase):
    """Coordinate extraction and angular conversion helpers."""

    def test_strip_z_returns_xy_pair(self):
        self.assertEqual(solarfunc.strip_z((10, 20, 30)), (10, 20))

    def test_strip_z_ignores_z_and_additional_coordinates(self):
        self.assertEqual(solarfunc.strip_z((1, 2, 300, 400, 500)), (1, 2))

    def test_strip_z_rejects_too_short_sequence(self):
        with self.assertRaises(IndexError):
            solarfunc.strip_z((1,))

    def test_sv_to_coord_returns_xy_pair(self):
        state = SimpleNamespace(x=1.5, y=-2.5, z=99)
        self.assertEqual(solarfunc.sv_to_coord(state), (1.5, -2.5))

    def test_sv_to_coord_rejects_object_without_y(self):
        with self.assertRaises(AttributeError):
            solarfunc.sv_to_coord(SimpleNamespace(x=1))

    def test_rect2polar_returns_degree_angle_in_first_quadrant(self):
        self.assertAlmostEqual(solarfunc.rect2polar((3, 4)), 53.13010235415598)

    def test_rect2polar_returns_negative_degree_angle_below_x_axis(self):
        self.assertAlmostEqual(solarfunc.rect2polar((1, -1)), -45.0)

    def test_rect2polar_ignores_additional_coordinates(self):
        self.assertAlmostEqual(solarfunc.rect2polar((1, 1, 999)), 45.0)

    def test_rect2polar_rejects_too_short_sequence(self):
        with self.assertRaises(IndexError):
            solarfunc.rect2polar((1,))

    def test_rect2polar_should_preserve_second_quadrant(self):
        """Known issue: atan(y/x) loses quadrant information when x is negative."""
        self.assertAlmostEqual(solarfunc.rect2polar((-1, 1)), 135.0)

    def test_rect2polar_should_accept_vertical_vector(self):
        """Known issue: dividing by x fails for a vertical vector."""
        self.assertAlmostEqual(solarfunc.rect2polar((0, 1)), 90.0)


class SolarFuncGeneralHelperTests(unittest.TestCase):
    """Daylight-saving behavior and invalid date handling."""

    def test_daylight_savings_winter_is_zero(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 1, 15), 0)

    def test_daylight_savings_summer_is_one(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 7, 15), 1)

    def test_daylight_savings_rejects_invalid_date(self):
        with self.assertRaises(ValueError):
            solarfunc.daylightSavings(2026, 2, 30)


class SolarFuncAstronomyWrapperTests(unittest.TestCase):
    """Verify wrapper calls and return-value transformations."""

    @patch("solarfunc.daylightSavings", return_value=1)
    @patch("solarfunc.ss.Moon")
    def test_moonphase_classifies_typical_phases(self, mock_moon_class, _mock_dst):
        cases = [
            (0.25, 0.20, ["Waxing", "Crescent"]),
            (0.75, 0.80, ["Waning", "Gibbous"]),
            (0.50, 0.40, ["Waxing", "Half Moon"]),
            (0.05, 0.04, ["Waxing", "New Moon"]),
            (1.00, 0.99, ["Waxing", "Full Moon"]),
        ]

        for current_phase, previous_phase, expected in cases:
            with self.subTest(current=current_phase, previous=previous_phase):
                current = MagicMock()
                current.phase.return_value = current_phase
                previous = MagicMock()
                previous.phase.return_value = previous_phase
                mock_moon_class.side_effect = [current, previous]

                result = solarfunc.moonphase(2026, 7, 16, 12, 0)

                self.assertEqual(result, expected)
                self.assertEqual(mock_moon_class.call_count, 2)
                mock_moon_class.reset_mock(side_effect=True)

    @patch("solarfunc.daylightSavings", return_value=1)
    @patch("solarfunc.ss.Moon")
    def test_moon_returns_second_position_value_as_degrees(
        self, mock_moon_class, _mock_dst
    ):
        moon_instance = mock_moon_class.return_value
        moon_instance.position.return_value = (12.5, math.pi / 3, -4.0)

        result = solarfunc.moon(2026, 7, 16, 6, 30)

        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 60.0)
        mock_moon_class.assert_called_once_with(
            2026, 7, 16, 6, 30, -5, 1, -71.0571, 42.3611, True
        )
        moon_instance.position.assert_called_once_with()

    @patch("solarfunc.ss.Heliocentric")
    def test_planets_returns_library_dictionary(self, mock_heliocentric):
        expected = {"Earth": (1, 2, 3), "Mars": (4, 5, 6)}
        mock_heliocentric.return_value.planets.return_value = expected

        result = solarfunc.planets(2026, 7, 16, 8, 45)

        self.assertIs(result, expected)
        mock_heliocentric.assert_called_once_with(
            2026, 7, 16, 8, 45, 0, 0, "rectangular", True
        )

    @patch("solarfunc.daylightSavings", return_value=1)
    @patch("solarfunc.ss.Sunriseset")
    def test_sunrise_set_returns_library_result(self, mock_sun_class, _mock_dst):
        mock_sun_class.return_value.riseset.return_value = (5.5, 20.25)

        result = solarfunc.sunriseSet(2026, 7, 16)

        self.assertEqual(result, (5.5, 20.25))
        mock_sun_class.assert_called_once_with(
            2026, 7, 16, -5, 1, -71.0571, 42.3611
        )

    @patch("solarfunc.astronomy.JupiterMoons", return_value="moon data")
    @patch("solarfunc.astronomy.Time.Make", return_value="time object")
    def test_jmoons_builds_time_then_gets_moon_data(
        self, mock_time_make, mock_jupiter_moons
    ):
        result = solarfunc.JMoons(2026, 7, 16, 9, 15)

        self.assertEqual(result, "moon data")
        mock_time_make.assert_called_once_with(2026, 7, 16, 9, 15, 0)
        mock_jupiter_moons.assert_called_once_with("time object")

    @patch("solarfunc.astronomy.Seasons", return_value="season data")
    def test_equinox_returns_season_data(self, mock_seasons):
        self.assertEqual(solarfunc.Equinox(2026), "season data")
        mock_seasons.assert_called_once_with(2026)

    @patch("solarfunc.daylightSavings", return_value=0)
    @patch("solarfunc.ss.Moon")
    def test_moonphase_on_first_day_uses_previous_calendar_date(
        self, mock_moon_class, _mock_dst
    ):
        current = MagicMock()
        current.phase.return_value = 0.5
        previous = MagicMock()
        previous.phase.return_value = 0.5
        mock_moon_class.side_effect = [current, previous]

        result = solarfunc.moonphase(2026, 3, 1, 12, 0)

        self.assertEqual(result, ["Waning", "Half Moon"])
        self.assertEqual(mock_moon_class.call_count, 2)
        current_call, previous_call = mock_moon_class.call_args_list
        self.assertEqual(current_call.args[:5], (2026, 3, 1, 12, 0))
        self.assertEqual(previous_call.args[:5], (2026, 2, 28, 12, 0))

    @patch("solarfunc.daylightSavings", return_value=0)
    @patch("solarfunc.ss.Moon")
    def test_moonphase_on_january_first_uses_previous_year(
        self, mock_moon_class, _mock_dst
    ):
        current = MagicMock()
        current.phase.return_value = 0.25
        previous = MagicMock()
        previous.phase.return_value = 0.20
        mock_moon_class.side_effect = [current, previous]

        result = solarfunc.moonphase(2026, 1, 1, 0, 30)

        self.assertEqual(result, ["Waxing", "Crescent"])
        previous_call = mock_moon_class.call_args_list[1]
        self.assertEqual(previous_call.args[:5], (2025, 12, 31, 0, 30))


if __name__ == "__main__":
    unittest.main(verbosity=2)
