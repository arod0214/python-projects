# Using turtle graphics, draw a 9 x 9 grid
# Hint: Resize the drawing canvas to give coordinates that are easier to use

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
	
    
