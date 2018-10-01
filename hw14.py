import turtle 


#Set up the screen and turtle
win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(10)
#Change the coordinates to make it easier to translate moves to screen coordinates:
win.setworldcoordinates(-1.5,-1.5,5.5, 5.5)

#Draw the horizontal bars of the game board:
for i in range(1,6):
	tic.penup()
	tic.goto(1,i)
	tic.pendown()
	tic.forward(4)

#Draw the vertical bars of the game board:
tic.left(90)    #Point the turtle in the right direction before drawing
for i in range(1,6):
	tic.penup()
	tic.goto(i,1)
	tic.pendown()
	tic.forward(4)

tic.penup()

for i in range(4):
   x = int(input("Enter x coordinate for X's move: "))
   y = int(input("Enter y coordinate for X's move: "))
   tic.goto(x+1.25,y+1.25)
   tic.write("2",font=('Arial', 40, 'normal'))
   z = input("Hit the enter key.")
   tic.goto(1.25,y+1.25)
   tic.write("2",font=('Arial', 40, 'normal'))

