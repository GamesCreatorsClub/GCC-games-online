import pygame, sys, random
screen = pygame.display.set_mode((640, 480))
pygame.init()

game_state = 3

exit_sprite = pygame.image.load("exit.png")
enemy_sprite = pygame.image.load("enemy.png")
smoke_sprite = pygame.image.load("smoke.png")

enemies = []
smoke = []

next_smoke = 0

def DrawText (text, position):
    global screen, front
    text = font.render (text, 1,(225, 225, 120))
    screen.blit (text , position)

# Create map
walls = []
level = [
"####################",
"# #     x#####     #",
"# # #########      #",
"# #    # #E    ### #",
"#    ### #    #    #",
"####        E      #",
"#      ##########  #",
"#E           ##### #",
"##########EE       #",
"#####        ##### #",
"#      ######EE    #",
"#  #               #",
"#  #   # #  ###### #",
"#o  #             E#",
"####################",
           
]

NORMAL_GAME_STATE = 0
STARTUP_SCREEN_STATE = 1
YOU_LOSE_STATE = 2
YOU_WIN_STATE = 3



block_size = 32
#player_start_rect = pygame.Rect(0,0, block_size, block_size)
exit_rect = pygame.Rect(0, 0, block_size, block_size)
enemy_start_rect = pygame.Rect(0,0, block_size, block_size)

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

    "rect": pygame.Rect(64, 416, block_size, block_size),
    "start_rect": pygame.Rect(32, 448, block_size, block_size),
    "speed": 4,
    "direction":0,
    "velocity":[0,0]
    }

enemy = {
    "images":[
        pygame.image.load("enemy_left_1.png"),
        pygame.image.load("enemy_right_1.png"), 
        pygame.image.load("enemy_up_1.png"),
        pygame.image.load("enemy_down_1.png"),
        pygame.image.load("enemy_left_2.png"),
        pygame.image.load("enemy_right_2.png"),  
        pygame.image.load("enemy_up_2.png"),
        pygame.image.load("enemy_down_2.png")
        ],
    "rect": pygame.Rect(448, 32, block_size, block_size),
    "start_rect": pygame.Rect(448, 32, block_size, block_size),
    "speed": 4,
    "direction":[0,1],
    "velocity":[0,0],   
    "active":True
}

last_fire_button_state = False

def UpdatePlayerPosition(player, walls):
    global next_smoke
    
    player_move_rect = player["rect"]

    force = -0.5
    player["velocity"][0] = 0

    # Make a temporary marker of the player position        
    #move_rect = player["rect"]

    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT]:
        #move_rect = move_rect.move(-player["speed"], 0)
        player["velocity"][0] = -player["speed"]
        player["direction"] = 0
        
    if key[pygame.K_RIGHT]:
        #move_rect = move_rect.move(player["speed"], 0)
        player["velocity"][0] = player["speed"]
        player["direction"] = 1
        
    if key[pygame.K_DOWN]:
        player["direction"] = 3
        #player_move_rect = player_move_rect.move(0, speed)
        
    if key[pygame.K_UP]:
        # Add Jetpack thrust
        player["direction"] = 2
        force = 1

        if next_smoke > 0:
            next_smoke = next_smoke - 1
        else:
            next_smoke = 2
            direction = (random.randint(-1,1),3)
            rect = player['rect']

            smokelet = {
                "rect" : rect,
                "image" : smoke_sprite,
                "direction": direction,
                "ttl" : 40
                }
            smoke.append(smokelet)
        
    player["velocity"][1] = player["velocity"][1] - force
    if player["velocity"][1] > 0 and player["direction"] == 2:
        player["direction"] = 3

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


def DrawPlayer(player):
#    screen.blit(sprite, player['rect'])
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

def DrawBullets():
    global bullets, screen

    # For each active bullet
    for bullet in bullets:
        if bullet["active"] == True:
            screen.blit(bullet["image"], bullet["rect"])
 
