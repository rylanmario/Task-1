# Name: calculator.py
# Author: Rylan Fessey
# Date created: October 2nd, 2022
# Date last modified: October 3nd, 2022
# Purpose: This program will take the dimensions of shapes, and calculate the area and parameter of the shape chosen.

from math import pi

#Main menu for the program
print("Geometry Calculator")
print("\n")
print("1. Calculate the area of a circle")
print("2. Calculate the area of a rectangle")
print("3. Calculate the area of a triangle")
print("4. Quit")
print("\n")
selection = float(input("Enter your choice (1-4): "))

#If statements for selections
if (selection == 1):
    radius = float(input("What is the radius of the circle in cm: "))
    circlearea = pi * radius**2
    circumfrence = 2 * pi * radius
    print("The area of the circle is", circlearea, "cm2")
    print("The circumference of the circle is", circumfrence, "cm")
    print("\n")
    input("Press any key to exit")
#Calculations for Circle

elif (selection == 2):
    recwidth = float(input("What is the width of the rectangle in cm: "))
    reclength = float(input("What is the length of the rectangle in cm: "))
    recarea = reclength * recwidth 
    recpermimeter = (reclength + recwidth) * 2
    print("The perimeter of the rectangle is", recpermimeter, "cm.")
    print("The area of the rectangle is", recarea, "cm2")
    print("\n")
    input("Press any key to exit")
# Calculations for rectangle

elif (selection == 3):
    base = float(input("What is the length of the triangles base: "))
    side1 = float(input("What is the length of the triangles second side: "))
    side2 = float(input("What is the length of the triangles third side: "))
    height = float(input("what is the height of the triangle: "))
    tripermimeter = base + side1 + side2
    triarea = base * height / 2
    print("The permimeter of the triangle is", tripermimeter, "cm")
    print("The area of the triangle is", triarea, "cm2")
    print("\n")
    input("Press any key to exit")
# Calculations for triangle

elif (selection == 4):
    quit()
# Quit command for user if they want to leave

else:
    print("Invalid Number. Please choose option 1-4")
# What will be displayed if the user types a number that is not 1-4.