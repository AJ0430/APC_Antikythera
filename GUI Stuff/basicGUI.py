import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from time import strftime
from tkinter import ttk
from turtle import title
from tkinter import messagebox
from PIL import Image, ImageTk


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
    label = Label(top, text = "Small Bodies in the Solar System") 

# insert elements by their
# index and names.
    cometsAndAsteroidsSelect.insert(1, "Comet McNaught")
    cometsAndAsteroidsSelect.insert(2, "Halley's Comet")
    cometsAndAsteroidsSelect.insert(3, "Apophis Asteroid")
    cometsAndAsteroidsSelect.insert(4, "Comet Neowise")
    cometsAndAsteroidsSelect.insert(5, "Comet Tsuchinshan-ATLAS")

# Print out the information related to small bodies im messing with this so it can add a text box that explains the small body within the database
    def small_bodies_info_window():
        
        random_font = id(object()) % 100
        if random_font < 1:
            custom_font = "Wingdings"
        else:
            custom_font = "Comic Sans MS"
        # Gets the cursor of what is selected from the list
        for i in cometsAndAsteroidsSelect.curselection():
            smallbodyselect = cometsAndAsteroidsSelect.get(i)
        new_window = tk.Toplevel(root)
        new_window.title(f"{smallbodyselect}")
        new_window.geometry("720x480")
        comet_img = Image.open(f"Resources/Small bodies/{smallbodyselect}.jpg")
        resized_image = comet_img.resize((320, 240), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(new_window, image=tk_image)
        image_label.pack(pady=0)
        image_label.image = tk_image
        Title = tk.Label(new_window, text=f"Information on {smallbodyselect}", font=(f"{custom_font}", 15))
        Title.pack(pady=0)
        Size_label = tk.Label(new_window, text=f"Type: ", font=("Impact", 15))
        Size_label.pack(pady=0)
        Size_label = tk.Label(new_window, text=f"Position: ", font=("Impact", 15))
        Size_label.pack(pady=0)
        Size_label = tk.Label(new_window, text=f"Size: ", font=("Impact", 15))
        Size_label.pack(pady=0)
        Size_label = tk.Label(new_window, text=f"Speed: ", font=("Impact", 15))
        Size_label.pack(pady=0)


    btn = Button(top, text='Information', command=small_bodies_info_window)

# pack the widgets
    btn.pack(side='bottom')
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
