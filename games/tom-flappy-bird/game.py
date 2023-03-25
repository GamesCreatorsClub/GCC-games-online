import pygame, sys, random


level_0 = [
"######################",
"#    B  M  M  M  B   #",
"# x     M  B  M      #",
"#    S  B     B  S   #",
"#    N     S     N   #",
"#    M  S  N  S  M   #",
"#LLLLMLLNLLMLLNLLM   #",
"###################  #",
"#    M  M  M  B  M   #",
"#    M  B  M     B   #",
"# o  B     B  S      #",
"#       S     N  S   #",
"#    S  N  S  M  N   #",
"#LLLLNLLMLLNLLMLLMLLL#",
"######################"
]

level_1 = [
"######################",
"#              E   # #",
"# ####### ########x# #",
"# #              ### #",
"#   ############     #",
"# ###          # ### #",
"#     ######## # #   #",
"#####        # # #   #",
"#   # ######## # # ###",
"# #       E      #  E#",
"# # ############ ### #",
"# #              #   #",
"# ################ # #",
"#o                  E#",
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

def ScoreGate(player, scoregate):
    global score
    for gate in scoregate:
            if gate['rect'].colliderect(player['rect']) == True & gate["active"]==True:
                # print ("collided")
                score +=1
                gate["active"]=False
                # print (score)
                             
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
    g_large_font = pygame.font.SysFont("minecraftiaregular", 50)
    g_small_font = pygame.font.SysFont("minecraftiaregular", 30)
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
    global game_state, score
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        game_state = 0
        score = 0
        player["rect"] = player["start_rect"]
        for enemy in enemies:
            enemy["rect"] = enemy["start_rect"]
        for gate in scoregate:
            gate ['active'] = True

def CreateMap(level, player, level_exit, enemies):
    global screen, walls
    block_size = 32
    
    # Reset the wall & enemy lists
    walls[:] = []
    pipedown[:] = []
    pipeup[:] = []
    pipe[:] = []
    building[:] = []
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

            elif col == "B":
                pipedown.append(pygame.Rect(x, y, block_size, block_size))

            elif col == "N":
                pipeup.append(pygame.Rect(x, y, block_size, block_size))

            elif col == "M":
                pipe.append(pygame.Rect(x, y, block_size, block_size))

            # Set the player position if we find an 'o'
            elif col == "o":
                player["rect"] = pygame.Rect(x, y, block_size, block_size)
                player["start_rect"] = pygame.Rect(x, y, block_size, block_size)

            # Set the exit position if we find an 'x'
            elif col == "x":
                level_exit["rect"] = pygame.Rect(x, y, block_size, block_size)

            # Set the building position if we find an 'L'
            elif col == "L":
                building.append(pygame.Rect(x, y, block_size, block_size))

            # Set the enemy position if we find an 'E'
            if col == "E":
                enemy = {
                    "image":pygame.image.load("enemy_32.png"),
                    "rect":pygame.Rect(x, y, block_size, block_size),
                    "start_rect":pygame.Rect(x, y, block_size, block_size),
                    "direction":[0,1],
                    "speed":4
                    }
                enemies.append(enemy)

            #Set buildings position if we find a 'B'
            if col == "B":
                building_rect = pygame.Rect(x, y, block_size, block_size)

            # Set invisible score thing
            if col == "S":
                gatenumber = {
                    "rect":pygame.Rect(x, y, block_size, block_size),
                    "active":True
                    }
                scoregate.append(gatenumber)
                            
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
pipedown = []
pipeup = []
pipe = []
building = []
scoregate = []
score = 0
wall_sprite = pygame.image.load("wall_32.png")
pipedown_sprite = pygame.image.load("pipe_2.png")
pipeup_sprite = pygame.image.load("pipe_3.png")
pipe_sprite = pygame.image.load("pipe_1.png")
building_sprite = pygame.image.load ("build_32.png")
game_state = 0

# Load sounds
#pygame.mixer.init(frequency=22050, size=-16, channels=8, buffer=4096)
#pygame.mixer.set_num_channels(8)
#music_sound = pygame.mixer.Sound("flapsong.wav")

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
    "speed":4,
    "velocity":[0,0],
    "direction":0
    }

# Music
#music_sound.play(loops=-1, maxtime=0, fade_ms=0)

CreateMap(level_0, player, level_exit, enemies)
is_maze_level = False
# === Main Game Loop ===
while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_state == 0:
        if is_maze_level:
            UpdatePlayerPosition(player, walls)
        else:
            UpdateJetPackPlayerPosition(player, walls)
            
        UpdateEnemyPosition(enemies, walls)

        if player['rect'].collidelist(pipedown) != -1:
            game_state = 2

        if player['rect'].collidelist(pipeup) != -1:
            game_state = 2
        
        if player['rect'].collidelist(pipe) != -1:
            game_state = 2

        
        
        # Check if we have reached the exit or hit enemy
        if player['rect'].colliderect(level_exit['rect']):
            game_state = 1
            
        for enemy in enemies:
            if player['rect'].colliderect(enemy['rect']):
                game_state = 2

        ScoreGate(player, scoregate)

        

        key = pygame.key.get_pressed()
        #if key[pygame.K_y]:
        #    print (scoregate)

        
        # -- Draw the screen --
        # Background
        ClearScreen("SkyBlue")

        # Walls
        for wall in walls:
            # shadow first...
            pygame.draw.rect(screen, (123, 197, 205), wall.move(10, 10))

        for wall in building:
            screen.blit(building_sprite, wall)
        
        # Player
        DrawPlayer(player)
        
        # Enemy
        for enemy in enemies:
            screen.blit(enemy['image'], enemy['rect'])
            
        for wall in walls:           
            # now the walls
            screen.blit(wall_sprite, wall)

        for wall in pipedown:           
            # now the walls
            screen.blit(pipedown_sprite, wall)

        for wall in pipeup:           
            # now the walls
            screen.blit(pipeup_sprite, wall)

        for wall in pipe:  
            # now the walls
            screen.blit(pipe_sprite, wall)

        DrawSmallText(str(score), (350, 216), "Black")       
        
        # Exit
        screen.blit(level_exit['image'], level_exit['rect'])

        
    elif game_state == 1:
        ClearScreen("DarkOliveGreen")
        DrawLargeText("Flap flap flap", (130, 100), "Green")
        CreateMap(level_1, player, level_exit, enemies)
        is_maze_level = True
        CheckForResetGame(player, enemies)
            
    elif game_state == 2:
        ClearScreen("FireBrick")
        DrawLargeText("GAME OVER", (90, 100), "Red")
        CheckForResetGame(player, enemies)

    
        
    pygame.display.flip()
    # End of the game loop


