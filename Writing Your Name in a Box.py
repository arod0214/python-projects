# Use turtle graphics to write your name to the screen, surrounded by a box or polygon. You may write your name in "cursive" by moving the turtle, or may use the write() command to have it printed to the graphics screen. 


import turtle
win = turtle.Screen()
x = turtle.Turtle()

for i in range(4):
    x.forward(100)
    x.left(90)

x.write("Amanda")
