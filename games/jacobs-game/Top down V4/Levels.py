import pygame
import Classes

############MAKING THE LEVElS############
levels = []
# E = normal enemy, e = heavy enemy, O = grenade enemy, N = machine gun enemy, M = mine, W = wall, S and s = stair types,
# g = assualt rifle, G = shotgun, q = SMG, Q = pistol, p = grenade launcher, P = RPG rocket launcher, t = starter AR, l = sniper
# a space = the floor, # and @ = Blocker, T = inner wall, a = ammo pouch, m = medi pouch,
# U = laser upgrade, u = stock upgrade, Y = mag upgrade
#
blank_level = []

test_level = [
        "###################@@###################",
        "#                 WTTW                M#",
        "#                 WTTW                 #",
        "#                 WTTW                 #",
        "#                 WTTW                 #",
        "#                 WTTW                 #",
        "#                 WTTW                 #",
        "#            WWWWWWTTWWWWWW            #",
        "#       N    WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW g G q Q p P#",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                         l t U u Y a m#",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#DDD                                   #",
        "###################@@###################",
        ]

#levels.append(blank_level)
if True:
    level_00 = [
        "###################@@###################",
        "#            sssssWTTW                 #",
        "#            sssssWTTW                 #",
        "#            sssssWTTW                 #",
        "#            sssssWTTW                 #",
        "#            sssssWTTW                 #",
        "#            sssssWTTW                 #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#       q    WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                           W          #",
        "#                  E        W          #",
        "#                            W         #",
        "#                            W         #",
        "#                                      #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_00)

    level_01 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#     u      sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#        E   WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#      M            WWWWWWWWWW         #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#                      E               #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_01)

    level_02 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#     O      sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#  a         sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#   WWW  WW  WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#     E   M                            #",
        "#                          W           #",
        "#                  E        W          #",
        "#                            W         #",
        "#                      Q      W        #",
        "#                              W       #",
        "#     m                                #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_02)

    level_03 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#         E  sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW         M  #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#     E      WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                                      #",
        "#                       W              #",
        "#                        WW            #",
        "#                          WW          #",
        "#                            WW        #",
        "#                              W       #",
        "#                          E           #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_03)

    level_04 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#      U     sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#      M     sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW     WWW M  #",
        "#            WTTTTTTTTTTTTW  WWW       #",
        "#     E      WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW      E     #",
        "#            WWWWWWWWWWWWWW            #",
        "#                          WW          #",
        "#                                      #",
        "#      e                               #",
        "#                                      #",
        "#                                      #",
        "#                                      #",
        "#     g  M                             #",
        "#                          E           #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_04)

    level_05 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#       E    sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#    M       WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#   E        WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW          M #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWWWWW         #",
        "#                                      #",
        "#    E                                 #",
        "#               WW                     #",
        "#             WW                       #",
        "#           WW           E             #",
        "#         WW                           #",
        "#      WWWM       O                    #",
        "#                                      #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_05)

    level_06 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "# a          sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS      M     #",
        "#      m     sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS      Y     #",
        "#       E    WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW   WWWWWW   #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#    E       WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                               E      #",
        "#                       G              #",
        "#                                      #",
        "#                                      #",
        "#       M                              #",
        "#                                      #",
        "#         e                            #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_06)

    level_07 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW  M M M M   #",
        "#                    E                 #",
        "#                                      #",
        "#                  E                   #",
        "#                                      #",
        "#                WWWWWWWWWW            #",
        "#                    e                 #",
        "#                                      #",
        "#E               WWWWWWWWWW            #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_07)

    level_08 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#   O        sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#       p    WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#       W                         WWWWW#",
        "#       W                    WWWWW     #",
        "#       W                              #",
        "#   E   W                 M         E  #",
        "#        W       E                     #",
        "#        W                             #",
        "#        W                             #",
        "#        W                             #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_08)

    level_09 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#         m  sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#  E         sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#        O   WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#    E                                 #",
        "#               WW             M       #",
        "#                 WW                   #",
        "#                   WW                 #",
        "#                e    WW               #",
        "#                       WW             #",
        "#     a                                #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_09)

    level_10 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#            sssssWTTWSSSSS            #",
        "#    O       WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#       P    WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "@            WTTTTTTTTTTTTW      M     @",
        "#            WTTTTTTTTTTTTW            #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#       M              e               #",
        "#                                      #",
        "#          WWWWW                       #",
        "#     WWWWW                    M       #",
        "#                                      #",
        "#     E                                #",
        "#                                      #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_10)

    level_11 = [
        "###################@@###################",
        "#            sssssWTTWSSSSS            #",
        "#           DsssssWTTWSSSSS            #",
        "#           DsssssWTTWSSSSS      M     #",
        "#           DsssssWTTWSSSSS            #",
        "#           DsssssWTTWSSSSS            #",
        "#      N     sssssWTTWSSSSS            #",
        "#            WWWWWWTTWWWWWW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW            #",
        "#            WTTTTTTTTTTTTW      WWWW  #",
        "#      M     WTTTTTTTTTTTTW  WWWW      #",
        "@            WTTTTTTTTTTTTW            @",
        "#            WTTTTTTTTTTTTW  M         #",
        "#            WWWWWWWWWWWWWW            #",
        "#                                      #",
        "#                                      #",
        "#          E      W                    #",
        "#                 W                    #",
        "#                 W                    #",
        "#                  W             O     #",
        "#      e           W                   #",
        "#                                      #",
        "#                                      #",
        "###################@@###################",
        ]
    levels.append(level_11)

########DEFINING THE LOAD LEVEL FUNCTION (creates and returns a list of blocks)###########

def load_level(level):
    block_list = []
    x = y = 0
    for row in level:
        for col in row:

            ### walls ###

            if col == "W":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"wall",pygame.image.load("wall.png"),False)
                block_list.append(tile)

            elif col == "T":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"inner wall",pygame.image.load("inner_wall.png"),False)
                block_list.append(tile)

            ### door ###

            elif col == "D":
                tile = Classes.Door(pygame.Rect(x,y,32,32),"Door",pygame.image.load("inner_wall.png"),True)
                block_list.append(tile)

            ### stairs ###

            elif col == "S":
                tile = Classes.Stairs(pygame.Rect(x,y,32,32),"up stairs",pygame.image.load("stairs.png"),True,"down")
                block_list.append(tile)

            elif col == "s":
                tile = Classes.Stairs(pygame.Rect(x,y,32,32),"down stairs",pygame.image.load("stairs.png"),True,"up")
                block_list.append(tile)

            ### mines ###
            
            elif col == "M":
                tile = Classes.Mine(pygame.Rect(x,y,32,32),"Mine",pygame.image.load("mine.png"),True,240,2000)
                block_list.append(tile)

            ### floor underneath ammo and medi pouches ###
            
            elif col == "a":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "m":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            ### floor underneath guns ###
            
            elif col == "g":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "G":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "q":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "Q":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "p":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "P":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            elif col == "t" or col == "l":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
            
            ### floor under upgrades ###

            elif col == "U":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
            
            elif col == "u":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
            
            elif col == "Y":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
            
            ### the floor and floor under enemies ###
            
            elif col == " " or col == "E" or col == "e" or col == "O" or col =="N":
                tile = Classes.Obstacle(pygame.Rect(x,y,32,32),"floor",pygame.image.load("floor.png"),True)
                block_list.append(tile)
                
            x = x + 32
        y = y + 32        
        x = 0
    return block_list

