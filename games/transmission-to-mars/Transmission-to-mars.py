import pygame, sys, random, time

# Player Functions
def UpdatePlayerPosition(player):
    player_move_rect = player['rect']
    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player["direction"] = 0 
        player_move_rect = player_move_rect.move(-player['speed'], 0)
    if key[pygame.K_RIGHT]:
        player["direction"] = 1 
        player_move_rect = player_move_rect.move(player['speed'], 0)  
    if key[pygame.K_UP]:
        player["direction"] = 2
        player_move_rect = player_move_rect.move(0, -player['speed'])
    if key[pygame.K_DOWN]:
        player["direction"] = 3
        player_move_rect = player_move_rect.move(0, player['speed'])
    if (player_move_rect[0] >= 0) & (player_move_rect[0] < (xlmt) - 112) & (player_move_rect[1] > 64) & (player_move_rect[1] < (ylmt) - 82):
        player['rect'] = player_move_rect

def MenuBackground(player):
    player_move_rect = player['rect']
    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player["direction"] = 0 
        player_move_rect = player_move_rect.move(-player['speed'], 0)
    if key[pygame.K_RIGHT]:
        player["direction"] = 1 
        player_move_rect = player_move_rect.move(player['speed'], 0)  
    if key[pygame.K_UP]:
        player["direction"] = 2
        player_move_rect = player_move_rect.move(0, -player['speed'])
    if key[pygame.K_DOWN]:
        player["direction"] = 3
        player_move_rect = player_move_rect.move(0, player['speed'])
    if (player_move_rect[0] >= 0) & (player_move_rect[0] < (xlmt) - 112) & (player_move_rect[1] > 64) & (player_move_rect[1] < (ylmt) - 82):
        player['rect'] = player_move_rect
        
# Enemy Functions
def SpawnEnemies():
    global num_pirate0
    #SPAWN ASTEROIDS
    if ((current_time % 1000) < 100) & (len(enemies) < 10):
        x = (xlmt) + 112
        y = random.randint(70, (ylmt)-85)
        enemy = {
            "image":pygame.image.load("asteroid0.png"),
            "rect":pygame.Rect(x, y, 95, 85),
            "start_rect":pygame.Rect(x, y, 95, 85),
            "HP":20,
            "direction":[-1,0],
            "speed":random.randint(8,20),
            "id": 0,
            "life_time": 0,
            "fire_rate": 0,
            "score": 20
            }
        enemies.append(enemy)
        
    #SPAWN PIRATES
    if num_pirate0 < 4:
        x = (xlmt) + 112
        y = random.randint(70, (ylmt)-85)
        enemy = {
            "image":pygame.image.load("pirate0.png"),
            "rect":pygame.Rect(x, y, 124, 103),
            "start_rect":pygame.Rect(x, y, 124, 103),
            "HP":50,
            "direction":[-1,0],
            "speed": 7,
            "id": 1,
            "life_time": 0,
            "fire_rate": 60,
            "score": 100
            }
        
        num_pirate0 += 1
        enemies.append(enemy)

def UpdateEnemyPosition(enemies, bullets):
    for enemy in enemies:
        if enemy['id'] == 0:
            enemy_move_rect = enemy['rect']
            enemy_direction = enemy['direction']
            enemy_speed = enemy['speed']
            shot = bullets
            # update the enemy move rectangle according to direction & speed
            enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)
        
            enemy['rect'] = enemy_move_rect
        if enemy['id'] == 1:
            enemy_move_rect = enemy['rect']
            enemy_direction = enemy['direction']
            enemy_speed = enemy['speed']
            shot = bullets
            # update the enemy move rectangle according to direction & speed
            enemy_move_rect = enemy['rect'].move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)
        
            enemy['rect'] = enemy_move_rect

def UpdateProjectile(player, bullets):
    for bullet in bullets:
            bullet_move_rect = bullet['rect']
            bullet_direction = bullet['direction']
            bullet_speed = bullet['speed']
            bullet_move_rect = bullet['rect'].move(bullet_direction[0] * bullet_speed, bullet_direction[1] * bullet_speed)
            bullet['rect'] = bullet_move_rect

