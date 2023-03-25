import pygame, sys, random, math
#import pygame, sys, random, math, copy, fileinput
#from pygame.locals import *

pygame.init()

PRECISION = 10

#pygame.mixer.pre_init()
pygame.mixer.init()

frameclock = pygame.time.Clock()
screen = pygame.display.set_mode ((800, 800))
screenRect = pygame.Rect(0, 0, 800 * PRECISION, 800 * PRECISION)

mapRect = pygame.Rect(-800, -800, 2400 * PRECISION, 2400 * PRECISION)

debug = False
debugcooldown = 1
boxes = False

def create360images(image):
    print('loading!')
    images = []
    for a in range(0, 360, 1):
        pygame.transform.rotate(image, a)
        images.append(pygame.transform.rotate(image, a))
    return images
    
 

screen.blit(pygame.image.load("game_data/loading1.png"), (0,0))
pygame.display.flip()

assetFolder = 'game_data'

stars = []

images = {
   'background1' : pygame.transform.rotate(pygame.image.load(assetFolder + "/nebula.png"), random.choice([0,90,180,270])),
   'background2' : pygame.transform.rotate(pygame.image.load(assetFolder + "/nebula2.png"), random.choice([0,90,180,270])),
   'background3' : pygame.transform.rotate(pygame.image.load(assetFolder + "/nebula3.png"), random.choice([0,90,180,270])),
   'background4' : pygame.transform.rotate(pygame.image.load(assetFolder + "/nebula4.png"), random.choice([0,90,180,270])),
   'spaceShip' : create360images(pygame.image.load(assetFolder + "/Ship.png")),
   'spaceShipBoost' : create360images(pygame.image.load(assetFolder + "/Ship-Boost.png")),
   'asteroid8' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/rock.png"), (128, 128))),
   'asteroid4' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/rock.png"), (64, 64))),
   'asteroid2' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/rock.png"), (32, 32))),
   'asteroid1' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/rock.png"), (16, 16))),
   'bullet' : create360images(pygame.image.load(assetFolder + "/bullet.png")),
   'star' : create360images(pygame.image.load(assetFolder + "/star.png")),
   'star2' : create360images(pygame.image.load(assetFolder + "/star2.png")),
   'explosion-big-frames' : [
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion1.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion2.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion3.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion4.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion5.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion6.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion7.png"), (128,128)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion8.png"), (128,128))
      ],
   'explosion-frames' : [
      pygame.image.load(assetFolder + "/explosion/explosion1.png"),
      pygame.image.load(assetFolder + "/explosion/explosion2.png"),
      pygame.image.load(assetFolder + "/explosion/explosion3.png"),
      pygame.image.load(assetFolder + "/explosion/explosion4.png"),
      pygame.image.load(assetFolder + "/explosion/explosion5.png"),
      pygame.image.load(assetFolder + "/explosion/explosion6.png"),
      pygame.image.load(assetFolder + "/explosion/explosion7.png"),
      pygame.image.load(assetFolder + "/explosion/explosion8.png")    
      ],
   'explosion-frames-small' : [
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion1.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion2.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion3.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion4.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion5.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion6.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion7.png"), (32,32)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/explosion/explosion8.png"), (32,32))
      ],
   'zap-frames' : [
      pygame.image.load(assetFolder + "/zappything/zap1.png"),
      pygame.image.load(assetFolder + "/zappything/zap2.png"),
      pygame.image.load(assetFolder + "/zappything/zap3.png"),
      pygame.image.load(assetFolder + "/zappything/zap4.png"),
      pygame.image.load(assetFolder + "/zappything/zap5.png"),
      pygame.image.load(assetFolder + "/zappything/zap6.png"),
      pygame.image.load(assetFolder + "/zappything/zap7.png"),
      pygame.image.load(assetFolder + "/zappything/zap8.png")
      ],
   'smoke-frames' : [
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke1.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke2.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke3.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke4.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke1.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke2.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke3.png"), (64,64)),
      pygame.transform.scale(pygame.image.load(assetFolder + "/smoke/smoke4.png"), (64,64))
      

      ],
   'playbutton' : pygame.image.load(assetFolder + "/play-rock.png"),
   'playbuttontext' : pygame.image.load(assetFolder + "/play.png"),
   'radar' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/radar.png"), (200,200)),
   'Rplayer' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/good.png"), (16,16)),
   'Rbullet' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/good.png"), (2,2)),
   'RpowerUp' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/special.png"), (16,16)),
   'Rbase' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/special.png"), (32,32)),
   'R-asteroid8' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/bad.png"),(32,32)),
   'R-asteroid4' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/bad.png"),(16,16)),
   'R-asteroid2' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/bad.png"),(8,8)),
   'R-asteroid1' : pygame.transform.scale(pygame.image.load(assetFolder + "/radar/bad.png"),(4,4)),
   'Repare' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/Repare.png"),(70,70))),
   'Base' : create360images(pygame.transform.scale(pygame.image.load(assetFolder + "/Base.png"),(128,128)))

   }

