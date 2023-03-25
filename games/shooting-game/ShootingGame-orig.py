#here we import pygame and sys
import pygame, sys, random, math

from random import randint

pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont("apple casual", 50)

#here we have the variables
screenRect = pygame.Rect(0, 0, 480, 768)
screen = pygame.display.set_mode((screenRect[2], screenRect[3]))

spaceShip = pygame.image.load("space-ship.png")
initialSpaceShipRect = pygame.Rect(screenRect[2] / 2, screenRect[3] - 64, 64, 64)
spaceShipRect = pygame.Rect(screenRect[2] / 2, screenRect[3] - 64, 64, 64)
spaceShipSpeed = 4


bullet = pygame.image.load("bullet.png")
bulletSize = (16, 16)
bulletSpeed = 8

enemy = pygame.image.load("enemy.png")
enemySize = (64, 64)
enemySpeed = 2
enemyAmplitude = 40
enemySinSpeed = 20.0
enemyCollideRectSize = 15

initialEnemyMinSpawnTime = 30
initialEnemyMaxSpawnTime = 90
enemyMinSpawnTime = initialEnemyMinSpawnTime
enemyMaxSpawnTime = initialEnemyMaxSpawnTime

initialFiringSpeed = 30
firingSpeed = initialFiringSpeed
gunHeat = 0

bullets = []
enemies = []

initialTimeToAddEnemy = 120
timeToAddEnemy = initialTimeToAddEnemy

gameState = 0

score = 0
scoreRect = pygame.Rect(screenRect[2] - 250, screenRect[3] - 30, 64, 64)


timeInGame = 0
oneSecond = 0
timeToSpeedUp = 0

