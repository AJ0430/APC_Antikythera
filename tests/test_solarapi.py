from __future__ import annotations

import unittest
from types import SimpleNamespace
from unittest.mock import patch

from Calculation_Stuff import solarapi


PLANETS = {
    "Mercury": (1.0, 0.0, 0.0),
    "Venus": (0.0, 2.0, 0.0),
    "Earth": (0.0, 3.0, 0.0),
    "Ceres": (4.0, 0.0, 0.0),
    "Chiron": (5.0, 0.0, 0.0),
    "Eris": (6.0, 0.0, 0.0),
}


def moon_states():
    return SimpleNamespace(
        io=SimpleNamespace(x=1, y=2),
        europa=SimpleNamespace(x=3, y=4),
        ganymede=SimpleNamespace(x=5, y=6),
        callisto=SimpleNamespace(x=7, y=8),
    )


def season_values():
    return SimpleNamespace(
        mar_equinox="March value",
        jun_solstice="June value",
        sep_equinox="September value",
        dec_solstice="December value",
    )


class RequestObjectTests(unittest.TestCase):
    def test_common_1_default_optional_fields(self):
        request = solarapi.Request("planets", 2026)
        self.assertEqual(request.request, "planets")
        self.assertEqual((request.month, request.day, request.hour, request.minute), (1, 1, 0, 0))
        self.assertEqual(request.response, 400)
        self.assertEqual(request.payload, [])
        self.assertIsNone(request.target)

    def test_common_2_explicit_fields_are_stored(self):
        request = solarapi.Request("moon", 2026, 8, 6, 14, 30, "target")
        self.assertEqual(
            (request.request, request.year, request.month, request.day, request.hour, request.minute, request.target),
            ("moon", 2026, 8, 6, 14, 30, "target"),
        )

    def test_uncommon_1_none_request_is_retained_for_handler_validation(self):
        request = solarapi.Request(None, 2026)
        self.assertIsNone(request.request)
        self.assertEqual(request.response, 400)
        self.assertEqual(request.payload, [])

    def test_uncommon_2_payload_lists_are_independent(self):
        first = solarapi.Request("moon", 2026)
        second = solarapi.Request("moon", 2026)
        first.payload.append("changed")
        self.assertEqual(first.payload, ["changed"])
        self.assertEqual(second.payload, [])


