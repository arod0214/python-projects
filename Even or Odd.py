import turtle
win = turtle.Screen()
x = turtle.Turtle()

num = int(input("Enter a number:"))
if num % 2 == 0:
    x.color("blue")
    x.left(180)
    x.forward(100)
else:
    x.color("red")
    x.forward(100)
