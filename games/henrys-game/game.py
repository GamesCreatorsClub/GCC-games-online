#print("Press SPACE to use movement item (you dont start with one of those)\nLeft click to use sycthe\nRespond to this with 'help' for the list of items and where to get them")
espeed = 0
current_time = 0
health = 5
scythecooldown = 100
playercooldown = 0
showborder = False
player_bugatti = False
#should be made to false after testing
the_number = 3
IWOKEUPINANEWBUGATTI = False
#time_reset = True
Ecount = 0
import pygame
bugatti_item_rect = pygame.Rect(200,200,32,32)
rebirths = 1
E = 20
speed = 3
espeedplus = 0
game_state = "limbo"
sythe = "standard scythe"
import time
import sys
import random

money = 0
kills = 0
randX = random.randint(0,1626)
randY = random.randint
(0,846)
def  Add_X_Offset(rect,offset):
    rect2 = pygame.Rect(rect.x - offset,rect.y,rect.width,rect.height)
    return rect2
def Pick_frame(images):
    anitime = current % 4000
current = pygame.time.get_ticks()
Etime = current / 10000

    
pygame.init()
#This is where we set up the window that displays our game. The resolution is set here
screen = pygame.display.set_mode((1626,846))
#This sets the windows caption
pygame.display.set_caption("Maze Game")

quitImage = pygame.image.load("quitimage.png")

clock = pygame.time.Clock()

platformerwall = pygame.image.load('platformer_wall.png')
wall = pygame.image.load('litterally_nothing.png')
acctualwall = pygame.image.load("Wall_revamped_resoluted.png")
#player = pygame.image.load('man-1.png')
normal_player = pygame.image.load('man-1.png')
doorimage = pygame.image.load('door_revamped_resoluted.png')
munniimage = pygame.image.load('gamemunni.png')
rich_player = pygame.image.load('money!.png')
crateimage = pygame.image.load('crate_resoluted.png')
evil_wall = pygame.image.load('spoik.png')
error = pygame.image.load('you_got_mail.png')
finish_image = pygame.image.load('finishsimpl.png')
player_left = pygame.image.load("character_left.png")
player_right = pygame.image.load("character_right.png")
player_image = pygame.image.load("character_right.png")
player = pygame.image.load("character_left.png")
player_sythe_right = pygame.image.load("character_sythe_right.png")
player_sythe_left = pygame.image.load("character_sythe_left.png")
chest_rightimage = pygame.image.load("closed_chest.png")
painting_image = pygame.image.load("painting.png")
blood_sythe_left = pygame.image.load("b_sythe_left.png")
blood_sythe_right = pygame.image.load("b_sythe_right.png")
error = pygame.image.load("you_got_mail_enlargened.png")
ded = pygame.image.load("youdieddedscreen.png")
win = pygame.image.load("the_you_win_screen.png")
Jbarrierimage = pygame.image.load("wall_revamped_resoluted.png")
Sbarrierimage = pygame.image.load("wol.png")
grassimage = pygame.image.load("grazz2.png")
jumpimage = pygame.image.load("srengbloc.png")
startimage = pygame.image.load("startbutton2.png")
hoverstart = pygame.image.load("stort.png")
icemode = pygame.image.load("icemodebutton.png")
icemodehover = pygame.image.load("icemodehover2.png")
pathimage = pygame.image.load("parf.png")
uppathimage = pygame.image.load("path_down.png")
sidepathimage = pygame.image.load("path_soidways.png")
crosspathimage = pygame.image.load("crosspath.png")
campfireimage = pygame.image.load("campfoyer1.png")
eye = pygame.image.load("eye_right.png")
hellmode = pygame.image.load("hellmode.png")
hellmodehover = pygame.image.load("hell,clicked.png")
bugatti = pygame.image.load("IWOKEUPINANEWBUGATII.png")
bugatti_left = pygame.image.load("IWOKEUPINANEWBUGATTI_left.png")
heart =  pygame.image.load("heart.png")
sycthe_recharge_image = pygame.image.load("sycthe_recharge_symbol.png")
Epress = pygame.image.load("Epress.png")
scythe_up = pygame.image.load("scythe_holding_up.png")
scythe_down = pygame.image.load("scythe_holding_down.png")

numbr = 20
spawns = 1

