import pygame

def Add_xoffset(rect, offset):
    
    new_rect = pygame.Rect(rect.x - offset, rect.y, rect.width, rect.height)
    return new_rect

def Pick_Frame(images):
    time = pygame.time.get_ticks()
    animation_time = time % 4000
    if animation_time < 3600:
        image = images[0]
    elif animation_time >= 400:
        image = images[1]
        
    return image


pygame.init()

screen = pygame.display.set_mode((640,480))

image = pygame.image.load("Monster.png")
image2 = pygame.image.load("brown.png")
image3 = pygame.image.load("green.png")
image4 = pygame.image.load("sky.png")
image5 = pygame.image.load("enemy2.png")
image6 = pygame.image.load("tile_tree.png")
image7 = pygame.image.load("hearts.png")
image8 = pygame.image.load("spikes.png")
image9 = pygame.image.load("heart2.png")
image10 = pygame.image.load("coin.png")
image11 = pygame.image.load("sun.png")
image12 = pygame.image.load("Brick.png")
image13 = pygame.image.load("brick_broken.png")
image14 = pygame.image.load("Monster_blinking.png")
image14 = pygame.image.load("sign.png")
image15 = pygame.image.load("stone.png")
image16 = pygame.image.load("stone2.png")
image17 = pygame.image.load("Wood.png")
image18 = pygame.image.load("ladder.png")
image19 = pygame.image.load("grass_ladder.png")
image20 = pygame.image.load("water.png")
image21 = pygame.image.load("underwater.png")
image22 = pygame.image.load("dead.png")
image23 = pygame.image.load("brickladder.png")
image24 = pygame.image.load("up.png")
image25 = pygame.image.load("cloud.png") 
image26 = pygame.image.load("hit.png")
image27 = pygame.image.load("grass2.png")
image28 = pygame.image.load("signscary.png")
image29 = pygame.image.load("enemygone.png")
image30 = pygame.image.load("bloodgrass.png")

player_images = [
    pygame.image.load("Monster.png"),
    pygame.image.load("Monster_blinking.png"),
    ]

main_font = pygame.font.SysFont("Ariel", 75, True)
lives_text = main_font.render("Lives:", False, (255,0,0))
score_font = pygame.font.SysFont("Ariel", 75, True)
main_text = main_font.render("START", False, (242, 245, 169))
setting_text = main_font.render("SETTING", False, (242, 245, 169))

game_state = "GAME"  

start_button_rect = pygame.Rect(208,250,200,50)
quit_button_rect = pygame.Rect(208,360,200,50)

player = {
    "rect": pygame.Rect(64,120,16,16),
    "Vx": 0.2,
    "Vy": 0,
    "can_jump": False,
    "lives": 5,
    "time_hit": -10000,
    "state": "normal"
    }
score = 0
x_offset = 0

grass = []
blocks = []
sky = []
enemies = []
spikes = []
hearts = []
trees = []
coins = []
bricks = []
broken_bricks = []
stones = []
stone = []
Wood = []
ladder = []
grass_ladder = []
water = []
underwater = []
dead = []
brickladder = []
up = []
sun = []
clouds = []
hit = []
signscary = []
enemygone = []
bloodgrass = []

