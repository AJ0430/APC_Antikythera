from __future__ import annotations

import os
import runpy
import shutil
import sqlite3
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "Database_Stuff" / "APC_Project-DatabaseCommands.py"
EXPECTED_TABLES = {"Planets", "Moons", "SmallBodies", "Eclipses", "Zodiac_Constellations"}


@contextmanager
def changed_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


class DatabaseBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.work = Path(self.temp_dir.name)
        (self.work / "Database_Stuff").mkdir()
        self.script_copy = self.work / "Database_Stuff" / SCRIPT.name
        shutil.copy2(SCRIPT, self.script_copy)
        self.run_script()
        self.database_path = self.work / "Database_Stuff" / "AntikytheraSystem.db"
        self.connection = sqlite3.connect(self.database_path)

    def tearDown(self):
        self.connection.close()
        self.temp_dir.cleanup()

    def run_script(self):
        with changed_directory(self.work):
            runpy.run_path(str(self.script_copy), run_name="__main__")

    def table_names(self):
        rows = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        return {row[0] for row in rows}

    def test_common_1_database_file_and_tables_are_created(self):
        self.assertTrue(self.database_path.is_file())
        self.assertGreater(self.database_path.stat().st_size, 0)
        self.assertTrue(EXPECTED_TABLES.issubset(self.table_names()))

    def test_common_2_representative_seed_rows_exist(self):
        earth = self.connection.execute(
            "SELECT NAME, RADIUS, PLANET_TYPE, NUMBER_OF_MOONS "
            "FROM Planets WHERE NAME='Earth'"
        ).fetchone()
        eclipse = self.connection.execute(
            "SELECT TYPE, DATE FROM Eclipses WHERE DATE='8/28/2026'"
        ).fetchone()
        self.assertEqual(earth, ("Earth", 6371.0, "Terrestrial", 1))
        self.assertEqual(eclipse, ("Lunar", "8/28/2026"))
        for table in EXPECTED_TABLES:
            with self.subTest(table=table):
                count = self.connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                self.assertGreater(count, 0)

    def test_uncommon_1_running_script_twice_does_not_duplicate_rows(self):
        before = {
            table: self.connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in EXPECTED_TABLES
        }
        self.connection.close()
        self.run_script()
        self.connection = sqlite3.connect(self.database_path)
        after = {
            table: self.connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in EXPECTED_TABLES
        }
        self.assertEqual(after, before)

    def test_uncommon_2_rerun_preserves_existing_primary_key_data(self):
        self.connection.execute("UPDATE Planets SET RADIUS = 7000 WHERE NAME = 'Earth'")
        self.connection.commit()
        self.connection.close()
        self.run_script()
        self.connection = sqlite3.connect(self.database_path)
        radius = self.connection.execute(
            "SELECT RADIUS FROM Planets WHERE NAME = 'Earth'"
        ).fetchone()[0]
        self.assertEqual(radius, 7000)


if __name__ == "__main__":
    unittest.main()
