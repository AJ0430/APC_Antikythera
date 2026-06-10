import sqlite3

database = sqlite3.connect("AntikytheraSystem.db")
cursor = database.cursor()

sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('McNaught', 'Comet', 'Oort Cloud', 1.58, 101.9);"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Halley', 'Comet', 'Inner and Outer Belt', 3.4, 55);"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Apophis', 'Asteroid', 'Solar System', 0.185, 30.73);"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Neowise', 'Comet', 'Solar System', 2.5, 1.5);"""
cursor.execute(sql_command)
sql_command = """INSERT OR IGNORE INTO SmallBodies VALUES('Tsuchinshan-ATLAS', 'Comet', 'Solar System', 5.9, 67.33);"""
cursor.execute(sql_command)

database.commit()
database.close()