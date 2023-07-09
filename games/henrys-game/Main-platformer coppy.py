speed = 3
game_state = "alive"
sythe = "standard scythe"
import pygame
import time
import sys
import random
money = 0
kills = 0
randX = random.randint(0,1626)
randY = random.randint(0,846)

pygame.init()
#This is where we set up the window that displays our game. The resolution is set here
screen = pygame.display.set_mode((1626,846))
#This sets the windows caption
pygame.display.set_caption("Maze Game")


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
evil_wall = pygame.image.load('evilwall_resoluted.png')
error = pygame.image.load('you_got_mail.png')
finish_image = pygame.image.load('finishsimpl.png')
player_left = pygame.image.load("character_left.png")
player_right = pygame.image.load("character_right.png")
player = pygame.image.load("character_left.png")
player_sythe_right = pygame.image.load("character_sythe_right.png")
player_sythe_left = pygame.image.load("character_sythe_left.png")
m_sythe_left = pygame.image.load("money_sythe_left.png")
m_sythe_right = pygame.image.load("money_sythe_right.png")
chest_rightimage = pygame.image.load("closed_chest.png")
painting_image = pygame.image.load("painting.png")
blood_sythe_left = pygame.image.load("b_sythe_left.png")
blood_sythe_right = pygame.image.load("b_sythe_right.png")
error = pygame.image.load("you_got_mail_enlargened.png")
ded = pygame.image.load("youdieddedscreen.png")
win = pygame.image.load("the_you_win_screen.png")
Jbarrierimage = pygame.image.load("wall_revamped_resoluted.png")
Sbarrierimage = pygame.image.load("wol.png")
grassimage = pygame.image.load("grazz.png")
jumpimage = pygame.image.load("sprheng.png")

health = 100
spawns = 1

location = (100,0)


x = y = 0
level = ["J                     #",
         "#                     #",
         "#                     DF",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                    K#",
         "#                    K#",
         "#C                   K#",
         "#                     #",
         "GGGGGGGGGGGGGGGGGGGGGGG"]


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
        if row == "M":
            munni = pygame.Rect(x +10,y +15,32,32)
            munniz.append(munni)
        if row == "S":
            Sbarrier = pygame.Rect(x,y,72,5)
            Sbarriers.append(Sbarrier)
        if row == "E":
            ewall = pygame.Rect(x,y,72,72)
            ewalls.append(ewall)
        if row == "F":
            finish = pygame.Rect(x,y,72,72)
            finishes.append(finish)
        if row == "K":
            enemy = {
            "health": 100,
            "rect": pygame.Rect(x,y,72,72),
            "speed": 3,
            "image": pygame.image.load('ye_eye_kite.png')
            }
            enemies.append(enemy)
        if row == "P":
            rect1 = pygame.Rect(x,y,72,72)
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
        if row == "P":
            platform = pygame.Rect(x,y,72,72)
            platforms.append(platform)
        if row == "J":
            Jbarrier = pygame.Rect(x,y,72,72)
            Jbarriers.append(Jbarrier)
        if row == "U":
            Jump = pygame.Rect(x,y,72,72)
            Jumps.append(Jump)

        x = x + 72
    y = y +72
    x = 0

vx = 0.2
vy = 0
clock = pygame.time.Clock()

location.x = 82
location.y = 760
game_over = False
canjump = False
    

#12 x 23 (72)

while not game_over:
    #This checks if the cross in the top right has been pressed (do not remove)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #This will fill the window with a solid RGB colour
            

    if game_state == "alive":
        dt = clock.tick(30)
    if game_state == "alive":
        myfont = pygame.font.SysFont("ariel",32)
        mytext = myfont.render("money: " + str(money) + "     spawns:  " + str(spawns) + "     scythe:  " + str(sythe),1,(0,0,0))
        myfont2 = pygame.font.SysFont("ariel",25)
        mytextbottom = myfont2.render("collecting money may help in upgrading the scythe",1,(0,0,0))

        keys = pygame.key.get_pressed()

        for s in Sbarriers:
            if location.colliderect(s):
                location.y = location.y +1
                

                    
        if keys[pygame.K_a]:
            location.x = location.x - vx*dt
            for w in walls:
                if location.colliderect(w):
                    location.midleft=(w.midright[0],location.midleft[1])



                    
        if keys[pygame.K_d]:
            location.x = location.x + vx*dt
            for w in walls:
                if location.colliderect(w):
                    location.midright=(w.midleft[0],location.midright[1])
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


        if keys[pygame.K_SPACE] and canjump:
            vy = -0.4
        vy += 0.001 * dt
        if vy > 0.4:
            vy = 0.4

        location.y += vy * dt
        location.y+=speed
        for w in walls:
            if location.colliderect(w):
                location.midbottom=(location.midbottom[0],w.midtop[1])
                canjump = True


            
        
        if money >= 10:
            sythe = "money scythe"
        if keys[pygame.K_m]:
            money = 100

        if keys[pygame.K_t]:
            location.x = location.x +36




        if keys[pygame.K_u]:
            location.y = location.y +36

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
                spawns = spawns -1
                location.x = 72
                location.y = 0

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
                Jumps.remove(u)

                


                
                
     




        for s in crates:
            if location.colliderect(s):
                money = money +random.randint(1,4)
                print(money)
                crates.remove(s)
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
                    location.y = 754
                    
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
            

        


        screen.fill((255,255,255))
        for w in walls:
            screen.blit(wall,w)
        screen.blit(player,location)
        for m in munniz:
            screen.blit(munniimage,m)
        for d in doors:
            screen.blit(doorimage,d)
        for s in crates:
            screen.blit(crateimage,s)
        for e in ewalls:
            screen.blit(evil_wall,e)
        for f in finishes:
            screen.blit(finish_image,f)
        for J in Jbarriers:
            screen.blit(Jbarrierimage,J)
        for S in Sbarriers:
            screen.blit(Sbarrierimage,s)
        for p in platforms:
            screen.blit(platformerwall,p)
        for a in Awalls:
            screen.blit(acctualwall,a)
        for g in grassess:
            screen.blit(grassimage,g)
        for u in Jumps:
            screen.blit(jumpimage,u)


        for enemy in enemies:  
            screen.blit(enemy["image"],enemy["rect"])

#1626,846

    if game_state == "dead":
        for i in range(20):
            screen.blit(error,randXYs[i])

    if game_state == "win":
        screen.blit(win,(1,1))


    #LEAVE THAT LAST (THE UPDATE)
    pygame.display.update()
    
        



#This will quit the program when game_over is true
pygame.quit()