screen.blit(pygame.image.load("game_data/loading2.png"), (0,0))
pygame.display.flip()


backgroundNum = random.randint(1, 4)

spaceShipImages = images['spaceShip']
spaceShipRect = spaceShipImages[0].get_rect()
spaceShipCentre = spaceShipRect.center
playerRect = spaceShipRect.move((400 - spaceShipCentre[0]) * PRECISION, (400 - spaceShipCentre[1]) * PRECISION)
player = {
   'rect' : playerRect,
   'images' : spaceShipImages,
   'angle': 0,
   'direction' : 0,
   'speed' : 0,
   'rotate' : True,
   'damage' : 0,
   'type' : 'Player'
   }
player['rect'][2] = player['rect'][2] * PRECISION
player['rect'][3] = player['rect'][3] * PRECISION

damageRect = pygame.Rect(8, 784, player['damage'], 8)
damageRectOutline = pygame.Rect(8, 784, 500, 8)



mousex = 0
mousey = 0
bullets = []
bulletCoolDown = 0
bulletCoolDownPeriod = 10



bulletPowerRect = pygame.Rect(8, 320, 8, bulletCoolDownPeriod)
bulletPowerOutline = pygame.Rect(8, 320, 8, 450)

asteroids = []
nextAsteroid = 0
nextAsteroidPeriod = 150

animations = []

shoot = pygame.mixer.Sound(assetFolder + '/Laser_shoot 21.wav')
#music = pygame.mixer.music.load(assetFolder + '/stock_mus_sparce_loop.ogg')

##music = pygame.mixer.Sound("game_data/bu-weak-and-broken.mp3")

#musicLength = music.get_length() * 10000
#musicStarted = musicLength

screen.blit(pygame.image.load("game_data/loading3.png"), (0,0))
pygame.display.flip()

    

score = 0

gamestate = 1

paused = False

playbutton = pygame.Rect(336, 336, 128, 128)

#'''hiscoreFile = open('hiscore.txt', 'r+')
#hiscoreFileLines = [line.strip() for line in hiscoreFile]     
#hiscore = hiscoreFileLines[len(hiscoreFileLines) - 1]
#
#print(hiscore)
#
#
#def changeHiscore(number):
#   global hiscoreFile, hiscore
#   hiscoreFile.write('\n' + str(number))
#   hiscoreFileLines = [line.strip() for line in hiscoreFile]   
#   hiscore = hiscoreFileLines[len(hiscoreFileLines) - 1]
#   
#
#print(hiscore)'''

max_speed = 100

joystick1 = {
    'ANY_BUTTON_PRESSED' : False,
    'BUTTON_0' : False,
    'BUTTON_1' : False,
    'BUTTON_2' : False,
    'BUTTON_3' : False,   
    'JOYSTICK_X' : 0,
    'JOYSTICK_Y' : 0
    }

   
def controllJoysticks():
    global joystick1
    joystick_count = pygame.joystick.get_count()
    #if joystick_count == 0:
        #print('XXXXXXX  NO JOYSTICK FOUND  XXXXXXX')      
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
          
        for i in range( axes ):
            axis = joystick.get_axis( i )
            if i == 0:
               joystick1['JOYSTICK_X'] = int(round(axis))
            if i == 1:
               joystick1['JOYSTICK_Y'] = int(round(axis))
            #textpaste.paste(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        #print(str(JOYSTICK_X) + ', ' + str(JOYSTICK_Y))
            
        buttons = joystick.get_numbuttons()
        
        for i in range( buttons ):
            button = joystick.get_button( i )
            if button == 0:
                pressed = False
            else:
                pressed = True
            if i == 0:
                joystick1['BUTTON_0'] = pressed
            if i == 1:
                joystick1['BUTTON_1'] = pressed
            if i == 2:
                joystick1['BUTTON_2'] = pressed
            if i == 3:
                joystick1['BUTTON_3'] = pressed
   