def DrawSmoke():
    global smoke, screen

    for smokelet in smoke:
        screen.blit(smokelet["image"], smokelet["rect"])

def UpdateSmoke(walls):
    global smoke, screen

    for i in range(len(smoke) - 1, -1, -1):
        smokelet = smoke[i]
        ttl = smokelet["ttl"]
        ttl = ttl - 1
        if ttl == 0:
            del smoke[i]
        else:
            smokelet["ttl"] = ttl
            
            smokelet_rect = smokelet["rect"].move(0, smokelet["direction"][1])
            if smokelet_rect.collidelist(walls) == -1:
                smokelet["rect"] = smokelet_rect

            smokelet_rect = smokelet["rect"].move(smokelet["direction"][0], 0)
            if smokelet_rect.collidelist(walls) == -1:
                smokelet["rect"] = smokelet_rect
        
 
def UpdateBullets():
    global bullets, walls, enemies

    # For each active bullet
    for bullet in bullets:

        if bullet["active"] == True:
            bullet["rect"] = bullet["rect"].move(bullet["velocity"][0], bullet["velocity"][1])

            if bullet["rect"].collidelist(walls) > -1:
                bullet["active"] = False
            else:
#               for i in range(len(enemies) - 1, -1, -1):
                for enemy in enemies:
#                   enemy = enemies[i]
                   if bullet['rect'].colliderect(enemy['rect']):
#                       del enemies[i]
                       enemies.remove(enemy)
                       bullet["active"] = False
 
def CheckFireBullet():
    global bullets, player, last_fire_button_state, keys, last_fire_button_state

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
    # Store the last button state in the global for the next time...
    last_fire_button_state = current_fire_button_state


def CheckPlayerEnemiesCollision(enemies, player):
    for enemy in enemies:
        if enemy["active"]:
            enemy_move_rect = enemy['rect']
            if enemy_move_rect.colliderect(player['rect']):
                return True
    return False

def UpdateEnemyPosition(enemies, walls):
    for enemy in enemies:
        if enemy["active"]:
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
                    enemy['direction'] = [0,-1]# up
                elif random_direction == 2:
                    enemy['direction'] = [1,0] # right
                elif random_direction == 3:
                    enemy['direction'] = [-1,0]# left
            else:
                enemy['rect'] = enemy_move_rect

def DrawEnemies():
    global enemies, screen
    for enemy in enemies:
        if enemy["active"]:
           DrawEnemy(enemy)

