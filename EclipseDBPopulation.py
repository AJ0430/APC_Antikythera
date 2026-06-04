import sqlite3

database = sqlite3.connect("AntikytheraSystem.db")
cursor = database.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS Eclipses('Solar','2/5/2000', 'Antarctica');"""
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

database.commit()
database.close()