def drawText(text, position, size):
   global screen, font
   font = pygame.font.SysFont("droidsansmono", size, True)
   text = font.render(text, 1, (255, 255, 255))
   screen.blit(text, position)


def debugger():
   global key, debug, debugcooldown, boxes
   if (key[pygame.K_F3] and not lastkey[pygame.K_F3]) or joystick1['BUTTON_2']:
#   if key[pygame.K_F3] or joystick1['BUTTON_2']:
       if key[pygame.K_LSHIFT]:
           boxes = not boxes

       debug = not debug

def movePlayer():
   global player, key, asteroids, images, gamestate, joystick1, max_speed
   if key[pygame.K_RIGHT] or joystick1['JOYSTICK_X'] == 1:
      player['angle'] -= 3
   if key[pygame.K_LEFT] or joystick1['JOYSTICK_X'] == -1:
      player['angle'] += 3
   if key[pygame.K_UP] or joystick1['JOYSTICK_Y'] == -1:
      player['images'] = images['spaceShipBoost']
      if player['speed'] < max_speed:
         player['speed'] += 1
   elif key[pygame.K_DOWN]  or joystick1['JOYSTICK_Y'] == 1:
      if player['speed'] > 0:
         player['speed'] -= 1
   else:
      player['images'] = images['spaceShip']
      if player['speed'] > 0:
         player['speed'] -= 1

   player['direction'] = player['angle']         
   player['angle'] = fixAngle(player['angle'])


   for asteroid in asteroids:
      if not player['rect'].colliderect(powerUps[0]['rect']):
          if player['rect'].colliderect(asteroid['rect']):
             player['damage'] = player['damage'] + asteroid['size']
             createAnimation(368 + random.randint(-32, 32), 368 + random.randint(-32, 32), images['zap-frames'], 1,False)
             if player['damage'] > 500:
                print('dead!!!')
                createAnimation(336, 336, images['explosion-big-frames'], 4,False)
                player['speed'] = 0
                gamestate = 1

   
def drawPlayer():
   global player
   
   rotatedPlayer = pygame.transform.rotate(player['image'], player['angle'])
   screen.blit(rotatedPlayer, player['rect'])


def createBullet(angle):
   global bulletCoolDown, images, PRECISION, bulletCoolDownPeriod
   
   if bulletCoolDown == 0:
      if bulletCoolDownPeriod < 50:
         bulletCoolDownPeriod += 0.4
      bulletCoolDown = int(bulletCoolDownPeriod)

      
      print("Added new bullet")
      bullet = {
                 'images' : images['bullet'],
                 'rect' : pygame.Rect(400 * PRECISION, 400 * PRECISION, 16 * PRECISION, 16 * PRECISION),
                 'direction' : angle,
                 'angle' : angle,
                 'angularSpeed': 0,
                 'speed' : 200,
                 'remove-offscreen' : True,
                 'rotate' : True,
                 'type': 'bullet'
              }
      bullets.append(bullet)
      shoot.play()
    

def createNewAsteroid():

   r = random.randint(0, 3)
   
   if r == 0:
      x = random.randint(0, 800)
      y = 0
      direction = random.randint(225, 315)
   elif r == 1:
      x = 800
      y = random.randint(0, 800)
      direction = random.randint(135, 225)
   elif r == 2:
      x = random.randint(0, 800)
      direction = random.randint(45, 135)
      y = 800
   elif r == 3:
      x = 0
      y = random.randint(0, 800) 
      direction = random.randint(-45, 45)
      if direction < 0:
         direction = 360 + direction
   
    
   speed = 10
   size = random.choice([8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 2, 2, 1])
   
   

   createAsteroid(x, y, size, speed, direction)

   

def createAsteroid(x, y, size, speed, direction):
   global asteroids, images, PRECISION

   print("Got direction " + str(direction))
   asteroidRect = pygame.Rect(x * PRECISION, y  * PRECISION, size * 16 * PRECISION, size * 16 * PRECISION)
   asteroid = {
              'images' : images['asteroid8'],
              'rect' : asteroidRect,
              'direction' : direction,
              'angle' : 0,
              'angularSpeed':1,
              'speed' : speed,
              'size' : size,
              'remove-offscreen' : False,
              'rotate' : True,
              'type': 'asteroid'
           }
   asteroid['images'] = images['asteroid' + str(asteroid['size'])]
   asteroids.append(asteroid)




