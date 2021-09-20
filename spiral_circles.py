# This program draws a design using repeated circles
import turtle

import random

# # Named constants
# NUM_CIRCLES = 36
# RADIUS = 43
# ANGLE = 83
# ANIMATION_SPEED = 0

# # Named constants
# NUM_CIRCLES = 36
# RADIUS = 43
# ANGLE = 88
# ANIMATION_SPEED = 0

# Named constants
NUM_CIRCLES = 36
RADIUS = 43
ANGLE = 88
ANIMATION_SPEED = 0

counter = 1
counterTwo = 50

keepGoing = True

while counter <= 1000:
    
    while keepGoing:
        # Set the animation speed
        turtle.speed(ANIMATION_SPEED)

        # Draw 36 circles, with the turtle tilted
        # by 10 degrees after each circle is drawn
        #for x in range(NUM_CIRCLES):
            
        turtle.colormode(255) 
            
        tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.pencolor(tup)
        turtle.circle(counterTwo)
        turtle.left(counter)
            
            
        counterTwo += 1
        
    counter += 5
