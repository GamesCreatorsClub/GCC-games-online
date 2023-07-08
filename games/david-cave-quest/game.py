import pygame, sys, time, random



block_width = 64 
block_height = 64

allnpcs = [
    {
        "image" : pygame.image.load("game_data/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "Hello Traveler. Press space to jump."
    },
    {
        "image" : pygame.image.load("game_data/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "If you are stuck like me press R to reset but I am not as powerful as you."
    },
    
    {
        "image" : pygame.image.load("game_data/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "Press A to throw."
    },
    {
        "image" : pygame.image.load("game_data/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "Press down to crouch so you will be safe."
    
    },
    {
        "image" : pygame.image.load("game_data/NPC.png"),
        "rect" : pygame.Rect(0, 0, block_width, block_height),
        "text" : "press shift to sprint."
    },
    
    
    ]


player = {
    "images":[
        pygame.image.load("game_data/player_left0.png"),
        pygame.image.load("game_data/player_right0.png"), 
        pygame.image.load("game_data/player_up_0.png"),
        pygame.image.load("game_data/player_down_0.png"),
        pygame.image.load("game_data/player_left1.png"),
        pygame.image.load("game_data/player_right1.png"),  
        pygame.image.load("game_data/player_up_1.png"),
        pygame.image.load("game_data/player_down_1.png")
        ],
    "rect": pygame.Rect(0, 0, block_width, block_height),
    "start_rect": pygame.Rect(0, 0, block_width, block_height),
    "speed": 6,
    "direction":0,
    "crouch": False,
    "crouch_image":pygame.image.load("game_data/player_crouch.png")
    }

level = 1
pygame.init()
pygame.display.set_caption("Cave Quest")

weapon_num = 0
weapon = 'potato'

game_state = "titleScreen"

#playerSprite = pygame.image.load("sprite.png")
wallSprite = pygame.image.load("game_data/wall.png")
floorSprite = pygame.image.load("game_data/floor.png")
spiderLeftSprite = pygame.image.load("game_data/enemyLeft.png")
spiderRightSprite = pygame.image.load("game_data/enemyRight.png")
bulletSprite = pygame.image.load("game_data/bullet2.png")
title = pygame.image.load("game_data/title.png")
title_two = pygame.image.load("game_data/title2.png")

exit_ = pygame.image.load("game_data/exit.png")
textBackgroundimage = pygame.image.load("game_data/backgroundText.png")
textBackground = []

bridgePlankImage = pygame.image.load("game_data/bridge_plank.png")
bridgePlankList = []

pillaImage = pygame.image.load("game_data/pilla.png")
pillaList = []

marbleImage = pygame.image.load("game_data/marble.png")
marbleList = []

marblePillaImage = pygame.image.load("game_data/marblePilla.png")
marblePillaList = []

lavaImage = pygame.image.load("game_data/lava.png")
lavaList = []

flash_waiter = 210
flash_on = True

move_rect = None

music = pygame.mixer.Sound("game_data/background-music.wav")
# sound: musicLength = music.get_length() * 1000
# sound: musicStarted = - musicLength


#foot_step_sound = pygame.mixer.Sound("game_data/.wav")
#foot_step_soundLength = music.get_length() * 1000
#foot_step_soundStarted = - foot_step_soundLength



frameclock = pygame.time.Clock()
fallingSpeed = 1
jumpingTime = 0
restTime = 0
bullets = []
for index in range(10):
    bullet = {
        "image" : bulletSprite,
        "rect": pygame.Rect(0, 0, 32, 32),
        "speed": 12,
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
   "############      #",
   "#           #     #",
   "# ####       #    #",
   "# #   #      |   ##",
   "# #1  | ###########",
   "# ######     |   x#",
   "#           #######",
   "#        ## #######",
   "########### #######",
   "###########      2#",
   "ttt################",
    ]
leveltwo = [
   "###################",
   "#x                #",
   "##     S#         #",
   "##########        #",
   "#      |   ##     #",
   "#   ##########    #",
   "##               ##",
   "###               #",
   "### # ##   3      o#",
   "#   | |   #########",
   "#S  | |  ##########",
   "###################",
   "ttt################",
    ]
levelthree = [
   "###################",
   "#                 #",
   "#x                #",
   "######~~####      #",
   "#     ## |  #     #",
   "# #      |   #    #",
   "#        |       ##",
   "#     #############",
   "#  ##      4 |   o#",
   "##        #########",
   "###SSS SS##########",
   "###################",
   "ttt################",
    ]
levelfour = [
   "###################",
   "#o                #",
   "##                #",
   "###########  S#   #",
   "#          ###    #",
   "# ######## |    S #",
   "#  5|     #########",
   "# ###             #",
   "# S##        #S   #",
   "#####~~~##   ######",
   "############ | ####",
   "#############|   x#",
   "ttt################",
    ]
levelfive = [
   "###################",
   "###################",
   "#                 #",
   "#o               x#",
   "###  ##------######",
   "#     #           #",
   "#     #           #",
   "#     #           #",
   "#     #           #",
   "# S S #S SS S SSS #",
   "###################",
   "###################",
   "ttt################",
    ]
levelsix = [
   "###################",
   "#x                #",
   "##                #",
   "##---######----   #",
   "#       |        -#",
   "#   ---###S S S S #",
   "#-        #########",
   "#   #-            #",
   "# S##        #S   #",
   "##########   ######",
   "#S       |   |    o#",
   "#####~~############",
   "ttt################",
    ]
levelseven = [
   "###################",
   "#                o#",
   "#S  -  ############",
   "#####             #",
   "#   |             #",
   "#   | --#--  ---# #",
   "#   |   |       | #",
   "#  S| S |SSS    |x#",
   "###################",
   "###################",
   "   # ##############",
   "     ##    ########",
   "#### ####~~~~######",
   "ttt################",
    ]
leveleight = [
   "###################",
   "##           x#####",
   "##  ----------#####",
   "##            #####",
   "#### S    S#  #####",
   "######--#---  #####",
   "##      |    ######",
   "##---   #  S#######",
   "##     ############",
   "##  ### | #########",
   "##     S#  |  o#####",
   "###################",
   "ttt################",
    ]
levelnine = [
   "###################",
   "#o                #",
   "#    S S   #      #",
   "############      #",
   "#x          #     #",
   "####    #    #    #",
   "#    #  #    |   ##",
   "#    |  #    | ####",
   "#  #####  #SS| S  #",
   "##  |     #########",
   "### |    ##########",
   "###~#~~############",
   "ttt################",
    ]
levelten = [
   "XXXXXXXXXXXXXXXXXXX",
   "X H  H  H   H  H  X",
   "XoH  H  H   H  H  X",
   "XXX  H  H   H  H  X",
   "XXXX H  H   H  H  X",
   "XXXXXH  H   H  H  X",
   "XXXXXX  H   H  H  X",
   "XXXXXXX H   H  H  X",
   "XXXXXXXXH   H  Hx X",
   "XXXXXXXXXXXXXXXXXXX",
   "XXXXXXXXXXXXXXXXXXX",
   "X                 X",
   "XXXXXXX S XXXXXXXXX",
   "tttXXXXXXXXXXXXXXXX",
    ]


allLevels = [levelone, leveltwo, levelthree, levelfour, levelfive, levelsix, levelseven, leveleight, levelnine, levelten]

levelmap = allLevels[0]
#print(levelmap)
levelloaded = False
level = 0
levelNum = 0
#speed = [4, 4]

x_margin = 4
y_margin = 4

#      |
#def's V

def LoadMap(levelmap):
    global screen, allLevels, marbleList, lavaList, marblePillaList, bridgePlankList, pillaList, wall, floors, enemies, npcs, block_width, block_height, player, textBackground, levelloaded, move_rect, exit_rect
#    if levelmap > allLevels[1]:
#        floorSprite = pygame.image.load("game_data/floor2.png")

    
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
            for i in range(len(bridgePlankList) -1, -1, -1):
                del bridgePlankList[i]
            for i in range(len(pillaList) -1, -1, -1):
                del pillaList[i]
            for i in range(len(marbleList) -1, -1, -1):
                del marbleList[i]
            for i in range(len(marblePillaList) -1, -1, -1):
                del marblePillaList[i]
            for i in range(len(lavaList) -1, -1, -1):
                del lavaList[i]
            
           
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
                    elif col == "3":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        allnpcs[2]['rect'] = pygame.Rect(x, y, block_width, block_height)
                        npcs.append(allnpcs[2])
                    elif col == "4":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        allnpcs[3]['rect'] = pygame.Rect(x, y, block_width, block_height)
                        npcs.append(allnpcs[3])
                    elif col == "5":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        allnpcs[4]['rect'] = pygame.Rect(x, y, block_width, block_height)
                        npcs.append(allnpcs[4])
                    elif col == "x":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        exit_rect = pygame.Rect(x, y, block_width, block_height)
                        
                        
                    elif col == "S":
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
                    elif col == "t":
                        textBackground.append(pygame.Rect(x, y, block_width, block_height))
                    elif col == "-":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        bridgePlankList.append(pygame.Rect(x, y, block_width, block_height / 4))
                    elif col == "|":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        pillaList.append(pygame.Rect(x, y, block_width, block_height))
                    elif col == "~":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        lavaList.append(pygame.Rect(x, y + 16, block_width, 48))
                    elif col == "X":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        marbleList.append(pygame.Rect(x, y, block_width, block_height))
                    elif col == "H":
                        floors.append(pygame.Rect(x, y, block_width, block_height))
                        marblePillaList.append(pygame.Rect(x, y, block_width, block_height))
        
                    else:
                        floors.append(pygame.Rect(x, y, block_width, block_height))

                    x += block_width
                y += block_height
                x = 0
        



def DrawPlayer(player):
    animation_step = player["speed"] * 3
    animation_frames = 2
    image_index = player["direction"]
    if player['crouch']:
        screen.blit(player['crouch_image'], player['rect'])
        

    else: 
        if image_index < 2: # Moving left/right?      
            if (player['rect'].left // animation_step) % animation_frames:
                image_index = image_index + 4
        else: # Moving Up/Down
            if (player['rect'].bottom // animation_step) % animation_frames:
                image_index = image_index + 4
    
        screen.blit(player['images'][image_index], player['rect'])

def UpdatePlayerPosition():
    global fallingSpeed, jumpingTime, key, bridgePlankList, marbleList, move_rect
    # key = pygame.key.get_pressed()

    move_rect[0] = player['rect'][0] + x_margin
    move_rect[1] = player['rect'][1] + y_margin
    if key[pygame.K_DOWN]:
        player['crouch'] = True

    else:
        player['crouch'] = False
        if key[pygame.K_RIGHT]:
           move_rect[0] = move_rect[0] + player['speed']
           player['direction'] = 1
        if key[pygame.K_LEFT]:
           move_rect[0] = move_rect[0] - player['speed']
           player['direction'] = 0

        if move_rect.collidelist(walls) == -1 and move_rect.collidelist(bridgePlankList) == -1 and move_rect.collidelist(marbleList) == -1:     
            player['rect'][0] = move_rect[0] - x_margin
            player['rect'][1] = move_rect[1] - y_margin


    move_rect[0] = player['rect'][0] + x_margin
    move_rect[1] = player['rect'][1] + y_margin

                   # if key[pygame.K_DOWN]:
                   #    move_rect[1] = move_rect[1] + player['speed'] * 16
    if key[pygame.K_SPACE] and jumpingTime == 0 and fallingSpeed == 1:
       #recomended -16 for falling speed
       fallingSpeed = -16
       #recomended 32 for jumping time 
       jumpingTime = 32
      
    if move_rect.collidelist(walls) == -1 and move_rect.collidelist(bridgePlankList) == -1 and move_rect.collidelist(marbleList) == -1:     
       player['rect'][0] = move_rect[0] - x_margin
       player['rect'][1] = move_rect[1] - y_margin
      
    move_rect[1] = move_rect[1] + fallingSpeed
    if jumpingTime > 0:
        jumpingTime = jumpingTime - 1

    if move_rect.collidelist(walls) == -1 and move_rect.collidelist(bridgePlankList) == -1 and move_rect.collidelist(marbleList) == -1:
        player['rect'][0] = move_rect[0] - x_margin
        player['rect'][1] = move_rect[1] - y_margin
        if fallingSpeed < 16:
           fallingSpeed = fallingSpeed + 1
    else:
        fallingSpeed = 1

def UpdateEnemyPosition(enemies, walls):
    global bridgePlankList, marbleList
    for enemy in enemies:
        enemy_move_rect = enemy['rect']
        enemy_direction = enemy['direction']
        enemy_speed = enemy['speed']
        
        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        # If the enemy has hit a wall, generate a new direction
        if enemy_move_rect.collidelist(walls) != -1 or enemy_move_rect.collidelist(bridgePlankList) != -1 or enemy_move_rect.collidelist(marbleList) != -1:
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
    if not player['crouch']:
            
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

#               |
#main game loop V


# sound: print("Music len=" + str(musicLength))
music.play()

while True:

    now = pygame.time.get_ticks()

    key = pygame.key.get_pressed()

# sound:     if (now - musicLength >= musicStarted):
# sound:         music.play()
# sound:         musicStarted = now
# sound:         print("Playing music!")
    
    if game_state == "inGame":

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
            LoadMap(levelmap)

        if key[pygame.K_q]:
            player['speed'] = 3
            for bullet in bullets:
                bullet['speed'] = 6
            for enemy in enemies:
                enemy['speed'] = 2
        elif key[pygame.K_LSHIFT]:
            player['speed'] = 18
            
            
        else:
            player['speed'] = 6
            for bullet in bullets:
                bullet['speed'] = 12
            for enemy in enemies:
                enemy['speed'] = 4
        
            
        


       
        
        if player['rect'].colliderect(exit_rect):
            player['rect'][0] = player['start_rect'][0]
            player['rect'][1] = player['start_rect'][1]
          
            #DrawText("You reached the exit!", text_rect)
            pygame.display.flip()
          
            time.sleep(0.5)
            level = levelNum % 3
            levelNum = levelNum + 1
            levelloaded = False
            
    #        player["rect"][0] = 64
    #        player["rect"][1] = 64
            pygame.display.flip()
    #        screen.text(text, 0, 0)
    #       print("levelNum: " + str(levelNum) + " level: " + str(level))
    #    if player_rect.colliderect():      
    #        screen.fill((100, 100, 100))
        for enemy in enemies:
            if not player['crouch']:
                if player['rect'].colliderect(enemy['rect']):
                    player['rect'][0] = player['start_rect'][0]
                    player['rect'][1] = player['start_rect'][1]

                    DrawText("You died", text_rect)
                    pygame.display.flip()
                    LoadMap(levelmap)
                      
                    time.sleep(3)
                            
        #            player["rect"][0] = 64
        #            player["rect"][1] = 64
                    pygame.display.flip()                               
         


        for floor_rect in floors:
            screen.blit(floorSprite, floor_rect)
            
        for textBackground_rect in textBackground:
            screen.blit(textBackgroundimage, textBackground_rect)

        for bridgePlank_rect in bridgePlankList:
            screen.blit(bridgePlankImage, bridgePlank_rect)

        

        for marble_rect in marbleList:
            screen.blit(marbleImage, marble_rect)

        for lava_rect in lavaList:
            screen.blit(lavaImage, lava_rect)
            

        for marblePilla_rect in marblePillaList:
            screen.blit(marblePillaImage, marblePilla_rect)

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

        for pilla_rect in pillaList:
            screen.blit(pillaImage, pilla_rect)

        DrawText("level: " + str(levelNum % len(allLevels) + 1), (textBackground[0][0], textBackground[0][1] + 20))
        for lava_rect in lavaList:
            if player['rect'].colliderect(lava_rect):
                    player['rect'][0] = player['start_rect'][0]
                    player['rect'][1] = player['start_rect'][1]

                    DrawText("You died", text_rect)
                    pygame.display.flip()
                    LoadMap(levelmap)
                      
                    time.sleep(3)
                            
        #            player["rect"][0] = 64
        #            player["rect"][1] = 64
                    pygame.display.flip()


        if key[pygame.K_ESCAPE] and key[pygame.K_LCTRL]:
                pygame.quit()
                sys.exit()
        for event in  pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
        FlipAndTick(30)

    elif game_state == "titleScreen":
        screen = pygame.display.set_mode((1216, 832))
        if key[pygame.K_ESCAPE] and key[pygame.K_LCTRL]:
                    pygame.quit()
                    sys.exit()
        for event in  pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
       
        if flash_on:
            screen.blit(title, (0, 0))
        else:       
            screen.blit(title_two, (0, 0))
            
            
        
        if key[pygame.K_SPACE]:
            game_state = "inGame"
        FlipAndTick(30)
