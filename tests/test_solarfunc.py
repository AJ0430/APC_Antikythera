from __future__ import annotations

import math
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from Calculation_Stuff import solarfunc


class Rect2PolarTests(unittest.TestCase):
    def test_common_1_first_quadrant_coordinate(self):
        angle, radius = solarfunc.rect2polar((3, 4))
        self.assertAlmostEqual(angle, 53.13010235415598)
        self.assertAlmostEqual(radius, 5.0)

    def test_common_2_second_quadrant_coordinate(self):
        angle, radius = solarfunc.rect2polar((-3, 4))
        self.assertAlmostEqual(angle, 126.86989764584402)
        self.assertAlmostEqual(radius, 5.0)

    def test_uncommon_1_origin_has_zero_angle_and_radius(self):
        self.assertEqual(solarfunc.rect2polar((0, 0)), [0.0, 0.0])

    def test_uncommon_2_negative_float_coordinate(self):
        angle, radius = solarfunc.rect2polar((-1.5, -2.0))
        self.assertAlmostEqual(angle, -126.86989764584402)
        self.assertAlmostEqual(radius, 2.5)


class StripZTests(unittest.TestCase):
    def test_common_1_three_dimensional_tuple(self):
        self.assertEqual(solarfunc.strip_z((1, 2, 3)), (1, 2))

    def test_common_2_three_dimensional_list(self):
        self.assertEqual(solarfunc.strip_z([4.5, -6.25, 9]), (4.5, -6.25))

    def test_uncommon_1_two_dimensional_input(self):
        self.assertEqual(solarfunc.strip_z((8, 9)), (8, 9))

    def test_uncommon_2_additional_dimensions_are_ignored(self):
        self.assertEqual(solarfunc.strip_z((1, 2, 3, 4, 5)), (1, 2))


class StateVectorToCoordinateTests(unittest.TestCase):
    def test_common_1_integer_state_vector(self):
        state = SimpleNamespace(x=12, y=-8, z=99)
        self.assertEqual(solarfunc.sv_to_coord(state), (12, -8))

    def test_common_2_float_state_vector(self):
        state = SimpleNamespace(x=12.5, y=-8.25, z=0.0)
        self.assertEqual(solarfunc.sv_to_coord(state), (12.5, -8.25))

    def test_uncommon_1_zero_coordinates(self):
        state = SimpleNamespace(x=0, y=0)
        self.assertEqual(solarfunc.sv_to_coord(state), (0, 0))

    def test_uncommon_2_extra_state_fields_are_ignored(self):
        state = SimpleNamespace(x=-1, y=2, z=3, vx=4, vy=5, vz=6)
        self.assertEqual(solarfunc.sv_to_coord(state), (-1, 2))


class DaylightSavingsTests(unittest.TestCase):
    def test_common_1_winter_is_standard_time(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 1, 15), 0)

    def test_common_2_summer_is_daylight_time(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 7, 15), 1)

    def test_uncommon_1_just_before_spring_transition(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 3, 8, 1, 59), 0)

    def test_uncommon_2_just_after_spring_transition(self):
        self.assertEqual(solarfunc.daylightSavings(2026, 3, 8, 3, 1), 1)


class MoonPhaseTests(unittest.TestCase):
    @staticmethod
    def moon_with_phase(value):
        moon = MagicMock()
        moon.phase.return_value = value
        return moon

    def test_common_1_waxing_gibbous(self):
        current = self.moon_with_phase(0.75)
        previous = self.moon_with_phase(0.70)
        with patch.object(solarfunc.ss, "Moon", side_effect=[current, previous]):
            self.assertEqual(solarfunc.moonphase(2026, 8, 6), ["Waxing", "Gibbous"])

    def test_common_2_waning_crescent(self):
        current = self.moon_with_phase(0.25)
        previous = self.moon_with_phase(0.30)
        with patch.object(solarfunc.ss, "Moon", side_effect=[current, previous]):
            self.assertEqual(solarfunc.moonphase(2026, 8, 6), ["Waning", "Crescent"])

    def test_uncommon_1_exact_half_moon_and_month_rollover(self):
        current = self.moon_with_phase(0.50)
        previous = self.moon_with_phase(0.40)
        with patch.object(solarfunc.ss, "Moon", side_effect=[current, previous]) as constructor:
            result = solarfunc.moonphase(2026, 3, 1, 0, 0)
        self.assertEqual(result, ["Waxing", "Half Moon"])
        self.assertEqual(constructor.call_args_list[1].args[:5], (2026, 2, 28, 0, 0))

    def test_uncommon_2_new_and_full_moon_boundaries(self):
        cases = [
            (0.02, 0.03, ["Waning", "New Moon"]),
            (1.00, 0.99, ["Waxing", "Full Moon"]),
        ]
        for current_value, previous_value, expected in cases:
            with self.subTest(current=current_value):
                current = self.moon_with_phase(current_value)
                previous = self.moon_with_phase(previous_value)
                with patch.object(solarfunc.ss, "Moon", side_effect=[current, previous]):
                    self.assertEqual(solarfunc.moonphase(2026, 8, 6), expected)