location = (100,870)


x = y = 0
level = ["##-U---------U---------U----------------------------------------------------",
         "##-U---------U---------U----------------------------------------------------",
         "##-U---------U---------U----------------------------------------------------",
         "##-U---------U---------U----------------------------------------------------",
         "##-ASSASSSSSSASSSSSSSSSA----------------------------------------------------",
         "##-U--U------U--------------------------------A-----------------------------",
         "##-U--U------U--------------------------------U-----------------------------",
         "##-U--U------U--------------------------------U-----------------------------",
         "##-ASSASSSSSSA-----------------------------ASAAASA--------------------------",
         "##-U--U------------------------------------U-U-U-U--------------------------",
         "##-U--U------------------------------------ASA-ASA--------------------------",
         "##-U--U---------------------------------------------------------------------",
         "##C-ASA---------------------------------------------------------------------"]

walls = []
doors = []
munniz = []
crates = []
ewalls = []
finishes = []
enemies = []
turnings = []
chest_rights = []
paintings = []
randXYs = []
Jbarriers = []
Sbarriers = []
platforms = []
Awalls = []
grassess = []
Jumps = []
lucases = []
bigrects = []
craterects = []
paths = []
Upaths = []
Spaths = []
Apaths = []
bugatti_item_rects = []
campfires = []
for i in range (20):
    xy = (random.randint(300,1326),random.randint(100,746))
    randXYs.append(xy)
  

for col in level:
    for row in col:
        if row == "T":
            rect1 = pygame.Rect(x,y ,72,72)
            walls.append(rect1)
        if row == "C":
            location = pygame.Rect(87,0,32,32)
#            player = {
#                "rect": pygame.Rect(870,32,32)
#                "speed": 3
#                "image": pygame.image.load("player_right.png")
        if row == "D":
            door = pygame.Rect(x,y,72,72)
            doors.append(door)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
        if row == "M":
            munni = pygame.Rect(x +10,y +15,32,32)
            munniz.append(munni)
            

        if row == "K":
            enemy = {
            "health": 1,
            "rect": pygame.Rect(x,y,72,72),
            "speed.x": 900,
            "speed.y": 900,
            "image": pygame.image.load('eye_left.png'),
            "cooldown": 0,
            "bugatti": random.randint(1,20),
            }
            grass = pygame.Rect(x,y,72,72)
            grassess.append(grass)
            enemies.append(enemy)
            
        if row == "#":
            rect1 = pygame.Rect(x,y,72,72)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
            Awall = pygame.Rect(x,y,72,72)
            Awalls.append(Awall)
            
        if row == "-":
            grass = pygame.Rect(x,y,72,72)
            grassess.append(grass)
            
        if row == "R":
            rect1 = pygame.Rect(x,y,72,72)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
            crate = pygame.Rect(x,y,72,72)
            crates.append(crate)
            craterect = pygame.Rect(x,y,75,75)
            craterects.append(craterect)
            
        if row == "P":
            path = pygame.Rect(x,y,72,72)
            paths.append(path)
            
        if row == "U":
            Upath = pygame.Rect(x,y,72,72)
            Upaths.append(Upath)
            
        if row == "S":
            Spath = pygame.Rect(x,y,72,72)
            Spaths.append(Spath)
            
        if row == "A":
            Apath = pygame.Rect(x,y,72,72)
            Apaths.append(Apath)
            
        if row == "F":
            campfire = pygame.Rect(x,y,72,72)
            campfires.append(campfire)
            rect1 = pygame.Rect(x+5,y+5,62,62)
            walls.append(rect1)
            turning = pygame.Rect(x+5,y+5,62,62)
            turnings.append(turning)
        x = x + 72
    y = y +72
    x = 0
x_offset = 0
spawnx = location.x + 950
spawny = random.randint(100,746)
eyes = 0
vy = 0.22
clock = pygame.time.Clock()
vx = 0.22
location.x = 82
location.y = 760
game_over = False
canjump = False
clide = False
time_hit = -1000
time_hit = pygame.time.get_ticks()
#if pygame.get.ticks() -time_hit > 500:
#   print("a")

#12 x 23 (72)

while not game_over:
    #This checks if the cross in the top right has been pressed (do not remove)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #This will fill the window with a solid RGB colour