level = [
    "                ",
    "                ",
    "                                                                                                                                                       bb",
    "                ",
    "                ",
    "                ",
    "                                                                                                                                        kkkk",
    "                                                                                                                                        bbbb                                                                                                                                                                                                                                                               ",
    "                                                                                                                                                                                                                                                                                                                                                                                                           ",
    "                                                                                                                                                                                                                                                                                                                                                                                                           ",
    "                                                                                                                                                                                                                                                                                                                 t              t                                                                          ",
    "                                                                                   S                                                                                                                                                     c    c    c    c    c         kkkkkkk                          v                                                                                                  ",
    "                                                                                                                                           n                                                                                            yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                                                                                                            ",
    "                                                                                                                             b          bbbb                                                                                            #######################################                                                                                                                            ",                           
    "                                                                                                     v                       m          mmbb                                                                                                                                                 yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyGG                                                                               ",        
    "                                                                                                                             m          mmbb                                                                                                                                              yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyGG                                                                               ",
    "                                                                                                        c                    m          mmbb                                                                                                                                            yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyGG                                                                               ",
    "                                                                                                                             m          mmbb                                                                                                                                          jj########################################################LL                                                                               ", 
    "                                                                                                                             m          mmbb                                                                                                                                      jjjjjjhhh#####################################################LL                          t                                 M                  ",                             
    "                       t                                                    t         t                             bb       m          mmbb                                                                                                                                   jjjjjhhhhhhhhh###################################################LL                                                                               ",
    "                                   bbb                                                                              bb       m          mmbb                                                                                                                                jjjjjhhhhhhhhhhhh###################################################LL                                                                               ",                       
    "                                                                                                     b        b     bb       m          mmbb                                                                                                                              jjjhhhhhhhhhhhhhhhh###################################################LL                                      c     c                     a        a  a",                      
    "                         e     c     e         c    k         c                       e         bbkkkkkkkkkkkkkkkkkkbb       m          mmbb                                                                 kkkkkkkk                                                   jjjjhhhhhhhhhhhhhhhhh###################################################yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyXXyyyyyyyXyyX",                                                                                                                          
    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy       m          mmbb                                               GGGyyyyyyyyyyyyyyyyyyyyyyyyyyyyy                                     jjjjjjjjjjjhhhhhhhhhhhhhhhhhh##############################################################yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy       m          mmbb                                               GGGyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyjj                             jjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhh#############################################################yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",                                          
    "######################################################################################################################QQQQQQQmQQQQQQQQQQmmbbQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQLLL################################hhjj                        jjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh####################################################################################################################################",
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL#################################hjjjj      kkkkk        jjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh####################################################################################################################################",
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL#################################hjjjjjjjjjjjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh####################################################################################################################################",                                                                     
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuxuuuuuLLL#################################hhjjjjjjjjjjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh####################################################################################################################################",
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL#################################hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh#####################################################################################################################",                                   
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL#################################jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj####################################################################################################################################",
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL#################################jjjjjjjjjajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj####################################################################################################################################",
    "######################################################################################################################uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuLLL###################################################################################################################################################################################################################################",
    ]
                                                    
x = y = 0
for row in level:
    for col in row:
        if col == "#":
            blocks.append(pygame.Rect(x, y, 16, 16))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        if col == "y":
            grass.append(pygame.Rect(x, y, 16, 16))

        if col == "s":
            sky.append(pygame.Rect(x, y, 640, 480))

        if col == "M":
            signscary.append(pygame.Rect(x, y, 640, 480))

        if col == "S":
            sun.append(pygame.Rect(x, y, 16, 16))

        if col == "k":
            spikes.append(pygame.Rect(x, y, 16, 16))

        if col == "a":
            enemygone.append(pygame.Rect(x, y, 16, 16))

        if col == "t":
            trees.append(pygame.Rect(x, y, 64, 64))

        if col == "c":
            coins.append(pygame.Rect(x, y, 16, 16))

        if col == "b":
            bricks.append(pygame.Rect(x, y, 16, 16))

        if col == "u":
            underwater.append(pygame.Rect(x, y, 16, 16))

        if col == "m":
            brickladder.append(pygame.Rect(x, y, 16, 16))

        if col == "x":
            dead.append(pygame.Rect(x, y, 16, 16))

        if col == "X":
            bloodgrass.append(pygame.Rect(x, y, 16, 16))

        if col == "h":
            stone.append(pygame.Rect(x, y, 16, 16))

        if col == "j":
            stones.append(pygame.Rect(x, y, 16, 16))

        if col == "Q":
            water.append(pygame.Rect(x, y, 16, 16))

        if col == "w":
            Wood.append(pygame.Rect(x, y, 16, 16))

        if col == "n":
            up.append(pygame.Rect(x, y, 16, 16))

        if col == "L":
            ladder.append(pygame.Rect(x, y, 16, 16))

        if col == "f":
            grass2.append(pygame.Rect(x, y, 16, 16))

        if col == "G":
            grass_ladder.append(pygame.Rect(x, y, 16, 16))

        if col == "e":
            enemy = {
                "rect": pygame.Rect(x,y,64,64),
                "Vx": -0.1,
                "Vy": 0,
                "image": image5
                }
            enemies.append(enemy)

        if col == "v":
            cloud = {
                "rect": pygame.Rect(x,y,64,64),
                "Vx": -0.1,
                "Vy": 0,
                "image": image25
                }
            clouds.append(cloud)

    
        x = x + 16
    y = y + 16
    x = 0

    
