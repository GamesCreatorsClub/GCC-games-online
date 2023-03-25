import sys, pygame
pygame.init()
score_font = pygame.font.SysFont("ALPHABETSOUP TILT BT",40)
# Chain together some variables
# to store the screen size
width = 1366
height = 768

size = (width, height)


player_left_score = 0
player_right_score = 0
 
# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [5, -15]
 
# Create a Tuple to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
white = (0, 0, 0)
 
# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(size)
 
# Load the image we want to bounce
# and store it in a variable called 'sprite'
sprite = pygame.image.load("Sprite.png")
paddle1 = pygame.image.load("paddle.png")
paddle1rect = paddle1.get_rect()
paddle2 = pygame.image.load("opponentspaddle.png")
paddle2rect = paddle2.get_rect()
paddle2rect[0] = 1342
line = pygame.image.load("line.png")
linerect = line.get_rect()
 
# Get a bounding rectangle from the sprite  
spriterect = sprite.get_rect()

frameclock = pygame.time.Clock()
# Game State
# 0 = Game Start Screen
# 1 = Game Running
game_state = 0
# Loop forever
while True:

    # Check the event list for a 'quit' event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Get the current state of all the keyboard keys
    pressed_keys = pygame.key.get_pressed()
    
    # === Update Section ====
    # According to game state
    # Game start state
    if game_state == 0:
        if pressed_keys[pygame.K_SPACE]:
            game_state = 1
    # Game running state
    # According to game state:
    # game start screen

 
    elif game_state == 1:
     
        # If the up or down arrows are pressed, move the paddle rect
        if pressed_keys[pygame.K_w]:
            paddle1rect = paddle1rect.move(0, -10)
        if pressed_keys[pygame.K_s]: 
            paddle1rect = paddle1rect.move(0, 10)
        if paddle1rect.top < 0:
            paddle1rect.top = 0    
        if paddle1rect.bottom > height:
            paddle1rect.bottom = height
        if pressed_keys[pygame.K_UP]:
            paddle2rect = paddle2rect.move(0, -10)
        if pressed_keys[pygame.K_DOWN]: 
            paddle2rect = paddle2rect.move(0, 10)
        if paddle2rect.top < 0:
            paddle2rect.top = 0    
        if paddle2rect.bottom > height:
            paddle2rect.bottom = height
              
       # Move the bounding rectangle according to the
        # current velocity
        spriterect = spriterect.move(velocity)
     
        if spriterect.left < 0:
            player_right_score = player_right_score + 1
            spriterect.center = (width/2, height/2)
            
        if spriterect.right > width:
            player_left_score = player_left_score + 1
            spriterect.center = (width/2, height/2)

        if spriterect.colliderect(paddle1rect) or spriterect.colliderect(paddle2rect): 
            # Yes - touching sides of screen so reverse X
            # velocity value
            velocity[0] = -velocity[0]
        if spriterect.top < 0 or spriterect.bottom > height:
            # Yes - touching top/bottom of screen so
            # reverse the Y velocity value
            velocity[1] = -velocity[1]
 
    # Draw everything
    # First clear the screen
    screen.fill(white)

    if game_state == 0:
        title_text = score_font.render("Press Spacebar to Start", 1, (255,255,255))
        screen.blit(title_text, (width/2 - title_text.get_width()/2, height/2 - title_text.get_height()/2))

    elif game_state == 1:
        # Blit the sprite to the current rectangle position
        screen.blit(sprite, spriterect)
        # Flip the screen we've just drawn to the front
        screen.blit(line, (width / 2 - linerect[2] / 2, height / 4))
        screen.blit(line, (width / 2 - linerect[2] / 2, (height / 4) * 2))
        screen.blit(line, (width / 2 - linerect[2] / 2, (height / 4) * 3))

        screen.blit(paddle1, paddle1rect)
        screen.blit(paddle2, paddle2rect)
        score_txt = score_font.render("The Scores Are: " + str(player_left_score) + " vs " + str(player_right_score),1, (24,255,7))
        screen.blit(score_txt, (0,0))

    pygame.display.flip()
   

    frameclock.tick(60)
# end of while loop - go round the loop again!