def move(objects):
   global bulletCoolDown, player, mapRect

   pdirection = fixAngle(player['direction'])
   par = -pdirection * math.pi / 180

   for i in range(len(objects) -1, -1, -1):
      obj = objects[i]

      direction = obj['direction']
      ar = -direction * math.pi / 180
      
      
      speed = obj['speed']
      rect = obj['rect']
      x = rect[0]
      y = rect[1]

      x = x + (speed * math.cos(ar))
      y = y + (speed * math.sin(ar))
      if obj['type'] == 'Star2':
          x = x - ((player['speed'] / 10) * math.cos(par))
          y = y - ((player['speed'] / 10) * math.sin(par))
      elif obj['type'] == 'Star':
          x = x - ((player['speed'] / 5) * math.cos(par))
          y = y - ((player['speed'] / 5) * math.sin(par))
      else:
          x = x - (player['speed'] * math.cos(par))
          y = y - (player['speed'] * math.sin(par))
      
      if obj['remove-offscreen']:
         if not screenRect.colliderect(rect):
            del objects[i]
      else:
         if obj['type'] == 'Star' or obj['type'] == 'Star2':
             edgeRect = screenRect
         else:
             edgeRect = mapRect
         if x > edgeRect[0] + edgeRect[2]:
            x = edgeRect[0] - rect[2] * PRECISION + 1
         elif x < edgeRect[0] - rect[2] * PRECISION:
            x = edgeRect[2] - 1

         if y > edgeRect[1] + edgeRect[3] * PRECISION:
            y = edgeRect[1] + 1 - rect[3] * PRECISION
         elif y < edgeRect[1] - rect[3] * PRECISION:
            y = edgeRect[3] - 1

      rect[0] = x
      rect[1] = y

      angle = obj['angle']
      angularSpeed = obj['angularSpeed']
      angle = angle + angularSpeed
      obj['angle'] = fixAngle(angle)

def fixAngle(a):
   if a < 0:
      a = a + 360
   if a >= 360:
      a = a - 360
   return a

def collideAstroids():
   global asteroids, bullets, images, PRECISION, score, player
   for i in range(len(asteroids) - 1, -1, -1):
      asteroid = asteroids[i]       
      for n in range(len(bullets) - 1, -1, -1):
         bullet = bullets[n]
         asteroidIsDeleted = False
         
         if asteroid['rect'].colliderect(bullet['rect']) or asteroid['rect'].colliderect(player['rect']):
            print('collided')
            score += asteroid['size'] * 100
            asteroid['size'] = asteroid['size'] / 2
            if not asteroidIsDeleted and asteroid['size'] == 0:
               createAnimation(asteroid['rect'][0] / PRECISION, asteroid['rect'][1] / PRECISION, images['explosion-frames-small'], 1, False)
               #try:
               del asteroids[i]
               #except:
               #   print('Asteroid del failed!')
               asteroidIsDeleted = True
            else:
               asteroid['rect'][2] = asteroid['size'] * 16 * PRECISION
               asteroid['rect'][3] = asteroid['size'] * 16 * PRECISION

               asteroid1direction = fixAngle(asteroid['direction'] - random.randint(0, 45))
               asteroid2direction = fixAngle(asteroid['direction'] + random.randint(0, 45))
               
               createAsteroid(asteroid['rect'][0] / PRECISION, asteroid['rect'][1] / PRECISION, asteroid['size'], 10, asteroid2direction)
               asteroid['direction'] = asteroid1direction
                  
               asteroid['images'] = images['asteroid' + str(asteroid['size'])]
               asteroids[i] = asteroid
            del bullets[n]
      


def createAnimation(x, y, frames, sleepTime, loop):
   global animations

   animation = {
      'rect' : pygame.Rect(x, y, 64, 64),
      'images' : frames,
      'frame' : 0,
      'frames' : len(frames),
      'timeTilNextframe' : sleepTime,
      'ticksOnOneFrame' :sleepTime,
      'loop' : loop
      
      }
   animations.append(animation)




def animateAnimations():
   global animations
   for i in range(len(animations) - 1, -1, -1):
      animation = animations[i]
      if animation['timeTilNextframe'] > 0:
         animation['timeTilNextframe'] -= 1
         animations[i] = animation
      else:
         animation['timeTilNextframe'] = animation['ticksOnOneFrame']
         animation['frame'] += 1
         animations[i] = animation
         if animation['frame'] > 7:
            if animation['loop']:
               animation['frame'] = 0
            else:
               del animations[i]
      
      
      