class HandleRequestTests(unittest.TestCase):
    def test_common_1_scalar_request_types_return_success(self):
        cases = [
            ("moonphase", ["Waxing", "Crescent"], "moonphase", (2026, 8, 6, 12, 30)),
            ("moon", 42.5, "moon", (2026, 8, 6, 12, 30)),
            ("sunriseset", (6.1, 19.8), "sunriseSet", (2026, 8, 6)),
        ]
        for request_name, payload, helper_name, expected_args in cases:
            with self.subTest(request=request_name):
                with patch.object(solarapi.sf, helper_name, return_value=payload) as helper:
                    result = solarapi.handle_request(
                        solarapi.Request(request_name, 2026, 8, 6, 12, 30)
                    )
                self.assertEqual(result.response, 200)
                self.assertEqual(result.error, "None")
                self.assertEqual(result.payload, payload)
                helper.assert_called_once_with(*expected_args)

    def test_common_2_collection_and_target_requests_return_success(self):
        def polar(coord):
            x, y = coord
            return [0.0, (x * x + y * y) ** 0.5]

        with self.subTest(request="all planets"):
            with patch.object(solarapi.sf, "planets", return_value=dict(PLANETS)), patch.object(
                solarapi.sf, "strip_z", side_effect=lambda value: value[:2]
            ), patch.object(solarapi.sf, "rect2polar", side_effect=polar):
                result = solarapi.handle_request(solarapi.Request("planets", 2026))
            self.assertEqual(set(result.payload), {"Mercury", "Venus", "Earth"})
            self.assertAlmostEqual(result.payload["Mercury"][1], 25.0)
            self.assertAlmostEqual(result.payload["Venus"][1], 162.5)
            self.assertAlmostEqual(result.payload["Earth"][1], 300.0)

        with self.subTest(request="target planet"):
            with patch.object(solarapi.sf, "planets", return_value=dict(PLANETS)), patch.object(
                solarapi.sf, "strip_z", side_effect=lambda value: value[:2]
            ), patch.object(solarapi.sf, "rect2polar", return_value=[90.0, 3.0]):
                result = solarapi.handle_request(
                    solarapi.Request("planets", 2026, target="Earth")
                )
            self.assertEqual((result.response, result.payload), (200, [90.0, 3.0]))

        with self.subTest(request="all Jupiter moons"):
            with patch.object(solarapi.sf, "JMoons", return_value=moon_states()), patch.object(
                solarapi.sf, "sv_to_coord", side_effect=lambda state: (state.x, state.y)
            ), patch.object(solarapi.sf, "rect2polar", side_effect=lambda coord: [coord[0], coord[1]]):
                result = solarapi.handle_request(solarapi.Request("jmoons", 2026))
            self.assertEqual(
                result.payload,
                {"Io": [1, 2], "Europa": [3, 4], "Ganymede": [5, 6], "Callisto": [7, 8]},
            )

        with self.subTest(request="target Jupiter moon"):
            with patch.object(solarapi.sf, "JMoons", return_value=moon_states()), patch.object(
                solarapi.sf, "sv_to_coord", side_effect=lambda state: (state.x, state.y)
            ), patch.object(solarapi.sf, "rect2polar", return_value=[63.4, 2.24]):
                result = solarapi.handle_request(
                    solarapi.Request("jmoons", 2026, target="Io")
                )
            self.assertEqual((result.response, result.payload), (200, [63.4, 2.24]))

        with self.subTest(request="all equinoxes"):
            with patch.object(solarapi.sf, "Equinox", return_value=season_values()):
                result = solarapi.handle_request(solarapi.Request("equinox", 2026))
            self.assertEqual(
                result.payload,
                {
                    "March Equinox": "March value",
                    "June Solstice": "June value",
                    "September Equinox": "September value",
                    "December Solstice": "December value",
                },
            )

        with self.subTest(request="target equinox"):
            with patch.object(solarapi.sf, "Equinox", return_value=season_values()):
                result = solarapi.handle_request(
                    solarapi.Request("equinox", 2026, target="September")
                )
            self.assertEqual((result.response, result.payload), (200, "September value"))

    def test_uncommon_1_whitespace_case_and_invalid_targets(self):
        with self.subTest(case="request name whitespace and case"):
            with patch.object(solarapi.sf, "moonphase", return_value=["Waxing", "Crescent"]):
                result = solarapi.handle_request(
                    solarapi.Request("  MOONPHASE ", 2026, 8, 6, 12, 30)
                )
            self.assertEqual((result.response, result.payload), (200, ["Waxing", "Crescent"]))

        with self.subTest(case="target whitespace and case"):
            with patch.object(solarapi.sf, "planets", return_value=dict(PLANETS)), patch.object(
                solarapi.sf, "strip_z", side_effect=lambda value: value[:2]
            ), patch.object(solarapi.sf, "rect2polar", return_value=[90.0, 3.0]):
                result = solarapi.handle_request(
                    solarapi.Request("planets", 2026, target=" earth ")
                )
            self.assertEqual(result.response, 200)

        error_cases = [
            ("planets", "Vulcan", "Planet not found"),
            ("jmoons", "Amalthea", "Jupiter moon not found"),
            ("equinox", "January", "Invalid month"),
        ]
        for request_name, target, expected_error in error_cases:
            with self.subTest(request=request_name, target=target):
                patches = []
                if request_name == "planets":
                    patches.append(patch.object(solarapi.sf, "planets", return_value=dict(PLANETS)))
                elif request_name == "jmoons":
                    patches.append(patch.object(solarapi.sf, "JMoons", return_value=moon_states()))
                else:
                    patches.append(patch.object(solarapi.sf, "Equinox", return_value=season_values()))
                with patches[0]:
                    result = solarapi.handle_request(
                        solarapi.Request(request_name, 2026, target=target)
                    )
                self.assertEqual(result.response, 404)
                self.assertEqual(result.error, expected_error)

        with self.subTest(case="unknown request"):
            result = solarapi.handle_request(solarapi.Request("not-a-command", 2026))
            self.assertEqual((result.response, result.error), (404, "Unknown request type"))

    def test_uncommon_2_exceptions_and_malformed_requests_become_500(self):
        with self.subTest(case="helper exception"):
            with patch.object(
                solarapi.sf, "moonphase", side_effect=RuntimeError("calculation failed")
            ):
                result = solarapi.handle_request(solarapi.Request("moonphase", 2026))
            self.assertEqual((result.response, result.error, result.payload), (500, "calculation failed", []))

        with self.subTest(case="non-string request"):
            result = solarapi.handle_request(solarapi.Request(None, 2026))
            self.assertEqual(result.response, 500)
            self.assertEqual(result.payload, [])

        with self.subTest(case="missing minor-body dictionary keys"):
            with patch.object(solarapi.sf, "planets", return_value={"Earth": (1, 0, 0)}):
                result = solarapi.handle_request(solarapi.Request("planets", 2026))
            self.assertEqual(result.response, 500)
            self.assertEqual(result.payload, [])

        with self.subTest(case="identical planet radii"):
            equal_radius_planets = {
                "Mercury": (1, 0, 0),
                "Venus": (0, 1, 0),
                "Earth": (-1, 0, 0),
                "Ceres": (2, 0, 0),
                "Chiron": (3, 0, 0),
                "Eris": (4, 0, 0),
            }
            with patch.object(solarapi.sf, "planets", return_value=equal_radius_planets), patch.object(
                solarapi.sf, "strip_z", side_effect=lambda value: value[:2]
            ), patch.object(solarapi.sf, "rect2polar", return_value=[0.0, 1.0]):
                result = solarapi.handle_request(solarapi.Request("planets", 2026))
            self.assertEqual(result.response, 500)
            self.assertEqual(result.payload, [])


if __name__ == "__main__":
    unittest.main()
