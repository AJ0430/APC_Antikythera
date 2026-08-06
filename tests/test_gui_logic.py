from __future__ import annotations

import math
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

from tests.import_helpers import FakeTurtleModule, has_top_level_call, load_ast_definitions

ROOT = Path(__file__).resolve().parents[1]
BASIC_GUI = ROOT / "GUI_Stuff" / "basicGUI.py"
MOON_GUI = ROOT / "GUI_Stuff" / "moonpopupgui.py"


class PositionSource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y


def load_planet_class(sun):
    return load_ast_definitions(
        BASIC_GUI,
        ["Planet"],
        {
            "turtle": FakeTurtleModule("fake_turtle"),
            "sunScreen": object(),
            "sunObject": sun,
            "cos": math.cos,
            "sin": math.sin,
        },
    )["Planet"]


def load_moon_class(parent):
    return load_ast_definitions(
        MOON_GUI,
        ["Moon"],
        {
            "turtle": FakeTurtleModule("fake_turtle"),
            "moonScreen": object(),
            "motherPlanet": parent,
            "cos": math.cos,
            "sin": math.sin,
        },
    )["Moon"]


class PlanetMovementTests(unittest.TestCase):
    def test_common_1_zero_angle_moves_right_of_sun(self):
        Planet = load_planet_class(PositionSource(10, -5))
        planet = Planet("Earth", [0, 100], "blue")
        planet.move_solarSystem()
        self.assertEqual(planet.goto_calls[-1], (110.0, -5.0))

    def test_common_2_quarter_turn_moves_above_sun(self):
        Planet = load_planet_class(PositionSource(10, -5))
        planet = Planet("Earth", [math.pi / 2, 100], "blue")
        planet.move_solarSystem()
        x, y = planet.goto_calls[-1]
        self.assertAlmostEqual(x, 10.0)
        self.assertAlmostEqual(y, 95.0)

    def test_uncommon_1_zero_radius_stays_on_sun(self):
        Planet = load_planet_class(PositionSource(-4, 7))
        planet = Planet("Earth", [1.234, 0], "blue")
        planet.move_solarSystem()
        self.assertEqual(planet.goto_calls[-1], (-4.0, 7.0))

    def test_uncommon_2_negative_radius_moves_opposite_direction(self):
        Planet = load_planet_class(PositionSource(0, 0))
        planet = Planet("Test", [0, -25], "red")
        planet.move_solarSystem()
        self.assertEqual(planet.goto_calls[-1], (-25.0, 0.0))


class MoonMovementTests(unittest.TestCase):
    def test_common_1_zero_angle_moves_right_of_parent(self):
        Moon = load_moon_class(PositionSource(-4, 7))
        moon = Moon("Io", 20, "gray")
        moon.angle = 0
        moon.move_moonPlanet()
        self.assertEqual(moon.goto_calls[-1], (16.0, 7.0))

    def test_common_2_half_turn_moves_left_of_parent(self):
        Moon = load_moon_class(PositionSource(-4, 7))
        moon = Moon("Io", 20, "gray")
        moon.angle = math.pi
        moon.move_moonPlanet()
        x, y = moon.goto_calls[-1]
        self.assertAlmostEqual(x, -24.0)
        self.assertAlmostEqual(y, 7.0)

    def test_uncommon_1_zero_radius_stays_on_parent(self):
        Moon = load_moon_class(PositionSource(3, 9))
        moon = Moon("Io", 0, "gray")
        moon.angle = math.pi / 3
        moon.move_moonPlanet()
        self.assertEqual(moon.goto_calls[-1], (3.0, 9.0))

    def test_uncommon_2_negative_radius_moves_opposite_direction(self):
        Moon = load_moon_class(PositionSource(0, 0))
        moon = Moon("Io", -10, "gray")
        moon.angle = math.pi / 2
        moon.move_moonPlanet()
        x, y = moon.goto_calls[-1]
        self.assertAlmostEqual(x, 0.0)
        self.assertAlmostEqual(y, -10.0)


class IncrementDatetimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.increment = staticmethod(load_ast_definitions(
            BASIC_GUI,
            ["increment_datetime"],
            {"timedelta": timedelta},
        )["increment_datetime"])

    def test_common_1_adds_hours_same_day(self):
        start = datetime(2026, 8, 6, 10, 30)
        self.assertEqual(self.increment(start, 2), datetime(2026, 8, 6, 12, 30))

    def test_common_2_adds_hours_across_midnight(self):
        start = datetime(2026, 8, 6, 23, 30)
        self.assertEqual(self.increment(start, 2), datetime(2026, 8, 7, 1, 30))

    def test_uncommon_1_negative_increment_moves_backward(self):
        start = datetime(2026, 8, 6, 1, 0)
        self.assertEqual(self.increment(start, -3), datetime(2026, 8, 5, 22, 0))

    def test_uncommon_2_fractional_increment_crosses_leap_day(self):
        start = datetime(2024, 2, 28, 23, 45)
        self.assertEqual(self.increment(start, 1.5), datetime(2024, 2, 29, 1, 15))


class FakeWidget:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.placed = False
        self.place_args = None
        self.insertions = []

    def place(self, *args, **kwargs):
        self.placed = True
        self.place_args = (args, kwargs)

    def insert(self, index, text):
        self.insertions.append((index, text))


class FakeTk:
    def __init__(self):
        self.widgets = []

    def Label(self, *args, **kwargs):
        widget = FakeWidget(*args, **kwargs)
        self.widgets.append(widget)
        return widget

    def Listbox(self, *args, **kwargs):
        widget = FakeWidget(*args, **kwargs)
        self.widgets.append(widget)
        return widget


class PlanetInfoWindowTests(unittest.TestCase):
    def setUp(self):
        self.tk = FakeTk()
        self.messagebox = SimpleNamespace(showerror=MagicMock())
        self.open_window = load_ast_definitions(
            BASIC_GUI,
            ["openPlanetWindow"],
            {"tk": self.tk, "messagebox": self.messagebox},
        )["openPlanetWindow"]

    def listbox_text(self):
        listboxes = [widget for widget in self.tk.widgets if "height" in widget.kwargs]
        self.assertEqual(len(listboxes), 1)
        return [text for _, text in listboxes[0].insertions]

    def test_common_1_earth_data_is_formatted(self):
        info = ("Earth", 6371, 5.97e24, "Terrestrial", 9.81, 15, 1, None, 1, 1)
        self.open_window(info)
        text = self.listbox_text()
        self.assertIn("Radius: 6371km", text)
        self.assertIn("Planet Type: Terrestrial", text)
        self.assertIn("Number of Moons: 1", text)

    def test_common_2_gas_giant_data_is_formatted(self):
        info = ("Jupiter", 79492, 1.90e27, "Gas Giant", 24.79, -108, 5.2, None, 95, 11.86)
        self.open_window(info)
        text = self.listbox_text()
        self.assertIn("Radius: 79492km", text)
        self.assertIn("Planet Type: Gas Giant", text)
        self.assertIn("Orbital Period: 11.86 Earth Years", text)

    def test_uncommon_1_none_planet_shows_error_and_returns(self):
        self.assertIsNone(self.open_window(None))
        self.messagebox.showerror.assert_called_once_with(
            "Error", "Planet not found in database."
        )
        self.assertEqual(self.tk.widgets, [])

    def test_uncommon_2_none_and_negative_fields_are_stringified(self):
        info = ("Unknown", -1, None, None, -2, -273, 0, None, 0, -1)
        self.open_window(info)
        text = self.listbox_text()
        self.assertIn("Radius: -1km", text)
        self.assertIn("Mass: Nonekg", text)
        self.assertIn("Planet Type: None", text)


class GuiImportSafetyTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_common_1_basic_gui_should_not_create_tk_at_import(self):
        """Known defect: basicGUI creates the root window during import."""
        self.assertFalse(has_top_level_call(BASIC_GUI, {"Tk"}))

    @unittest.expectedFailure
    def test_common_2_basic_gui_should_not_run_mainloop_at_import(self):
        """Known defect: basicGUI enters mainloop during import."""
        self.assertFalse(has_top_level_call(BASIC_GUI, {"mainloop"}))

    @unittest.expectedFailure
    def test_uncommon_1_moon_gui_should_not_create_toplevel_at_import(self):
        """Known defect: moonpopupgui creates a Toplevel during import."""
        self.assertFalse(has_top_level_call(MOON_GUI, {"Toplevel"}))

    @unittest.expectedFailure
    def test_uncommon_2_moon_gui_should_not_assign_popup_at_import(self):
        """Known defect: moonpopupgui assigns its popup during import."""
        compact_source = "".join(MOON_GUI.read_text(encoding="utf-8").split())
        self.assertNotIn("popup=tk.Toplevel()", compact_source)


if __name__ == "__main__":
    unittest.main()
