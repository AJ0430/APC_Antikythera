import sqlite3
import math

database = sqlite3.connect("AntikytheraSystem.db")
cursor = database.cursor()

sql_command = """CREATE TABLE IF NOT EXISTS Planets (
NAME TEXT NOT NULL PRIMARY KEY,
RADIUS[km] REAL NOT NULL,
MASS[kg] REAL NOT NULL,
PLANET_TYPE TEXT NOT NULL,
GRAVITATIONAL_PULL[m/s^2] REAL NOT NULL,
AVG_SURFACE_TEMP[°C] REAL NOT NULL,
DISTANCE_TO_SUN[AU] REAL NOT NULL,
ORBITAL_POSITION TEXT,
NUMBER_OF_MOONS INTEGER NOT NULL,
ORBITAL_PERIOD[Earth years] REAL NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Moons(
NAME TEXT NOT NULL PRIMARY KEY,
RADIUS INTEGER NOT NULL,
MASS INTEGER NOT NULL,
GRAVITATIONAL_PULL INTEGER NOT NULL,
ORBITAL_POSITION TEXT NOT NULL,
ORBITED_PLANET TEXT NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Small_Bodies(
NAME TEXT NOT NULL PRIMARY KEY,
TYPE TEXT NOT NULL,
POSITION TEXT NOT NULL,
SIZE INTEGER NOT NULL,
SPEED INTEGER NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Eclipses(
TYPE TEXT NOT NULL,
DATE TEXT NOT NULL PRIMARY KEY,
LOCATION TEXT NOT NULL)
;"""

cursor.execute(sql_command)

<<<<<<< Updated upstream
sql_command = """CREATE TABLE IF NOT EXISTS Zodiac_Constellations(
NAME TEXT NOT NULL PRIMARY KEY,
DATE_START TEXT NOT NULL,
DATE_END TEXT NOT NULL)
;"""

cursor.execute(sql_command)

database.commit()
database.close()
=======
#Adding in Planet Data to table
sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Mercury', 2439.5, 3.29e23, 'Terrestrial', 3.7, 254, 0.39, NULL, 0, 0.24);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Venus', 6052, 4.87e24, 'Terrestrial', 8.87, 462, 0.73, NULL, 0, 0.62);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Earth', 6371, 5.97e24, 'Terrestrial', 9.81, 15, 1, NULL, 1, 1);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Mars', 3389.5, 6.42e23, 'Terrestrial', 3.71, -65, 1.38, NULL, 2, 1.9);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Jupiter', 79492, 1.90e27, 'Gas Giant', 24.79, -108, 5.20, NULL, 95, 11.86);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Saturn', 60268, 5.68e26, 'Gas Giant', 10.44, -139, 9.58, NULL, 274, 29.46);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Uranus', 25559, 8.68e25, 'Ice Giant', 8.69, -197, 19.22, NULL, 27, 84);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Neptune', 24629, 1.02e26, 'Ice Giant', 11.15, -201, 30.10, NULL, 14, 164.8);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Planets VALUES ('Pluto', 1186, 1.31e22, 'Dwarf Planet', 0.62, -229, 39.26, NULL, 5, 248);"""
cursor.execute(sql_command)

database.commit()

database.close()
>>>>>>> Stashed changes
