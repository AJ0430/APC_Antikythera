import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
import turtle
from turtle import title
from math import *

#Please let me know if these imports are blocking anything or can be improved to use our classes - Rafael
from tkinter import messagebox

# ******* Getting the functions into this folder ******* #
import sys
import os

# Adds the parent directory (APC_Antikythera) to Python's search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes_and_Objects import APC_Functions as apcfunc
# ******* end of import ******* #

# temporarily commented this out as the image is not currently integrated on the GIT repo
from PIL import Image, ImageTk 


import sqlite3

database = sqlite3.connect("Database_Stuff/AntikytheraSystem.db")
cursor = database.cursor()


class Planet(turtle.RawTurtle):
    def __init__(self, name, radius, color):
        super().__init__(sunScreen, shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move_solarSystem(self):
        x = self.radius*cos(self.angle) #Angle in radians
        y = self.radius*sin(self.angle)
        
        self.goto(sunObject.xcor()+x, sunObject.ycor()+y)
        
class Moon(turtle.RawTurtle):
    def __init__(self, name, radius, color):
            super().__init__(moonScreen, shape='circle')
            self.name = name
            self.radius = radius
            self.c = color
            self.color(self.c)
            self.up()
            self.pd()
            self.angle = 0
    def move_moonPlanet(self):
        x = self.radius*cos(self.angle) #Angle in radians
        y = self.radius*sin(self.angle)
        
        self.goto(motherPlanet.xcor()+x, motherPlanet.ycor()+y)


month = "January"
day = 1
year = 2000
global pSelection
global cSelection
pSelection = False
cSelection = False
global planetAnimation
planetAnimation = False


# fixed date selection tab that works on the main window
def dateSelectionFixed():
    title = ttk.Label(text = "Select date:", font=("Arial", 20))
    title.place(x = 1000, y = 0)
    # List of Months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    # Makes January the default selection in the dropdown
    selected_month = tk.StringVar(value=months[0])

    # Create dropdown
    monthDropdown = tk.OptionMenu(root, selected_month, *months)  # Call changeDay when month changes

    #monthDropdown.config(width=15)  
    monthDropdown.place(x = 1150, y = 0)

    # List of Years (2000 to 2030)
    years = [str(year) for year in range(2000, 2031)]

    # Makes 2000 the default selection in the dropdown
    selected_year = tk.StringVar(value=years[0])

    # Create dropdown
    yearDropdown = tk.OptionMenu(root, selected_year, *years)  # Call changeDay when year changes
    yearDropdown.place(x = 1280, y = 0)

    
    # Makes 1st the default selection in the dropdown
    days = [str(day) for day in range(1, 32)]
    selected_day = tk.StringVar(value=days[0])  # Default value

    # Create dropdown
    dayDropdown = tk.OptionMenu(root, selected_day, *days) 
    dayDropdown.place(x = 1225, y = 0)


    # Button to show current selection
    def show_selection():
        # checks if selected date is valid
        if selected_year.get() in ["2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028"] and selected_month.get() == "February" and (selected_day.get() == "30" or selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have " + selected_day.get() + " days in the year " + selected_year.get() + ".")
            messagebox.showinfo("Current Selection", f"{current}")
        elif selected_month.get() == "February" and selected_year.get() not in ["2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028"] and (selected_day.get() == "29" or selected_day.get() == "30" or selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have " + selected_day.get() + " days in the year " + selected_year.get() + ".")
            messagebox.showinfo("Current Selection", f"{current}")
        elif selected_month.get() in ["April", "June", "September", "November"] and (selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have 31 days.")
            messagebox.showinfo("Current Selection", f"{current}")
        
        # saves the selected date and exits the date selection window
        else:
            current = "Current Selection: " + selected_month.get() + " " + selected_day.get() + ", " + selected_year.get()

    def show_EclipseMenu():
        eclipseTitle = tk.Label(text= "Eclipse Info", font=("Arial", 20))
        eclipseTitle.place(x=1000, y=65)
        eclipseInfo = tk.Listbox(height=3, width=60, activestyle='dotbox', font=('Arial', 10))
        eclipseInfo.place(x = 1000, y = 100)

        month = selected_month.get()
        day = selected_day.get()
        year = selected_year.get()

        #print(f"date info: {month}, {day}, {year}")

        eclipse = apcfunc.showEclipses(month, day, year)
        #print(f"GUI Eclipse Info: {eclipse}")

        if eclipse == None:
            eclipseInfo.insert(1, "No Eclipse On This Day")
        else:
            eclipseInfo.insert(1, f"Type of Eclipse: {eclipse[0]}")
            eclipseInfo.insert(2, f"Date of Eclipse: {eclipse[1]}")
            eclipseInfo.insert(3, f"Location of Eclipse: {eclipse[2]}")


    show_btn = tk.Button(root, text="Confirm Date", command=lambda:(show_selection(), showEclipseMenu()))
    show_btn.place(x = 1210, y = 30)

    root.mainloop()
    global dateInfo
    dateInfo = [selected_month.get(), selected_day.get(), selected_year.get()]
    print (dateInfo)


# the planet selection window that shows all the information on the planet selected - Joe
def openPlanetWindow(info):

    # makes sure there is valid information sent into the function before continuing
    if info is None:
        messagebox.showerror(
            "Error",
            "Planet not found in database."
        )
        return

    # creates a window with the title being the name of the planet
    window = tk.Label(text = info[0] + " Major Body Information", font=("Arial", 20))
    window.place(x = 1000, y = 200)
    informationDisplay = tk.Listbox(height = 8, 
                  width = 35, 
                  activestyle = 'dotbox', 
                  font = "ComicSansMS",
                  fg = "black")
    informationDisplay.place(x = 1000, y = 235)
    informationDisplay.insert(1, f"Radius: {info[1]}km")
    informationDisplay.insert(2, f"Mass: {info[2]}kg")
    informationDisplay.insert(3, f"Planet Type: {info[3]}")
    informationDisplay.insert(4, f"Gravitational Pull: {info[4]}m/s^2")
    informationDisplay.insert(5, f"Avg Surface Temperature: {info[5]}°C")
    informationDisplay.insert(6, f"Distance to Sun: {info[6]}AU")
    informationDisplay.insert(7, f"Number of Moons: {info[8]}")
    informationDisplay.insert(8, f"Orbital Period: {info[9]} Earth Years")

# creates a listbox of the planets and places them in the menu
def planet_selection():
    global pSelection
    if pSelection == False:
        # list of planets for selection
        title = ttk.Label(text = "Major Bodies", font=("Arial", 20))
        title.grid(row = 0, column = 0, padx=10, pady=10, sticky="W")

        planetSelect = tk.Listbox(height = 9, 
                  width = 20, 
                  activestyle = 'dotbox', 
                  font = "ComicSansMS",
                  fg = "black")
        planetSelect.grid(row = 1, column = 0, padx=10, pady=10, sticky="W")

        planetSelect.insert(1, "Mercury")
        planetSelect.insert(2, "Venus")
        planetSelect.insert(3, "Earth")
        planetSelect.insert(4, "Mars")
        planetSelect.insert(5, "Jupiter")
        planetSelect.insert(6, "Saturn")
        planetSelect.insert(7, "Uranus")
        planetSelect.insert(8, "Neptune")
        planetSelect.insert(9, "Pluto")
    pSelection = True

    # function inside the planet manu window that when ran will show the appropriate information on the planet selected - Joe
    def show_selected_planet():

        selection = planetSelect.curselection()

        if selection:

            planetName = planetSelect.get(selection[0])     # gets the selected planet from the user

            planetInfo = apcfunc.showPlanetInfo(planetName) # runs the showPlanetInfo function from APC_Functions

            openPlanetWindow(planetInfo)        # calls the planetInfo windows method to pass in information to it for everything to be displayed
    
    # creates a button on the planet selection window which when pressed, will show the appropriate information for the planet selected
    infoButton = tk.Button(root, text="Planet Information",command=show_selected_planet)
    infoButton.grid(row=2, column=0, padx=10, pady=5, sticky="W")

# creates a listbox of the minor bodies and places them in the menu
def com_ast_selection():
    
    global cSelection
    if cSelection == False:
        # list of commets and asteroids for selection
        title = ttk.Label(text = "Small Bodies", font=("Arial", 20))
        title.grid(row = 3, column = 0, padx=10, pady=10, sticky="W")

        cometsAsteroidsSelect = tk.Listbox(height = 10, 
                  width = 20, 
                  activestyle = 'dotbox', 
                  font = "ComicSansMS",
                  fg = "black")
        cometsAsteroidsSelect.grid(row = 4, column = 0, padx=10, pady=10, sticky="W")

        cometsAsteroidsSelect.insert(1, "McNaught")
        cometsAsteroidsSelect.insert(2, "Halleys")
        cometsAsteroidsSelect.insert(3, "Apophis")
        cometsAsteroidsSelect.insert(4, "Neowise")
        cometsAsteroidsSelect.insert(5, "Tsuchinshan-ATLAS")
        cometsAsteroidsSelect.insert(6, "Ceres")
        cometsAsteroidsSelect.insert(7, "Vesta")
    cSelection = True
    
    def small_bodies_info_window():
        # Font selector
        custom_font = "Comic Sans MS"

        # Gets the cursor of what is selected from the list
        for i in cometsAsteroidsSelect.curselection():
            smallbodyselect = cometsAsteroidsSelect.get(i)

        title = ttk.Label(text = smallbodyselect + " Small Body Information", font=("Arial", 20))
        title.place(x = 1000, y = 445)

        informationDisplay = tk.Listbox(height = 5, 
                  width = 35, 
                  activestyle = 'dotbox', 
                  font = "Impact",
                  fg = "black")
        try:
            new_window = tk.Toplevel(root)
            new_window.title("Small Body Image")
            new_window.geometry("720x480")
            comet_img = Image.open(f"Resources/Small_bodies/{smallbodyselect}.jpg")
            resized_image = comet_img.resize((320, 240), Image.LANCZOS)
            tk_image = ImageTk.PhotoImage(resized_image)
            image_label = tk.Label(new_window, image=tk_image)
            image_label.pack(pady=0)
            image_label.image = tk_image
        except:
            print("Error Importing image please try again")

        cursor.execute(f"SELECT * FROM SmallBodies WHERE NAME = '{smallbodyselect}'")
        smallbodiesinfo = cursor.fetchone()

        informationDisplay.place(x = 1000, y = 480)

        smallbodiestype = smallbodiesinfo[1]  
        informationDisplay.insert(1, "Type: " + smallbodiestype)


        smallbodiestype = smallbodiesinfo[2]
        informationDisplay.insert(2, "Location: " + smallbodiestype)


        smallbodiestype = smallbodiesinfo[3]
        informationDisplay.insert(3, "Radius: " + str(smallbodiestype) + " km")


        smallbodiestype = smallbodiesinfo[4]
        informationDisplay.insert(4, "Speed: " + str(smallbodiestype) + " km/sec")

    btn = tk.Button(root, text="Small Bodies Information",command=small_bodies_info_window)
    btn.grid(row=5, column=0, padx=10, pady=5, sticky="W")
    
def solarSystemView():
    global planetAnimation
    if planetAnimation == False:
        sunScreen.resetscreen()
        sunObject.showturtle()
        sunObject.pendown()
        sunObject.shape("circle")
        sunObject.color("yellow")
        
        mercury = Planet("Mercury", 40, 'grey')
        venus = Planet("Venus",80, 'orange')
        earth=Planet("Earth",100,'blue')
        mars = Planet("Mars",150, 'red')
        jupiter=Planet("Jupiter",180, 'brown')
        saturn=Planet("Saturn",230, 'pink')
        uranus=Planet("Uranus",250, 'light blue')
        neptune=Planet("Neptune",280, 'black')
        pluto=Planet("Pluto",300, 'green')
        solarSystem = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    
        while True: #placeholder to calculate angle based on date entered
            canvas.update()
            for i in solarSystem:
                i.move_solarSystem()
            mercury.angle += 0.05
            venus.angle += 0.03
            earth.angle += 0.01
            mars.angle += 0.007
            jupiter.angle += 0.02
            saturn.angle += 0.018
            uranus.angle += 0.016
            neptune.angle += 0.005
            pluto.angle += 0.003
    planetAnimation = True

def planetAndMoonView():
    moonScreen.resetscreen()
    motherPlanet.showturtle()
    motherPlanet.pendown()
    motherPlanet.shape("circle")
    motherPlanet.color("purple")
    
    radius = 40
    moonChildOne = Moon("moon", radius, 'light blue')
    planetAndMoons = [moonChildOne]
    
    while True: #Placeholder to calculate angle based on date entered
        moonCanvas.update()
        for i in planetAndMoons:
            i.move_moonPlanet()
        moonChildOne.angle += 0.05

# creating main window
root = tk.Tk()
root.title('Antikythera')
root.geometry("1920x1080")

# creating solar system graphic location
canvas = tk.Canvas(root, width=650, height=650, bg='white')
canvas.place(x=300, y=0)

sunScreen = turtle.TurtleScreen(canvas)
sunObject = turtle.RawTurtle(sunScreen)
sunObject.penup()
sunObject.setposition(0, 0)
sunObject.hideturtle()

#creating planet and moon view
moonCanvas = tk.Canvas(root, width=350, height=300, bg='white')
moonCanvas.place(x=1000, y=150)

moonScreen = turtle.TurtleScreen(moonCanvas)
motherPlanet = turtle.RawTurtle(moonScreen)
motherPlanet.penup()
motherPlanet.setposition(0,0)
motherPlanet.hideturtle()

#places button to start drawing moon and planet
start_moonPlanet_drawing = tk.Button(root, text="Draw Planet and Moon(s)", command = planetAndMoonView)
start_moonPlanet_drawing.place(x=1120, y=470)

# places a buttone that starts the drawing of the solar system
start_drawing = tk.Button(root, text="Draw System", command=solarSystemView)
start_drawing.place(x = 600, y = 670)

menubar = Menu(root)

# Adding File Menu and commands
planets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Major and Minor Bodies', menu = planets)
# Adds a menu dropdown option to place the planet selection menu in the main window
planets.add_command(label="Open Planet selection", command=planet_selection)
# Adds a menu dropdown that places the comets and asteroid selection
planets.add_command(label="Open Comet and Asteroid selection", command=com_ast_selection)
# Command Menu
command = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Commands', menu = command)
command.add_command(label="Open Date Selection", command=dateSelectionFixed)
command.add_command(label ='Exit Program', command = root.destroy)
root.config(menu = menubar)
mainloop()


# prints final selected date to consol (for testing purposes)
print (dateInfo[0] + " " + dateInfo[1] + " " + dateInfo[2])