def DrawExplosion(explosion_rect, explode_start, explosion_image):
    now = pygame.time.get_ticks()
    animation_time = 90
    if (now - explode_start) < animation_time:
        screen.blit(explosion_image['image'][0], explosion_rect)
    elif(now - explode_start) < animation_time * 2:
        screen.blit(explosion_image['image'][1], explosion_rect)
    elif(now - explode_start) < animation_time * 3:
        screen.blit(explosion_image['image'][2], explosion_rect)
    elif(now - explode_start) < animation_time * 4:
        screen.blit(explosion_image['image'][3], explosion_rect)
    elif(now - explode_start) < animation_time * 5:
        screen.blit(explosion_image['image'][4], explosion_rect)

def CreateProjectiles(player, enemies):
    global laser_shot_time, laser_fire_rot
    key = pygame.key.get_pressed()
    laser_cooldown = 150
    # Create bullets for the player laser
    if (key[pygame.K_SPACE] & ((current_time - laser_shot_time) >= laser_cooldown)):
        laser_shot_time = current_time
        laser0.play()
        laser_fire_rot = laser_fire_rot + 1
        if laser_fire_rot % 2 == 0:
            bullet = {
                "image":pygame.image.load("laser_shot0.png"),
                "spark":pygame.image.load("laserspark.png"),
                "rect":pygame.Rect(player["rect"][0]+ 100, player["rect"][1] + 22, 23, 3),
                "start_rect":pygame.Rect(player["rect"][0]+ 100, player["rect"][1] + 22, 23, 3),
                "direction":[1,0],
                "speed":20,
                "id": 0
                }
        else:
            bullet = {
                "image":pygame.image.load("laser_shot0.png"),
                "spark":pygame.image.load("laserspark.png"),
                "rect":pygame.Rect(player["rect"][0]+ 100, player["rect"][1] + 57, 23, 3),
                "start_rect":pygame.Rect(player["rect"][0]+ 100, player["rect"][1] + 57, 23, 3),
                "direction":[1,0],
                "speed":20,
                "id": 0
                }
        screen.blit(bullet["spark"], (bullet["start_rect"][0] - 6,bullet["start_rect"][1] - 6))
        bullets.append(bullet)

    # Create bullets for enemies
    for enemy in enemies:
        enemy['life_time'] += 1
        # Bullets for PIRATE enemy
        if enemy['id'] == 1:
            if ((enemy['life_time'] % enemy['fire_rate']) == 0):
                plasma0.play()
                bullet = {
                    "image":pygame.image.load("purple_shot0.png"),
                    "rect":pygame.Rect(enemy["rect"][0] + 15, enemy["rect"][1] + 45, 13, 6),
                    "start_rect":pygame.Rect(enemy["rect"][0] + 15, enemy["rect"][1] + 45, 16, 6),
                    "direction":[-1,0],
                    "speed":25,
                    "id": 1
                    }
                bullets.append(bullet)

def PowerUpBlit():
    if power_up != []:
        for power in power_up:
            screen.blit(power['image'], power['rect'])

def UpdatePowerUp(power_up):
    for power in power_up:
            power_move_rect = power['rect']
            power_direction = power['direction']
            power_speed = power['speed']
            power_move_rect = power['rect'].move(power_direction[0] * power_speed, power_direction[1] * power_speed)
            power['rect'] = power_move_rect           

def PlayerDamage():
    global shield_power, shield_visible, impact_time
    ship_hit_explosion0.play()
    shield_visible = 1
    impact_time = current_time
    shield_power -= 1
             
# Screen Blitting Functions

def PlayerBlit(player, shield, impact_time):
    global shield_visible, shield_visible
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if current_time % 300 < 150:
            screen.blit(player["exhaust"][0], player["rect"])
        else:
            screen.blit(player["exhaust"][1], player["rect"])
    elif current_time % 300 < 150:
        screen.blit(player["exhaust"][2], player["rect"])
    else:
        screen.blit(player["exhaust"][3], player["rect"])

    shield['rect'][0] = player['rect'][0] - 11
    shield['rect'][1] = player['rect'][1] - 9
    
    if shield_visible == 1:
        if current_time - impact_time < 600:
            screen.blit(shield['image'], shield['rect'])
            if current_time % 2 == 0:
                screen.blit(player["hit"][0], player["rect"])
            else:
                screen.blit(player["hit"][1], player["rect"])
        else:
            shield_visible = 0
    else:
        screen.blit(player["image"], player["rect"])

