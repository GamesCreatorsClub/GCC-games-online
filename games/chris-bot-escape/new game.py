
import pygame, sys, random

# Defining functions that we will call in the game to do stuff

debug = False
cheat = False
pushed_door_for = 0


def UpdatePlayerPosition(player, walls):
    global have_rock, cheat, debug, pushed_door_for
    
    player_move_rect = player['rect'] 
    speed = player['speed'] 
    # Read the keyboard input and move the marker 
    key = pygame.key.get_pressed()
    if key[pygame.K_y]:
        cheat = not cheat
    if key[pygame.K_t]:
        debug = not debug
    if key[pygame.K_a]: 
        player["direction"] = 0 
        player_move_rect = player_move_rect.move(-speed, 0) 
    if key[pygame.K_d]: 
        player["direction"] = 1 
        player_move_rect = player_move_rect.move(speed, 0) 
    if key[pygame.K_w]: 
        player["direction"] = 2 
        player_move_rect = player_move_rect.move(0, -speed) 
    if key[pygame.K_s]: 
        player["direction"] = 3 
        player_move_rect = player_move_rect.move(0, speed)
    if key[pygame.K_x] and have_rock:
        have_rock = False
        if player["direction"] == 0:
            rock = pygame.Rect(player_move_rect[0] - 32, player_move_rect[1], 32, 32)
            rocks.append(rock)
        elif player["direction"] == 1:
            rock = pygame.Rect(player_move_rect[0] + 32, player_move_rect[1], 32, 32)
            rocks.append(rock)
        elif player["direction"] == 2:
            rock = pygame.Rect(player_move_rect[0], player_move_rect[1] - 32, 32, 32)
            rocks.append(rock)
        elif player["direction"] == 3:
            rock = pygame.Rect(player_move_rect[0], player_move_rect[1] + 32, 32, 32)
            rocks.append(rock)

        
    # Only if the marker has not hit a wall do we update the player
    hit_rock = player_move_rect.collidelist(rocks)
    
    if hit_rock >= 0:
        if not have_rock:
            have_rock = True
            del rocks[hit_rock]
            #remove it from rocks
    else:
        doorIndex = player_move_rect.collidelist(doors)
        if doorIndex == -1:
            pushed_door_for = 0
        else:
            if pushed_door_for == 0:
                pushed_door_for = 50
            else:
                pushed_door_for = pushed_door_for - 1
                if pushed_door_for == 0:
                    del doors[doorIndex]
        
        if player_move_rect.collidelist(walls) == -1 and player_move_rect.collidelist(doors) == -1: 
            player['rect'] = player_move_rect

    #hit the door and delete it
    hit_door = player_move_rect.collidelist(doors)

    if hit_door == True:
        print ("hit door")