def drawAnimations():
   global animations, images
   for animation in animations:
      screen.blit(animation['images'][animation['frame']],animation['rect'])

def drawObjects(objects):
   for obj in objects:
      drawObject(obj)

def drawObject(obj):
   global PRECISION, debug, screen, boxes
   
   objImages = obj['images']
   objRect = obj['rect']
   objAngle = fixAngle(int(obj['angle']))
   if objRect.colliderect(screenRect):
       if obj['rotate']:
          rotatedImg = objImages[objAngle]
          img_center = rotatedImg.get_rect().center
          obj_center = objRect.center
          #img_center = img_center * PRECISION
          draw_center = [(obj_center[0] / PRECISION) - img_center[0], (obj_center[1] / PRECISION) - img_center[1]] 
           
          screen.blit(rotatedImg, draw_center)
          #objRect = objRect.move(objRect[0] + img_center[0],objRect[1] + img_center[1])

       else:
          img_center = objImages[0].get_rect().center
          draw_center = [(objRect[0] - img_center[0]) / PRECISION, (objRect[1] - img_center[1]) / PRECISION] 
          screen.blit(objImages[0], draw_center)
          #objRect = objRect.move((objRect[0] + img_center[0]) / PRECISION, (objRect[1] + img_center[1]) PRECISION)
       
       if boxes:
           if not obj['type'] == 'Star' and not obj['type'] == 'Star2':
             drawText('(' + str(objRect[0]/ PRECISION) + ', ' + str(objRect[1]/ PRECISION) + ')', ((objRect[0] / PRECISION),(objRect[1] / PRECISION)), 8)
             drawText('Size: ' + str(objRect[2] / 16 / PRECISION), ((objRect[0] / PRECISION),(objRect[1] + objRect[3])  / PRECISION), 8)
             drawText(obj['type'], (objRect[0] / PRECISION + objRect[2] / PRECISION,objRect[1] / PRECISION), 8)
             pygame.draw.rect(screen, (39, 183, 39), pygame.Rect(objRect[0] / PRECISION, objRect[1] / PRECISION, objRect[2] / PRECISION, objRect[3] / PRECISION), 1)


def drawRObjects(objects):
   for obj in objects:
      drawRObject(obj)

def drawRObject(obj):
   global PRECISION, debug, screen, boxes, images, radarRect
   objRect = obj['rect']
   pos = calcRadarPos(objRect)
   if radarRect.collidepoint(pos):
       onscreen = True
   else:
       onscreen = False
   
   if objRect.colliderect(screenRect): 
       if obj['type'] == 'Player':     
           screen.blit(images['Rplayer'], pos)

       elif obj['type'] == 'bullet':     
           screen.blit(images['Rbullet'], pos)
       elif obj['type'] == 'reparePack':     
           screen.blit(images['RpowerUp'], pos)
       elif obj['type'] == 'Base':     
           screen.blit(images['Rbase'], pos)
       elif obj['type'] == 'asteroid':      
           screen.blit(images['R-asteroid' + str(obj['size'])], pos)

radarRect = pygame.Rect(600, 600, 200, 200)
radar = False
def calcRadarPos(pos):
    return (((pos[0] / PRECISION) / 4) + 600,((pos[1] / PRECISION) / 4) + 600)

def drawRadar():
   global screen, images, radarRect, radar
   if radar:
       screen.blit(images['radar'], radarRect)
       drawRObjects(asteroids)
       drawRObjects(bullets)
       drawRObjects(powerUps)
       drawRObject(player)
powerUps = []
def createPowerUps():
    global powerUps
    powerUps = []
    base = {
                     'images' : images['Base'],
                     'rect' : pygame.Rect(336 * PRECISION, 336 * PRECISION, 128 * PRECISION, 128 * PRECISION),
                     'direction' :0,
                     'angle' : 0,
                     'angularSpeed': 0,
                     'speed' : 0,
                     'remove-offscreen' : False,
                     'rotate' : False,
                     'type' : 'Base'
                  }
    powerUps.append(base)
    counter = 12
    while counter > 0:
        counter -= 1
        if counter :
            powerup = {
                         'images' : images['Repare'],
                         'rect' : pygame.Rect(random.randint(-800,1600) * PRECISION, random.randint(-800,1600) * PRECISION, 64 * PRECISION, 64 * PRECISION),
                         'direction' :  random.randint(0, 359),
                         'angle' : random.randint(0, 359),
                         'angularSpeed': 2,
                         'speed' : 2,
                         'remove-offscreen' : False,
                         'rotate' : True,
                         'energy': 50,
                         'type' : 'reparePack'
                      }
            
        powerUps.append(powerup)
    
    
