import sys, pygame, random

pygame.init()

alpha = 0 

# Chain together some variables
# to store the screen size
screensize = width, height = 1024, 1024


# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [1, -3]


# Create a Tuple to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
black = (0, 0, 0)
blue = (144, 255, 255)
 

# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(screensize)

 

# Load the image we want to bounce
# and store it in a variable called 'mrbounce'
mrbounce = pygame.image.load("mrbounce.png")
 

# Get a bounding rectangle from the mrbounce
mrbouncerect = mrbounce.get_rect()



# Loop forever
while True:
    
    # Check the event list for a 'quit' event
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

 
    # Move the bounding rectangle according to the
    # current velocity
    mrbouncerect = mrbouncerect.move(velocity)

 

    # Check of the bounding rectangle has touched the
    # edges of the window.
    if mrbouncerect.left < 0 or mrbouncerect.right > width:
        # Yes - touching sides of screen so reverse X
        # velocity value
        velocity[0] = -velocity[0] + random.randint(-2, 2)
        
    if mrbouncerect.top < 0 or mrbouncerect.bottom > height:
        # Yes - touching top/bottom of screen so
        # reverse the Y velocity value
        velocity[1] = -velocity[1] + random.randint(-2, 2)

    alpha += 1
    rotatedmrbounce = pygame.transform.rotate(mrbounce, alpha)
 

    # Draw everything
    # First clear the screen
    screen.fill(blue)
    # Blit the mrbounce to the current rectangle position
    screen.blit(rotatedmrbounce, mrbouncerect)
    # Flip the screen we've just drawn to the front

    pygame.display.flip()

# end of while loop - go round the loop again!