def DrawHud():
    screen.blit(hud, (0,0))
    DrawSmallText("SHIELD", (16,10), "Blue")
    DrawSmallText("SCORE", (xlmt - 300, 10), "Blue")
    DrawSmallText(str(score), (xlmt - 150, 10), "Yellow")
    shield_bar_image = shield_power
    if shield_bar_image < 0:
        shield_bar_image = 0
    screen.blit(shield_bar["image"][shield_bar_image], (150,8))

# Helper Functions
def InitText():
    global g_large_font, g_small_font
    g_large_font = pygame.font.SysFont("SimHei", int(100 * (res/100)))
    g_small_font = pygame.font.SysFont("SimHei", 40)
    return False

def DrawLargeText(text, position, colour):
    font_colour = pygame.Color(colour)
    rendered_text = g_large_font.render(text, 1, font_colour)
    shadow_text = g_large_font.render(text, 1, (0, 0, 0))
    #screen.blit(shadow_text, (position[0] + 5, position [1] + 5))
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

# This function resets lots of variables and changes the gamestate so that the current level restarts
# Lists of enemies, bullets and power ups are cleared
def CheckForResetGame(player, enemies):
    global game_state, num_pirate0
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        game_state = 1
        player["rect"] = player["start_rect"]
        background['rect0'][0] = 0
        background['rect1'][0] = 1920
        shield_power = 4
        score = 0
        num_pirate0 = 0
        enemies.clear()
        bullets.clear()
        power_up.clear()
        
# Creates and moves the background image
def Background(background):
    global j
    pic1 = background['rect0']
    pic2 = background['rect1']
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        pic1[0] = pic1[0] - 10
        pic2[0] = pic2[0] - 10
    else:
        pic1[0] -= 5
        pic2[0] -= 5
    #print(background['rect0'].left)
    screen.blit(background['normal'], pic1)
    screen.blit(background['normal'], pic2)
    if pic1[0] <= -1920:
        pic1[0] +=3840
    if pic2[0] <= -1920:
        pic2[0] +=3840

##############################################################################
# === GAME INITIALISATION CODE STARTS HERE ===
# Initialisation

global xlmt, ylmt, res, score, current_time, shield_visible


# Set the ratio of screen size and ability to change res
x_ratio = 16
y_ratio = 10
res = 70
xlmt = x_ratio * res
ylmt = y_ratio * res

# Set up a load of constants which need to be allocated for various checks
shield_power = 4
shield_visible = 0
screen = pygame.display.set_mode((xlmt, ylmt))
score = 0
laser_shot_time = 0
laser_fire_rot = 0
impact_time = 0
laser_damage = 10
shield_visible = 0
pygame.init()
InitText()
enemies = []
bullets = []
power_up = []
explosion_rect = []
n = 0
num_pirate0 = 0
game_state = 1
j = 0
score = 0
# Load background images and info
background = {
    "normal":pygame.image.load("background1.png"),
    "rect0":pygame.Rect(0, 0, 1920, 1080),
    "rect1":pygame.Rect(1920, 0, 1920, 1080),
    "blur":[
        pygame.image.load("background1.png"),
        pygame.image.load("background1.png"),
        pygame.image.load("background1.png")
        ]
    }
# Load player info
player = {
    "image":pygame.image.load("craft1.png"),
    "hit":[
        pygame.image.load("craft1_hit0.png"),
        pygame.image.load("craft1_hit1.png")
        ],
    "exhaust":[
        pygame.image.load("exhaust_fast0.png"),
        pygame.image.load("exhaust_fast1.png"),
        pygame.image.load("exhaust_slow0.png"),
        pygame.image.load("exhaust_slow1.png"),
        ],
    "rect":pygame.Rect((xlmt/2)-41, (ylmt)/2 , 112, 82),
    "start_rect":pygame.Rect((xlmt/2)-41, (ylmt)/2, 112, 82),
    "speed":15,
    "direction":1    
    }
