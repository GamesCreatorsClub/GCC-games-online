import pygame
import Classes

############MAKING THE LEVElS############
levels = []
# E = normal enemy, e = heavy enemy, O = grenade enemy, R = machine gun enemy, M = mine, W = wall, S and s = stair types,
# g = assualt rifle, G = Pump Shotgun, q = SMG, Q = M1911, p = grenade launcher, P = rocket launcher,
# t = starter AR, l = Gewehr, F = FN FAL, A = Auto Shotgun, f = Flamethrower 
# a space = the floor, # and @ = Blocker, T = inner wall, a = ammo pouch, m = medi pouch,
# U = laser upgrade, u = stock upgrade, Y = mag upgrade, I = Flashbang upgrade
#
blank_level = []

test_level = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                 WTTW                MW",
        "W                 WTTW                 W",
        "W                 WTTW                 W",
        "W                 WTTW                 W",
        "W     E           WTTW                 W",
        "W                 WTTW                 W",
        "W            WWWWWWTTWWWWWW            W",
        "W            WTTTTTTTTTTTTW            W",
        "W            WTTTTTTTTTTTTW            W",
        "W            WTTTTTTTTTTTTW            W",
        "W            WTTTTTTTTTTTTW g G q Q p PW",
        "W            WTTTTTTTTTTTTW            W",
        "W            WTTTTTTTTTTTTW            W",
        "W            WWWWWWWWWWWWWW            W",
        "W                            A  f   F  W",
        "W     M                                W",
        "W  WWWWWWWW                            W",
        "W                                      W",
        "W                         l t U u Y a mW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]

#levels.append(blank_level)
if True:
    #This level was designed by Aiken Stewart
    level_00 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W       W                            ##W",
        "W      mW                       t    ##W",
        "W       W                     W        W",
        "W  e    W                      W       W",
        "W       W                       W      W",
        "W       W         E              W     W",
        "W       W                         W    W",
        "W       W                          W   W",
        "W       W                              W",
        "W       W                              W",
        "W       W                          I   W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWW         WWWWWW   WWWWWWWWWWW",
        "s                    W                 W",
        "#  E                 W                 W",
        "#                    W                 W",
        "#                    W     e           W",
        "#          M         W                 W",
        "#                    W                 W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_00)
   
    level_01 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                   W                  W",
        "W                   W                  W",
        "W              E    W                  W",
        "W                   W                  W",
        "WWWWWWWW            W                  W",
        "s      W                               W",
        "#      W                               W",
        "#      W      WWWWWWWWWWWWWWW          W",
        "#      W                               W",
        "#      W                               W",
        "#      W                               W",
        "W              W                       W",
        "W              W                       W",
        "W              W                       W",
        "W              W           W   WWWWWWWWW",
        "W              W           W           W",
        "W          E   W           W           W",
        "W              W           W   g       S",
        "W                          W           #",
        "W                          W           #",
        "W  R                       W           #",
        "W                          W           #",
        "W                          W           #",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_01)

if True:
    level_02 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "s                                      W",
        "#      Z                               W",
        "#                       WWWWWWWW       W",
        "#                              W       W",
        "#                          E   W       S",
        "#                              W       #",
        "WWWWW    WWWWW                 W       #",
        "W                              W       #",
        "W                              W       #",
        "W                              W       #",
        "W                              W       W",
        "W                              W       W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W     WWW                              W",
        "W                                      W",
        "W           W                          W",
        "W      O    W                          W",
        "W           W                          W",
        "W a                                    W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_02)
    #This level was designed by Aiken Stewart
    level_03 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W          W                           W",
        "W          W                           S",
        "W          W E                         #",
        "W          W                           #",
        "W          WWWWW                       #",
        "s              W                       #",
        "#              W                       #",
        "#      O       W                       W",
        "#              W                       W",
        "#              WWWWW   WWWWWWWWW       W",
        "#              W               W       W",
        "W      WWWWWWWWW               W       W",
        "W      W                       W       W",
        "W      W                       W       W",
        "W      W                       W       W",
        "W      W                       W       W",
        "W                  W           W       W",
        "W                  W           W       W",
        "W                  W           W       W",
        "W      W           W           W       W",
        "W      W           W           W       W",
        "W      W   e       W E         W     m W",
        "W      W           W           W       W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_03)

    level_04 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                     Z                W",
        "W                                      W",
        "W                                      W",
        "W                         WWWWWW       W",
        "W  M                           W       S",
        "W                              W       #",
        "W                              W       #",
        "W              WWWWWWWW        W       #",
        "W                     W        W       #",
        "W                  e  W        W       #",
        "W                     W        WWWWWWWWW",
        "W                     W                W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWW                    W",
        "s                 W                    W",
        "#                 W                    W",
        "#                 M        E           W",
        "#                 M                    W",
        "#                 W                    W",
        "#                 W                    W",
        "W                 W                    W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_04)

    level_05 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      W",
        "#                                      W",
        "#                                      W",
        "#                                      W",
        "#                                      W",
        "#                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      S",
        "W                                      #",
        "W                                      #",
        "W                                      #",
        "W                                      #",
        "W                                      #",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_05)

    level_06 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_06)

    level_07 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_07)

    level_08 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_08)

    level_09 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_09)

    level_10 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_10)

    level_11 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_11)

    level_12 = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "s                                      S",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "W                                      W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        ]
    levels.append(level_12)
