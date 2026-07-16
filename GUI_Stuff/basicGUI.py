import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
import turtle
from turtle import title
from math import *

class Planet(turtle.RawTurtle):
    def __init__(self, name, radius, color):
        super().__init__(screen, shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle) #Angle in radians
        y = self.radius*sin(self.angle)
        
        self.goto(my_turtle.xcor()+x, my_turtle.ycor()+y)

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
    my_turtle.showturtle()
    my_turtle.pendown()
    my_turtle.shape("circle")
    my_turtle.color("yellow")
    
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
            i.move()
        mercury.angle += 0.05
        venus.angle += 0.03
        earth.angle += 0.01
        mars.angle += 0.007
        jupiter.angle += 0.02
        saturn.angle += 0.018
        uranus.angle += 0.016
        neptune.angle += 0.005
        pluto.angle += 0.003
    
# creating main window
root = tk.Tk()
root.title('Antikythera')
root.geometry("1920x1080")

#creating solar system graphic location
canvas = tk.Canvas(root, width=650, height=650, bg='white')
canvas.place(anchor=tk.CENTER)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
my_turtle = turtle.RawTurtle(screen)
my_turtle.penup()
my_turtle.setposition(0, 0)
my_turtle.hideturtle()

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