#    for w in walls:      
#        if location.colliderect(w):
#            canjump = True

 #   if Etime > 100:
        
    if game_state == "limbo":
        current = 0
        screen.fill((255,255,255))
        play_button_rect = pygame.Rect(553,293,630,300)
        quit_button_rect = pygame.Rect(1410,740,210,100)
        screen.blit(startimage,(553,293))
        Espeed = 0
        health = 5
        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hoverstart,(553,293))
            if pygame.mouse.get_pressed(1)[0]:
                GM = "standard"
                location.x = 972
                location.y = 754
                game_state = "alive"
                grassimage = pygame.image.load("graz.png")
                vx = 0.22
        hellmoderect = pygame.Rect(100,100,300,200)
        for enemy in enemies:
            enemies.remove(enemy)
        Ecount = 0
        screen.blit(hellmode,(100,100))
        if hellmoderect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hellmodehover,(100,100))
            if pygame.mouse.get_pressed(1)[0]:
                GM = "hell"
                location.x = 972
                location.y = 754
                grassimage = pygame.image.load("ash_ketsherm.png")
                game_state = "alive"
                pathimage = pygame.image.load("ash_ketsherm.png")
                uppathimage = pygame.image.load("ash_ketsherm.png")
                sidepathimage = pygame.image.load("ash_ketsherm.png")
                crosspathimage = pygame.image.load("ash_ketsherm.png")
                campfireimage = pygame.image.load("ash_ketsherm.png")
    if game_state == "alive":
        for enemy in enemies:
            if enemy["cooldown"] > 0:
                enemy["cooldown"] = enemy["cooldown"] - 1
        if location.y >= 850:
            location.y = 750
        if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(1)[0]:
                game_state = "limbo"
        dt = clock.tick(30)
    if game_state == "alive":
#1626,846
        #650
        #338
        main_font = pygame.font.SysFont("Ariel",25)
        rebirths = main_font.render("Rebirths: "+ str(spawns),False,(20,20,20))
        playercooldown = playercooldown +1
#        myfont = pygame.font.SysFont("ariel",32)
#        mytext = myfont.render("money: " + str(money) + "     spawns:  " + str(spawns) + "     scythe:  " + str(sythe),1,(0,0,0))
#        myfont2 = pygame.font.SysFont("ariel",25)
#        mytextbottom = myfont2.render("collecting money may help in upgrading the scythe",1,(0,0,0))
#        while time_reset == True:
        current_time = time.time
        Etime = current % 600
        if GM == "standard":
            if Etime == 1:
                if Ecount < 4:
                    enemy = {
                    "health": 3,
                    "rect": pygame.Rect(spawnx,spawny,72,72),
                    "speed.x": 5,
                    "speed.y": 5,
                    "image": pygame.image.load('eye_left.png'),
                    "cooldown": 0,
                    "bugatti": random.randint(1,20),
                    }
                    enemies.append(enemy)
                    Ecount = Ecount +1

        if GM == "hell":
            if Etime < 100:
                if Ecount < 25:
                    enemy = {
                    "health": 100,
                    "rect": pygame.Rect(spawnx,spawny,72,72),
                    "speed.x": 5,
                    "speed.y": 5,
                    "image": pygame.image.load('eye_left.png'),
                    "cooldown": 0,
                    "bugatti": random.randint(1,20),
                    }
                    enemies.append(enemy)
                    Ecount = Ecount +1
            
        keys = pygame.key.get_pressed()
#        for s in Sbarrierers:
#            if location.colliderect(s):
#                location.y = location.y +1
        for enemy in enemies:
            if GM == "standard":
                if enemy["health"] < 3:
                    if enemy["speed.x"] > 0:
                        enemy["image"] = pygame.image.load("angryboi_left.png")
                    else:
                        enemy["image"] = pygame.image.load("angryboi.png")
                else:
                    if enemy["speed.x"] > 0:
                        enemy["image"] = pygame.image.load("eye_left.png")
                    else:
                        enemy["image"] = pygame.image.load("eye_right.png")
            if GM == "hell":
                if enemy["health"] < 3:
                    if enemy["speed.x"] > 0:
                        enemy["image"] = pygame.image.load("angryboi_left.png")
                    else:
                        enemy["image"] = pygame.image.load("angryboi.png")
                else:
                    if enemy["speed.x"] > 0:
                        enemy["image"] = pygame.image.load("helleye_right.png")
                    else:
                        enemy["image"] = pygame.image.load("helleye_lefte.png")
            

        if GM == "standard" or GM == "hell":
            bartime = current
