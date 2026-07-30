# Replicate Antikythera

## Applied Programming Concepts (ELEC 3225)

## Professor Rawlins

## Summer 2026

```
Written by: Harrison Brown, Rafael Enamorado, Joe Machado, Milo Silverman, Ashton Vallejo, & David Vozzo
```
## Table of Contents:

## Section I: Introduction

### ❖ I.a: General Introduction

### ❖ I.b: Initial Setup

## Section II: Running the Program

## Section III: Interacting with the GUI

### ❖ III.a: Draw System Function

### ❖ III.b: Major and Minor Bodies Menu

### ❖ III.c: Commands Menu

## Section IV: Other Functions/Program Highlights

### ❖ IV.a: Viewing Planet Information

### ❖ IV.b: Alternate Way to Exit Program


## Section I: Introduction

### Section I.a: General Introduction:

Welcome to the Replicate Antikythera User Manual.

This guide will explain to you how to use this program’s features, which include:
● Seeing where planets will be located in the solar system on a particular date
● Planet information based on planet that is chosen
● Information on Earth’s Moon
● Highlight any comets/asteroids that occurred on a particular date
● Highlight any lunar/solar eclipses that occurred on a particular date
● Show Zodiac Constellations based on the date that is chosen

**Before you begin, please read the section below on the setup you must complete prior to running this code:**

### Section I.b: Initial Setup:

Please see the instructions on how to get the program to run properly below:

(This is a **Draft**. Update this section when you have a working code.)

1. Open the github link
2. Clone the repository to VS Code (or VS?)
3. Install necessary libraries using: python -m pip install -r requirements.txt
4. Install Python extension in VS Code (if not already installed)
6. Run "APC Project.py" to start the program


## Section II: Running the Program

When you want to run the program, you’ll want to make sure you’re in the “basic_GUI.py” file as that is where
most of this project runs from. This file is located in the “GUI Stuff” folder.

When you have the �le open, just press the “Run” button to begin (Play button in VS Code, and by pressing Ctrl
+ F5 in VS)

You should see the GUI pop up in front of you.

## Section III: Interacting with the GUI

When you �rst open the program, you will see a window that looks like this:

This is the main window that you will interact with and where all the menus will show up in (when you open
them). You will �rst a white box with a button below it labeled “Draw System”. This will be where a solar system
model will show up with an animation of the planets revolving around the sun.


The only other thing on here that is worth noting is the menu bar. There are two main menus that are here are the
“Major and Minor Bodies” which allows you to choose what astronomical bodies you want to see the information
on. The other menu is called “Commands”, and in that menu it allows you to bring up the date selection as well as
an alternate way to quit the program.

### Section III.a: Draw System Function

When you press the “Draw System” button, it will do a small animation of all the planets coming out from the
center and then start revolving around a yellow circle (which is meant to be the Sun). This function will
continuously loop until you exit the program.

### Section III.b: Major and Minor Bodies Menu

When you �rst open the “Major and Minor Bodies” menu, you’ll see two options, one for “Open Planet Selection”
and one for “Open Comet and Asteroid Selection”. When you press the _Planet Selection_ menu, you will see a small
selection window that will pop up with all the planets and a button that says “Planet Information”. The _Planet
Information_ button will be mentioned in Section IV.a. Similarly, when you press the _Comet and Asteroid Selection_


menu, you will see a selection menu for all the comets and asteroids as well as a button to similar to the one above
called “Small Bodies Information”. The comet information button will be explained in Section IV.b.

When both menus are open at the same time your screen will look something like this:

### Section III.c: Commands Menu

The _Commands_ menu doesn’t really have much to it. The only thing that is worth noting in this menu is the
“Open Date Selection” command. This brings up a small date selection window on the right side of the solar
system block. All the selection options here are dropdown menus, so when you select your options, just use the
dropdown menu to select your date.

The date selection will look something like this:


## Section IV: Other Functions/Program Highlights

### Section IV.a: Viewing Planet Information

The _Planet Information_ button allows you to see some information on the selected planet in the _Planet Selection_
menu.
If no planet is selected, then when the button is pressed nothing will happen.
An example is shown below for the planet _Neptune_ :


### Section IV.b: Viewing Small Bodies Information

The small bodies Information button allows you to have a general overview on the small body selected. Select a
small body using your cursor and press _the Small Bodies Information_ Button to display general information about
any small body in the list.

Here is an example of general information on Neowise being displayed.


### Section IV.c: Alternate Way to Exit Program

If for some reason you don’t want to you use the “X” in the corner of the window to quit, you can also press the
_Exit Program_ button in the _Commands_ menu to exit the program.

The photo below shows the _Exit Program_ button highlighted:



