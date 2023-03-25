import sys, pygame, random, math, time

pygame.init()

alpha = 0 

frameclock = pygame.time.Clock()
# Chain together some variables
# to store the screen size
width = 1024
height = 512

screensize = (width, height)

myScore = 10
enemyScore = 10


#GAMESTATE 0 --> menue
#GAMESTATE 1 --> options
#GAMESTATE 2 --> ingame
#gameSTATE 3 --> Some one lost!
gameSTATE = 0



PI = math.pi

x = 512
y = 256
speed = 10
angle = PI + 0.5

ballspeedCounter = 0
slowmoCounter = 0
# Create a Tupl0 to hold the red, green and blue
# values to pruduce black (i.e. 0 for each)
black = (0, 0, 0)
blue = (144, 255, 255)

hitPaddle = False
previousmrbouncey = 0

# Create the main game window and store it
# in a variable called 'screen'
screen = pygame.display.set_mode(screensize)
screen_rect = pygame.Rect(0, 0, 1024, 512)

MOUSEDOWN = False

options  = {
   'twoplayer': False, 
   'AI difficulty' : 0
   }

# Load the image we want to bounce
# and store it in a variable called 'mrbounce'
mrbounce = pygame.image.load("Ball.png")
paddle = pygame.image.load("paddle.png")
paddle2 = pygame.image.load("paddle2.png")
powerUpImage = pygame.image.load("powerupz.png")


paddlespeed = 7

# Get a bounding rectangle from the mrbounce
mrbouncerect = mrbounce.get_rect()
paddleRect = paddle.get_rect()
paddle2Rect = paddle2.get_rect()
paddle2Rect[0] = 1024 - paddle2Rect[2]
paddle2Rect[1] = 156
paddleRect[1] = 156
powerUpRect = powerUpImage.get_rect()


deBug = False

def DrawText(text, position):
   global screen, font
   font = pygame.font.SysFont("apple casual" , 50)
   text = font.render(text, 1,(255, 255, 255))
   screen.blit(text, position)
   
def enemyAI():
    global paddle2Rect, mrbouncerect, previousmrbouncey, paddlespeed, options
    if options['AI difficulty'] == 0:
       paddle2Rect[1] = 156
    elif options['AI difficulty'] == 1:  
       if not paddle2Rect[1] == mrbouncerect[1]:
           if paddle2Rect[1] > mrbouncerect[1]  - 50:
               paddle2Rect[1] -= paddlespeed
           if paddle2Rect[1] < mrbouncerect[1] - 50:
               paddle2Rect[1] += paddlespeed
    elif options['AI difficulty'] == 2:
       paddle2Rect[1] = mrbouncerect[1] - 100
            
    
 #   paddle2Rect[1] += mrbouncerect[1] - paddle2Rect[1]
    
   

def moveMrbounce():
    global angle, PI, mrbouncerect, sx, sy, x, y, paddleRect, paddle2Rect, myScore, hitPaddle, speed

    if angle < 0:
        angle = angle + 2 * PI
    if angle >= 2 * PI:
        angle = 2 * PI - angle
 
    x = x + (speed * math.cos(angle))
    y = y + (speed * math.sin(angle))
    sx = x
    sy = y

    if mrbouncerect.colliderect(paddleRect) or mrbouncerect.colliderect(paddle2Rect):
    
    #(sx + mrbouncerect[2] > 1024 - paddle2Rect[2] and sy > paddle2Rect[1] and sy < paddle2Rect[1] + paddle2Rect[3]) or (sx < 0 + paddleRect[2] and sy > paddleRect[1] and sy < paddleRect[1] + paddleRect[3]):
    
        if not hitPaddle:
                    
            if angle > PI:
                angle = 3 * PI - angle
            else:
                angle = PI - angle
                                
            #x = x + (speed * math.cos(angle))
            #y = y + (speed * math.sin(angle))
        hitPaddle = True
    else:
        hitPaddle = False
    
    if sy > 512 - mrbouncerect[3] or sy < 0:
        if angle > PI:
            angle = 2 * PI - angle
        else:
            angle = 2 * PI - angle
        
    
    mrbouncerect[0] = x
    mrbouncerect[1] = y

powerUpRect[1] = random.randint(10, 500)
powerUpRect[0] = random.randint(50, 940)
#print('power up at ' + str(powerUpRect[0]) + ', ' + str(powerUpRect[1]))  

def powerUp():
    global powerUpRect, mrbouncerect, speed, paddlespeed, myScore, slowmoCounter,ballspeedCounter, paddleRect,paddle2Rect
    if powerUpRect.colliderect(mrbouncerect):
        powerUpindex = random.randint(0,2)
        if powerUpindex == 0:
           ballspeedCounter = 300
        elif powerUpindex == 1:
            slowmoCounter = 100
        else:
           paddleRect[1] = 0
           paddle2Rect[1] = 0
            
        powerUpRect[1] = random.randint(10, 500)
        powerUpRect[0] = random.randint(50, 940)
        #print('power up at ' + str(powerUpRect[0]) + ', ' + str(powerUpRect[1])) 

    if ballspeedCounter > 0:
        speed = 40 # 40
        ballspeedCounter -= 1
    else:
        speed = 10 # 10
        
    if slowmoCounter > 0:
        speed = 3 # 3
        paddlespeed = 4
        slowmoCounter -= 1
    else:
        speed = 10 # 10
        paddlespeed = 7

    
#            |    
#TITLE STUFF V
play_button = pygame.image.load('play.png')
play_rect = play_button.get_rect()
play_rect[0] = 384
play_rect[1] = 128

options_button = pygame.image.load('options.png')
options_buttonRect = options_button.get_rect()
options_buttonRect[0] = 0
options_buttonRect[1] = 512 - options_buttonRect[3]

backdrop = pygame.image.load('SCREEN.png')


#    
#OPTIONS STUFF V


onePlayer = pygame.image.load('options-selectedOneplayer.png')
twoPlayer = pygame.image.load('options-selectedTwoplayer.png')
changePlayerRect = twoPlayer.get_rect()

changePlayerRect[0] = 512
changePlayerRect[1] = 200

optionsSCREEN = pygame.image.load('optionsSCREEN.png')

backButton = pygame.image.load('Back.png')
backRect = backButton.get_rect()


options  = {
   'twoplayer': False, 
   'AI difficulty' : 1
   }

redwon = pygame.image.load('WIN.red.png')
greenwon = pygame.image.load('WIN.green.png')


# Loop forever
while True:
    key = pygame.key.get_pressed()
    # Check the event list for a 'quit' event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()           
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
           MOUSEDOWN = True
        else:
           MOUSEDOWN = False

            
    if gameSTATE == 0:
       if MOUSEDOWN and play_rect.collidepoint(mouse_position):
          gameSTATE = 2
          powerUpRect[1] = random.randint(10, 500)
          powerUpRect[0] = random.randint(50, 940)
          ballspeedCounter = 0
          slowmoCounter = 0
          paddlespeed = 7
          paddle2Rect[0] = 1024 - paddle2Rect[2]
          paddle2Rect[1] = 156
          paddleRect[1] = 156
          x = 512
          y = 256
          myScore = 10
          enemyScore = 10
       if MOUSEDOWN and options_buttonRect.collidepoint(mouse_position):
          gameSTATE = 1
          #print('Entered Options room')

       screen.blit(backdrop, (0,0)) 
       screen.blit(play_button, play_rect)
       screen.blit(options_button, options_buttonRect)
    elif gameSTATE == 2:
       moveMrbounce()
    
       
       if key[pygame.K_s]:  
           paddleRect[1] += paddlespeed
       if key[pygame.K_w]:
           paddleRect[1] -= paddlespeed
       if key[pygame.K_F3]:
           deBug = not deBug
       if options['twoplayer']:
          if key[pygame.K_DOWN]:  
              paddle2Rect[1] += paddlespeed
          if key[pygame.K_UP]:
              paddle2Rect[1] -= paddlespeed
       else:
          peviousmrbouncey = mrbouncerect[1] 
          enemyAI()
     
     
       moveMrbounce()
       powerUp()
       if mrbouncerect[0] > 1024:
           x = 512
           y = 256
           myScore += 1
           enemyScore -= 1
       if mrbouncerect[0] < 0:
           x = 512
           y = 256
           myScore -= 1
           enemyScore += 1  


       if myScore < 1 or enemyScore < 1:
          gameSTATE = 3
#       if myScore < 1:
#          print('RED WON!!!')
#          gameSTATE = 0
#          exit
#       if enemyScore < 1:
#          print('GREEN WON!!!')
#          gameSTATE = 0


      # angle += 1
      # rotatedmrbounce = pygame.transform.rotate(mrbounce, alpha)

    
       if slowmoCounter > 0:
           screen.fill((255, 120, 230))
       elif ballspeedCounter > 0:
           screen.fill((255, 245, 0))
       else:
           screen.fill(black)
       DrawText(str(myScore), (0, 0))
       DrawText(str(enemyScore), (920, 0))
       screen.blit(mrbounce, mrbouncerect)
       screen.blit(paddle, paddleRect)
       screen.blit(paddle2, paddle2Rect)
       screen.blit(powerUpImage, powerUpRect)

       if deBug:
          DrawText('Difficulty: ' + str(options['AI difficulty']), (40, 0))
          DrawText('TwoPlayer: ' + str(options['twoplayer']), (40, 40))
       # Flip the screen we've just drawn to the front


    elif gameSTATE == 1:
      #print('inoptions')
      if MOUSEDOWN and changePlayerRect.collidepoint(mouse_position):
            options['twoplayer'] = not options['twoplayer']
            time.sleep(0.1)
      if MOUSEDOWN and backRect.collidepoint(mouse_position):
         gameSTATE = 0
      screen.blit(optionsSCREEN, (0,0))

      if options['twoplayer']:
         screen.blit(twoPlayer, changePlayerRect)
      else:
         screen.blit(onePlayer, changePlayerRect)
      screen.blit(backButton, backRect)

    elif gameSTATE == 3:
       #print(gameSTATE)
       if MOUSEDOWN:
          gameSTATE = 0
       if myScore < 1:
          screen.blit(redwon, (0,0))
       else:
          screen.blit(greenwon, (0,0))
       DrawText('***Click to return to menu***', (0,0))
       
       
    pygame.display.flip()

    frameclock.tick(30)

       # end of while loop - go round the loop again!
