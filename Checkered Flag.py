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
