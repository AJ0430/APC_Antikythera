import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
import turtle
from turtle import title
from math import *

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
        

def createPlanetAndMoonPopUp():
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


#creating popup
popup = tk.Toplevel()
popup.title("Planet and Moon")
popup.config(width=350, height=300)

#creating planet and moon view
moonCanvas = tk.Canvas(popup, width=350, height=300, bg='white')
moonCanvas.place()

moonScreen = turtle.TurtleScreen(moonCanvas)
motherPlanet = turtle.RawTurtle(moonScreen)
motherPlanet.penup()
motherPlanet.setposition(0,0)
motherPlanet.hideturtle()

#places button to start drawing moon and planet
start_moonPlanet_drawing = tk.Button(text="Draw Planet and Moon(s)", command = createPlanetAndMoonPopUp)
start_moonPlanet_drawing.place(x=1120, y=470)