######DEFINING THE GET GUNS FUNCTION (creates and returns a list of guns you can pick up)###########

def get_guns(level,inventory):
    gun_list = []
    x = y = 0
    for row in level:
        for col in row:
            if col == "g":
                tile = Classes.Better_Gun((x,y),pygame.image.load("assault rifle.png"),0.1,25,5,0.5,25,100,"AR",1,32,0.25)
                gun_list.append(tile)

            elif col == "G":
                tile = Classes.Better_Gun((x,y),pygame.image.load("shotgun.png"),1,90,20,20,2,10,"Shotgun",7,32,0.3)
                gun_list.append(tile)

            elif col == "q":
                tile = Classes.Better_Gun((x,y),pygame.image.load("SMG.png"),0.0001,20,20,2,50,100,"SMG",1,32,0.25)
                gun_list.append(tile)

            elif col == "Q":
                tile = Classes.Better_Gun((x,y),pygame.image.load("pistol.png"),0.5,50,1,1,10,20,"Pistol",1,32,0.3)
                gun_list.append(tile)
            
            elif col == "p":
                tile = Classes.Better_Gun((x,y),pygame.image.load("grenade launcher.png"),1,0,0,0,5,10,"Grenade Launcher",1,32,0.3)
                gun_list.append(tile)
            
            elif col == "P":
                tile = Classes.Better_Gun((x,y),pygame.image.load("rpg loaded.png"),1,0,0,0,1,5,"Rocket Launcher",1,32,0.3)
                gun_list.append(tile)

            elif col == "t":   
                tile = Classes.Better_Gun((x,y),pygame.image.load("gun.png"),0.2,20,5,0.5,25,100,"Starter AR",1,32,0.25)
                gun_list.append(tile)
            
            elif col == "l":
                #pos,image,fire_rate,dmg,spread,spread_climb,max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil
                tile = Classes.Better_Gun((x,y),pygame.image.load("sniper.png"),0.75,250,0,0,5,20,"Sniper",1,48,0.6)
                gun_list.append(tile)
            x = x + 32
        y = y + 32        
        x = 0
    return gun_list
    
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
                tile = Classes.Upgrade("Laser",(x,y),pygame.image.load("laser.png"))
                packs_list.append(tile)

            elif col == "u":
                tile = Classes.Upgrade("Stock",(x,y),pygame.image.load("gun stock.png"))
                packs_list.append(tile)
            
            elif col == "Y":
                tile = Classes.Upgrade("Mag",(x,y),pygame.image.load("magazine.png"))
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
                enemy = Classes.Enemy(pygame.Rect(x,y,64,64),"enemy",4,100,10,pygame.image.load("enemy.png"))
                enemies.append(enemy)

            elif col == "e":
                enemy = Classes.Heavy_Enemy(pygame.Rect(x,y,64,64),"heavy enemy",4,250,10,pygame.image.load("heavy enemy.png"))
                enemies.append(enemy)
            
            elif col == "O":
                enemy = Classes.Grenade_Enemy(pygame.Rect(x,y,64,64),"grenade enemy",4,120,10,pygame.image.load("grenade enemy.png"))
                enemies.append(enemy)      

            elif col == "N":
                enemy = Classes.Machine_Enemy(pygame.Rect(x,y,64,64),"machine enemy",4,120,10,pygame.image.load("machine enemy.png"))
                enemies.append(enemy)      
     
            x += 32
        y += 32
        x = 0
    return enemies
    