class MoonPositionTests(unittest.TestCase):
    def test_common_1_explicit_time_returns_degrees(self):
        moon_info = MagicMock()
        moon_info.position.return_value = (99, math.pi / 2, 123)
        with patch.object(solarfunc, "daylightSavings", return_value=1), patch.object(
            solarfunc.ss, "Moon", return_value=moon_info
        ) as constructor:
            result = solarfunc.moon(2026, 8, 6, 14, 30)
        self.assertAlmostEqual(result, 90.0)
        constructor.assert_called_once_with(
            2026, 8, 6, 14, 30, -5, 1, -71.0571, 42.3611, True
        )

    def test_common_2_default_time_is_noon(self):
        moon_info = MagicMock()
        moon_info.position.return_value = (1, math.pi, 3)
        with patch.object(solarfunc, "daylightSavings", return_value=0), patch.object(
            solarfunc.ss, "Moon", return_value=moon_info
        ) as constructor:
            result = solarfunc.moon(2026, 1, 15)
        self.assertAlmostEqual(result, 180.0)
        self.assertEqual(constructor.call_args.args[:5], (2026, 1, 15, 12, 0))

    def test_uncommon_1_negative_position_angle(self):
        moon_info = MagicMock()
        moon_info.position.return_value = (4, -math.pi / 4, 999)
        with patch.object(solarfunc, "daylightSavings", return_value=1), patch.object(
            solarfunc.ss, "Moon", return_value=moon_info
        ):
            self.assertAlmostEqual(solarfunc.moon(2026, 8, 6), -45.0)

    def test_uncommon_2_library_exception_propagates(self):
        with patch.object(solarfunc, "daylightSavings", return_value=1), patch.object(
            solarfunc.ss, "Moon", side_effect=ValueError("invalid date")
        ):
            with self.assertRaisesRegex(ValueError, "invalid date"):
                solarfunc.moon(2026, 13, 1)


class PlanetAdapterTests(unittest.TestCase):
    def test_common_1_explicit_time_delegates_to_model(self):
        model = MagicMock()
        model.planets.return_value = {"Earth": (1, 2, 3)}
        with patch.object(solarfunc.ss, "Heliocentric", return_value=model) as constructor:
            result = solarfunc.planets(2026, 8, 6, 10, 15)
        self.assertEqual(result, {"Earth": (1, 2, 3)})
        constructor.assert_called_once_with(2026, 8, 6, 10, 15, 0, 0, "rectangular", True)

    def test_common_2_default_time_is_noon(self):
        model = MagicMock()
        model.planets.return_value = {"Mars": (4, 5, 6)}
        with patch.object(solarfunc.ss, "Heliocentric", return_value=model) as constructor:
            self.assertEqual(solarfunc.planets(2026, 8, 6), {"Mars": (4, 5, 6)})
        self.assertEqual(constructor.call_args.args[:5], (2026, 8, 6, 12, 0))

    def test_uncommon_1_empty_result_is_returned_unchanged(self):
        model = MagicMock()
        model.planets.return_value = {}
        with patch.object(solarfunc.ss, "Heliocentric", return_value=model):
            self.assertEqual(solarfunc.planets(2026, 8, 6), {})

    def test_uncommon_2_library_exception_propagates(self):
        with patch.object(solarfunc.ss, "Heliocentric", side_effect=RuntimeError("model failed")):
            with self.assertRaisesRegex(RuntimeError, "model failed"):
                solarfunc.planets(2026, 8, 6)


