import sys, pygame
pygame.init()
import pygame, Buttons
import pygame, Example
from pygame.locals import *

#game state
#1 = running
#0 = Game start screen
game_state = 0

score_font = pygame.font.SysFont("Jokerman", 40)
score_font1 = pygame.font.SysFont("Jokerman", 100)

#Caption
pygame.display.set_caption("Naeem's Awesome Pong Game")

# Colour Defintions
white = pygame.Color(255,255,255)
black = pygame.Color( 0, 0 ,0)
gray = pygame.Color(90, 90, 90)
silver = pygame.Color( 200, 200, 200)
red = pygame.Color( 200, 0 , 0)
blue = pygame.Color(0, 255, 0)
##background
#pointes
score1 = 0
score2 = 0
 
# Chain together some variables
# to store the screen size
size = width, height = 1024, 640
 
# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [19, -27]
 
# Create a Tuple to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
 
# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(size)
 
# Load the image we want to bounce
# and store it in a variable called 'sprite'
paddle1 = pygame.image.load("paddle.png")
sprite = pygame.image.load("sprite01.png")
background = pygame.image.load("Background.png")
paddle2 = pygame.image.load("paddle.png")
StartScreen = pygame.image.load("Start Screen.png")
P1Gameover = pygame.image.load("Game_OverP1.png")
P2Gameover = pygame.image.load("Game_OverP2.png")


 
# Get a bounding rectangle from the sprite
spriterect = sprite.get_rect()
spriterect = spriterect.move(512, 0)
backgroundrect = background.get_rect()
paddle1rect = paddle1.get_rect()
paddle1rect[0]= 10
paddle2rect = paddle2.get_rect()
paddle2rect[0] = 980
Startrect = StartScreen.get_rect()
GMp1rect = P1Gameover.get_rect()
GMp2rect = P2Gameover.get_rect()


 #Making the clock
clock = pygame.time.Clock()
#timer
timer = 2000

# Loop forever
while True:

    # Check the event list for a 'quit' event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    #game start section
    if game_state == 0:
        screen.blit(StartScreen, Startrect)
        # Flip the screen we've just drawn to the front
        pygame.display.flip()
        #Wait 120ms
        clock.tick(30)
        
        if pressed_keys[pygame.K_SPACE]:
            game_state = 1
            timer = 2000

    elif game_state == 2:
        if score1 < score2:
            screen.blit(P1Gameover, GMp1rect)
        else:
            screen.blit(P2Gameover, GMp2rect) 
        # Flip the screen we've just drawn to the front
        pygame.display.flip()
        #Wait 120ms
        clock.tick(30)
        
        if pressed_keys[pygame.K_SPACE]:
            game_state = 0
            timer = 2000
            score1 = 0
            score2 = 0
            

    elif game_state == 1:
        

        score_txt1 = score_font.render("Score :" + str(score1), 1, (red))
        score_txt2 = score_font.render("Score :" + str(score2), 1, (red))
            

        #Get the what the current key is

        #if up or down move the paddle
        if pressed_keys[pygame.K_UP]:
            paddle1rect = paddle1rect.move(0, -20)
        if pressed_keys[pygame.K_DOWN]:
            paddle1rect = paddle1rect.move(0, 20)

        if pressed_keys[pygame.K_w]:
            paddle2rect = paddle2rect.move(0, -20)
        if pressed_keys[pygame.K_s]:
            paddle2rect = paddle2rect.move(0, 20)


        #The Paddle collision so it does'nt go off screen

        if paddle1rect.top < 0:
            paddle1rect.top = 0     
        if paddle1rect.bottom > height:
            paddle1rect.bottom = height

        # The second players collison
        if paddle2rect.top < 0:
            paddle2rect.top = 0
        if paddle2rect.bottom > height:
            paddle2rect.bottom = height


        # Move the bounding rectangle according to the
        # current velocity
        if timer < 0: 
            spriterect = spriterect.move(velocity)
        else:
            timer = timer - clock.get_time()
        # Check of the bounding rectangle has touched the
        # edges of the window.

        #Other players 

        if spriterect.right > width:
            score2 = score2 + 1
            spriterect.center = (width/2, height/2)
            
        if spriterect.left < 0:
            score1 = score1 + 1
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
        # Blit the sprite to the current rectangle position
        screen.blit(background, backgroundrect)
        screen.blit(sprite, spriterect)
        screen.blit(paddle1, paddle1rect)
        screen.blit(paddle2, paddle2rect)
        
        screen.blit(score_txt1,(50,0))
        screen.blit(score_txt2,(850, 0))

        if ((score1 - score2) < -10) or ((score1 - score2) > 10):
                game_state = 2
            
        
        # Flip the screen we've just drawn to the front
        pygame.display.flip()
        #Wait 120ms
        clock.tick(30)
        
    # end of while loop - go round the loop again!
