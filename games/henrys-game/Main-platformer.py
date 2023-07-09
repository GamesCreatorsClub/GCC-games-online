import pygame
rp1 = pygame.image.load("character1.png")
rp2 = pygame.image.load("character2.png")
rp3 = pygame.image.load("character3.png")
rp4 = pygame.image.load("character2.png")
rebirths = 1
speed = 3
game_state = "limbo"
sythe = "standard scythe"
import time
import sys
import random
money = 0
kills = 0
m_sythe_left = pygame.image.load("money_sythe_left.png")
randX = random.randint(0,1626)
randY = random.randint(0,846)
def  Add_X_Offset(rect,offset):
    rect2 = pygame.Rect(rect.x - offset,rect.y,rect.width,rect.height)
    return rect2
images_r = [rp1,rp2,rp3,rp4]
images_l = []
def Pick_frame(images):
    current = pygame.time.get_ticks()
    anitime = current % 4000
    if anitime <= 1000:
        image = images [0]
    elif anitime <= 2000:
        image = images[1]
    elif anitime <= 3000:
        image = images[2]
    elif anitime <= 4000:
        image = images[3]
        print("hi")
    image = images[0]
    return image

    
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
m_sythe_right = pygame.image.load("money_sythe_right.png")
chest_rightimage = pygame.image.load("closed_chest.png")
character_left = pygame.image.load("character_left.png")
painting_image = pygame.image.load("painting.png")
blood_sythe_left = pygame.image.load("b_sythe_left.png")
blood_sythe_right = pygame.image.load("b_sythe_right.png")
error = pygame.image.load("you_got_mail_enlargened.png")
ded = pygame.image.load("youdieddedscreen.png")
win = pygame.image.load("the_you_win_screen.png")
Jbarrierimage = pygame.image.load("wall_revamped_resoluted.png")
Sbarrierimage = pygame.image.load("wol.png")
grassimage = pygame.image.load("grazz.png")
jumpimage = pygame.image.load("srengbloc.png")
startimage = pygame.image.load("startbutton2.png")
hoverstart = pygame.image.load("stort.png")
icemode = pygame.image.load("icemodebutton.png")
icemodehover = pygame.image.load("icemodehover2.png")

health = 100
spawns = 1

location = (100,0)


x = y = 0
level = ["J                     ",
         "#                     ",
         "#                         ",
         "#                   PP    ",
         "#                       PP",
         "#                  UP  ",
         "#               PP     RM",
         "#     RM               RRMR",
         "#     PP    # PU       PPPP",
         "#C        PP#         ",
         "#      PP   D    K      T     ",
         "GGGGGGGGGGGGGGGGGGGGGGG#    ",
         "         EEEEEEEEEEEEEEEEEEE"]

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
        if row == "S":
            Sbarrier = pygame.Rect(x,y,72,5)
            Sbarriers.append(Sbarrier)
        if row == "E":
            ewall = pygame.Rect(x,y,72,72)
            ewalls.append(ewall)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
        if row == "F":
            finish = pygame.Rect(x,y,72,72)
            finishes.append(finish)
        if row == "K":
            enemy = {
            "health": 100,
            "rect": pygame.Rect(x,y,72,72),
            "speed": 2,
            "image": pygame.image.load('ye_eye_kite.png')
            }
            enemies.append(enemy)
        if row == "P":
            rect1 = pygame.Rect(x,y,72,24)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
            platform = pygame.Rect(x,y,72,72)
            platforms.append(platform)
        if row == "#":
            rect1 = pygame.Rect(x,y,72,72)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
            Awall = pygame.Rect(x,y,72,72)
            Awalls.append(Awall)
        if row == "G":
            rect1 = pygame.Rect(x,y,72,72)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
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
            platform = pygame.Rect(x,y,72,72)
            platforms.append(platform)
        if row == "J":
            Jbarrier = pygame.Rect(x,y,72,72)
            Jbarriers.append(Jbarrier)
        if row == "U":
            Jump = pygame.Rect(x,y-48,72,72)
            Jumps.append(Jump)
        if row == "T":
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)


        x = x + 72
    y = y +72
    x = 0
x_offset = 0


vy = 0
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

    if game_state == "limbo":
        screen.fill((255,255,255))
        play_button_rect = pygame.Rect(553,293,630,300)
        quit_button_rect = pygame.Rect(1410,740,210,100)
        quit_rect = pygame.Rect(1410,10,210,100)
 #       rect.fill(quit_rect,(255,0,255))
        icemoderect = pygame.Rect(100,100,300,200)
        screen.blit(startimage,(553,293))
        screen.blit(icemode,(100,100))
        screen.blit(quitImage,(1410,10))
        if icemoderect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(icemodehover,(100,100))
            if pygame.mouse.get_pressed(1)[0]:
                GM = "ice"
                vx = 0
                location.x = 72
                location.y = 754
                game_state = "alive"
                grassimage = pygame.image.load("smoygraz.png")
        if quit_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(1)[0]:
                print("m")
        if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(hoverstart,(553,293))
            if pygame.mouse.get_pressed(1)[0]:
                GM = "standard"
                location.x = 72
                location.y = 754
                game_state = "alive"
                grassimage = pygame.image.load("grazz.png")
                vx = 0.22
    if game_state == "alive":
        if location.y >= 850:
            location.y = 750
        if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed(1)[0]:
                game_state = "limbo"
        dt = clock.tick(30)
    if game_state == "alive":
        main_font = pygame.font.SysFont("Ariel",20)
