import pygame, sys, random

block_size = 32

level_0 = [
"######################",
"#  E                E#",
"#               x    #",
"# ####       ####    #",
"#        E           #",
"#  E                 #",
"#       ###########  #",
"#                  E #",
"#      E             #",
"#          E         #",
"#   #    #   ###     #",
"#     E              #",
"#                    #",
"#         o     E    #",
"######################"
]

level_1 = [
"######################",
"#E                 # #",
"# ####### ########x# #",
"# #       E      ### #",
"#   ############     #",
"# ###          # ### #",
"#     ######## # #   #",
"#####        # # # # #",
"#   # ######## # # ###",
"# #       E      #  E#",
"# # ############ ### #",
"# #              #   #",
"# ################ # #",
"#o                 # #",
"######################",
]


level_2 = [

"######################",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"#                    #",
"######################",
]
            
# Player Functions
def UpdateJetPackPlayerPosition(player, walls):
    player_move_rect = player["rect"]

    # reset the x movement velocity to zero
    player["velocity"][0] = 0

    # Create gravity force
    force = -0.5

    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player["direction"] = 0
        # Add left movement velocity
        player["velocity"][0] = -2

    if key[pygame.K_RIGHT]:
        player["direction"] = 1
        # Add right movement velocity
        player["velocity"][0] = 2

    if key[pygame.K_UP]:
        # Add Jetpack thrust
        force = 1
        
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

def UpdatePlayerPosition(player, walls):
    player_move_rect = player['rect']
    speed = player['speed']
    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player["direction"] = 0
        player_move_rect = player_move_rect.move(-speed, 0)
    if key[pygame.K_RIGHT]:
        player["direction"] = 1
        player_move_rect = player_move_rect.move(speed, 0)
    if key[pygame.K_UP]:
        player["direction"] = 2 
        player_move_rect = player_move_rect.move(0, -speed)
    if key[pygame.K_DOWN]:
        player["direction"] = 3 
        player_move_rect = player_move_rect.move(0, speed)

    # Only if the marker has not hit a wall do we update the player
    if player_move_rect.collidelist(walls) == -1:
        player['rect'] = player_move_rect

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

# Enemy Functions
def UpdateEnemyPosition(enemies, walls):
    for enemy in enemies:
        enemy_move_rect = enemy['rect']
        enemy_direction = enemy['direction']
        enemy_speed = enemy['speed']
        
        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        # If the enemy has hit a wall, generate a new direction
        if enemy_move_rect.collidelist(walls) != -1:
            random_direction = random.randint(0, 3)
            if random_direction == 0:
                enemy['direction'] = [0,1] # down
            elif random_direction == 1:
                enemy['direction'] = [0,-1] # up
            elif random_direction == 2:
                enemy['direction'] = [1,0] # right
            elif random_direction == 3:
                enemy['direction'] = [-1,0] # left
        else:
            enemy['rect'] = enemy_move_rect
        
# Helper Functions
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

def CheckForResetGame(player, enemies):
    global game_state
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        game_state = 0
        player["rect"] = player["start_rect"]
        for enemy in enemies:
            enemy["rect"] = enemy["start_rect"]

def CreateMap(level, player, level_exit, enemies):
    global screen, walls, spawn_points, block_size
    
    # Reset the wall & enemy lists
    walls[:] = []
    enemies[:] = []

    # Fill the walls array with rectangles for each '#'
    x = y = 0
    for row in level:
        for col in row:
            if col == " ":
                x += block_size
                continue
            
            elif col == "#":
                walls.append(pygame.Rect(x, y, block_size, block_size))

            # Set the player position if we find an 'o'
            elif col == "o":
                player["rect"] = pygame.Rect(x, y, block_size, block_size)
                player["start_rect"] = pygame.Rect(x, y, block_size, block_size)

            # Set the exit position if we find an 'x'
            elif col == "x":
                level_exit["rect"] = pygame.Rect(x, y, block_size, block_size)

            # Set the enemy position if we find an 'E'
            if col == "E":
                spawn_points.append(pygame.Rect(x, y, block_size, block_size))
                
            x += block_size
        y += block_size
        x = 0

