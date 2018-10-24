# Implement the following pseudocode to draw a checkered flag to the screen.

# 1.  Ask the user for the size of the checkered flag (n).
# 2.  Draw an n x n grid to the screen.
# 3.  For i = 0,2,4,...,n*n-1:
# 4.     row = i // n
# 5.     offset = row % 2
# 6.     col = (i % n) + offset
# 7.     fillSquare(row,col,"black")

# You do not have to use main(), a function, or a file for this program.

from turtle import *

n = input("Enter the size of the checkered flag (n)")

  
def setUpScreen(n):
    win = Screen()
    win.setworldcoordinates(-0.5, n+0.5,n+0.5,-0.5)
    return win

def drawGrid(n):
    tic = Turtle()
    tic.speed(10)
    #Draw the vertical bars of the game board:
    for i in range(0,n+1):
        tic.up()
        tic.goto(0,i)
        tic.down()
        tic.forward(n)  


def fillSquare(row,col,color):
    color = tic.color("black")
    for i = n*n-1:
        row = i // n
        offset = row % 2
        col = (i % n) + offset
    t = Turtle()
    t.hideturtle()  #Hides cursor and speeds up drawing
    t.speed(10)
    t.up()
    t.goto(x,y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(1)
        t.left(90)
    t.end_fill()
