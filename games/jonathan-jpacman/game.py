import pygame, sys, time, random
#walls = []
#end_rect = pygame.Rect(0,0,32,32)
#enemy_start_rect = pygame.Rect(0,0,32,32)

enemies = []
enemy_start_rects = []

def InitText():
    global g_large_font, g_small_font
    g_large_font = pygame.font.SysFont("jokerman", 50)
    g_small_font = pygame.font.SysFont("jokerman", 18)
    return False

def DrawLargeText(text, position, colour):
    font_colour = pygame.Color(colour)
    rendered_text = g_large_font.render(text, 1, font_colour)
    shadow_text = g_large_font.render(text, 1, (0, 0, 0))
    screen.blit(shadow_text, (position[0] + 5, position [1] + 5))
    screen.blit(rendered_text, position)
    return False

def DrawSmallText(text, position, colour):
    font_colour = pygame.Color(colour)
    rendered_text = g_small_font.render(text, 1, font_colour)
    screen.blit(rendered_text, position)
    return False

def ClearScreen(colour):
    clear_colour = pygame.Color(colour)
    screen.fill(clear_colour)

def UpdateEnemyPosition(enemies, walls):
    for enemy in enemies:
        enemy_move_rect = enemy['rect']
        enemy_direction = enemy['direction']
        enemy_speed = enemy['speed']

        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        random_direction = 0
        # If the enemy has hit a wall, generate a new direction
        if enemy_move_rect.collidelist(walls) != -1:
            random_direction = random.randint(0, 3)

            if random_direction == 0:
                enemy['direction'] = [0,1] # down
            elif random_direction == 1:
                enemy['direction'] = [0,-1]# up
            elif random_direction == 2:
                enemy['direction'] = [1,0] # right
            elif random_direction == 3:
                enemy['direction'] = [-1,0]# left
        else:
            enemy['rect'] = enemy_move_rect

