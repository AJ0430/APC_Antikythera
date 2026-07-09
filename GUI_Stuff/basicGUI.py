import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
import turtle
from turtle import title
from solarSystemView import *

#asteroid and comet selection window
def open_CometsAsteroids_window():
# select an option from a menu
# create a root window.
    top = tk.Tk()

# create listbox object
    cometsAndAsteroidsSelect = Listbox(top, height = 10, 
                  width = 45, 
                  bg = "black",
                  activestyle = 'dotbox', 
                  font = "ComicSansMS",
                  fg = "white")

# Define the size of the window.
    top.geometry("600x600")  

# Define a label for the list.  
    label = Label(top, text = "Small Bodies in the Solar System") 

# insert elements by their
# index and names.
    cometsAndAsteroidsSelect.insert(1, "Comet McNaught")
    cometsAndAsteroidsSelect.insert(2, "Halley's Comet")
    cometsAndAsteroidsSelect.insert(3, "Apophis Asteroid")
    cometsAndAsteroidsSelect.insert(4, "Comet Neowise")
    cometsAndAsteroidsSelect.insert(5, "Comet Tsuchinshan-ATLAS")
# pack the widgets
    label.pack()
    cometsAndAsteroidsSelect.pack()


# Display until User 
# exits themselves.
    top.mainloop()

def planet_selection():
    # list of planets for selection

    title = ttk.Label(text = "Planet Selection", font=("Arial", 20))
    title.pack(pady=10, anchor="w")

    planetSelect = tk.Listbox()
    planetSelect.pack(anchor="w")

    planetSelect.insert(1, "Mercury")
    planetSelect.insert(2, "Venus")
    planetSelect.insert(3, "Earth")
    planetSelect.insert(4, "Mars")
    planetSelect.insert(5, "Jupiter")
    planetSelect.insert(6, "Saturn")
    planetSelect.insert(7, "Uranus")
    planetSelect.insert(8, "Neptune")
    planetSelect.insert(9, "Pluto")
    
def solarSystemView():
    title = ttk.Label(text = "Solar System", font=("Arial", 20))
    title.pack(pady=10, anchor="n")
    
    screen = turtle.Screen()
    screen.tracer(50)
    
    sun.shape('circle')
    sun.color('yellow')
    
    mercury = Planet("Mercury", 40, 'grey')
    
    solarSystem = [mercury]
    
    while True: #placeholder to calculate angle based on date entered
        screen.update()
        for i in solarSystem:
            i.move()
        mercury.angle += 0.05
    
# creating main window
root = Tk()
root.title('Antikythera')
root.geometry("1200x600")

# Creating Menubar
menubar = Menu(root)

# Adding File Menu and commands
planets = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Planets', menu = planets)
planets.add_command(label="Open Planet selection", command=planet_selection)
planets.add_separator()
planets.add_command(label ='Exit', command = root.destroy)

solarSystemMenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Solar System View", command=solarSystemView)
solarSystemMenu.add_separator()
solarSystemMenu.add_command(label='Exit', command = root.destroy)

# Adding File Menu and commands
cometsAndAsteroids = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Comets and Asteroids', menu = cometsAndAsteroids)
cometsAndAsteroids.add_command(label="Open Comet and Asteroid selection", command=open_CometsAsteroids_window)
cometsAndAsteroids.add_separator()

# Command Menu
command = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Commands', menu = command)
command.add_command(label ='Search', command = None)
command.add_separator()
command.add_command(label ='Exit Program', command = root.destroy)

planet_selection

# display Menu
root.config(menu = menubar)
mainloop()