########DEFINING THE LOAD LEVEL FUNCTION (creates and returns a list of blocks)###########

def load_level(level):
    block_list = []
    x = y = 0
    for row in level:
        for col in row:

            ### walls ###

            if col == "W":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"wall",pygame.image.load("Environment/Walls.png"),False)
                block_list.append(tile)

            elif col == "T":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"inner wall",pygame.image.load("Environment/inner_wall.png"),False)
                block_list.append(tile)

            ### door ###

            elif col == "D":
                tile = Classes.Door(pygame.Rect(x,y,32,32),"Door",pygame.image.load("Environment/inner_wall.png"),True)
                block_list.append(tile)

            ### stairs ###

            elif col == "S":
                tile = Classes.Stairs(pygame.Rect(x,y,32,192),"up stairs",pygame.image.load("Environment/newstairsdown.png"),True,"down")
                block_list.append(tile)

            elif col == "s":
                tile = Classes.Stairs(pygame.Rect(x,y,32,192),"down stairs",pygame.image.load("Environment/newstairsup.png"),True,"up")
                block_list.append(tile)

            ### mines ###
            
            elif col == "M":
                tile = Classes.Mine(pygame.Rect(x,y,32,32),"Mine",pygame.image.load("Environment/mine.png"),True,240,2000)
                block_list.append(tile)

            x = x + 32
        y = y + 32        
        x = 0
    return block_list

######DEFINING THE GET GUNS FUNCTION (creates and returns a list of guns you can pick up)###########



def get_guns(level):
    gun_list = []
    x = y = 0
    for row in level:
        for col in row:
            if col == "g":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/M4A1.png"),0.1,25,5,0.5,25,100,"M4",1,32,0.25,"Full Auto",(32,0))
                gun_list.append(tile)
            
            elif col == "t":   
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/AK 47.png"),0.15,20,5,0.5,25,100,"AK 47",1,32,0.25,"Full Auto",(28,0))
                gun_list.append(tile)

            elif col == "G":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/Pump Shotgun.png"),1,90,20,20,2,10,"Pump Action Shotgun",7,32,0.3,"Semi Auto",(32,0))
                gun_list.append(tile)

            elif col == "A":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/Auto Shotgun.png"),0.7,90,20,20,2,10,"Auto Shotgun",7,32,0.3,"Full Auto",(28,0))
                gun_list.append(tile)

            elif col == "q":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/MP40.png"),0.001,20,20,2,50,100,"MP40",1,32,0.25,"Full Auto",(32,0))
                gun_list.append(tile)

            elif col == "Q":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/M1911.png"),0.2,20,1,1,10,20,"M1911",1,32,0.3,"Semi Auto",(24,0))
                gun_list.append(tile)
            
            elif col == "p":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/grenade launcher.png"),1,0,0,0,5,10,"Grenade Launcher",1,32,0.3,"Semi Auto",(54,0))
                gun_list.append(tile)
            
            elif col == "P":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/Rocket Launcher Loaded.png"),1,0,0,0,1,5,"Rocket Launcher",1,32,0.3,"Semi Auto",(32,0))
                gun_list.append(tile)
            
            elif col == "l":
                #pos,image,fire_rate,dmg,spread,spread_climb,max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/Gewehr 98.png"),0.75,90,0,0,5,20,"Gewehr 98",1,48,0.6,"Semi Auto",(30,0))
                gun_list.append(tile)
            
            elif col == "f":
                tile = Classes.Flamethrower((x,y),pygame.image.load("Guns Cropped/Flame Thrower.png"),0,0,20,0,100,0,"Flamethrower",0,0,0,"Full Auto",(32,0))
                gun_list.append(tile)
            
            elif col == "F":
                tile = Classes.Better_Gun((x,y),pygame.image.load("Guns Cropped/FN FAL.png"),0.3,70,3,0.25,16,48,"FN FAL",1,32,0.4,"Semi Auto",(32,0))
                gun_list.append(tile)
            x = x + 32
        y = y + 32        
        x = 0
    return gun_list
    
