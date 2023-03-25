import sys
import pygame

pygame.init()

# Chain together some variables
# to store the screen size
size = width, height = 1024, 700
STARTING = 0
PLAYING = 1
game_status = STARTING

# Create a velocity List variable to store
# movement values for [X, Y] in one place
velocity = [5, -10]
left_hits = 0
right_hits = 0
# Create a Tuple to hold the red, green and blue
# values to produce black (i.e. 0 for each)
black = (0, 0, 0)
white = (255, 255, 255)
something = (125, 56, 100)

# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("georgia", 36)
pygame.display.set_caption("Pong game")

# Load the image we want to bounce
# and store it in a variable called 'sprite'
ball = pygame.image.load("pongball.png")
screen0 = pygame.image.load("Amazing start screen.png")
screen0rect = screen0.get_rect()
left_paddle = pygame.image.load("paddle.png")
right_paddle = pygame.image.load("paddle.png")
left_paddle_rect = left_paddle.get_rect()
right_paddle_rect = right_paddle.get_rect()
left_paddle_rect.top = 250
right_paddle_rect.right = 1024
right_paddle_rect.top = 250

# Get a bounding rectangle from the ball
ball_rect = ball.get_rect()

# Loop forever
while True:
    # do starting stuff
    # Check the event list for a 'quit' event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Check if we need to move the paddles
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if right_paddle_rect.bottom < 700:
            right_paddle_rect.top += 10
    if key[pygame.K_UP]:
        if right_paddle_rect.top > 0:
            right_paddle_rect.bottom -= 10
    if key[pygame.K_s]:
        if left_paddle_rect.bottom < 700:
            left_paddle_rect.top += 10
    if key[pygame.K_w]:
        if left_paddle_rect.top > 0:
            left_paddle_rect.bottom -= 10
    if key[pygame.K_SPACE]:
        game_status = PLAYING

    screen.fill(white)
    if game_status == STARTING:
        screen.blit(screen0, screen0rect)
    elif game_status == PLAYING:

        # Move the bounding rectangle according to the
        # current velocity
        ball_rect = ball_rect.move(velocity)
        # Check of the bounding rectangle has touched the
        # edges of the window.
        if ((ball_rect.left < left_paddle_rect.right)
            and (ball_rect.bottom > left_paddle_rect.top)
            and (ball_rect.top < left_paddle_rect.bottom)):
            velocity[0] = -velocity[0]
        elif ball_rect.left < 0:
            velocity[0] = -velocity[0]
            right_hits += 1

        if ((ball_rect.right > right_paddle_rect.left)
            and (ball_rect.bottom > right_paddle_rect.top)
            and (ball_rect.top < right_paddle_rect.bottom)):
            velocity[0] = -velocity[0]
        elif ball_rect.right > 1024:
            velocity[0] = -velocity[0]
            left_hits += 1

        if ball_rect.top < 0 or ball_rect.bottom > height:
            # touching top/bottom of screen so
            # reverse the Y velocity value
            velocity[1] = -velocity[1]

        # Blit the ball to current rectangle position
        text = font.render(str(left_hits), True, something, white)
        text2 = font.render(str(right_hits), True, something, white)
        text_rect = text.get_rect()
        text2_rect = text2.get_rect()
        text2_rect.right = 1024
        screen.blit(text, text_rect)
        screen.blit(text2, text2_rect)
        screen.blit(ball, ball_rect)
        screen.blit(left_paddle, left_paddle_rect)
        screen.blit(right_paddle, right_paddle_rect)

    # Flip the screen we've just drawn to the front
    pygame.display.flip()
    # end of while loop - go round the loop again!