def doPowerUps():
    global powerUps
    for i in range(len(powerUps) - 1, -1, -1):
        powerUp = powerUps[i]
        rect = powerUp['rect']
        if player['rect'].colliderect(rect):
            if player['damage'] > 0:
                player['damage'] = player['damage'] - 1
                if not powerUp['type'] == 'Base':
                    powerUp['energy'] -= 1
                    if powerUp['energy'] < 1:
                        createAnimation(rect[0] / PRECISION, rect[1] / PRECISION, images['smoke-frames'], 2, False)
                        del powerUps[i]
            

    
    
def createStars():
    global stars
    stars = []
    counter = 0
    while counter < 50:
        counter += 1
        if counter < 2:
            star = {
                         'images' : images['star2'],
                         'rect' : pygame.Rect(random.randint(0,800) * PRECISION, random.randint(0,800) * PRECISION, 3 * PRECISION, 3 * PRECISION),
                         'direction' : 0,
                         'angle' : 0,
                         'angularSpeed': 0,
                         'speed' : 0,
                         'remove-offscreen' : False,
                         'rotate' : False,
                         'type' : 'Star2'
                      }
        else:
            star = {
                     'images' : images['star'],
                     'rect' : pygame.Rect(random.randint(0,800) * PRECISION, random.randint(0,800) * PRECISION, 3 * PRECISION, 3 * PRECISION),
                     'direction' : 0,
                     'angle' : 0,
                     'angularSpeed': 0,
                     'speed' : 0,
                     'remove-offscreen' : False,
                     'rotate' : False,
                     'type' : 'Star'
                  }
        stars.append(star)

#createAnimation(00, 00, images['explosion-frames'], 1, True)
def mainGame():
   global backgroundNum,  key, lastkey, images, joystick1, bulletCoolDown, stars, powerUps, nextAsteroid, nextAsteroidPeriod, gamestate,  bulletCoolDownPeriod, bulletPowerRect, bulletPowerOutline, frameclock, max_speed, paused, radar
   now = pygame.time.get_ticks()
   
   if key[pygame.K_p] and not lastkey[pygame.K_p]:
       paused = not paused
   if not paused:
       if key[pygame.K_r] and not lastkey[pygame.K_r]:
           radar = not radar
           
       if key[pygame.K_SPACE] or joystick1['BUTTON_0']:
          createBullet(player['angle'])
         
       else:
          if bulletCoolDownPeriod > 5:
                bulletCoolDownPeriod -= 0.12

       if bulletCoolDown > 0:
          bulletCoolDown = bulletCoolDown - 1

       if nextAsteroid > 0:
          nextAsteroid = nextAsteroid - 1
       else:
          nextAsteroid = nextAsteroidPeriod
          createNewAsteroid()

       if key[pygame.K_v] or joystick1['BUTTON_1']:
           max_speed = 200
       else:
           max_speed = 100

       animateAnimations()
       move(bullets)
       move(asteroids)
       move(stars)
       move(powerUps)
       collideAstroids()
       doPowerUps()
       movePlayer()    
   
   screen.blit(images['background' + str(backgroundNum)], (0, 0))
   
   
   drawObjects(stars)   
   drawObjects(asteroids)   
   drawObjects(powerUps)
   drawObjects(bullets)
   drawObject(player)
   drawAnimations()
   
   damageRect[2] = player['damage']
   pygame.draw.rect(screen, (0, 0, 0), damageRectOutline)
   pygame.draw.rect(screen, (222, 92, 38), damageRect)
   pygame.draw.rect(screen, (255, 255, 255), damageRectOutline, 1)

   bulletPowerRect[3] = 500 - bulletCoolDownPeriod * 10
   pygame.draw.rect(screen, (0, 0, 0), bulletPowerOutline)
   pygame.draw.rect(screen, (222, 92, 38), bulletPowerRect)
   pygame.draw.rect(screen, (255, 255, 255), bulletPowerOutline, 1)

   if paused:
       drawText('Press P to resume!' , (200, 400), 25)
       
   drawRadar()
   #drawText('HIScore: ' + str(score), (500,0), 25)
  
   if debug:
      
      drawText('Damage:' + str(player['damage']), (8,769), 15)
      drawText('Score: ' + str(score), (0,0), 25)
      drawText('Speed: ' + str(player['speed']), (0,30), 25)
      drawText('Angle: ' + str(player['angle']), (0,60), 25)
      drawText('bullet interval: ' + str(bulletCoolDownPeriod), (0,90), 25)
      drawText('fps: ' + str(round(frameclock.get_fps() * 100) / 100), (615,0), 25)
      drawText('next bullet: ' + str(bulletCoolDown), (0,120), 25)
   else:
      drawText('Damage:', (8,769), 15)
      #drawText('Bullet Power', (0,756), 15)
      drawText(str(score), (8,8), 30)
   
   
   
   pygame.display.flip()