# Load HUD image, black bar
hud = pygame.image.load("hud_bar.png")
# Load shield image
shield = {
    'image':pygame.image.load("shield0.png"),
    'rect':pygame.Rect(player['rect'][0], player['rect'][1], 137, 100)
    }
# Load shield bar images
shield_bar = {
    "image":[
        pygame.image.load("shield_bar0.png"),
        pygame.image.load("shield_bar1.png"),
        pygame.image.load("shield_bar2.png"),
        pygame.image.load("shield_bar3.png"),
        pygame.image.load("shield_bar4.png")
        ]
    }
# Load images for the standard explosion
explosion_image = {
        "image":[
            pygame.image.load("explosion0.png"),
            pygame.image.load("explosion1.png"),
            pygame.image.load("explosion2.png"),
            pygame.image.load("explosion3.png"),
            pygame.image.load("explosion4.png")
            ]
        }
purple_planet = pygame.image.load("planet1.png")
text_flash = 0
explode_start = 0

# Load Sounds
pygame.mixer.init()
pygame.mixer.set_num_channels(8)
exploding_asteroid = pygame.mixer.Sound("darkexplosion.wav")
laser0 = pygame.mixer.Sound("las.wav")
ship_hit_explosion0 = pygame.mixer.Sound("explosion-04.wav")
plasma0 = pygame.mixer.Sound("dual-neutron-disruptor.wav")