class SunriseSetTests(unittest.TestCase):
    def test_common_1_summer_date_uses_daylight_time(self):
        model = MagicMock()
        model.riseset.return_value = (5.5, 20.25)
        with patch.object(solarfunc, "daylightSavings", return_value=1), patch.object(
            solarfunc.ss, "Sunriseset", return_value=model
        ) as constructor:
            result = solarfunc.sunriseSet(2026, 8, 6)
        self.assertEqual(result, (5.5, 20.25))
        constructor.assert_called_once_with(2026, 8, 6, -5, 1, -71.0571, 42.3611)

    def test_common_2_winter_date_uses_standard_time(self):
        model = MagicMock()
        model.riseset.return_value = (7.1, 16.4)
        with patch.object(solarfunc, "daylightSavings", return_value=0), patch.object(
            solarfunc.ss, "Sunriseset", return_value=model
        ) as constructor:
            self.assertEqual(solarfunc.sunriseSet(2026, 1, 15), (7.1, 16.4))
        self.assertEqual(constructor.call_args.args[4], 0)

    def test_uncommon_1_leap_day_is_forwarded(self):
        model = MagicMock()
        model.riseset.return_value = (6.0, 17.5)
        with patch.object(solarfunc, "daylightSavings", return_value=0), patch.object(
            solarfunc.ss, "Sunriseset", return_value=model
        ) as constructor:
            solarfunc.sunriseSet(2024, 2, 29)
        self.assertEqual(constructor.call_args.args[:3], (2024, 2, 29))

    def test_uncommon_2_library_exception_propagates(self):
        with patch.object(solarfunc, "daylightSavings", return_value=0), patch.object(
            solarfunc.ss, "Sunriseset", side_effect=ValueError("invalid date")
        ):
            with self.assertRaisesRegex(ValueError, "invalid date"):
                solarfunc.sunriseSet(2026, 2, 30)


class JupiterMoonAdapterTests(unittest.TestCase):
    def test_common_1_explicit_time_uses_astronomy_time(self):
        fake_time = object()
        fake_moons = object()
        with patch.object(solarfunc.astronomy.Time, "Make", return_value=fake_time) as make, patch.object(
            solarfunc.astronomy, "JupiterMoons", return_value=fake_moons
        ) as jupiter_moons:
            result = solarfunc.JMoons(2026, 8, 6, 3, 45)
        self.assertIs(result, fake_moons)
        make.assert_called_once_with(2026, 8, 6, 3, 45, 0)
        jupiter_moons.assert_called_once_with(fake_time)

    def test_common_2_default_time_is_noon(self):
        fake_time = object()
        with patch.object(solarfunc.astronomy.Time, "Make", return_value=fake_time) as make, patch.object(
            solarfunc.astronomy, "JupiterMoons", return_value="moons"
        ):
            self.assertEqual(solarfunc.JMoons(2026, 8, 6), "moons")
        make.assert_called_once_with(2026, 8, 6, 12, 0, 0)

    def test_uncommon_1_leap_day_is_forwarded(self):
        fake_time = object()
        with patch.object(solarfunc.astronomy.Time, "Make", return_value=fake_time) as make, patch.object(
            solarfunc.astronomy, "JupiterMoons", return_value=object()
        ):
            solarfunc.JMoons(2024, 2, 29, 23, 59)
        make.assert_called_once_with(2024, 2, 29, 23, 59, 0)

    def test_uncommon_2_time_creation_exception_propagates(self):
        with patch.object(solarfunc.astronomy.Time, "Make", side_effect=ValueError("bad time")):
            with self.assertRaisesRegex(ValueError, "bad time"):
                solarfunc.JMoons(2026, 13, 1)


class EquinoxAdapterTests(unittest.TestCase):
    def test_common_1_current_year_delegates_to_engine(self):
        seasons = object()
        with patch.object(solarfunc.astronomy, "Seasons", return_value=seasons) as seasons_fn:
            self.assertIs(solarfunc.Equinox(2026), seasons)
        seasons_fn.assert_called_once_with(2026)

    def test_common_2_different_year_is_forwarded(self):
        seasons = object()
        with patch.object(solarfunc.astronomy, "Seasons", return_value=seasons) as seasons_fn:
            self.assertIs(solarfunc.Equinox(2030), seasons)
        seasons_fn.assert_called_once_with(2030)

    def test_uncommon_1_earliest_datetime_year_is_forwarded(self):
        with patch.object(solarfunc.astronomy, "Seasons", return_value="seasons") as seasons_fn:
            self.assertEqual(solarfunc.Equinox(1), "seasons")
        seasons_fn.assert_called_once_with(1)

    def test_uncommon_2_engine_exception_propagates(self):
        with patch.object(solarfunc.astronomy, "Seasons", side_effect=RuntimeError("engine failed")):
            with self.assertRaisesRegex(RuntimeError, "engine failed"):
                solarfunc.Equinox(-1)


if __name__ == "__main__":
    unittest.main()
