import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
from turtle import title


# planet selection window (obsolete?)
def open_planet_window():

 # Create a popup window
    popup = tk.Toplevel(root)
    #popup.overrideredirect(True)
    popup.geometry("300x200")

    # Create a Listbox inside the popup
    planetSelect = tk.Listbox(popup)
    planetSelect.pack(fill="both", expand=True)

    planetSelect.insert(1, "Mercury")
    planetSelect.insert(2, "Venus")
    planetSelect.insert(3, "Earth")
    planetSelect.insert(4, "Mars")
    planetSelect.insert(5, "Jupiter")
    planetSelect.insert(6, "Saturn")
    planetSelect.insert(7, "Uranus")
    planetSelect.insert(8, "Neptune")
    planetSelect.insert(9, "Pluto")

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
    label = Label(top, text = "Planets in the Solar System") 

# insert elements by their
# index and names.
    cometsAndAsteroidsSelect.insert(1, "Mercury")
    cometsAndAsteroidsSelect.insert(2, "Venus")
    cometsAndAsteroidsSelect.insert(3, "Earth")
    cometsAndAsteroidsSelect.insert(4, "Mars")
    cometsAndAsteroidsSelect.insert(5, "Jupiter")
    cometsAndAsteroidsSelect.insert(6, "Saturn")
    cometsAndAsteroidsSelect.insert(7, "Uranus")
    cometsAndAsteroidsSelect.insert(8, "Neptune")
    cometsAndAsteroidsSelect.insert(9, "Pluto")

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
