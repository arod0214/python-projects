##1.  Draw a 4 x 4 grid to the screen (see 2048 Lab).
##2.  Let row = 0
##3.  For each line in the file:
##4.      Split the line into nums
##5.      For i in range(len(nums)):
##6.          Move to (i,row)
##7.          Write nums[i] to the graphics window
##8.      row = row + 1


import turtle 


#Set up the screen and turtle
win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(10)
#Change the coordinates to make it easier to translate moves to screen coordinates:
win.setworldcoordinates(-0.5,3.5,4.5,-1.0)
tic.penup()
row = 0
file = open("input.txt",'r')

for line in file:
    nums = line.split(",")
    for i in range(len(nums)):
        tic.goto(i,row)
        tic.write(nums[i])
    row = row +1
