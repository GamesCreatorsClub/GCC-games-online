import pygame, sys, time, random



block_width = 64 
block_height = 64

allnpcs = [
    {
        "image" : pygame.image.load("assets/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "Hello Traveler. Press space to jump."
    },
    {
        "image" : pygame.image.load("assets/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "If you are stuck like me press R to reset but I am not as powerful as you, mighty person."
    }
    ]


player = {
    "images":[
        pygame.image.load("assets/player_left0.png"),
        pygame.image.load("assets/player_right0.png"), 
        pygame.image.load("assets/player_up_0.png"),
        pygame.image.load("assets/player_down_0.png"),
        pygame.image.load("assets/player_left1.png"),
        pygame.image.load("assets/player_right1.png"),  
        pygame.image.load("assets/player_up_1.png"),
        pygame.image.load("assets/player_down_1.png")
        ],
    "rect": pygame.Rect(0, 0, block_width, block_height),
    "start_rect": pygame.Rect(0, 0, block_width, block_height),
    "speed": 4,
    "direction":0
    }

level = 1
pygame.init()
pygame.display.set_caption("Maze")

weapon_num = 0
weapon = 'potato'

#playerSprite = pygame.image.load("Sprite.png")
wallSprite = pygame.image.load("assets/wall.png")
floorSprite = pygame.image.load("assets/floor.png")
spiderLeftSprite = pygame.image.load("assets/enemyLeft.png")
spiderRightSprite = pygame.image.load("assets/enemyRight.png")
bulletSprite = pygame.image.load("assets/bullet2.png")

exit_ = pygame.image.load("assets/exit.png")
textBackgroundimage = pygame.image.load("assets/BackgroundText.png")
textBackground = []

frameclock = pygame.time.Clock()
fallingSpeed = 1
jumpingTime = 0
restTime = 0
bullets = []
for index in range(10):
    bullet = {
        "image" : bulletSprite,
        "rect": pygame.Rect(0, 0, 32, 32),
        "speed": 8,
        "velocity": [0,0],
        "active": False
             }
    bullets.append(bullet)

enemies = []
npcs = []
walls = []
floors = []
exits = []
levelone = [
   "###################",
   "#o                #",
   "#      x          #",
   "############      #",
   "#           #     #",
   "# ####       #    #",
   "# #   #          ##",
   "# #1    ###########",
   "# ######          #",
   "#         #  ######",
   "#        ## #######",
   "########### #######",
   "###########      2#",
   "ttt################",
    ]
leveltwo = [
   "###################",
   "#x                #",
   "##     E#         #",
   "##########        #",
   "#          ##     #",
   "#   ##########    #",
   "##               ##",
   "###               #",
   "### # ##          o#",
   "#         #########",
   "#E       ##########",
   "###################",
   "ttt################",
    ]
levelthree = [
   "###################",
   "#x                #",
   "##                #",
   "############      #",
   "#           #     #",
   "# #          #    #",
   "#                ##",
   "#     #############",
   "#  ##            o#",
   "##        #########",
   "###EE  EE##########",
   "###################",
   "ttt################",
    ]
allLevels = [levelone, leveltwo, levelthree]

levelmap = levelone
#print(levelmap)
levelloaded = False;
level = 0
levelNum = 0
#speed = [4, 4]

x_margin = 4
y_margin = 4

#      |
#def's V

def LoadMap(levelmap):
    global screen, wall, floors, enemies, npcs, block_width, block_height, player, textBackground, levelloaded, move_rect, exit_rect
       
    if levelloaded == False:
            screen = pygame.display.set_mode ((levelmap[0].__len__() * block_width, levelmap.__len__() * block_height))
            for i in range(len(walls) -1, -1, -1):
                del walls[i]
            for i in range(len(floors) -1, -1, -1):
                del floors[i]
            for i in range(len(enemies) -1, -1, -1):
                del enemies[i]
            for i in range(len(npcs) -1, -1, -1):
                del npcs[i]
            for i in range(len(textBackground) -1, -1, -1):
                del textBackground[i]
           
            #print("levelNum: " + str(levelNum) + " level: " + str(level) + str(levelmap))

            x = y = 0
            for row in levelmap:
                for col in row:
                    if col == "#":
                        walls.append(pygame.Rect(x, y, block_width, block_height))

                    elif col == "o":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        player['start_rect'] = pygame.Rect(x, y, block_width, block_height)
                        player['rect'][0] = player['start_rect'][0]
                        player['rect'][1] = player['start_rect'][1]
                        move_rect = pygame.Rect(x, y, block_width - x_margin * 2, block_height - y_margin * 2)

                    elif col == "1":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        allnpcs[0]['rect'] = pygame.Rect(x, y, block_width, block_height)
                        npcs.append(allnpcs[0])
                    elif col == "2":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        allnpcs[1]['rect'] = pygame.Rect(x, y, block_width, block_height)
                        npcs.append(allnpcs[1])
                        #npc2['rect'] = pygame.Rect(x, y, block_width, block_height)
                
                    elif col == "x":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        exit_rect = pygame.Rect(x, y, block_width, block_height)
                        
                    if col == "E":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        enemy = {
                            "imageLeft": spiderLeftSprite,
                            "imageRight": spiderRightSprite,
                            "rect":pygame.Rect(x, y, block_width, block_height),
                            "start_rect":pygame.Rect(x, y, block_width, block_height),
                            "direction":[0,1],
                            "speed":4
                        }
                        enemies.append(enemy)
                    if col == "t":
                        textBackground.append(pygame.Rect(x, y, block_width, block_height))
        
                    else:
                        floors.append(pygame.Rect(x, y, block_width, block_height))

                    x += block_width
                y += block_height
                x = 0
        



def DrawPlayer(player):
    animation_step = player["speed"] * 3
    animation_frames = 2
    image_index = player["direction"]
    if image_index < 2: # Moving left/right?      
        if (player['rect'].left // animation_step) % animation_frames:
            image_index = image_index + 4
    else: # Moving Up/Down
        if (player['rect'].bottom // animation_step) % animation_frames:
            image_index = image_index + 4
    
    screen.blit(player['images'][image_index], player['rect'])

def UpdatePlayerPosition():
    global fallingSpeed, jumpingTime, key
    # key = pygame.key.get_pressed()

    move_rect[0] = player['rect'][0] + x_margin
    move_rect[1] = player['rect'][1] + y_margin

    if key[pygame.K_RIGHT]:
       move_rect[0] = move_rect[0] + player['speed']
       player['direction'] = 1
    if key[pygame.K_LEFT]:
       move_rect[0] = move_rect[0] - player['speed']
       player['direction'] = 0

    if move_rect.collidelist(walls) == -1:     
        player['rect'][0] = move_rect[0] - x_margin
        player['rect'][1] = move_rect[1] - y_margin


    move_rect[0] = player['rect'][0] + x_margin
    move_rect[1] = player['rect'][1] + y_margin

                   # if key[pygame.K_DOWN]:
                   #    move_rect[1] = move_rect[1] + player['speed'] * 16
    if key[pygame.K_SPACE] and jumpingTime == 0:
       #recomended -16 for falling speed
       fallingSpeed = -16
       #recomended 32 for jumping time 
       jumpingTime = 32
      
    if move_rect.collidelist(walls) == -1:     
       player['rect'][0] = move_rect[0] - x_margin
       player['rect'][1] = move_rect[1] - y_margin
      
    move_rect[1] = move_rect[1] + fallingSpeed
    if jumpingTime > 0:
        jumpingTime = jumpingTime - 1

    if move_rect.collidelist(walls) == -1:
        player['rect'][0] = move_rect[0] - x_margin
        player['rect'][1] = move_rect[1] - y_margin
        if fallingSpeed < 16:
           fallingSpeed = fallingSpeed + 1
    else:
        fallingSpeed = 1

def UpdateEnemyPosition(enemies, walls):
    for enemy in enemies:
        enemy_move_rect = enemy['rect']
        enemy_direction = enemy['direction']
        enemy_speed = enemy['speed']
        
        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        # If the enemy has hit a wall, generate a new direction
        if enemy_move_rect.collidelist(walls) != -1:
            random_direction = random.randint(0, 1)
            if random_direction == 0:
                enemy['direction'] = [1,0] # right
            elif random_direction == 1:
                enemy['direction'] = [-1,0] # left
        else:
            enemy['rect'] = enemy_move_rect

def DrawEnemies():
    for enemy in enemies:
        if enemy['direction'][0] > 0:
            screen.blit(enemy['imageRight'], enemy['rect'])
        else:
            screen.blit(enemy['imageLeft'], enemy['rect'])

  
def FlipAndTick(tick):
   pygame.display.flip()
   if tick == 0:
     frameclock.tick(30)
   else:
       frameclock.tick(tick)

def DrawText(text, position):
   global screen, font
   font = pygame.font.SysFont("apple casual" , 50)
   text = font.render(text, 1,(255, 255, 255))
   screen.blit(text, position)

def CheckFireBullet():
    global  bullrts, player, last_fire_button_state, key
    
    current_fire_button_state = key[pygame.K_a]
    if current_fire_button_state and not last_fire_button_state:

        for bullet in bullets:
            if bullet['active'] == False:
                bullet['rect'] = pygame.Rect(player['rect'][0], player['rect'][1], 32, 32)
                bullet['velocity'] = [0, 0]
                if player['direction'] == 0:
                    bullet['velocity'] = [-bullet['speed'], 0]
                if player['direction'] == 1:
                    bullet['velocity'] = [bullet['speed'], 0]

                bullet['active'] = True
                print("Just fired a bullet")

                last_fire_button_state = current_fire_button_state
                break

    last_fire_button_state = current_fire_button_state
        
def UpdateBullets():
    global bullets, walls, enemies

    for bullet in bullets:
        if bullet['active']:
            bullet['rect'] = bullet['rect'].move(bullet['velocity'][0], bullet['velocity'][1])
            if bullet['rect'].collidelist(walls) > -1: #or bullet['rect'].collidelist(enemies) > -1:
                bullet['active'] = False
            for i in range(len(enemies) - 1, -1, -1):
                enemy = enemies[i]
                if bullet['rect'].colliderect(enemy['rect']):
                    bullet['active'] = False
                    del enemies[i]

def DrawBullets():
        global bullets, screen
        for bullet in bullets:
            if bullet['active']:
                screen.blit(bullet['image'], bullet['rect'])

#player_rect = pygame.Rect(0, 0, block_width, block_height)
#player_start_rect = pygame.Rect(0, 0, block_width, block_height)

text_rect = pygame.Rect(20, 20, block_width, block_height)
print("levelNum: " + str(levelNum) + " level: " + str(level))
#               |
#main game loop V
while True:

    key = pygame.key.get_pressed()
 
    
    if levelloaded == False:

        levelmap = allLevels[levelNum % len(allLevels)]
        LoadMap(levelmap)
        levelloaded = True

 
   
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    UpdateEnemyPosition(enemies, walls)
    UpdatePlayerPosition()
   
    CheckFireBullet()
    UpdateBullets()
         
    if key[pygame.K_r]:
        player['rect'][0] = player['start_rect'][0]
        player['rect'][1] = player['start_rect'][1]
        for enemy in enemies:
            enemy['rect'][0] = enemy['start_rect'][0]
            enemy['rect'][1] = enemy['start_rect'][1]

    if key[pygame.K_z]:
        weapon_num = weapon_num + 1
        if weapon_num % 2 == 0:
            weapon = "potato"
            bullet['image'] = bulletSprite
            print(weapon)
         
        if weapon_num % 2 == 1: 
            weapon = "other"
            bullet['image'] = bulletSprite
            print(weapon)
            print(bullet['image'])
       
    if key[pygame.K_ESCAPE] and key[pygame.K_LCTRL]:
            pygame.quit()
            sys.exit()


   
    
    if player['rect'].colliderect(exit_rect):
        player['rect'][0] = player['start_rect'][0]
        player['rect'][1] = player['start_rect'][1]
      
        DrawText("You reached the exit!", text_rect)
        pygame.display.flip()
      
        time.sleep(3)
        level = levelNum % 3
        levelNum = levelNum + 1
        levelloaded = False
        
#        player["rect"][0] = 64
#        player["rect"][1] = 64
        pygame.display.flip()
#        screen.text(text, 0, 0)
        print("levelNum: " + str(levelNum) + " level: " + str(level))
#    if player_rect.colliderect():      
#        screen.fill((100, 100, 100))
    for enemy in enemies:
        if player['rect'].colliderect(enemy['rect']):
            player['rect'][0] = player['start_rect'][0]
            player['rect'][1] = player['start_rect'][1]

            DrawText("You died", text_rect)
            pygame.display.flip()
              
            time.sleep(3)
                    
#            player["rect"][0] = 64
#            player["rect"][1] = 64
            pygame.display.flip()                               
 


    for floor_rect in floors:
        screen.blit(floorSprite, floor_rect)
        
    for textBackground_rect in textBackground:
        screen.blit(textBackgroundimage, textBackground_rect)

    for wall in walls:
        screen.blit(wallSprite, wall)
#    if player['rect'].colliderect(npc1['rect']):
#        DrawText(npc1['text'], text_rect)
#    if player['rect'].colliderect(npc2['rect']):
#        DrawText(npc2['text'], text_rect)

    screen.blit(exit_, exit_rect)
    for npc in npcs:
        if player['rect'].colliderect(npc['rect']):
            DrawText(npc['text'], text_rect)
        screen.blit(npc['image'], npc['rect'])

    DrawEnemies()

    DrawBullets()

    DrawPlayer(player)

    DrawText("level: " + str(level + 1), (textBackground[0][0], textBackground[0][1] + 20))
   
    FlipAndTick(0)