#            print(bartime)
            if espeed < the_number and espeed > -the_number:
                if keys[pygame.K_a]:
                    location.x = location.x - vx*dt
                    player_image = pygame.image.load("character_left.png")
                    for w in walls:
                        if location.colliderect(w):
                            location.midleft=(w.midright[0],location.midleft[1])
            else:
                if espeed > 0:
                    if keys[pygame.K_a]:
                       espeed = espeed -0.05
#            for enemy in enemies:
#                if Etime 
                            
            for enemy in enemies:
                if enemy["speed.x"] > E:
                    enemy["speed.x"] = E
                if enemy["speed.x"] < -E:
                    enemy["speed.x"] = -E
                if enemy["speed.y"] > E:
                    enemy["speed.y"] = E
                if enemy["speed.y"] < -E:
                    enemy["speed.y"] = -E

                if location.x - enemy["rect"].x > 0:
                     enemy["speed.x"] = enemy["speed.x"] + 0.2
                else:
                    enemy["speed.x"] = enemy["speed.x"] - 0.2

                if location.y - enemy["rect"].y > 0:
                     enemy["speed.y"] = enemy["speed.y"]  + 0.2
                else:
                     enemy["speed.y"] = enemy["speed.y"] - 0.2
            for enemy in enemies:
                if enemy["rect"].y > 774 or enemy["rect"].y < 0:
                    enemy["speed.y"]= enemy["speed.y"]*-1
 #                   if enemy["speed.y"] > 10:
 #                       enemy["speed.y"] = enemy["speed.y"] -4
                if enemy["rect"].x < 0:
                    enemy["speed.x"] = enemy["speed.x"]*1

            if vx > 0:
                for w in walls:
                      if location.colliderect(w):
                        location.midright=(w.midleft[0],location.midright[1])

            if vx < 0:
                for w in walls:
                    if location.colliderect(w):
                        location.midleft=(w.midright[0],location.midleft[1])


                    
            current = pygame.time.get_ticks()
            if espeed < the_number and espeed > -the_number:
               if keys[pygame.K_d]:
                    location.x = location.x + vx*dt
                    player_image = pygame.image.load("character_right.png")
                    for w in walls:
                        if location.colliderect(w):
                            location.midright=(w.midleft[0],location.midright[1])
            else:
                if keys[pygame.K_d]:
                    if espeed < 0:
                        espeed = espeed +0.05

            if keys[pygame.K_w]:
                location.y = location.y - vy*dt
                for w in walls:
                    if location.colliderect(w):
                        location.midtop=(location.midtop[0],w.midbottom[1])
                

            if keys[pygame.K_s]:
                location.y = location.y + vy*dt

 #           if keys[pygame.K_f]:
 #               time_reset = False
 #               HS = current
 #               print(hs)
            

        if GM == "ice":
            location.x = location.x +vx*dt
            if keys[pygame.K_a]:
                vx = vx -0.008
                player_image = pygame.image.load("character_left.png")
            


            if keys[pygame.K_d]:
                vx = vx +0.008
                player_image = pygame.image.load("character_right.png")
            if vx > 0:
                vx = vx -0.001
                for w in walls:
                      if location.colliderect(w):
                        location.midright=(w.midleft[0],location.midright[1])
                        vx = 0

            if keys[pygame.K_w]:
                location.y = location.y - vy*dt
            if vx < 0:
                vx = vx +0.001
                for w in walls:
                    if location.colliderect(w):
                        location.midleft=(w.midright[0],location.midleft[1])
                        vx = 0
            if vx >= 0.3:
                vx = 0.3
            if vx <= -0.3:
                vx = -0.3
                

            Jbarrier.x+=speed
        
            Jbarrier.x-=speed

        if keys[pygame.K_d]:
            player = player_right
            if keys[pygame.K_e]:
                if money < 10:
                    player = player_sythe_right
                if money >= 10:
                    player = m_sythe_right
        if IWOKEUPINANEWBUGATTI == True:
            if keys[pygame.K_SPACE]:
                player_bugatti = True
                vx = 0.25
            else:
                player_bugatti = False
                vx = 0.2

                

        if keys[pygame.K_a]:
            player = player_left
            if keys[pygame.K_e]:
                if money < 10:
                    player = player_sythe_left
                if money >= 10:
                    player = m_sythe_left
                 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_t:
                    if bartime > 200:
                        bartime = 0
                        if showborder == True:
                            showborder = False
                        else:
                            showborder = True
        if scythecooldown > 0:
            if pygame.mouse.get_pressed(1)[0]:
                if keys[pygame.K_d]:
                    player_image = pygame.image.load("Character_sythe_right.png")
                elif keys[pygame.K_w]:
                    player_image = pygame.image.load("scythe_holding_up.png")
                elif keys[pygame.K_s]:
                    player_image = pygame.image.load("scythe_holding_down.png")
                else:
                    player_image = pygame.image.load("Character_sythe_left.png")

        




