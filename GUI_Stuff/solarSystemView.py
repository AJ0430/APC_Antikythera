import turtle
from math import *

sun=turtle.Turtle()

class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__(shape='circle')
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
        
        self.goto(sun.xcor()+x, sun.ycor()+y)