def mainMenu():
   global backgroundNum, images, mousex, mousey, MOUSEDOWN, gamestate, stars, nextAsteroid, nextAsteroidPeriod, asteroids, flash, score,player
   if key[pygame.K_RETURN]  or joystick1['BUTTON_0']:
      print('pressed')
      gamestate = 2
      score = 0
      player['damage'] = 0
      nextAsteroid = 0
      createStars()
      createPowerUps()
      for i in range(len(asteroids) - 1, -1, -1):
         del asteroids[i]
   if key[pygame.K_e] and not lastkey[pygame.K_e]:
      if key[pygame.K_b]:
         createAnimation(mousex, mousey, images['explosion-big-frames'], 1, False)
      else:
         createAnimation(mousex, mousey, images['explosion-frames'], 1, False)
   if key[pygame.K_s]  and not lastkey[pygame.K_s]:
      createAnimation(mousex, mousey, images['smoke-frames'], 1, False)
   if key[pygame.K_z]  and not lastkey[pygame.K_z]:
      createAnimation(mousex, mousey, images['zap-frames'], 1, False)
         

   if nextAsteroid > 0:
      nextAsteroid = nextAsteroid - 1
   else:
      nextAsteroid = nextAsteroidPeriod
      createNewAsteroid()
   
   animateAnimations()
   move(asteroids)
   move(stars)
   collideAstroids()
   
   screen.blit(images['background' + str(backgroundNum)], (0, 0))
   drawObjects(stars)
   drawObjects(asteroids)
   if debug:
       drawText('fps: ' + str(round(frameclock.get_fps() * 10) / 10), (0,0), 25)
   
   drawAnimations()
   #screen.blit(images['playbutton'], (336,336))
   #screen.blit(images['playbuttontext'], (336,336))
   if flash > 0:
      flash = flash - 1
   else:
      flash = 100

   if flash > 25:
      drawText('press ENTER to start!' , (200, 400), 25)
   pygame.display.flip()
   

def changeCaption():
   global captionWaiter, caption

   if captionWaiter < 0:
      caption = '~' + caption + '~'
      if len(caption) > 20:
         caption = " Asteroids "
      pygame.display.set_caption(caption)
      captionWaiter = 30
   else:
      captionWaiter -= 1


flash = 100
captionWaiter = 0
caption = " Asteroids "

#print("Music len=" + str(musicLength))

key = pygame.key.get_pressed()
#def rungame():
createStars()
#   global frameclock, key, lastkey, mousex, mousey, gamestate, music, musicStarted, musicLength
while True:

      key = pygame.key.get_pressed()
      now = pygame.time.get_ticks()

      controllJoysticks()
      debugger()
      for event in  pygame.event.get():
         if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
               hiscoreFile.close()
               
         if event.type == pygame.MOUSEMOTION:
              mousex = event.pos[0]
              mousey = event.pos[1]
         if event.type == pygame.MOUSEBUTTONDOWN:
              MOUSEDOWN = True
         else:
              MOUSEDOWN = False
      if key[pygame.K_q] and key[pygame.K_LCTRL]:
         pygame.quit()
         sys.exit()
      
      changeCaption()
      
     # if now - musicLength >= musicStarted:
      #   music.play()
     #    musicStarted = now
         
      if gamestate == 1:
         mainMenu()
      elif gamestate == 2:  
         mainGame()
      frameclock.tick(30)
      lastkey = key

      
########################
# Now, the actual game #
########################

#pygame.mixer.music.play(-1)
#rungame()
