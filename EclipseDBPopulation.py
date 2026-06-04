import sqlite3

database = sqlite3.connect("AntikytheraSystem.db")
cursor = database.cursor()

sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '1/4/2011', 'Europe, Africa, c Asia');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '6/1/2011', 'e Asia, n North America, Iceland');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '7/1/2011', 's Indian Ocean');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/25/2011', 's Africa, Antarctica, Tasmania, N.Z.');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/20/2012', 'Asia, Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/13/2012', 'Australia, New Zealand, South Pacific, s South America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '5/10/2013', 'Australia, New Zealand, c Pacific');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '11/3/2013', 'e Americas, s Europe, Africa');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '4/29/2014', 's Indian, Australia, Antarctica');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '10/23/2014', 'n Pacific, North America');"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO Eclipses VALUES('Solar', '3/20/2015', 'Iceland, Europe, n Africa, n Asia');"""
cursor.execute(sql_command)




database.commit()
database.close()