def DrawEnemy(enemy):
    global debug_text
    animation_step = enemy["speed"] * 3
    animation_frames = 2
    image_index = 2
    if enemy["direction"] == [0,1]:
        image_index = 3
    if enemy["direction"] == [-1,0]:
        image_index = 0
    if enemy["direction"] == [1,0]:
        image_index = 1
        
    if image_index < 2: # Moving left/right?      
        if (enemy['rect'].left // animation_step) % animation_frames:
            image_index = image_index + 4
    else: # Moving Up/Down
        if (enemy['rect'].bottom // animation_step) % animation_frames:
            image_index = image_index + 4
    debug_text = "index=" + str(image_index)
    screen.blit(enemy['images'][image_index], enemy['rect'])


game_running = True

# Fill the walls array with rectangles for each '#'
x = y = 0
for row in level:
    for col in row:
        if col == "#":
            walls.append(pygame.Rect(x, y, block_size, block_size))

        # Set the player position if we find an 'o'
        if col == "o": 
            player_start_rect = pygame.Rect(x, y, block_size, block_size)

        if col == "x":
            exit_rect = pygame.Rect(x, y, block_size, block_size)

        # Set the enemy position if we find an 'E'
        if col == "E":
            new_enemy = {
			    "images":[
			        pygame.image.load("enemy_left_1.png"),
			        pygame.image.load("enemy_right_1.png"), 
			        pygame.image.load("enemy_up_1.png"),
			        pygame.image.load("enemy_down_1.png"),
			        pygame.image.load("enemy_left_2.png"),
			        pygame.image.load("enemy_right_2.png"),  
			        pygame.image.load("enemy_up_2.png"),
			        pygame.image.load("enemy_down_2.png")
			        ],
			    "rect": pygame.Rect(448, 32, block_size, block_size),
			    "start_rect": pygame.Rect(448, 32, block_size, block_size),
			    "speed": 4,
			    "direction":[0,1],
			    "velocity":[0,0],   
			    "active":True
			}

            new_enemy["rect"] = pygame.Rect(x, y, block_size, block_size)
            new_enemy["start_rect"] = pygame.Rect(x, y, block_size, block_size)
            enemies.append(new_enemy)       
            
        x += block_size
    y += block_size
    x = 0

# Global Game Variables
game_state = STARTUP_SCREEN_STATE
enemy_direction = [0,1]

enemy_rect = enemy_start_rect
font = pygame.font.SysFont("jingjing", 50)
bullets = []
for index in range(10):
    bullet = {
        "image":pygame.image.load("exit.png"),
        "rect":pygame.Rect(0, 0, 16, 16),
        "speed":8,
        "velocity":[0,0],
        "active":False
        }
    bullets.append(bullet)

debug_text = ""

small_rect = exit_rect.inflate(-100, -100)

while game_running:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if game_state == NORMAL_GAME_STATE:
        CheckFireBullet()
        UpdateSmoke(walls)
        UpdateBullets()
        UpdatePlayerPosition(player, walls)
        UpdateEnemyPosition(enemies, walls)

        if player['rect'].colliderect(exit_rect):
            game_state = YOU_WIN_STATE
    
        # Draw the screen
        # Background
        screen.fill((0, 0, 0))

        # Walls
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall)

        # Exit sprite
        screen.blit(exit_sprite, exit_rect)

        DrawSmoke()
        #DrawEnemy(enemy)
        DrawEnemies()
        #screen.blit(enemy_sprite, enemy_rect)
        DrawBullets()

        # Player
        DrawPlayer(player)
        enemy_speed = 4


        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy_rect.move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)
        

        enemyCollidedWithWall = 0
        if enemy_move_rect.collidelist(walls) != -1:
            enemyCollidedWithWall = 1
            random_direction = random.randint(0, 3)
            if random_direction == 0:
                enemy_direction = [0,1] 
            elif random_direction == 1:
                enemy_direction = [0,-1] 
            elif random_direction == 2:
                enemy_direction = [1,0] 
            elif random_direction == 3:
                enemy_direction = [-1,0] 
        else:
            enemy_rect = enemy_move_rect


        text = font.render("col " + str(enemyCollidedWithWall) + " px " + str(player['rect'][0]) + " py " + str(player['rect'][1]), 1, (128, 0, 128)) 
        #screen.blit(text, (0, 0))
        text = font.render(debug_text, 1, (128, 0, 128)) 
        screen.blit(text, (0, 0))
        if CheckPlayerEnemiesCollision(enemies, player):
            game_state = YOU_LOSE_STATE

    elif game_state == YOU_WIN_STATE: # 'You Made It' Screen -----------
        screen.fill((0, 128, 0))
        DrawText("You Made It!", (130, 100))
    
        if keys[pygame.K_SPACE]:
            game_state = NORMAL_GAME_STATE
            player_rect = player_start_rect
            enemy_rect = enemy_start_rect
      
    if game_state == YOU_LOSE_STATE: # 'You Lose!' Screen -----------
        screen.fill((128, 0, 0))
        DrawText("Oh No - You Lose!", (90, 100))
        
        if keys[pygame.K_SPACE]:
            game_state = NORMAL_GAME_STATE
            player_rect = player_start_rect
            enemy_rect = enemy_start_rect
        
    if game_state == STARTUP_SCREEN_STATE: 
        screen.fill((128, 0, 0))
        DrawText("Press space to begin!", (10, 300))

        if keys[pygame.K_SPACE]:
            game_state = NORMAL_GAME_STATE
        

    pygame.display.flip()

#pygame.quit()

