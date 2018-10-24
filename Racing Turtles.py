# Work through the Turtle Racing Lab in the textbook.  Submit your code with step 5 completed.  You may use any of the given suggestions or your own idea to complete step 5.  

# Turtle Racing Lab: http://interactivepython.org/courselib/static/thinkcspy/Labs/lab03_01.html



import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('yellow')

amy = turtle.Turtle()    # 3.  Create two turtles
mike = turtle.Turtle()
amy.color('purple')
mike.color('blue')
amy.shape('turtle')
mike.shape('turtle')

mike.up()                  # 4.  Move the turtles to their starting point
amy.up()
mike.goto(-100,20)
amy.goto(-100,-20)

for i in range(5):
    mike.forward(random.randrange(150,201))
    amy.forward(random.randrange(150,201))

wn.exitonclick()
    
                  
