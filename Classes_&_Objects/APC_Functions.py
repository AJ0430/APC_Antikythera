# this will be the py file that contains all the functions used by the project

import APC_Classes_Objects as classes   # imports all code from our classes and objects .py file
#from GUI_Stuff import basicGUI as GUI

import sqlite3

database = sqlite3.connect("Database_Stuff/AntikytheraSystem.db")
cursor = database.cursor()

# test to make sure the classes from the classes & objects .py file can be used in this functions .py file
print(f"Mercury Mass: {classes.Mercury.mass}")

# creating the zodiac sign function


def showEclipses(year, month, day): # If given date results in an eclipse display it in the bottom left of the GUI.
    cursor.execute("""SELECT * FROM Eclipses WHERE DATE = '?' + '/' + '?' + '/' + '?'""", (month, day, year))
    if cursor.fetchone() != None:
        eclipseInfo = cursor.fetchone()
        print(eclipseInfo[0])
        print(eclipseInfo[1])
        print(eclipseInfo[2])
    else:
        print('No Eclipse Occuring On This Day.')

def showPlanetInfo(buttonName):
    if buttonName == 'Mercury':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Mercury'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Venus':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Venus'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Earth':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Earth'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Mars':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Mars'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Jupiter':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Jupiter'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Saturn':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Saturn'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Uranus':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Uranus'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Neptune':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Neptune'""")
        planetInfo = cursor.fetchone()
    elif buttonName == 'Pluto':
        cursor.execute("""SELECT * FROM Planets WHERE NAME = 'Pluto'""")
        planetInfo = cursor.fetchone()

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