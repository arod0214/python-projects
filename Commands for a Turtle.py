# The program turtleString.py takes a string as input and uses that string to control what the turtle draws on the screen (inspired by code.org's graph paper programming). Currently, the program processes the following commands:

# 'F': moves the turtle forward
# 'L': turns the turtle 90 degrees to the left
# 'R': turns the turtle 90 degrees to the right
# '^': lifts the pen
# 'v': lowers the pen

# For example, if the user enters the string "FLFLFLFL^FFFvFLFLFLFL", the turtle would move forward and then turn left. It repeats this 4 times, drawing a square. Next, it lifts the pen and move forward 3, puts the pen back down and draw another square.

# Modify this program to allow the user also to specify with the following symbols:

# 'B': moves the turtle backwards
# 'r': change the pen color to red
# 'g': change the pen color to green
# 'b': change the pen color to blue


import turtle

def doAction(t,c):
    if c == 'F':            #move forward
        t.forward(50)
    elif c == 'L':          #turn left
        t.left(90)
    elif c == 'R':          #turn right
        t.right(90)
    elif c == '^':          #lift pen
        t.up()
    elif c == 'v':          #lower pen
        t.down()
    elif c == 'B':
        t.backward(50)
    elif c == 'r':
        t.color("red")
    elif c == 'g':
        t.color("green")
    elif c == 'b':
        t.color("blue")
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", c)


def main():
    silas = turtle.Turtle()
    myWin = turtle.Screen()     #The graphics window
    commands = input("Please enter a command string: ")
    for ch in commands:         # Loop once for each letter in the string commands.
                               # The letter for each time through the loop is stored in ch.
        doAction(silas,ch)

    print("See graphics window for your image")
    myWin.exitonclick()         #Close the window when clicked

main()