clock = pygame.time.Clock()
   

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
  
    dt = clock.tick(30)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        game_running = False

    #add enemy movement
    for enemy in enemies:
        enemy["rect"].x += enemy["Vx"] * dt

    for cloud in clouds:
        cloud["rect"].x += cloud["Vx"] * dt / 2

    if game_state == "GAME":
        
        if keys[pygame.K_a]:
            player["rect"].x -= player["Vx"] * dt

        if keys[pygame.K_d]:
            player["rect"].x += player["Vx"] * dt

        if keys[pygame.K_SPACE] and player["can_jump"]:
            player["Vy"] = -0.45
            player["can_jump"] = False
            
        player["Vy"] += 0.001 * dt
        if player["Vy"] > 0.3:
            player["Vy"] = 0.2  
               
        player["rect"].y += player ["Vy"] * dt
        # move in the y direction
        
    player_lives = player["lives"]
    for spike in spikes:
        if player["rect"].colliderect(spike):
            if pygame.time.get_ticks() - player["time_hit"] > 500:
                player["lives"] -= 1
                player["Vy"] = -0.6
                player["time_hit"] = pygame.time.get_ticks()
                player["state"] = "damaged"
                player["rect"].y = player["rect"].y - abs(player["Vy"] * dt) - 1
            

    for enemy in enemies:
        if player["rect"].colliderect(enemy["rect"]):
            if pygame.time.get_ticks() - player["time_hit"] > 500:
                player["lives"] -= 1
                player["Vy"] = -0.6
                player["time_hit"] = pygame.time.get_ticks()
                enemies.remove(enemy)
                player["state"] = "damaged"
                player["rect"].y = player["rect"].y - abs(player["Vy"] * dt) - 1

    for cloud in clouds:
        if player["rect"].colliderect(cloud["rect"]):
            if pygame.time.get_ticks() - player["time_hit"] > 500:
                player["lives"] -= 1
                player["Vy"] = -0.6
                player["time_hit"] = pygame.time.get_ticks()
                clouds.remove(cloud)
                player["state"] = "damaged"
                player["rect"].y = player["rect"].y - abs(player["Vy"] * dt) - 1
    if player_lives > 0 and player["lives"] <= 0:
        game_state = "GAME-OVER"
    
    if keys[pygame.K_r]:
        player["rect"].x = 0
        player["rect"].y = 0
        game_state = "GAME"

