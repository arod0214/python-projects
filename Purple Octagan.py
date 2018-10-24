# Write a program that draws a purple octagon on the screen using turtles.


import turtle
win = turtle.Screen()
x = turtle.Turtle()

for i in range (8):
    x.color("purple")
    x.forward(100)
    x.left(45)
    
