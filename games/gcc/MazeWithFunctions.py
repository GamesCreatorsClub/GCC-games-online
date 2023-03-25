import pygame, sys, random

level_0 = [
"######################",
"#       E#         # #",
"# ###### # ####### # #",
"# #              ### #",
"#   ############     #",
"# # #          # #####",
"#     ### ####   #   #",
"# ### #     x# ### # #",
"#   # ######## # # ###",
"# #              #   #",
"#   ############ ### #",
"# #              #   #",
"# ####### # ###### # #",
"#o        #    E     #",
"######################",
]

level_1 = [
"######################",
"#E                 # #",
"# ####### ########x# #",
"# #              ### #",
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

clock = pygame.time.Clock()


# Player Functions
def UpdatePlayerPosition(player, walls):
    player_move_rect = player['rect']
    speed = player['speed']
    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_move_rect = player_move_rect.move(-speed, 0)
    if key[pygame.K_RIGHT]:
        player_move_rect = player_move_rect.move(speed, 0)
    if key[pygame.K_UP]:
        player_move_rect = player_move_rect.move(0, -speed)
    if key[pygame.K_DOWN]:
        player_move_rect = player_move_rect.move(0, speed)

    # Only if the marker has not hit a wall do we update the player
    if player_move_rect.collidelist(walls) == -1:
        player['rect'] = player_move_rect

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
    global screen, walls
    block_size = 32
    
    # Reset the wall & enemy lists
    walls.clear()
    enemies.clear()

    # Fill the walls array with rectangles for each '#'
    x = 0 
    y = 0
    for row in level:
        for col in row:
            if col == " ":
                x += block_size
                continue
            
            if col == "#":
                walls.append(pygame.Rect(x, y, block_size, block_size))

            # Set the player position if we find an 'o'
            elif col == "o":
                player["rect"] = pygame.Rect(x, y, block_size - 10, block_size - 10)
                player["start_rect"] = pygame.Rect(x, y, block_size - 10, block_size - 10)

            # Set the exit position if we find an 'x'
            elif col == "x":
                level_exit["rect"] = pygame.Rect(x, y, block_size, block_size)

            # Set the enemy position if we find an 'E'
            elif col == "E":
                enemy = {
                    "image":pygame.image.load("enemy_32.png"),
                    "rect":pygame.Rect(x, y, block_size, block_size),
                    "start_rect":pygame.Rect(x, y, block_size, block_size),
                    "direction":[0,1],
                    "speed":4
                    }
                enemies.append(enemy)
            
            x += block_size
        y += block_size
        x = 0

# === ACTUAL GAME CODE STARTS HERE ===
# One-off initialisation to start
pygame.init()
InitText()
screen = pygame.display.set_mode((len(level_0[0]) * 32, len(level_0) * 32))
walls = []
enemies = []
wall_sprite = pygame.image.load("wall_32.png")
game_state = 0

level_exit = {
    "image":pygame.image.load("exit_32.png"),
    "rect":pygame.Rect(0, 0, 32, 32)
    }

player = {
    "image":pygame.image.load("sprite_32.png"),
    "rect":pygame.Rect(0, 0, 32, 32),
    "start_rect":pygame.Rect(0, 0, 32, 32),
    "speed":4    
    }

CreateMap(level_0, player, level_exit, enemies)

# === Main Game Loop ===
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_state == 0:
        UpdatePlayerPosition(player, walls)
        UpdateEnemyPosition(enemies, walls)
        
        # Check if we have reached the exit or hit enemy
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
            # now the walls
            screen.blit(wall_sprite, wall)
            
        # Player
        screen.blit(player['image'], player['rect'])
        # Exit
        screen.blit(level_exit['image'], level_exit['rect'])
        # Enemy
        for enemy in enemies:
            screen.blit(enemy['image'], enemy['rect'])
        
    elif game_state == 1:
        ClearScreen("DarkOliveGreen")
        DrawLargeText("You Made It!", (130, 100), "Green")
        CreateMap(level_1, player, level_exit, enemies)
        CheckForResetGame(player, enemies)
            
    elif game_state == 2:
        ClearScreen("FireBrick")
        DrawLargeText("Oh No - You Lose!", (90, 100), "Red")
        CheckForResetGame(player, enemies)
    
    shadow_text = g_large_font.render("fps: " + str(clock.get_fps()), 1, (255, 255, 255))
    screen.blit(shadow_text, (300, 5))
    
    pygame.display.flip()
    # End of the game loop


