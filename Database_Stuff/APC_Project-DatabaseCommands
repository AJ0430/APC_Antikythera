import sqlite3
import math

db_folder = "Database_Stuff/"
database = sqlite3.connect(db_folder + "AntikytheraSystem.db")
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
ORBITAL_POSITION TEXT,
ORBITED_PLANET TEXT NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS SmallBodies(
NAME TEXT NOT NULL PRIMARY KEY,
TYPE TEXT NOT NULL,
POSITION TEXT NOT NULL,
SIZE INTEGER NOT NULL,
SPEED INTEGER NOT NULL,
DATE_START TEXT NOT NULL,
DATE_END TEXT NOT NULL,
YEAR INTEGER NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Eclipses(
TYPE TEXT NOT NULL,
DATE TEXT NOT NULL PRIMARY KEY,
LOCATION TEXT NOT NULL)
;"""

cursor.execute(sql_command)

sql_command = """CREATE TABLE IF NOT EXISTS Zodiac_Constellations(
NAME TEXT NOT NULL PRIMARY KEY,
DATE_START TEXT NOT NULL,
DATE_END TEXT NOT NULL)
;"""

cursor.execute(sql_command)

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


#Adding in Moon Data to Table
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


#Adding in Small Body Data to Table
sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('McNaught', 'Comet', 'Oort Cloud', 1.58, 101.9, 'January' , 'February', 2007);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Halley', 'Comet', 'Inner and Outer Belt', 3.4, 55, 'January', 'April', 1986);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Apophis', 'Asteroid', 'Solar System', 0.185, 30.73, 'April', 'April', 2029);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Neowise', 'Comet', 'Solar System', 2.5, 1.5, 'July', 'July', 2020);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Tsuchinshan-ATLAS', 'Comet', 'Solar System', 5.9, 67.33, 'September', 'September', 2024);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Ceres', 'Asteroid', 'Main Asteroid Belt', 469.7, 17.9, 'Not Visible', 'Not Visible', 0);"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Vesta', 'Asteroid', 'Main Asteroid Belt', 525.4, 19.34, 'Not Visible', 'Not Visible', 0);"""
cursor.execute(sql_command)


#Adding in Eclipse Data to Table
#Solar eclipses from 2000-2030, data from https://eclipse.gsfc.nasa.gov/
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/5/2000', 'Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/1/2000', 'South Pacific Ocean, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/31/2000', 'Asia, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/25/2000', 'Central America, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/21/2001', 'Africa, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/14/2001', 'Central America, North America, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/10/2002', 'Asia, Australia, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/4/2002', 'Africa, Antarctica, Indonesia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/31/2003', 'Europe, Asia, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/23/2003', 'Australia, New Zealand, Antarctica, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/19/2004', 'Antarctica, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/14/2004', 'Asia, Hawaii, Alaska');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '4/8/2005', 'New Zealand, North America, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/3/2005', 'Africa, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/29/2006', 'Africa, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '9/22/2006', 'South America, Africa, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/19/2007', 'Asia, Alaska');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '9/11/2007', 'South America, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/7/2008', 'Asia, Australia, New Zealand');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '8/1/2008', 'North America, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/26/2009', 'Africa, Antarctica, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/22/2009', 'Asia, Pacific Ocean, Hawaii');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/15/2010', 'Africa, Asia');""" 
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/11/2010', 'South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/4/2011', 'Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/1/2011', 'Asia, North America, Iceland');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/1/2011', 'Indian Ocean');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/25/2011', 'Africa, Antarctica, Tasmania, N.Z.');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/20/2012', 'Asia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/13/2012', 'Australia, New Zealand, South Pacific, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/10/2013', 'Australia, New Zealand, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/3/2013', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '4/29/2014', 'Indian, Australia, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/23/2014', 'Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/20/2015', 'Iceland, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '9/13/2015', 'Africa, India, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/9/2016', 'Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '9/1/2016', 'Africa, Indian Ocean');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/26/2017', 'South America, Atlantic, Africa, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '8/21/2017', 'North America, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/15/2018', 'Antarctica, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/13/2018', 'Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '8/11/2018', 'Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/6/2019', 'Asia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/2/2019', 'Pacific, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/26/2019', 'Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/21/2020', 'Africa, Asia, Europe');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/14/2020', 'South America, Antarctica, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/10/2021', 'North America, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/4/2021', 'South Africa, Antarctica, Atlantic');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/30/2022', 'Pacific, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/25/2022', 'Europe, Africa, Asia, Middle East, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '4/20/2023', 'Asia, East Indies, Australia, Philippines, New Zealand');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/14/2023', 'North America, Central America, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '4/8/2024', 'North America, Central America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/2/2024', 'Pacific, South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/29/2025', 'Africa, Europe, Russia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '9/21/2025', 'Pacific, New Zealand, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/17/2026', 'Argentina, Chile, Africa, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '8/12/2026', 'North America, Africa, Europe');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '2/6/2027', 'South America, Antarctica, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '8/2/2027', 'Africa, Europe, Middle East, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/26/2028', 'North America, Central America, South America, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/22/2028', 'South East Asia, East Indies, Australia, New Zealand');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/14/2029', 'North America, Central America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/12/2029', 'Arctic, Scandinavia, Alaska, Asia, Canada');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/11/2029', 'Chile, Argentina');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '12/5/2029', 'Chile, Argentina, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/25/2030', 'Africa, Indian Ocean, East Indies, Australia, Antarctica');"""
cursor.execute(sql_command)