def CheckFireBullet():
    global bullets, player, last_fire_button_state, keys

    key = pygame.key.get_pressed()
    current_fire_button_state = key[pygame.K_SPACE]
    if current_fire_button_state and not last_fire_button_state:

        
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
 
def DrawBullets():
    global bullets, screen, walls

    # For each active bullet
    for bullet in bullets:
        if bullet["active"] == True:
            screen.blit(bullet["image"], bullet["rect"])
            #bullet["velocity"][1]
            if bullet["rect"].collidelist(walls) > -1:
                bullet["active"] = False
 
def UpdateBullets():
    global bullets, walls, enemies

    # For each active bullet
    for bullet in bullets:

        if bullet["active"] == True:
            bullet["rect"] = bullet["rect"].move(bullet["velocity"][0], bullet["velocity"][1])

            if bullet["rect"].collidelist(walls) > -1:
                bullet["active"] = False


            for enemy in enemies:
                if bullet["rect"].colliderect(enemy['rect']):
                    enemies.remove(enemy)
                    bullet["active"] = False
                
  


# === ACTUAL GAME CODE STARTS HERE ===
# One-off initialisation to start
pygame.init()
bullets = []
for index in range(10):
    bullet = {
        "image":pygame.image.load("exit_32.png"),
        "rect":pygame.Rect(0, 0, 16, 16),
        "speed":8,
        "velocity":[0,0],
        "active":False
        }
    bullets.append(bullet)



 

InitText()
screen = pygame.display.set_mode((len(level_0[0]) * 32, len(level_0) * 32))
walls = []
enemies = []
spawn_points = []
wall_sprite = pygame.image.load("wall_32.png")
game_state = 0
enemy_tta = 0
max_enemies = 4

level_exit = {
    "image":pygame.image.load("exit_32.png"),
    "rect":pygame.Rect(0, 0, 32, 32)
    }

player = {
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
    "rect":pygame.Rect(0, 0, 32, 32),
    "start_rect":pygame.Rect(0, 0, 32, 32),
    "speed":6,
    "velocity":[0,0],
    "direction":0
    }

CreateMap(level_0, player, level_exit, enemies)

# === Main Game Loop ===
while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_state == 0:
    
        if enemy_tta > 0:
            enemy_tta = enemy_tta - 1                    
        else:
            if len(enemies) < max_enemies:
                where = random.randint(0, len(spawn_points) - 1)
                enemy = {
                        "image":pygame.image.load("enemy_32.png"),
                        "start_rect":spawn_points[where],
                        "rect":pygame.Rect(spawn_points[where][0], spawn_points[where][1], block_size, block_size),
                        "direction":[0,1],
                        "speed":2,
                        "active":True
                        }
                enemies.append(enemy)
                enemy_tta = random.randint(30, 120)
            else:
                enemy_tta = random.randint(30, 120)

        #UpdatePlayerPosition(player, walls)
        UpdateJetPackPlayerPosition(player, walls)
        UpdateEnemyPosition(enemies, walls)

        CheckFireBullet()
        UpdateBullets()

        if player['rect'].colliderect(level_exit['rect']):
            game_state = 1
            
        for enemy in enemies:
            if player['rect'].colliderect(enemy['rect']):
                game_state = 2

        # -- Draw the screen --
        # Background
        ClearScreen("RoyalBlue")

        # Walls
        for wall in walls:
            # shadow first...
            pygame.draw.rect(screen, (50, 50, 170), wall.move(10, 10))

        # Player
        DrawPlayer(player)
        
        # Enemy
        for enemy in enemies:
            screen.blit(enemy['image'], enemy['rect'])

        DrawBullets()
        
        for wall in walls:           
            # now the walls
            screen.blit(wall_sprite, wall)
        
        # Exit
        screen.blit(level_exit['image'], level_exit['rect'])

        
    elif game_state == 1:
        ClearScreen("AR DELANEY")
        DrawLargeText("well done you ain't dead!!!!", (130, 100), "Green")
        CreateMap(level_1, player, level_exit, enemies)
        CheckForResetGame(player, enemies)
            
    elif game_state == 2:
        ClearScreen("AR DELANEY")
        DrawLargeText("better luck next time", (90, 100), "Red")
        CheckForResetGame(player, enemies)
        
    pygame.display.flip()
    # End of the game loop


