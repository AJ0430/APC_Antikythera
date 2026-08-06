from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock

from tests.import_helpers import load_apc_functions_with_fake_database


class MonthConversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_apc_functions_with_fake_database()

    def test_common_1_january_converts_to_one(self):
        self.assertEqual(self.module.monthConversion("January"), 1)

    def test_common_2_july_converts_to_seven(self):
        self.assertEqual(self.module.monthConversion("July"), 7)

    def test_uncommon_1_wrong_case_returns_zero(self):
        self.assertEqual(self.module.monthConversion("january"), 0)

    def test_uncommon_2_unknown_or_none_returns_zero(self):
        for month in ("NotAMonth", "", None):
            with self.subTest(month=month):
                self.assertEqual(self.module.monthConversion(month), 0)


class CursorBackedTestCase(unittest.TestCase):
    def setUp(self):
        self.module = load_apc_functions_with_fake_database()
        self.cursor = MagicMock()
        self.module.cursor = self.cursor

    def call_quietly(self, function, *args):
        with redirect_stdout(io.StringIO()):
            return function(*args)


class ShowEclipsesTests(CursorBackedTestCase):
    def test_common_1_solar_eclipse_row_is_returned(self):
        row = ("Solar", "4/8/2024", "North America")
        self.cursor.fetchone.return_value = row
        result = self.call_quietly(self.module.showEclipses, "April", 8, 2024)
        self.assertEqual(result, row)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Eclipses WHERE DATE = ?", ["4/8/2024"]
        )

    def test_common_2_lunar_eclipse_row_is_returned(self):
        row = ("Lunar", "8/28/2026", "North America")
        self.cursor.fetchone.return_value = row
        result = self.call_quietly(self.module.showEclipses, "August", 28, 2026)
        self.assertEqual(result, row)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Eclipses WHERE DATE = ?", ["8/28/2026"]
        )

    def test_uncommon_1_missing_date_returns_none(self):
        self.cursor.fetchone.return_value = None
        result = self.call_quietly(self.module.showEclipses, "January", 1, 2001)
        self.assertIsNone(result)

    def test_uncommon_2_unknown_month_queries_month_zero(self):
        self.cursor.fetchone.return_value = None
        result = self.call_quietly(self.module.showEclipses, "NotAMonth", 9, 2026)
        self.assertIsNone(result)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Eclipses WHERE DATE = ?", ["0/9/2026"]
        )


class ShowPlanetInfoTests(CursorBackedTestCase):
    def test_common_1_earth_row_is_returned(self):
        row = ("Earth", 6371, 5.97e24, "Terrestrial", 9.81, 15, 1, None, 1, 1)
        self.cursor.fetchone.return_value = row
        self.assertEqual(self.module.showPlanetInfo("Earth"), row)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Planets WHERE NAME = ?", ("Earth",)
        )

    def test_common_2_mars_row_is_returned(self):
        row = ("Mars", 3389.5, 6.42e23, "Terrestrial", 3.71, -65, 1.38, None, 2, 1.9)
        self.cursor.fetchone.return_value = row
        self.assertEqual(self.module.showPlanetInfo("Mars"), row)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Planets WHERE NAME = ?", ("Mars",)
        )

    def test_uncommon_1_missing_planet_returns_none(self):
        self.cursor.fetchone.return_value = None
        self.assertIsNone(self.module.showPlanetInfo("Vulcan"))

    def test_uncommon_2_quote_in_name_remains_parameterized(self):
        self.cursor.fetchone.return_value = None
        malicious_name = "Earth' OR 1=1 --"
        self.assertIsNone(self.module.showPlanetInfo(malicious_name))
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM Planets WHERE NAME = ?", (malicious_name,)
        )


class ShowMoonInfoTests(CursorBackedTestCase):
    def test_common_1_io_selects_io_row(self):
        self.cursor.fetchone.return_value = ("Io", 1821, 8.93e22, 1.796, None, "Jupiter")
        self.module.showMoonInfo("Io")
        self.cursor.execute.assert_called_once_with("SELECT * FROM Moons WHERE NAME = 'Io'")

    def test_common_2_europa_selects_europa_row(self):
        self.cursor.fetchone.return_value = ("Europa", 1560, 4.8e22, 1.315, None, "Jupiter")
        self.module.showMoonInfo("Europa")
        self.cursor.execute.assert_called_once_with("SELECT * FROM Moons WHERE NAME = 'Europa'")

    def test_uncommon_1_unknown_moon_does_not_query_database(self):
        self.assertIsNone(self.module.showMoonInfo("Amalthea"))
        self.cursor.execute.assert_not_called()
        self.cursor.fetchone.assert_not_called()

    @unittest.expectedFailure
    def test_uncommon_2_matching_row_should_be_returned(self):
        """Known defect: showMoonInfo fetches moonInfo but never returns it."""
        row = ("Io", 1821, 8.93e22, 1.796, None, "Jupiter")
        self.cursor.fetchone.return_value = row
        self.assertEqual(self.module.showMoonInfo("Io"), row)


class ShowSmallBodiesTests(CursorBackedTestCase):
    def test_common_1_visible_start_month_returns_name(self):
        self.cursor.fetchone.return_value = (
            "Neowise", "Comet", "Sky", 5, 10, "July", "August", 2020
        )
        result = self.call_quietly(self.module.showSmallbodies, "July", 2020)
        self.assertEqual(result, "Neowise")
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM SmallBodies WHERE (DATE_START = ? OR DATE_END = ?) AND YEAR = ?",
            ["July", "July", "2020"],
        )

    def test_common_2_visible_end_month_returns_name(self):
        self.cursor.fetchone.return_value = (
            "Neowise", "Comet", "Sky", 5, 10, "July", "August", 2020
        )
        result = self.call_quietly(self.module.showSmallbodies, "August", 2020)
        self.assertEqual(result, "Neowise")
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM SmallBodies WHERE (DATE_START = ? OR DATE_END = ?) AND YEAR = ?",
            ["August", "August", "2020"],
        )

    def test_uncommon_1_no_visible_body_returns_none(self):
        self.cursor.fetchone.return_value = None
        result = self.call_quietly(self.module.showSmallbodies, "March", 2026)
        self.assertIsNone(result)

    def test_uncommon_2_numeric_inputs_are_stringified(self):
        self.cursor.fetchone.return_value = None
        result = self.call_quietly(self.module.showSmallbodies, 7, "02020")
        self.assertIsNone(result)
        self.cursor.execute.assert_called_once_with(
            "SELECT * FROM SmallBodies WHERE (DATE_START = ? OR DATE_END = ?) AND YEAR = ?",
            ["7", "7", "02020"],
        )


if __name__ == "__main__":
    unittest.main()
