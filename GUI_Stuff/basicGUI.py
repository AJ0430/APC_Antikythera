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
#from PIL import Image, ImageTk
import sqlite3

#database = sqlite3.connect("Database_Stuff/AntikytheraSystem.db")
#cursor = database.cursor()


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


month = "January"
day = 1
year = 2000
global runProgram
runProgram = True
global pSelection
global cSelection
pSelection = False
cSelection = False
global planetAnimation
planetAnimation = False

def exitPLEASE():
    global runProgram
    runProgram = False
    root.destroy()

def backToDateSelect():
    root.destroy()
    global pSelection
    global cSelection
    pSelection = False
    cSelection = False
    global planetAnimation
    planetAnimation = False

# date selection window
def dateSelect():
    # Create main application window
    root = tk.Tk()
    root.title("Date Selection")
    root.geometry("500x500")

    # List of Months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Makes January the default selection in the dropdown
    selected_month = tk.StringVar(value=months[0])  # Default value

    # Create dropdown
    monthDropdown = tk.OptionMenu(root, selected_month, *months)  # Call changeDay when month changes
    #monthDropdown.config(width=15)  
    monthDropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")


    # List of Years (2000 to 2030)
    years = [str(year) for year in range(2000, 2031)]

    # Makes 2000 the default selection in the dropdown
    selected_year = tk.StringVar(value=years[0])  # Default value

    # Create dropdown
    yearDropdown = tk.OptionMenu(root, selected_year, *years)  # Call changeDay when year changes
    yearDropdown.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    
    # Makes 1st the default selection in the dropdown
    days = [str(day) for day in range(1, 32)]
    selected_day = tk.StringVar(value=days[0])  # Default value

    # Create dropdown
    dayDropdown = tk.OptionMenu(root, selected_day, *days) 
    dayDropdown.grid(row=0, column=1, padx=10, pady=10, sticky="n")


    # Button to show current selection
    def show_selection():
        if selected_year.get() in ["2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028"] and selected_month.get() == "February" and (selected_day.get() == "30" or selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have " + selected_day.get() + " days in the year " + selected_year.get() + ".")
            messagebox.showinfo("Current Selection", f"{current}")
        elif selected_month.get() == "February" and selected_year.get() not in ["2000", "2004", "2008", "2012", "2016", "2020", "2024", "2028"] and (selected_day.get() == "29" or selected_day.get() == "30" or selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have " + selected_day.get() + " days in the year " + selected_year.get() + ".")
            messagebox.showinfo("Current Selection", f"{current}")
        elif selected_month.get() in ["April", "June", "September", "November"] and (selected_day.get() == "31"):
            current = ("Invalid date selection: " + selected_month.get() + " does not have 31 days.")
            messagebox.showinfo("Current Selection", f"{current}")
        else:
            current = "Current Selection: " + selected_month.get() + " " + selected_day.get() + ", " + selected_year.get()
            root.destroy()  # Close the date selection window after a valid selection


    show_btn = tk.Button(root, text="Confirm Date", command=show_selection)
    show_btn.grid(row=1, column=1, columnspan=2, pady=20)
    root.bind("<Return>", lambda event: show_selection())

    # Run the Tkinter event loop
    root.mainloop()
    return [selected_month.get(), selected_day.get(), selected_year.get()]


#asteroid and comet selection window
small_font = False
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
    cometsAndAsteroidsSelect.insert(1, "McNaught")
    cometsAndAsteroidsSelect.insert(2, "Halleys")
    cometsAndAsteroidsSelect.insert(3, "Apophis")
    cometsAndAsteroidsSelect.insert(4, "Neowise")
    cometsAndAsteroidsSelect.insert(5, "Tsuchinshan-ATLAS")
    cometsAndAsteroidsSelect.insert(6, "Ceres")
    cometsAndAsteroidsSelect.insert(7, "Vesta")

# Print out the information related to small bodies im messing with this so it can add a text box that explains the small body within the database
    def small_bodies_info_window():

        global small_font
        # Font selector
        random_font = id(object()) % 100
        if small_font == False:
            if random_font < 1:
                custom_font = "Wingdings"
            else:
                custom_font = "Comic Sans MS"
        else:
            custom_font = "Comic Sans MS"
        
        small_font = True

        # Gets the cursor of what is selected from the list
        for i in cometsAndAsteroidsSelect.curselection():
            smallbodyselect = cometsAndAsteroidsSelect.get(i)

        
        new_window = tk.Toplevel(root)
        new_window.title(f"{smallbodyselect}")
        new_window.geometry("720x480")
        comet_img = Image.open(f"Resources/Small_Bodies/{smallbodyselect}.jpg")
        resized_image = comet_img.resize((320, 240), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(new_window, image=tk_image)
        image_label.pack(pady=0)
        image_label.image = tk_image
        Title = tk.Label(new_window, text=f"Information on {smallbodyselect}", font=(f"{custom_font}", 15))
        Title.pack(pady=0)

        cursor.execute(f"SELECT * FROM SmallBodies WHERE NAME = '{smallbodyselect}'")
        smallbodiesinfo = cursor.fetchone()

        smallbodiestype = smallbodiesinfo[1]  
        Size_label = tk.Label(new_window, text=f"Type: {smallbodiestype}", font=("Impact", 15))
        Size_label.pack(pady=0)


        smallbodiestype = smallbodiesinfo[2]
        Size_label = tk.Label(new_window, text=f"Position: {smallbodiestype}", font=("Impact", 15))
        Size_label.pack(pady=0)


        smallbodiestype = smallbodiesinfo[3]
        Size_label = tk.Label(new_window, text=f"Size: {smallbodiestype}km", font=("Impact", 15))
        Size_label.pack(pady=0)


        smallbodiestype = smallbodiesinfo[4]
        Size_label = tk.Label(new_window, text=f"Speed: {smallbodiestype}km/s", font=("Impact", 15))
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
    global pSelection
    if pSelection == False:
        # list of planets for selection
        title = ttk.Label(text = "Planet Selection", font=("Arial", 20))
        title.grid(row = 0, column = 0, padx=10, pady=10, sticky="N")

        planetSelect = tk.Listbox(height = 10, 
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

def com_ast_selection():
    global cSelection
    if cSelection == False:
        # list of commets and asteroids for selection
        title = ttk.Label(text = "Small Bodies", font=("Arial", 20))
        title.grid(row = 3, column = 0, padx=10, pady=10, sticky="N")

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
    
def solarSystemView():
    global planetAnimation
    if planetAnimation == False:
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
    planetAnimation = True



runProgram = True
while runProgram == True:
    dateInfo = dateSelect()
    print("Selected Date: ", dateInfo[0], dateInfo[1], dateInfo[2])
    # creating main window
    root = tk.Tk()
    root.title('Antikythera')
    root.geometry("1920x1080")

    #creating solar system graphic location
    canvas = tk.Canvas(root, width=650, height=650, bg='white')
    canvas.place(x=300, y=0)

    screen = turtle.TurtleScreen(canvas)
    my_turtle = turtle.RawTurtle(screen)
    my_turtle.penup()
    my_turtle.setposition(0, 0)
    my_turtle.hideturtle()

    start_drawing = tk.Button(root, text="Draw System", command=solarSystemView)
    start_drawing.place(x = 575, y = 670)

    selectDate = tk.Button(root, text="Select Date", command=backToDateSelect)
    selectDate.place(x = 675, y = 670)

    menubar = Menu(root)

    # Adding File Menu and commands
    planets = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Planets', menu = planets)
    planets.add_command(label="Open Planet selection", command=planet_selection)

    # Adding File Menu and commands
    cometsAndAsteroids = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Comets and Asteroids', menu = cometsAndAsteroids)
    cometsAndAsteroids.add_command(label="Open Comet and Asteroid selection", command=com_ast_selection)

    # Command Menu
    command = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Commands', menu = command)
    command.add_command(label ='Exit Program', command = exitPLEASE)
    root.config(menu = menubar)
    mainloop()