#crtl Z = back button.
    if game_state == "MENU":
        screen.fill((22, 183, 255))
        pygame.draw.rect(screen, (251, 230, 28), start_button_rect)
        pygame.draw.rect(screen, (251, 230, 28), quit_button_rect)
        pygame.draw.rect(screen, (221, 230, 28), start_button_rect)
        screen.blit(main_text, start_button_rect)
        screen.blit(setting_text, quit_button_rect)
      
        
    if game_state.startswith("GAME"):
        


        
        for block in blocks:
            if player["rect"].colliderect(block):
                player["rect"].bottom = block.top
                player["can_jump"] = True
                player["state"] = "normal"

        for coin in coins:
            if player["rect"].colliderect(coin):
                coins.remove(coin)
                score += 1
                
        for brick in bricks:
            if player["rect"].colliderect(brick):
                player["rect"].bottom = brick.top
                player["can_jump"] = True
                player["state"] = "normal"

        for s in stones:
            if player["rect"].colliderect(s):
                player["rect"].bottom = s.top
                player["can_jump"] = True
                player["state"] = "normal"

        for s in stone:
            if player["rect"].colliderect(s):
                player["rect"].bottom = s.top
                player["can_jump"] = True
                player["state"] = "normal"
                
        x_offset = player["rect"].x - 100
        if x_offset <0:
            x_offset = 0

        for w in Wood:
            if player["rect"].colliderect(w):
                player["rect"].bottom = w.top
                player["can_jump"] = True
                player["state"] = "normal"

        
        for X in bloodgrass:
            if player["rect"].colliderect(X):
                player["rect"].bottom = X.top
                player["can_jump"] = True
                player["state"] = "normal"


        for L in ladder:
            if player["rect"].colliderect(L):
                player["rect"].bottom = L.top
                player["can_jump"] = True
                player["state"] = "normal"


        for G in grass_ladder:
            if player["rect"].colliderect(G):
                player["rect"].bottom = G.top
                player["can_jump"] = True
                player["state"] = "normal"


        for m in brickladder:
            if player["rect"].colliderect(m):
                player["rect"].bottom = m.top
                player["can_jump"] = True
                player["state"] = "normal"

                
        for g in grass:
            if player["rect"].colliderect(g):
                player["rect"].bottom = g.top
                player["can_jump"] = True
                player["state"] = "normal"

        screen.fill((0,168,243))
        
        
        for block in blocks:
            screen.blit(image2, Add_xoffset(block, x_offset))
     
        for g in grass:
            screen.blit(image3, Add_xoffset(g, x_offset))

        for Q in water:
            screen.blit(image20, Add_xoffset(Q, x_offset))

        for n in up:
            screen.blit(image24, Add_xoffset(n, x_offset))

        for j in stones:
            screen.blit(image15, Add_xoffset(j, x_offset))

        for w in Wood:
            screen.blit(image17, Add_xoffset(w, x_offset))
        
        for a in enemygone:
            screen.blit(image29, Add_xoffset(a, x_offset))

        for M in signscary:
            screen.blit(image28, Add_xoffset(M, x_offset))

        for X in dead:
            screen.blit(image22, Add_xoffset(X, x_offset))

        for m in brickladder:
            screen.blit(image23, Add_xoffset(m, x_offset))

        for tree in trees:
            screen.blit(image6, Add_xoffset(tree, x_offset))

        for L in ladder:
            screen.blit(image18, Add_xoffset(L, x_offset))

        for u in underwater:
            screen.blit(image21, Add_xoffset(u, x_offset))

        for G in grass_ladder:
            screen.blit(image19, Add_xoffset(G, x_offset))

        for enemy in enemies:
            screen.blit(enemy["image"], Add_xoffset(enemy["rect"],x_offset))

        for spike in spikes:
            screen.blit(image8, Add_xoffset(spike, x_offset))

        for coin in coins:
            screen.blit(image10, Add_xoffset(coin, x_offset))
            
        for Brick in bricks:
            screen.blit(image12, Add_xoffset(Brick, x_offset))

        for Brick in broken_bricks:
            screen.blit(image13, Add_xoffset(Brick, x_offset))

        for h in stone:
            screen.blit(image16, Add_xoffset(h, x_offset))

        for X in bloodgrass:
            screen.blit(image30, Add_xoffset(X, x_offset))

        for cloud in clouds:
            screen.blit(cloud["image"], Add_xoffset(cloud["rect"],x_offset))
            
        screen.blit(image11, (screen.get_width()-100,100))

        for i in range(0, 5):
            if i + 1 > player["lives"]:
                screen.blit(image9, (i*54+180,0))
            else:
                screen.blit(image7, (i*54+180,0))

        score_text = score_font.render("Score: " + str(score), False, (246, 255, 0))

        screen.blit(lives_text, (0,0))
        screen.blit(score_text, (0,50))        
        
        if game_state == "GAME-OVER":
            gameover_text = score_font.render("GAME OVER", False, (246, 0, 0))
            screen.blit(gameover_text, (50,200))
            
        #player_rect.y += 1


        if player["state"] == "normal":
            screen.blit(Pick_Frame(player_images), Add_xoffset(player["rect"], x_offset))
        else:
            screen.blit(image26, Add_xoffset(player["rect"], x_offset))
    pygame.display.update()


pygame.quit()