# E = normal enemy, e = heavy enemy, O = grenade enemy, N = machine gun enemy, Z = Patrol Enemy,
# M = mine, W = wall, S and s = stair types,
# g = assualt rifle, G = Pump Shotgun, q = SMG, Q = M1911, p = grenade launcher, P = rocket launcher,
# t = starter AR, l = Gewehr, F = FN FAL, A = Auto Shotgun, f = Flamethrower 
# a space = the floor, # and @ = Blocker, T = inner wall, a = ammo pouch, m = medi pouch,
# U = laser upgrade, u = stock upgrade, Y = mag upgrade, I = flashbang upgrade

########DEFINING THE GET PACKS FUNCTION (creates and returns a list of medi and ammo packs)##############

def get_packs(level):
    packs_list = []
    x = y = 0
    for row in level:
        for col in row:
            if col == "a":
                tile = Classes.Ammo_pouch(pygame.Rect(x,y,32,32))
                packs_list.append(tile)
                
            elif col == "m":
                tile = Classes.Medi_pouch(pygame.Rect(x,y,32,32))
                packs_list.append(tile)

            elif col == "U":
                tile = Classes.Upgrade("Laser",(x,y),pygame.image.load("Upgrades/laser.png"))
                packs_list.append(tile)

            elif col == "u":
                tile = Classes.Upgrade("Stock",(x,y),pygame.image.load("Upgrades/gun stock.png"))
                packs_list.append(tile)
            
            elif col == "Y":
                tile = Classes.Upgrade("Mag",(x,y),pygame.image.load("Upgrades/magazine.png"))
                packs_list.append(tile)

            elif col == "I":
                tile = Classes.Upgrade("Flashbang",(x,y),pygame.image.load("grenade.png"))
                packs_list.append(tile)

            x = x + 32
        y = y + 32        
        x = 0
    return packs_list
    
########DEFINING THE GET ENEMIES FUNCTION (creates and returns a list of enemies)###########

def get_enemies(level):
    enemies = []
    x = y = 0
    for row in level:
        for col in row:
            if col == "E":
                enemy = Classes.Enemy(pygame.Rect(x,y,51,51),"enemy",4,100,10,pygame.image.load("Characters Cropped/Grey Rifle.png"))
                enemies.append(enemy)

            elif col == "e":
                enemy = Classes.Heavy_Enemy(pygame.Rect(x,y,51,51),"heavy enemy",4,250,10,pygame.image.load("Characters Cropped/Red Rifle.png"))
                enemies.append(enemy)
            
            elif col == "O":
                enemy = Classes.Grenade_Enemy(pygame.Rect(x,y,64,64),"grenade enemy",4,120,10,pygame.image.load("Characters Cropped/Lime Rifle.png"))
                enemies.append(enemy)      

            elif col == "R":
                enemy = Classes.Machine_Enemy(pygame.Rect(x,y,51,51),"machine enemy",4,120,10,pygame.image.load("Characters Cropped/Dababy.png"))
                enemies.append(enemy)

            elif col == "Z":
                enemy = Classes.Patrol_Enemy(pygame.Rect(x,y,51,51),"patrol enemy",8,120,10,pygame.image.load("Characters Cropped/Rifle Player.png"),True)
                enemies.append(enemy)      
     
            x += 32
        y += 32
        x = 0
    return enemies
    