#               V
#               V
#main game loop V
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    key = pygame.key.get_pressed() 
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()


    if gameState == 0:
        if gunHeat > 0:
            gunHeat = gunHeat - 1
        if timeToAddEnemy > 0:
            timeToAddEnemy = timeToAddEnemy - 1
        if oneSecond > 0:
            oneSecond = oneSecond - 1
        else:
            oneSecond = 60
            timeInGame = timeInGame + 1
            if timeToSpeedUp > 0:
                timeToSpeedUp = timeToSpeedUp - 1
            else:
                timeToSpeedUp = 2
                if enemyMinSpawnTime > 2:
                    enemyMinSpawnTime = enemyMinSpawnTime - 1
                if enemyMaxSpawnTime > 4:
                    enemyMaxSpawnTime = enemyMaxSpawnTime - 1

                if firingSpeed > 25:
                    firingSpeed = firingSpeed - 1
        
        for i in range(bullets.__len__() - 1, -1, -1):
            bulletObject = bullets[i]
            bulletRect = bulletObject["rect"]
            bulletSpd = bulletObject["speed"]
            bulletRect[0] = bulletRect[0] + bulletSpd[0]
            bulletRect[1] = bulletRect[1] + bulletSpd[1]
            if not bulletRect.colliderect(screenRect):
                del bullets[i]

        for i in range(enemies.__len__() - 1, -1, -1):
            enemyObject = enemies[i]
            enemySpd = enemyObject["speed"]
            enemySeedRect = enemyObject["seedRect"]
            sinSpeed = enemyObject["sinSpeed"]
            amplitude = enemyObject["amplitude"]
            enemySeedRect[0] = enemySeedRect[0] + enemySpd[0]
            enemySeedRect[1] = enemySeedRect[1] + enemySpd[1]
            enemyRect = enemyObject["rect"]
            enemyRect[0] = enemySeedRect[0] + math.sin(enemySeedRect[1] / sinSpeed) * amplitude 
            enemyRect[1] = enemySeedRect[1]

            enemyCollideRect = enemyObject["collideRect"]
            enemyCollideRect[0] = enemyRect[0] + enemyCollideRectSize
            enemyCollideRect[1] = enemyRect[1] + enemyCollideRectSize

            enemyDeleted = False
            if not enemyRect.colliderect(screenRect):
                del enemies[i]
                enemyDeleted = True
                if score > 5:
                    score = score - 5
                
            j = 0
            while not enemyDeleted and j < bullets.__len__():
                bulletRect = bullets[j]["rect"]
                if bulletRect.colliderect(enemyCollideRect):
                    del enemies[i]
                    del bullets[j]
                    enemyDeleted = True
                    score = score + 10
                j = j + 1
            if not enemyDeleted and enemyCollideRect.colliderect(spaceShipRect):
                gameState = 1

        if key[pygame.K_LEFT]:
            if spaceShipRect[0] - spaceShipSpeed > 0:
                spaceShipRect[0] = spaceShipRect[0] - spaceShipSpeed
        if key[pygame.K_RIGHT]:
            if spaceShipRect[0] < screenRect[2] - spaceShipRect[2] + spaceShipSpeed:
                spaceShipRect[0] = spaceShipRect[0] + spaceShipSpeed
        if key[pygame.K_UP]:
            if spaceShipRect[1] - spaceShipSpeed > 0:
                spaceShipRect[1] = spaceShipRect[1] - spaceShipSpeed
        if key[pygame.K_DOWN]:
            if spaceShipRect[1] < screenRect[3] - spaceShipRect[3] + spaceShipSpeed:
                spaceShipRect[1] = spaceShipRect[1] + spaceShipSpeed

        if key[pygame.K_SPACE]:
            if (gunHeat == 0):
                bulletObject = {
                    "sprite"
                    :
                    bullet,
        "rect": pygame.Rect(spaceShipRect[0] + spaceShipRect[2] / 2, spaceShipRect[1], bulletSize[0], bulletSize[1]),
                    "speed": (0, -bulletSpeed
                         *
                      3)
                    }
                bullets.append(bulletObject)
                gunHeat = firingSpeed

        
        if timeToAddEnemy == 0:
            timeToAddEnemy = random.randint(enemyMinSpawnTime, enemyMaxSpawnTime)
            amplitude = random.randint(0, enemyAmplitude)
            sinSpeed = random.uniform(enemySinSpeed / 2, enemySinSpeed)
            enemyX = random.randint(amplitude, screenRect[2] - enemySize[0] - amplitude)
            enemyY = 0 - enemySize[1]
            enemyObject = {
                    "sprite": enemy,
                     "rect": pygame.Rect(enemyX, enemyY, enemySize[0], enemySize[1]),
                      "collideRect": pygame.Rect(enemyX + enemyCollideRectSize, enemyY + enemyCollideRectSize,\
                                               enemySize[0] - enemyCollideRectSize * 2, enemySize[1] - enemyCollideRectSize * 2),
                    "seedRect": pygame.Rect(enemyX, enemyY, enemySize[0], enemySize[1]),
                    "speed": (0, enemySpeed),
                    "amplitude": amplitude,
                    "sinSpeed": sinSpeed
                    }
            enemies.append(enemyObject)

        
        screen.fill((0, 0, 0))

        for enemyObject in enemies:
            screen.blit(enemyObject["sprite"], enemyObject["rect"])

        for bulletObject in bullets:
            screen.blit(bulletObject["sprite"], bulletObject["rect"])
            
        
        screen.blit(spaceShip, spaceShipRect)

        text = font.render("Score: " + str(score), 1, (255, 255, 255))
        screen.blit(text, scoreRect)
        pygame.display.flip()
        
    elif gameState == 1:
        text = font.render("You are dead! Score: " + str(score), 1, (255, 255, 255))
        youAreDeadRect = pygame.Rect((screenRect[2] - text.get_width()) / 2, screenRect[3] / 2, 64, 64)
        screen.blit(text, youAreDeadRect)
        pygame.display.flip()

        if key[pygame.K_RETURN]:
            score = 0
            for i in range(bullets.__len__() - 1, -1, -1):
                del bullets[i]
            for i in range(enemies.__len__() - 1, -1, -1):
                del enemies[i]
            timeToAddEnemy = initialTimeToAddEnemy
            gameState = 0
            spaceShipRect[0] = initialSpaceShipRect[0]
            spaceShipRect[1] = initialSpaceShipRect[1]
            enemyMinSpawnTime = initialEnemyMinSpawnTime
            enemyMaxSpawnTime = initialEnemyMaxSpawnTime
            firingSpeed = initialFiringSpeed
            timeInGame = 0
            oneSecond = 0
            timeToSpeedUp = 0


    

    clock.tick(60)
    

