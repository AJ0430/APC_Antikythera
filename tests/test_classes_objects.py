from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from tests.import_helpers import load_classes_with_fake_database


class ClassTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_classes_with_fake_database()

    @staticmethod
    def printed_text(obj):
        output = io.StringIO()
        with redirect_stdout(output):
            obj.printInfo()
        return output.getvalue()


class SolarBodyConstructorTests(ClassTestBase):
    def test_common_1_typical_attributes_are_stored(self):
        body = self.module.solarBodies("Body", 10, 20, 30, "position")
        self.assertEqual(
            (body.name, body.mass, body.radius, body.gravitationalPull, body.orbitalPostion),
            ("Body", 10, 20, 30, "position"),
        )

    def test_common_2_float_attributes_are_stored(self):
        body = self.module.solarBodies("Ceres", 9.39e20, 473.0, 0.28, "orbit")
        self.assertEqual(body.name, "Ceres")
        self.assertAlmostEqual(body.mass, 9.39e20)
        self.assertAlmostEqual(body.radius, 473.0)

    def test_uncommon_1_zero_values_are_retained(self):
        body = self.module.solarBodies("Origin", 0, 0, 0, None)
        self.assertEqual((body.mass, body.radius, body.gravitationalPull), (0, 0, 0))
        self.assertIsNone(body.orbitalPostion)

    def test_uncommon_2_mutable_orbital_position_is_stored_by_reference(self):
        position = [1, 2, 3]
        body = self.module.solarBodies("Body", 1, 2, 3, position)
        self.assertIs(body.orbitalPostion, position)


class PlanetConstructorTests(ClassTestBase):
    def test_common_1_earth_fields_and_inheritance(self):
        planet = self.module.planets(
            "Earth", 5.97e24, 6371, 9.81, "position", "Terrestrial", 15, 1, 1, 1
        )
        self.assertIsInstance(planet, self.module.solarBodies)
        self.assertEqual((planet.type, planet.surfaceTemp, planet.sunDistance), ("Terrestrial", 15, 1))
        self.assertEqual((planet.moons, planet.period), (1, 1))

    def test_common_2_gas_giant_fields_are_stored(self):
        planet = self.module.planets(
            "Jupiter", 1.90e27, 79492, 24.79, None, "Gas Giant", -108, 5.2, 95, 11.86
        )
        self.assertEqual(planet.name, "Jupiter")
        self.assertEqual(planet.type, "Gas Giant")
        self.assertEqual(planet.moons, 95)

    def test_uncommon_1_zero_and_none_fields_are_retained(self):
        planet = self.module.planets("Unknown", 0, 0, 0, None, None, 0, 0, 0, 0)
        self.assertIsNone(planet.type)
        self.assertEqual((planet.mass, planet.radius, planet.moons, planet.period), (0, 0, 0, 0))

    def test_uncommon_2_negative_values_are_not_silently_changed(self):
        planet = self.module.planets("Test", -1, -2, -3, "x", "Test", -4, -5, -6, -7)
        self.assertEqual(
            (planet.mass, planet.radius, planet.gravitationalPull, planet.surfaceTemp),
            (-1, -2, -3, -4),
        )


class MoonConstructorTests(ClassTestBase):
    def test_common_1_earth_moon_fields_and_inheritance(self):
        moon = self.module.moons("The Moon", 7.35e22, 1737.4, 1.62, "position", "Earth")
        self.assertIsInstance(moon, self.module.solarBodies)
        self.assertEqual(moon.planetOrbiting, "Earth")

    def test_common_2_io_fields_are_stored(self):
        moon = self.module.moons("Io", 8.93e22, 1821, 1.796, "position", "Jupiter")
        self.assertEqual((moon.name, moon.planetOrbiting), ("Io", "Jupiter"))
        self.assertEqual((moon.radius, moon.gravitationalPull), (1821, 1.796))

    def test_uncommon_1_none_parent_is_retained(self):
        moon = self.module.moons("Rogue", 1, 2, 3, None, None)
        self.assertIsNone(moon.planetOrbiting)
        self.assertIsNone(moon.orbitalPostion)

    def test_uncommon_2_zero_and_negative_values_are_retained(self):
        moon = self.module.moons("Test", 0, -1, -2, "unknown", "Planet")
        self.assertEqual((moon.mass, moon.radius, moon.gravitationalPull), (0, -1, -2))


