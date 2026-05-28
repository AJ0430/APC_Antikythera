import sqlite3

database = sqlite3.connect("AntikytheraSystem.db")
cursor = database.cursor()

sql_command = """CREATE TABLE IF NOT EXISTS Planets (
NAME TEXT NOT NULL PRIMARY KEY,
RADIUS INTEGER NOT NULL,
MASS INTEGER NOT NULL,
PLANET_TYPE TEXT NOT NULL,
GRAVITATIONAL_PULL INTEGER NOT NULL,
AVG_SURFACE_TEMP INTEGER NOT NULL,
DISTANCE_TO_SUN INTEGER NOT NULL,
ORBITAL_POSITION TEXT NOT NULL,
NUMBER_OF_MOONS INTEGER NOT NULL,
ORBITAL_PERIOD INTEGER NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Moons (
NAME TEXT NOT NULL PRIMARY KEY,
RADIUS[km] REAL NOT NULL,
MASS[kg] REAL NOT NULL,
GRAVITATIONAL_PULL[m/s^2] REAL NOT NULL,
ORBITAL_POSITION TEXT,
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

sql_command = """INSERT OR IGNORE INTO Moons VALUES('The Moon', 1737.5, 7.35e22, 1.62, NULL, 'Earth');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Titan', 2574.7, 1.35e23, 1.35, NULL, 'Saturn');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Callisto', 4410.3, 1.08e23, 1.24, NULL, 'Jupiter');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Io', 1821.6, 8.93e22, 1.80, NULL, 'Jupiter');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Europa', 1560.8, 4.80e22, 1.31, NULL, 'Jupiter');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Triton', 1353.4, 2.14e22, 0.78, NULL, 'Neptune');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Deimos', 6.2, 1.48e15, 0.003, NULL, 'Mars');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Moons VALUES('Titania', 788.9, 3.53e21, 0.38, NULL, 'Uranus');"""
cursor.execute(sql_command)

database.commit()

database.close()