#1626,846
        #650
        #338
        rebirths = main_font.render("Rebirths: "+ str(spawns),False,(0,0,0))
#        myfont = pygame.font.SysFont("ariel",32)
#        mytext = myfont.render("money: " + str(money) + "     spawns:  " + str(spawns) + "     scythe:  " + str(sythe),1,(0,0,0))
#        myfont2 = pygame.font.SysFont("ariel",25)
#        mytextbottom = myfont2.render("collecting money may help in upgrading the scythe",1,(0,0,0))

        keys = pygame.key.get_pressed()

        for s in Sbarriers:
            if location.colliderect(s):
                location.y = location.y +1
                
        
        if GM == "standard":                    
            if keys[pygame.K_a]:
                location.x = location.x - vx*dt
                player_image = pygame.image.load("character_left.png")
                for w in walls:
                    if location.colliderect(w):
                        location.midleft=(w.midright[0],location.midleft[1])
                        
            if keys[pygame.K_d]:
                location.x = location.x + vx*dt
                player_image = pygame.image.load("character_right.png")
                for w in walls:
                    if location.colliderect(w):
                        location.midright=(w.midleft[0],location.midright[1])
            

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

        if keys[pygame.K_a]:
            player = player_left
            if keys[pygame.K_e]:
                if money < 10:
                    player = player_sythe_left
                if money >= 10:
                    player = m_sythe_left


        if (keys[pygame.K_SPACE] == True and canjump == True) or keys[pygame.K_t]:
            canjump = False
            vy = -0.55
        vy += 0.001 * dt
        if vy > 0.4:
            vy = 0.4
            



        if keys[pygame.K_q]:
            for w in walls:
                if clide == True:
                    walls.remove(w)

        location.y += vy * dt
        location.y+=speed
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
                    vy = 0
 
                


                    
                
        x_offset = location.x -220
        
        if money >= 10:
            sythe = "money scythe"
        if keys[pygame.K_m]:
            money = 100

        if keys[pygame.K_r]:
            location.x = 72
            location.y = 754
            money = 0
        
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

        for enemy in enemies:
            if location.colliderect(enemy["rect"]):
                if keys[pygame.K_e] or keys [pygame.K_a]:
                    if money >= 10:
                        enemies.remove(enemy)
#                        kills = kill +1
                    if money <= 10:
        

                        spawns = spawns -1
                        location.x = 72
                        location.y = 754
                        
                        
                else:
                    spawns = spawns -1
                    location.x = 72
                    location.y =   754
 
#        for t in turnings:
#            if colliderect location:
#                turnings.remove turning
        
        for enemy in enemies:
            enemy['rect'].x = enemy['rect'].x + enemy['speed']
            for turning in turnings:
                if turning.colliderect(enemy["rect"]):
                    enemy["speed"] *= -1
                    enemy['rect'].x = enemy['rect'].x + enemy['speed']
            


        if spawns <= -1:
            game_state = "dead"
            spawns = 1
            

        


        screen.fill((180,200,255))
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
        for S in Sbarriers:
            screen.blit(Sbarrierimage,s)
        screen.blit(rebirths,(0,0))
        for p in platforms:
            screen.blit(platformerwall,Add_X_Offset(p,x_offset))
        for a in Awalls:
            screen.blit(acctualwall,Add_X_Offset(a,x_offset))
        for g in grassess:
            screen.blit(grassimage,Add_X_Offset(g,x_offset))
        for u in Jumps:
            screen.blit(jumpimage,Add_X_Offset(u,x_offset))

        screen.blit(player_image,Add_X_Offset(location,x_offset))
#        print(vx)

        for enemy in enemies:  
            screen.blit(enemy["image"],Add_X_Offset(enemy["rect"],x_offset))
        for w in walls:
            screen.blit(wall,Add_X_Offset(w,x_offset))
        screen.blit(quitImage,(1410,740))
#1626,846

    if game_state == "dead":
        for i in range(20):
            screen.blit(error,randXYs[i])

    if game_state == "win":
        screen.blit(win,(1,1))
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed(1)[0]:
            game_state = "limbo"
        dt = clock.tick(30)

    #LEAVE THAT LAST (THE UPDATE)
    pygame.display.update()
    
        



#This will quit the program when game_over is true
pygame.quit()