class PlanetPrintInfoTests(ClassTestBase):
    def test_common_1_earth_output_contains_every_field(self):
        planet = self.module.planets(
            "Earth", 5.97e24, 6371, 9.81, "position", "Terrestrial", 15, 1, 1, 1
        )
        text = self.printed_text(planet)
        expected_lines = (
            "Name: Earth",
            "Mass: 5.97e+24 kg",
            "Radius: 6371 km",
            "Gravitational Pull: 9.81 m/s^2",
            "Orbital Position: position",
            "Type: Terrestrial",
            "Surface Temperature: 15 C",
            "Distance from Sun: 1 AU",
            "Number of Moons: 1",
            "Orbital Period: 1 Earth Years",
        )
        for expected in expected_lines:
            with self.subTest(expected=expected):
                self.assertIn(expected, text)

    def test_common_2_gas_giant_output_uses_given_values(self):
        planet = self.module.planets(
            "Jupiter", 1.9e27, 79492, 24.79, None, "Gas Giant", -108, 5.2, 95, 11.86
        )
        text = self.printed_text(planet)
        self.assertIn("Name: Jupiter", text)
        self.assertIn("Type: Gas Giant", text)
        self.assertIn("Number of Moons: 95", text)

    def test_uncommon_1_none_values_are_printed_without_crashing(self):
        planet = self.module.planets("Unknown", None, None, None, None, None, None, None, None, None)
        text = self.printed_text(planet)
        self.assertIn("Mass: None kg", text)
        self.assertIn("Type: None", text)
        self.assertIn("Orbital Position: None", text)

    def test_uncommon_2_negative_values_are_printed_verbatim(self):
        planet = self.module.planets("Test", -1, -2, -3, "x", "Test", -4, -5, -6, -7)
        text = self.printed_text(planet)
        self.assertIn("Radius: -2 km", text)
        self.assertIn("Surface Temperature: -4 C", text)
        self.assertIn("Orbital Period: -7 Earth Years", text)


class MoonPrintInfoTests(ClassTestBase):
    def test_common_1_earth_moon_output_contains_every_field(self):
        moon = self.module.moons("The Moon", 7.35e22, 1737.4, 1.62, "position", "Earth")
        text = self.printed_text(moon)
        expected_lines = (
            "Name: The Moon",
            "Mass: 7.35e+22 kg",
            "Radius: 1737.4 km",
            "Gravitational Pull: 1.62 m/s^2",
            "Orbital Position: position",
            "Planet Orbiting: Earth",
        )
        for expected in expected_lines:
            with self.subTest(expected=expected):
                self.assertIn(expected, text)

    def test_common_2_io_output_contains_parent_planet(self):
        moon = self.module.moons("Io", 8.93e22, 1821, 1.796, "position", "Jupiter")
        text = self.printed_text(moon)
        self.assertIn("Name: Io", text)
        self.assertIn("Planet Orbiting: Jupiter", text)

    def test_uncommon_1_none_values_are_printed_without_crashing(self):
        moon = self.module.moons("Unknown", None, None, None, None, None)
        text = self.printed_text(moon)
        self.assertIn("Mass: None kg", text)
        self.assertIn("Planet Orbiting: None", text)

    def test_uncommon_2_negative_values_are_printed_verbatim(self):
        moon = self.module.moons("Test", -1, -2, -3, "x", "Planet")
        text = self.printed_text(moon)
        self.assertIn("Radius: -2 km", text)
        self.assertIn("Gravitational Pull: -3 m/s^2", text)


if __name__ == "__main__":
    unittest.main()