#        if (keys[pygame.K] == True and canjump == True) or keys[pygame.K_t]:
#            canjump = False
#            vy = -0.55
#        vy += 0.001 * dt
#        if vy > 0.4:
#            vy = 0.4
            


        if keys[pygame.K_q]:
            for w in walls:
                if clide == True:
                    for w in walls:
                        wall.remove(w)

#        location.y += vy * dt
#        location.y+=speed
        for w in walls:
            if location.colliderect(w):
                if location.midbottom[1] > w.midtop[1]:
                    canjump = True
                else:
                    canjump = False
                if vy > 0:
                    location.midbottom=(location.midbottom[0],w.midtop[1])
                if vy < 0:
                    canjump = False
                    location.midtop=(location.midtop[0],w.midbottom[1])
 
 
                

                    
                
        x_offset = location.x -740
        
        if money >= 10:
            sythe = "money scythe"
        if keys[pygame.K_m]:
            money = 100
        if keys[pygame.K_q]:
            enemy = {
            "health": 3,
            "rect": pygame.Rect(spawnx,spawny,72,72),
            "speed.x": 5,
            "speed.y": 5,
            "image": pygame.image.load('eye_left.png'),
            "cooldown": 0,
            "bugatti": random.randint(1,20),
            }
            enemies.append(enemy)

        if keys[pygame.K_x]:
            enemy = {
            "health": 3,
            "rect": pygame.Rect(spawnx,spawny,72,72),
            "speed.x": 5,
            "speed.y": 5,
            "image": pygame.image.load('eye_left.png'),
            "cooldown": 0,
            "bugatti": 20
            }
            enemies.append(enemy)
            
