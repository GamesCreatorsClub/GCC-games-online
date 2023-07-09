speed = 5
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

giantblob = pygame.image.load("giantblob.png")
clock = pygame.time.Clock()
wall = pygame.image.load('wall_revamped_resoluted.png')
#player = pygame.image.load('man-1.png')
normal_player = pygame.image.load('wall_revamped_resoluted.png')
doorimage = pygame.image.load('door_revamped_resoluted.png')
munniimage = pygame.image.load('gamemunni.png')
rich_player = pygame.image.load('money!.png')
crateimage = pygame.image.load('crate_resoluted.png')
evil_wall = pygame.image.load('evilwall_resoluted.png')
error = pygame.image.load('you_got_mail.png')
finish_image = pygame.image.load('finishsimpl.png')
player_left = pygame.image.load("whitedot.png")
player_right = pygame.image.load("whitedot.png")
player = pygame.image.load("whitedot.png")
player_sythe_right = pygame.image.load("blackdot.png")
player_sythe_left = pygame.image.load("blackdot.png")
m_sythe_left = pygame.image.load("blackdot.png")
m_sythe_right = pygame.image.load("money_sythe_right.png")
chest_rightimage = pygame.image.load("closed_chest.png")
painting_image = pygame.image.load("painting.png")
blood_sythe_left = pygame.image.load("b_sythe_left.png")
blood_sythe_right = pygame.image.load("b_sythe_right.png")
error = pygame.image.load("you_got_mail_enlargened.png")
ded = pygame.image.load("youdieddedscreen.png")
win = pygame.image.load("the_you_win_screen.png")

health = 100
spawns = 1

location = (82,0)


x = y = 0
level = ["#C#####################",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "#                     #",
         "################T######"]

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
        if row == "D":
            door = pygame.Rect(x,y,72,72)
            doors.append(door)
        if row == "M":
            munni = pygame.Rect(x +10,y +15,32,32)
            munniz.append(munni)
        if row == "S":
            crate = pygame.Rect(x,y,72,72)
            crates.append(crate)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)
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
        if row == "#":
            rect1 = pygame.Rect(x,y,72,72)
            walls.append(rect1)
            turning = pygame.Rect(x,y,72,72)
            turnings.append(turning)

        x = x + 72
    y = y +72
    x = 0


game_over = False


#12 x 23 (72)

while not game_over: 
    #This checks if the cross in the top right has been pressed (do not remove)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    #This will fill the window with a solid RGB colour

    if game_state == "alive":
        myfont = pygame.font.SysFont("ariel",32)
        mytext = myfont.render("money: " + str(money) + "     spawns:  " + str(spawns) + "     scythe:  " + str(sythe),1,(0,0,0))
        myfont2 = pygame.font.SysFont("ariel",25)
        mytextbottom = myfont2.render("collecting money may help in upgrading the scythe",1,(230,230,230))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            location.y+=speed
            for w in walls:
                 if location.colliderect(w):
                     location.midbottom=(location.midbottom[0],w.midtop[1])
                     
        if keys[pygame.K_w]:
            location.y-=speed
            for w in walls:
                if location.colliderect(w):
                    location.midtop=(location.midtop[0],w.midbottom[1])
                    if keys[pygame.K_e]:
                        player = player_sythe_right

                    
        if keys[pygame.K_d]:
            location.x+=speed
            for w in walls:
                if location.colliderect(w):
                    location.midright=(w.midleft[0],location.midright[1])

        if keys[pygame.K_a]:
            location.x-=speed
            for w in walls:
                if location.colliderect(w):
                    location.midleft=(w.midright[0],location.midleft[1])
        if keys[pygame.K_o]:
            player = giantblob

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
            location.y = 0
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
                        location.y = 0
                        
                        
                else:
                    spawns = spawns -1
                    location.x = 72
                    location.y = 0
                
        
        for enemy in enemies:
            enemy['rect'].x = enemy['rect'].x + enemy['speed']
            for turning in turnings:
                if turning.colliderect(enemy["rect"]):
                    enemy["speed"] *= -1
                    enemy['rect'].x = enemy['rect'].x + enemy['speed']

            


        if spawns <= -1:
            game_state = "dead"

        



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



        for enemy in enemies:  
            screen.blit(enemy["image"],enemy["rect"])

        screen.blit(mytext,(200,0))
#1626,846
        screen.blit(mytextbottom,(523,811))
    if game_state == "dead":
        for i in range(20):
            screen.blit(error,randXYs[i])

    if game_state == "win":
        screen.blit(win,(1,1))


    #LEAVE THAT LAST (THE UPDATE)
    pygame.display.update()
    
        



#This will quit the program when game_over is true
pygame.quit()

