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
