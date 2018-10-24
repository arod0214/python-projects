# Write a program that asks the user for a max radius, and prints out a chart of the radius and area of a circle, where the radius starts at 1 and goes up to the max radius. (Assume the user enters a positive integer as the max radius.)


import turtle 
win = turtle.Screen()
tic = turtle.Turtle()
win.setworldcoordinates(-10,-10,15,15)

for i in range(1,11):
    tic.penup()
    tic.goto(1,i)
    tic.pendown()
    tic.forward(9)

tic.left(90)    
for i in range(1,11):
	tic.penup()
	tic.goto(i,1)
	tic.pendown()
	tic.forward(9)
	
    