#        for enemy in enemies:
#            if enemy["rect"].colliderect(rect1):
#                enemy["speed.x"] = enemy["speed.x"]*-1
                
        for m in munniz:
            if location.colliderect(m):
                munniz.remove(m)
                money = money +1
                print(money)
                
        for e in ewalls:
            if location.colliderect(e):
                spawns = spawns -2
                location.x = 72
                location.y = 754

        for f in finishes:
            if location.colliderect(f):
                game_state = "win"

        for J in Jbarriers:
            if location.colliderect(J):
                print("A")

        for u in Jumps:
            if location.colliderect(u):
                vy = -0.8
                vy += 0.001 * dt
                if vy > 0.4:
                    vy = 0.4
        location.x = location.x + espeed
        if espeed > 0:
            espeed = espeed -0.05
        else:
            espeed = espeed +0.05
 #       if espeed <= 1.5:
 #           espeed = 0
        if pygame.mouse.get_pressed(1)[0]:
            scythecooldown = scythecooldown -1
            if scythecooldown <= 0:
                scythecooldown = 0
        else:
            scythecooldown = scythecooldown +0.25
            if scythecooldown >= 100:
                scythecooldown = 100
            
        for enemy in enemies:
            if GM == "standard":
                if scythecooldown > 0:
                    if pygame.mouse.get_pressed(1)[0]:
                        if location.colliderect(enemy["rect"]):
                            if enemy["cooldown"] <= 0:
                                if keys[pygame.K_d]:
                                    espeedplus = 3
                                if keys[pygame.K_a]:
                                    espeedplus = -3
                                if keys[pygame.K_w]:
                                    espeedplus = 3
                                if keys[pygame.K_s]:
                                    espeedplus = -3
                                enemy["health"] = enemy["health"] - 1
                                if not keys[pygame.K_w] or not [pygame.K_s]:
                                    enemy["speed.x"] = enemy["speed.x"]*-1 +espeedplus
                                else:
                                    enemy["speed.y"] = enemy["speed.y"]*-1 +espeedplus
                                enemy["cooldown"] = 50
                                if enemy["health"] <= 0:
                                    enemy["image"] = pygame.image.load("eyered.png")
                    else:
                        if playercooldown > 15:
                            if location.colliderect(enemy["rect"]):
                                playercooldown = 0
                                if keys[pygame.K_a]:
                                    espeed = 7
                                if keys[pygame.K_d]:
                                    espeed = -7
                                else:
                                    espeed = -7
                                health = health -1
                                if health <= 0:
                                    game_state = "dead"
                if scythecooldown <= 0:
                    if playercooldown > 15:
                        if location.colliderect(enemy["rect"]):
                            playercooldown = 0
                            if keys[pygame.K_a]:
                                espeed = 7
                            if keys[pygame.K_d]:
                                espeed = -7
                            else:
                                espeed = -7
                            health = health -1
                            print(health)
                            if health <= 0:
                                game_state = "dead"
                        

            if GM == "hell":
                if location.colliderect(enemy["rect"]):
                    game_state = "dead"
                

        if espeed < the_number and espeed > -the_number:
            espeed = 0
        for w in walls:
            if location.colliderect(w):
                espeed = 0

        randomE = random.randint(0,1)
        if randomE == 0:
            spawnx = location.x - 950
        else:
            spawnx = location.x + 950

            

        spawny = random.randint(100,746)
        if spawnx < 144 or spawnx > 3000 :
            spawnx = spawnx*-1
             
#        for t in turnings:
#            if colliderect location:
#                turnings.remove turning
        
        for enemy in enemies:
            enemy['rect'].x = enemy['rect'].x + enemy['speed.x']
            enemy['rect'].y = enemy["rect"].y + enemy["speed.y"]
            for turning in turnings:
                if turning.colliderect(enemy["rect"]):
 #                   print("yeah bro the enemy acctually collided idk why its not reacting to it tho")
 #                   print(enemy["speed.x"],"before")
                    enemy["speed.x"] *= -1
 #                   print(enemy["speed.x"],"after")
 #                   enemy["speed.y"] *= -1


#if no enemies spawn then this'll error
            


        if spawns <= -1:
            game_state = "dead"
            spawns = 1
            

        


        if GM == "standard":
            screen.fill((180,200,255))
        if GM == "hell":
            screen.fill((100,40,40))
#        screen.blit(player,Add_X_Offset(location,x_offset))
        for m in munniz:
            screen.blit(munniimage,Add_X_Offset(m,x_offset))
        for d in doors:
            screen.blit(doorimage,Add_X_Offset(d,x_offset))
        for s in crates:
            screen.blit(crateimage,Add_X_Offset(s,x_offset))
        for e in ewalls:
            screen.blit(evil_wall,Add_X_Offset(e,x_offset))
        for f in finishes:
            screen.blit(finish_image,Add_X_Offset(f,x_offset))
        for J in Jbarriers:
            screen.blit(Jbarrierimage,Add_X_Offset(J,x_offset))
        screen.blit(rebirths,(0,0))
        for p in platforms:
            screen.blit(platformerwall,Add_X_Offset(p,x_offset))
        for a in Awalls:
            screen.blit(acctualwall,Add_X_Offset(a,x_offset))
        for g in grassess:
            screen.blit(grassimage,Add_X_Offset(g,x_offset))
        for u in Jumps:
            screen.blit(jumpimage,Add_X_Offset(u,x_offset))
        for p in paths:
            screen.blit(pathimage,Add_X_Offset(p,x_offset))
        for a in Apaths:
            screen.blit(crosspathimage,Add_X_Offset(a,x_offset))
        for s in Spaths:
            screen.blit(sidepathimage,Add_X_Offset(s,x_offset))
        for u in Upaths:
            screen.blit(uppathimage,Add_X_Offset(u,x_offset))
        for f in campfires:
            screen.blit(campfireimage,Add_X_Offset(f,x_offset))
        for enemy in enemies:
            for bugatti_item_rect in bugatti_item_rects:
                screen.blit(bugatti_item_image,(Add_X_Offset(bugatti_item_rect,x_offset)))