def DrawPlayer(player):
    animation_step = player["speed"] * 3
    image_index = player["direction"]
    if image_index < 2: # Moving left/right?      
        if (player['rect'].left // animation_step) % 2:
            image_index = image_index + 4
    else: # Moving Up/Down
        if (player['rect'].bottom // animation_step) % 2:
            image_index = image_index + 4
    
    screen.blit(player['images'][image_index], player['rect'])

def UpdatePlayerPosition(player, walls):
    oldplayer = player['rect']
    if key[pygame.K_d] and player['rect'][0] < 576:
       player['rect'] = player['rect'].move((1*player['speed']),0)
       player["direction"] = 1
    if key[pygame.K_a] and player['rect'][0] > 0:
       player['rect'] = player['rect'].move((-1*player['speed']),0)
       player["direction"] = 0
    if key[pygame.K_w] and player['rect'][1] > 0:
       player['rect'] = player['rect'].move(0,(-1*player['speed']))
       player["direction"] = 2
    if key[pygame.K_s] and player['rect'][1] < 384:
       player['rect'] = player['rect'].move(0,(1*player['speed']))
       player["direction"] = 3

    if player['rect'].collidelist(walls) != -1:
       player['rect'] = oldplayer

def GCCUpdateJetPackPlayerPosition(player, walls):
    global key
    player_move_rect = player["rect"]

    # reset the x movement velocity to zero
    player["velocity"][0] = 0

    # Create gravity force
    force = -0.5

    # Read the keyboard input and move the marker
    if key[pygame.K_a]:
        player["direction"] = 0
        # Add left movement velocity
        player["velocity"][0] = -4

    if key[pygame.K_d]:
        player["direction"] = 1
        # Add right movement velocity
        player["velocity"][0] = 4

    if key[pygame.K_w]:
        # Add Jetpack thrust
        force = 4
        
    player["velocity"][1] = player["velocity"][1] - force

    if player["velocity"][1] > player["speed"]:
        player["velocity"][1] = player["speed"]

    if player["velocity"][1] < -player["speed"]:
        player["velocity"][1] = -player["speed"]
    
    player_move_rect = player_move_rect.move(player["velocity"][0], 0)
    if player_move_rect.collidelist(walls) == -1:
        player["rect"] = player_move_rect
    else:
        player_move_rect = player['rect']
        player["velocity"][0] = 0

    player_move_rect = player_move_rect.move(0, player["velocity"][1])
    if player_move_rect.collidelist(walls) == -1:
        player["rect"] = player_move_rect
    else:
        player["velocity"][1] = 0       

def UpdateJetPackPlayerPosition(player, walls):
    global gravity, enemies
    global jetpackPower # update the enemy move rectangle according to direction & speed

    #oldplayer = player['rect']
    
    if key[pygame.K_w] and player['rect'][1] > 0:
       #player['rect'] = player['rect'].move(0,(-1*player['speed']))
       player["direction"] = 2
       #player['velocity'][1] = -player["speed"]
       player['velocity'][1] = player['velocity'][1] - jetpackPower
       if player['velocity'][1] < player["speed"]:
            player['velocity'][1] = -player["speed"]
    else:
        #player['rect'] = player['rect'].move(0,(1*player['speed']))
        player["direction"] = 3
        player['velocity'][1] = player['velocity'][1] - gravity
        if player['velocity'][1] > player["speed"]:
            player['velocity'][1] = player["speed"]
    #if key[pygame.K_s] and player['rect'][1] < 384:
    #   player['rect'] = player['rect'].move(0,(1*player['speed']))
    #   player["direction"] = 3
    if key[pygame.K_d] and player['rect'][0] < 576:
       #player['rect'] = player['rect'].move((1*player['speed']),0)
       player["direction"] = 1
       player['velocity'][0] = player["speed"]
    elif key[pygame.K_a] and player['rect'][0] > 0:
       #player['rect'] = player['rect'].move((-1*player['speed']),0)
       player["direction"] = 0
       player['velocity'][0] = -player["speed"]
    else:
        player['velocity'][0] = 0

    oldplayer = player['rect']
    player['rect'] = player['rect'].move(0, player['velocity'][1])
    if player['rect'].collidelist(walls) != -1:
       player['rect'] = oldplayer

    oldplayer = player['rect']
    player['rect'] = player['rect'].move(player['velocity'][0], 0)
    if player['rect'].collidelist(walls) != -1:
       player['rect'] = oldplayer

gravity = -0.05
jetpackPower = 0.1

#Bullets!

bullets = []
for index in range(10):
    bullet = {
        "image":pygame.image.load("All_Direction_Bullet.png"),
        "rect":pygame.Rect(0, 0, 16, 16),
        "speed": 8,
        "velocity":[0,0],
        "active":False
        }
    bullets.append(bullet)
 


def DrawBullets():
    global bullets, screen

    # For each active bullet
    for bullet in bullets:
        if bullet["active"] == True:
            screen.blit(bullet["image"], bullet["rect"])

def UpdateBullets():
    global bullets, walls, enemies

    # For each active bullet
    for bullet in bullets:

        if bullet["active"] == True:
            bullet["rect"] = bullet["rect"].move(bullet["velocity"][0], bullet["velocity"][1])

            if bullet["rect"].collidelist(walls) > -1:
                bullet["active"] = False
            for i in range(len(enemies) - 1, -1, -1):
                enemy = enemies[i]
                if bullet["rect"].colliderect(enemy['rect']):
                    del enemies[i]
                    bullet["active"] = False

def CheckFireBullet():
    global bullets, player, last_fire_button_state, key

    current_fire_button_state = key[pygame.K_SPACE]
    if current_fire_button_state and not last_fire_button_state:
            #print (player["direction"])
            # Find the next available bullet
            for bullet in bullets:
                if bullet["active"] == False:
                    # Move it to the player's position
                    bullet["rect"] = player["rect"]
                    # Reset the bullet velocity
                    bullet["velocity"] = [0,0]               

                    # Set its velocity according to the player's direction
                    if player["direction"] == 0: # left
                        bullet["velocity"][0] = -bullet["speed"]
                    if player["direction"] == 1: # right
                        bullet["velocity"][0] = bullet["speed"]
                    if player["direction"] == 2: # up
                        bullet["velocity"][1] = -bullet["speed"]
                    if player["direction"] == 3: # down
                        bullet["velocity"][1] = bullet["speed"]                

                    # Activate it
                    bullet["active"] = True                  

                    # break out of the for loop
                    last_fire_button_state = current_fire_button_state

                    break
    # Store the last button state in the global for the next time...
    last_fire_button_state = current_fire_button_state
 
def MakeNewEnemy():
    pos = random.randint(0, len(enemy_start_rects) - 1)
    random_direction = random.randint(0, 3)

    if random_direction == 0:
        direction = [0,1] # down
    elif random_direction == 1:
        direction = [0,-1]# up
    elif random_direction == 2:
        direction = [1,0] # right
    elif random_direction == 3:
        direction = [-1,0]# left
        
    enemy = {
         "image": pygame.image.load("enemy_32.png"),
         "rect": pygame.Rect(enemy_start_rects[pos][0], enemy_start_rects[pos][1], 28, 28),
         'direction' : direction,
         'speed' : 5
        }
    enemies.append(enemy)


    
player = {
        "image": pygame.image.load("sprite.png"),
        "images":[
                pygame.image.load("player_left_0.png"),
                pygame.image.load("player_right_0.png"), 
                pygame.image.load("player_up_0.png"),
                pygame.image.load("player_down_0.png"),
                pygame.image.load("player_left_1.png"),
                pygame.image.load("player_right_1.png"),  
                pygame.image.load("player_up_1.png"),
                pygame.image.load("player_down_1.png")
                ],
        "rect": pygame.Rect(32,32,28,28),
        "p_start_rect": pygame.Rect(32,32,28,28),
        "speed": 2,
        "direction": 0,
        "velocity": [0, 0]
        }

        

def CreateLevel(level_definition):
        global walls
        global end_rect
        global enemy_start_rect
        global player
        global jetpacklevel
        player['p_start_rect'] = pygame.Rect(32,128,28,28)
        
        walls = []
        x = y =0
        for row in level_definition:
            for col in row:
                if col == "#":
                    walls.append(pygame.Rect(x, y, 32, 32))            
                if col == "X":
                    end_rect = pygame.Rect(x,y,32,32)
                if col == "E":
                    enemy_start_rects.append(pygame.Rect(x, y, 32, 32))

                x += 32
            y +=32
            x = 0
        levelloaded = True
        jetpacklevel = False

def ResetGameLevel():
    global player
    global enemy_rect
    player['rect'] = player['p_start_rect']
    #enemy_rect = enemy_start_rect
    del enemies[:]

pygame.init()
screen = pygame.display.set_mode((640, 480))  


#sprite = pygame.image.load("sprite.png")
wallpic = pygame.image.load("SpriteWall.png")
endpic = pygame.image.load("SpriteEnd.png")
#endsprite = pygame.image.load("EndScript.png")
#enemy_sprite = pygame.image.load("enemy_32.png")
#hit_enemy = pygame.image.load("HitEnemy.png")

#player = pygame.Rect(32,32,28,28)

levelone = [
    "####################",
    "#     #       #    #",
    "#     #       #    #",
    "#     #       #    #",
    "#     #       #    #",
    "#                  #",
    "#       ####     # #",
    "#                #X#",
    "#        E       ###",
    "#     #####        #",
    "#                  #",
    "# #### ## # # # ## #",
    "#                  #",
    "####################",
    "####################"
    ]
oldlevelone = [
    "####################",
    "# # #### #   E#   X#",
    "# #   #  # ## # ####",
    "# # # # #  #  #   ##",
    "#   # # ## # #### ##",
    "### # #  # # ##   ##",
    "#   # ## # #  # ####",
    "# ###  # # ## # # ##",
    "# #  # # #  #   # ##",
    "# # ## # ## # ### ##",
    "#   ## #  # # # #  #",
    "# #### ## # # # ## #",
    "# #         #      #",
    "####################",
    "####################"
    ]
leveltwo = [
    "####################",
    "# #   #   E#    #X #",
    "# # ### ## # ## #  #",
    "# # #   #  # #   # #",
    "#     ### ## ## ## #",
    "# # ###   #  #  ## #",
    "### #   ### ## ### #",
    "#   # ###   #  #   #",
    "# ### #   ### ### ##",
    "# #     # #   #    #",
    "# ######### ###### #",
    "#   ### ### #    # #",
    "# #     #     ##   #",
    "# #     #     ##   #",
    "####################"
    ]


level = levelone
InitText()
x = y =0
end_rect = pygame.Rect(0,0,32,32)
#size = width, height = level[0].__len__() * 32, level.__len__() * 32

enemy_direction = [0,1]

CreateLevel(levelone)
ResetGameLevel()
gamestate = 0
jetpacklevel = True
max_enemies = 20
max_next_enemy_time = 50
next_enemy_time = random.randint(0, max_next_enemy_time)

            ##MAIN GAME LOOP##
            ##STARTS HERE!!!##
    
while True:
    
    pygame.time.Clock().tick(60)

    if next_enemy_time > 0:
        next_enemy_time = next_enemy_time - 1
    else:
        next_enemy_time = random.randint(0, max_next_enemy_time)
        if len(enemies) < max_enemies:
            MakeNewEnemy()

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
           
    if gamestate == 0:
        #speed = player['speed']
        enemy_speed = 1

        # update the enemy move rectangle according to direction & speed
        #enemy_move_rect = enemy_rect.move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        if jetpacklevel:
            GCCUpdateJetPackPlayerPosition(player, walls)
        else:
            UpdatePlayerPosition(player, walls)

        UpdateEnemyPosition(enemies, walls)
        
        #oldplayer = player['rect']
        #if key[pygame.K_d] and player['rect'][0] < 576:
        #    player['rect'] = player['rect'].move((1*player['speed']),0)
        #if key[pygame.K_a] and player['rect'][0] > 0:
        #    player['rect'] = player['rect'].move((-1*player['speed']),0)
        #if key[pygame.K_w] and player['rect'][1] > 0:
        #    player['rect'] = player['rect'].move(0,(-1*player['speed']))
        #if key[pygame.K_s] and player['rect'][1] < 384:
        #    player['rect'] = player['rect'].move(0,(1*player['speed']))

        #if player['rect'].collidelist(walls) != -1:
         #   player['rect'] = oldplayer

        #if enemy_move_rect.collidelist(walls) != -1:
        #    random_direction = random.randint(0, 3)
        #    if random_direction == 0:
        #        enemy_direction = [0,(1*enemy_speed)] 
        #    elif random_direction == 1:
        #        enemy_direction = [0,(-1*enemy_speed)] 
        #    elif random_direction == 2:
        #        enemy_direction = [(1*enemy_speed),0] 
        #    elif random_direction == 3:
        #        enemy_direction = [(-1*enemy_speed),0] 
        #else:
        #    enemy_rect = enemy_move_rect

        CheckFireBullet() 
        UpdateBullets() 




        # Level Up!
        if player['rect'].colliderect(end_rect):
            #DrawText("Level Up!"(0,255,0))
            ClearScreen("DarkOliveGreen")
            DrawLargeText("You Made It!", (130, 100), "Green")
            
            pygame.display.flip()
            time.sleep(1)
            CreateLevel(leveltwo)
            ResetGameLevel()

        else:
            for enemy in enemies:
                if player['rect'].colliderect(enemy['rect']):
                    time.sleep(1)
                    gamestate = 1
                                         
        screen.fill((0,0,0))
        for wall in walls:
            screen.blit(wallpic, wall)

        
        DrawPlayer(player)
        DrawBullets()
        screen.blit(endpic, end_rect)
        for enemy in enemies:
            screen.blit(enemy['image'], enemy['rect'])

        pygame.display.flip()

    elif gamestate == 1:
        #DrawText("Oh No! You Lose"(255,0,0))
        ClearScreen("FireBrick")
        DrawLargeText("Oh No - You Lose!", (90, 100), "Red")
        pygame.display.flip()
        if key[pygame.K_SPACE]:
            ResetGameLevel()
            gamestate=0