#Lunar eclipses from 2000-2030, data from https://eclipse.gsfc.nasa.gov/
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/21/2000', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/16/2000', 'Asia, Pacific Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/9/2001', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/5/2001', 'Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/30/2001', 'Asia, Pacific, Australia, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/26/2002', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/24/2002', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/20/2002', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/16/2003', 'Pacific, Americas, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/9/2003', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/4/2004', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/28/2004', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/24/2005', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/17/2005', 'Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/14/2006', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/7/2006', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/3/2007', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/28/2007', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/21/2008', 'Americas, Europe, Africa, Atlantic');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/16/2008', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/9/2009', 'Europe, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/6/2009', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/31/2009', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/26/2010', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/21/2010', 'Asia, Australia, Pacific, Americas, Europe');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/15/2011', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/10/2011', 'Europe, Africa, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/4/2012', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/28/2012', 'Europe, Africa, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/25/2013', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/18/2013', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/15/2014', 'Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/8/2014', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/4/2015', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/28/2015', 'Pacific, Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/23/2016', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/16/2016', 'Europe, Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/11/2017', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/7/2017', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/31/2018', 'Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/27/2018', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/21/2019', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/16/2019', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/10/2020', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/5/2020', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/5/2020', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/20/2020', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/26/2021', 'Asia, Australia, PAcific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/19/2021', 'Americas, Europe, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/16/2022', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/8/2022', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/5/2023', 'Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/28/2023', 'Americas, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/25/2024', 'Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/18/2024', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/14/2025', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/7/2025', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/3/2026', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/28/2026', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/20/2027', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/18/2027', 'Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/17/2027', 'Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/12/2028', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/6/2028', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/31/2028', 'Europe, Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/26/2029', 'Americas, Europe, Africa, Mid East');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/20/2029', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/15/2030', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/9/2030', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '', '');"""
cursor.execute(sql_command)

#Lunar eclipses from 2000-2030, data from https://eclipse.gsfc.nasa.gov/
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/21/2000', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/16/2000', 'Asia, Pacific Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/9/2001', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/5/2001', 'Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/30/2001', 'Asia, Pacific, Australia, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/26/2002', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/24/2002', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/20/2002', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/16/2003', 'Pacific, Americas, Europe, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/9/2003', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/4/2004', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/28/2004', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/24/2005', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/17/2005', 'Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/14/2006', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/7/2006', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/3/2007', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/28/2007', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/21/2008', 'Americas, Europe, Africa, Atlantic');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/16/2008', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/9/2009', 'Europe, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/6/2009', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/31/2009', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/26/2010', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/21/2010', 'Asia, Australia, Pacific, Americas, Europe');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/15/2011', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/10/2011', 'Europe, Africa, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/4/2012', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/28/2012', 'Europe, Africa, Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/25/2013', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/18/2013', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/15/2014', 'Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/8/2014', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '4/4/2015', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/28/2015', 'Pacific, Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/23/2016', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/16/2016', 'Europe, Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/11/2017', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/7/2017', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/31/2018', 'Asia, Australia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/27/2018', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/21/2019', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/16/2019', 'South America, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/10/2020', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/5/2020', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/5/2020', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/20/2020', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/26/2021', 'Asia, Australia, PAcific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/19/2021', 'Americas, Europe, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/16/2022', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '11/8/2022', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/5/2023', 'Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '10/28/2023', 'Americas, Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '5/25/2024', 'Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/18/2024', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/14/2025', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '9/7/2025', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '3/3/2026', 'Asia, Australia, Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/28/2026', 'Pacific, Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '2/20/2027', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/18/2027', 'Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '8/17/2027', 'Pacific, Americas');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '1/12/2028', 'Americas, Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '7/6/2028', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/31/2028', 'Europe, Africa, Asia, Australia, Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/26/2029', 'Americas, Europe, Africa, Mid East');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/20/2029', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '6/15/2030', 'Europe, Africa, Asia, Australia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Lunar', '12/9/2030', 'Americas, Europe, Africa, Asia');"""
cursor.execute(sql_command)
# end of eclipse data

#Adding in Zodiac Constellation Data to Table
sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Aries', 'April 19', 'May 13');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Taurus', 'May 14', 'June 19');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Gemini', 'June 20', 'July 20');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Cancer', 'July 21', 'August 9');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Leo', 'August 10', 'September 15');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Virgo', 'September 16', 'October 30');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Libra', 'October 31', 'November 22');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Scorpio', 'November 23', 'November 29');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Ophiuchus', 'November 30', 'December 17');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Sagittarius', 'December 18', 'January 18');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Capricorn', 'January 19', 'February 15');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Aquarius', 'February 16', 'March 11');"""
cursor.execute(sql_command)

sql_command = """INSERT OR IGNORE INTO Zodiac_Constellations VALUES('Pisces', 'March 12', 'April 18');"""
cursor.execute(sql_command)

database.commit()

database.close()