#        for t in turnings:
#            pygame.draw.rect(screen,(0,255,0),Add_X_Offset(t,x_offset),1)
                
        current_time = current/1000
        main_font = pygame.font.SysFont("Ariel",25)
        rebirths = main_font.render("Rebirths: "+ str(spawns) +"   current time:" +str(current_time),False,(0,0,0))
        screen.blit(rebirths,(0,0))
#        screen.blit(grassimage,Add_X_Offset(x_offset,0))
        screen.blit(player_image,Add_X_Offset(location,x_offset))
#        print(vx)

        for enemy in enemies:  
            screen.blit(enemy["image"],Add_X_Offset(enemy["rect"],x_offset))
            if showborder == True:
                pygame.draw.rect(screen,(255,0,0),Add_X_Offset(enemy["rect"],x_offset),1)
        for w in walls:
            screen.blit(wall,Add_X_Offset(w,x_offset))
        screen.blit(quitImage,(1410,740))
        for enemy in enemies:
            if enemy["bugatti"] == 20:
                if enemy["speed.x"] > 0:
                    screen.blit(bugatti,(Add_X_Offset(enemy["rect"],x_offset+10)[0],enemy["rect"].y+12))
                else:
                    screen.blit(bugatti_left,(Add_X_Offset(enemy["rect"],x_offset+10)[0],enemy["rect"].y+12))
        if player_bugatti == True:
            if keys[pygame.K_d]:
                screen.blit(bugatti,(Add_X_Offset(location,x_offset+35)[0],location.y-17))
            if keys[pygame.K_a]:
                screen.blit(bugatti_left,(Add_X_Offset(location,x_offset+35)[0],location.y-17))                    
#1626,846
    if health > 4 and game_state == "alive":
        screen.blit(heart,(270,0))
    if health > 3 and game_state == "alive":
        screen.blit(heart,(285,0))
    if health > 2 and game_state == "alive":
        screen.blit(heart,(300,0))
    if health > 1 and game_state == "alive":
        screen.blit(heart,(315,0))
    if health > 0 and game_state == "alive":
        screen.blit(heart,(330,0))

    if scythecooldown > 1 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(370,0))
    if scythecooldown > 10 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(385,0))
    if scythecooldown > 20 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(400,0))
    if scythecooldown > 30 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(415,0))
    if scythecooldown > 40 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(430,0))
    if scythecooldown > 50 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(445,0))
    if scythecooldown > 60 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(460,0))
    if scythecooldown > 70 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(475,0))
    if scythecooldown > 80 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(490,0))
    if scythecooldown > 99 and game_state == "alive":
        screen.blit(sycthe_recharge_image,(505,0))
    
    if game_state == "dead":
        for i in range(20):
            screen.blit(error,randXYs[i])

    if game_state == "win":
        screen.blit(win,(1,1))
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed(1)[0]:
            game_state = "limbo"
        dt = clock.tick(30)

    main_font = pygame.font.SysFont("Ariel",25)
    for enemy in enemies:
            enemydeathpointx = enemy["rect"].x
            enemydeathpointy = enemy["rect"].y
            if enemy["health"] <= 0:
                if enemy["bugatti"] != 20:
                    enemies.remove(enemy)
                    Ecount = Ecount -1
                else:
                    A_random_number = random.randint(1,4)
                    if A_random_number == 4:
                        bugatti_item_rect = pygame.Rect(enemydeathpointx,enemydeathpointy,32,32)
                        bugatti_item_rects.append(bugatti_item_rect)
                        bugatti_item_image = pygame.image.load("bugatti_item.png")
                    enemies.remove(enemy)
                    Ecount = Ecount -1
    if location.colliderect(bugatti_item_rect):
        screen.blit(Epress,(505,700))
        if keys[pygame.K_e]:
            IWOKEUPINANEWBUGATTI = True
            if bugatti_item_rects != []:
                bugatti_item_rects.remove(bugatti_item_rect)                   

    #LEAVE THAT LAST (THE UPDATE)
    pygame.display.update()
    
        



#This will quit the program when game_over is true
pygame.quit()
