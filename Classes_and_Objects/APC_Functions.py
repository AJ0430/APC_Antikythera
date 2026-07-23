# this will be the py file that contains all the functions used by the project

from . import APC_Classes_Objects as classes   # imports all code from our classes and objects .py file

import sqlite3

database = sqlite3.connect("Database_Stuff/AntikytheraSystem.db")
cursor = database.cursor()

# test to make sure the classes from the classes & objects .py file can be used in this functions .py file
# print(f"Mercury Mass: {classes.Mercury.mass}")

# creating the zodiac sign function
# def showZodiacSigns(GUI.year, GUI.month, GUI.day):
    # start here

def monthConversion(month):
    monthNumber = 0
    if (month == 'January'):
        monthNumber = 1
    elif (month == 'February'):
        monthNumber = 2
    elif (month == 'March'):
        monthNumber = 3
    elif (month == 'April'):
        monthNumber = 4
    elif (month == 'May'):
        monthNumber = 5
    elif (month == 'June'):
        monthNumber = 6
    elif (month == 'July'):
        monthNumber = 7
    elif (month == 'August'):
        monthNumber = 8
    elif (month == 'September'):
        monthNumber = 9
    elif (month == 'October'):
        monthNumber = 10
    elif (month == 'November'):
        monthNumber = 11
    elif (month == 'December'):
        monthNumber = 12
    
    return monthNumber

def showEclipses(month, day, year): # If given date results in an eclipse display it in the bottom left of the GUI.
    month = monthConversion(month)
    full_date = str(month) + '/' + str(day) + '/' + str(year)
    print(f"From showEclipses/fulldate: {full_date}")
    cursor.execute("""SELECT * FROM Eclipses WHERE DATE = ?""", [full_date])
    eclipseInfo = cursor.fetchone()
    print(f"From showEclipses: {eclipseInfo}")
    return eclipseInfo

def showPlanetInfo(planetName):
    # goes into the DB, and looks for the entry in the table for the appropriate planet name
    cursor.execute("""SELECT * FROM Planets WHERE NAME = ?""", (planetName,))
    planetInfo = cursor.fetchone()

    # sends the information back
    return planetInfo

def showMoonInfo(buttonName):
    if buttonName == 'Moon':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Moon'""")
        moonInfo = cursor.fetchone()
# from here on out, the code will be for the other moons of the solar system, which may be added later on
    elif buttonName == 'Phobos':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Phobos'""")
        moonInfo = cursor.fetchone()
    elif buttonName == 'Deimos':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Deimos'""")
        moonInfo = cursor.fetchone()
    elif buttonName == 'Io':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Io'""")
        moonInfo = cursor.fetchone()
    elif buttonName == 'Europa':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Europa'""")
        moonInfo = cursor.fetchone()
    elif buttonName == 'Ganymede':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Ganymede'""")
        moonInfo = cursor.fetchone()
    elif buttonName == 'Callisto':
        cursor.execute("""SELECT * FROM Moons WHERE NAME = 'Callisto'""")
        moonInfo = cursor.fetchone()

    # functions remaining:
    # Orb. posistion - determined by solar_lib library that Ashton has implemented
    # cant think of any more functions to add at the moment, but if I do think of any I will add them here
#showEclipses('February', 5, 2000)
