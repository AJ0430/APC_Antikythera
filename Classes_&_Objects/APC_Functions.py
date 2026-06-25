# this will be the py file that contains all the functions used by the project

import APC_Classes_Objects as classes   # imports all code from our classes and objects .py file
from GUI_Stuff import basicGUI as GUI

# test to make sure the classes from the classes & objects .py file can be used in this functions .py file
print(f"Mercury Mass: {classes.Mercury.mass}")

# creating the zodiac sign function
def showZodiacSigns(GUI.year, GUI.month, GUI.day):
    # start here