def DrawPlayer(player):
    animation_step = player["speed"] * 3 
    image_index = player["direction"] 
    if image_index < 2: # Moving left/right?      
          if (player["rect"].left // animation_step) % 2: 
            image_index = image_index + 4 
    else: # Moving Up/Down
        if(player["rect"].bottom // animation_step) % 2: 
              image_index = image_index + 4 


    screen.blit(player["images"][image_index], player["rect"])



 
# Helper Functions
def InitText():
    global g_large_font, g_small_font
    g_large_font = pygame.font.SysFont("jokerman", 50)
    g_small_font = pygame.font.SysFont("jokerman", 18)
    return False

def DrawLargeText(text, position, colour):
    global g_large_font, g_small_font
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
            # check if we hit an enemy
            for enemy in enemies:
                if enemy["active"] and bullet["rect"].colliderect(enemy["rect"]):
                    bullet["active"] = False
                    enemy["active"] = False
 
def CheckFireBullet():
    global bullets, player, last_fire_button_state, keys
    current_fire_button_state = keys[pygame.K_SPACE]
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

    last_fire_button_state = current_fire_button_state

        
# Enemy Functions
def UpdateEnemyPosition(enemies, walls):
    for enemy in enemies:
        if enemy["active"]:
            enemy_move_rect = enemy['rect']
            enemy_direction = enemy['direction']
            enemy_speed = enemy['speed']
            
            # update the enemy move rectangle according to direction & speed
            enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

            # If the enemy has hit a wall, generate a new direction
            if enemy_move_rect.collidelist(walls) != -1 or enemy_move_rect.collidelist(rocks) != -1 or enemy_move_rect.collidelist(doors) != -1:
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
               

def CreateMap(level, player, level_exit):
    global screen, walls, enemies, doors
    block_size = 32
    
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
                player["rect"] = pygame.Rect(x, y, block_size / 2, block_size / 2)
                player["start_rect"] = pygame.Rect(x, y, block_size / 2, block_size / 2)

            # Set the exit position if we find an 'x'
            elif col == "x":
                level_exit["rect"] = pygame.Rect(x, y, block_size, block_size)

            #set the rock position
            elif col == "R":
                rocks.append(pygame.Rect(x, y, block_size, block_size))


            #set the door position
            elif col == "d":
                doors.append(pygame.Rect(x, y, block_size, block_size))

            # Set the enemy position if we find an 'E'
            if col == "E":
                enemy = {
                    "image":pygame.image.load("enemy_bot.png"),
                    "rect":pygame.Rect(x, y, block_size, block_size),
                    "start_rect":pygame.Rect(x, y, block_size, block_size),
                    "direction":[0,1],
                    "speed":4,
                    "active":True
                    }
                enemies.append(enemy)
            
            x += block_size
        y += block_size
        x = 0

def DrawBullets():
    global bullets, screen
    # For each active bullet
    for bullet in bullets:
        if bullet["active"] == True:
            screen.blit(bullet["image"], bullet["rect"])
        

def DrawEnemies():
    global enemies, screen
    for enemy in enemies:
        if enemy["active"]:
            screen.blit(enemy['image'], enemy['rect'])

def CheckForResetGame(player, enemies):
    global game_state, keys
    if keys[pygame.K_SPACE]:
        game_state = 0
        player["rect"] = player["start_rect"]
        for enemy in enemies:
            enemy["rect"] = enemy["start_rect"]
            enemy["active"] = True

#Game Initialise - stuff we do once at the beginning

screen = pygame.display.set_mode((480, 384))
pygame.init()
InitText()

# Create map
walls = []
level = [
"###############",
"#x        E  ##",
"#####  ##    ##",
"####r   ##    #",
"######d########",
"#             #",
"#   ######### #",
"#     E   #   #",
"#         #   #",
"# #########   #",
"#o R   R      #",
"###############",
]

have_rock = False
game_state = 0
block_size = 32
power = False

walls = []
enemies = []
keys = []
rocks = []
doors = []
wall_sprite = pygame.image.load("new wall.png")
rock_sprite = pygame.image.load("new wall.png")
door_sprite = pygame.image.load("door.png")
game_state = 0;
last_fire_button_state = False
rock_int_rect = pygame.Rect(450, 354, 0, 0)

level_exit = {
    "image":pygame.image.load("exit_builder.png"),
    "rect":pygame.Rect(0, 0, 32, 32)
    }

player_rect = pygame.Rect(0,0, block_size, block_size)



player = { 
    "images":[ 
        pygame.image.load("bot sprite left.png"), 
        pygame.image.load("bot sprite right.png"), 
        pygame.image.load("bot sprite up.png"), 
        pygame.image.load("bot sprite down.png"), 
        pygame.image.load("bot sprite left.png"), 
        pygame.image.load("bot sprite right.png"), 
        pygame.image.load("bot sprite up.png"), 
        pygame.image.load("bot sprite down.png")
        ], 
    "rect":pygame.Rect(0, 0, 32, 32), 
    "start_rect":pygame.Rect(0, 0, 32, 32), 
    "speed":4, 
    "direction":0 
    }



        
bullets = []
for index in range(10):
    bullet = {
        "image":pygame.image.load("orb.png"),
        "rect":pygame.Rect(0, 0, 16, 16),
        "speed":8,
        "velocity":[0,0],
        "active":False
        }
    bullets.append(bullet)

CreateMap(level, player, level_exit)

#GAME LOOP - Repeating loop. Check state, then call update and draw

game_running = True

while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    UpdatePlayerPosition(player, walls)

    if game_state == 0:
        UpdateEnemyPosition(enemies, walls)
        CheckFireBullet()
        UpdateBullets()


           
    
        # Check if we have reached the exit or hit enemy
        if player['rect'].colliderect(level_exit['rect']):
            game_state = 1;
            
        for enemy in enemies:
            if enemy["active"] and player['rect'].colliderect(enemy['rect']) and not cheat:
                game_state = 2;


        
        # -- Draw the screen --
        # Background
        ClearScreen("light grey")                                                                                                                                                                                                                                                                                                                                                                 

        # Walls
        for wall in walls:
            # shadow first...
            pygame.draw.rect(screen, (20, 50, 170), wall.move(10, 10))

        for rock in rocks:           
            # now the walls
            screen.blit(rock_sprite, rock)

        
        for door in doors:
            screen.blit(door_sprite, door)
            
        # Draw Stuff...
        DrawPlayer(player)
        DrawBullets()
        DrawEnemies()
        
           
        for wall in walls:           
            # now the walls
            screen.blit(wall_sprite, wall)

        if have_rock:
            screen.blit(rock_sprite, rock_int_rect)

        # Exit
        screen.blit(level_exit['image'], level_exit['rect'])

        if debug:
            if cheat:
                DrawSmallText("Cheat is on",  (0,0), "red")
            DrawSmallText("dp: " + str(pushed_door_for),  (375, 350), "black")
            
    elif game_state == 1:
        screen.fill((128, 0, 0))
        DrawLargeText("you won",  (90,100), "red")
        CheckForResetGame(player, enemies)

    elif game_state == 2:
        screen.fill((128, 0, 0))
        DrawLargeText("Oh No - You Lose!",  (90,100), "red")
        CheckForResetGame(player, enemies)

    pygame.display.flip()