# === Main Game Loop ===
while True:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Loop starts recording the current time which is used in multiple functions
    current_time = pygame.time.get_ticks()
    
    key = pygame.key.get_pressed()
    # Zeroth Game State draws the menu with the game background and interface in the background
    if game_state == 0:
        ClearScreen("black")
        Background(background)
        DrawHud()
        #MenuBackground(player)
        PlayerBlit(player, shield, impact_time)
        DrawLargeText("Transmission to Mars", (xlmt/5 - 3, (ylmt * 0.3) - 3), "Orange")
        DrawLargeText("Transmission to Mars", (xlmt/5, (ylmt * 0.3)), "Yellow")
        screen.blit(purple_planet, (xlmt/2 - 350,700))
        if text_flash % 30 < 15:
            DrawLargeText("Press Enter to Begin", (xlmt/5 - 3, (ylmt * 0.75) - 3), "DarkRed")
            DrawLargeText("Press Enter to Begin", (xlmt/5, ylmt * 0.75), "Red")
            text_flash += 1
        else:
            text_flash += 1
        if key[pygame.K_RETURN]:
            game_state = 1
            #cut_scene = True
            #while cut_scene == True:
                
            
    # 1st Game State game starts here with player position in centre of right side of screen
    elif game_state == 1:
        UpdatePlayerPosition(player)
        UpdateEnemyPosition(enemies, bullets)
        
        # Enemy Spawning
        SpawnEnemies()
        #SpawnPowerUp(player, enemies, bullets)

        # Check for collision of player with enemies
        for enemy in enemies:
            if player['rect'].colliderect(enemy['rect']):
                PlayerDamage()
                enemies.remove(enemy)
                # If the enemy that is hit is PIRATE then reduce pirate counter by 1
                if enemy['id'] == 1:
                    num_pirate0 -= 1
                # Check to see if shield is negative, i.e. player is killed, change game state to 3
                if shield_power == -1:
                    game_state = 3
                    shield_power = 4
            # Remove any enemies that have an x coord of less than 90, i.e. off screen
            if enemy['rect'][0] < -90:
                enemies.remove(enemy)
                # If the enemy that is hit is PIRATE then reduce pirate counter by 1
                if enemy['id'] == 1:
                    num_pirate0 -= 1

        # Check for collision of bullets with enemies, only checks if there are any enemies otherwise unneccesary
        if enemies != []:
            for enemy in enemies:
                for bullet in bullets:
                    if (enemy['rect'].colliderect(bullet['rect']) | enemy['rect'].colliderect(bullet['rect'])) & (bullet['id'] == 0):
                        # For player remove the damage value from the laser from the enemies 'HP' value to determine new 'HP'
                        if enemy['HP'] > laser_damage:
                                enemy['HP'] -= laser_damage
                                # Remove 'bullets' as soon as they hit their target
                                bullets.remove(bullet)
                        # If the damage done takes 'HP' below 0 initiate removal of the 'enemy' and make other changes
                        else:
                            exploding_asteroid.play()
                            explode_start = pygame.time.get_ticks()
                            explosion_rect = enemy['rect'] # Starts explosion at enemies last 'rect'
                            score = score + enemy['score'] # Increase the total score by the individual 'score' value of the enemy destroyed
                            #power = {
                             #   "image":pygame.image.load("powerup0.png"),
                              #  "rect":pygame.Rect(enemy["rect"][0], enemy["rect"][1], 48, 50),
                               # "start_rect":pygame.Rect(enemy["rect"][0], enemy["rect"][1], 48, 50),
                                #"direction":[-4,-1],
                                #"speed":1,
                                #"id": 0
                                #}
                            #power_up.append(power)

                            if enemy['id'] == 1:
                                num_pirate0 -= 1
                            bullets.remove(bullet)
                            enemies.remove(enemy)
                            
                    # If any bullets x position is off the screen remove it from 'enemies'
                    if bullet['rect'][0] > xlmt + 30:
                        bullets.remove(bullet)
                        
        # Check for collisions between enemy bullets and Player
        for bullet in bullets:
            if bullet['id'] == 1:
                if bullet['rect'].colliderect(player['rect']):
                    PlayerDamage()
                    bullets.remove(bullet)
                    if shield_power == -1:
                        game_state = 3
                        shield_power = 4
                    
                                
        # -- Draw the screen --
        # Background
        ClearScreen("black") # Clear screen
        Background(background) # draw starry background
        DrawHud() # Draw the Hud at top of screen
        CreateProjectiles(player, enemies) # Create any projectiles
        UpdateProjectile(player, bullets) # Move all projectiles
        
        UpdatePowerUp(power_up) # Move all power_ups
        PowerUpBlit() # Draw the power_ups
        
        # Player Blitting
        PlayerBlit(player, shield, impact_time)
     
        if n == 0:
            if key[pygame.K_g]:
                DetectCollision(player, enemies, bullets)
                n = 1
            
        # Enemy
        for enemy in enemies:
            #EnemyBlit(enemy)
            screen.blit(enemy['image'], enemy['rect'])

        # Draw bullets on screen
        for bullet in bullets:
            screen.blit(bullet['image'], bullet['rect'])

        # Check for explosion 'rect's at each rect draw explosion
        if explosion_rect != []:
            DrawExplosion(explosion_rect, explode_start, explosion_image)
        
        #skip level cheat
        
        if key[pygame.K_y]:
            game_state = 1
        if key[pygame.K_u]:
            game_state = 3

    # Game state 2 not in use at the moment
    elif game_state == 2:
        ClearScreen("Aquamarine3")
        DrawLargeText("Maze Complete", (200, 250), "RoyalBlue")
        CheckForResetGame(player, enemies)
    # Game state 3, game over, display text and then begin resetting variables        
    elif game_state == 3:
        ClearScreen("black") # Clear screen
        Background(background) # draw starry background
        DrawHud() # Draw the Hud at top of screen
        
        #UpdatePowerUp(power_up) # Move all power_ups
        PowerUpBlit() # Draw the power_ups
        
        # Player Blitting
        PlayerBlit(player, shield, impact_time)
            
        # Enemy
        for enemy in enemies:
            #EnemyBlit(enemy)
            screen.blit(enemy['image'], enemy['rect'])

        DrawLargeText("GAME OVER", (xlmt * 0.35, ylmt * 0.45), "Red")
        DrawLargeText("GAME OVER", (200, 250), "Red")
        j = 0
        score = 0
        explosion_rect = []
        CheckForResetGame(player, enemies)

    pygame.display.flip()
    # End of the game loop
