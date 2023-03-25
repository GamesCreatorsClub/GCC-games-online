#here we import pygame and sys
import pygame, sys, random, math


GAME_STATE_WAIT_FOR_START = 0
GAME_STATE_NORMAL = 1
GAME_STATE_DIED = 2
GAME_STATE_INSTRUCTIONS = 3
GAME_STATE_HIGH_SCORE = 4
GAME_STATE_PAUSED = 5

MOVEMENT_TYPE_DOWN = 1
MOVEMENT_TYPE_SIN = 2
MOVEMENT_TYPE_FORMATION = 3

pygame.init()
clock = pygame.time.Clock()

smallFont = pygame.font.SysFont("apple casual", 32)
bigFont = pygame.font.SysFont("apple casual", 48)

#here we have the variables
screenRect = pygame.Rect(0, 0, 480, 768)
screen = pygame.display.set_mode((screenRect[2], screenRect[3]))

spaceShip = pygame.image.load("space-ship.png")
spaceShipLeft = pygame.image.load("space-ship-left.png")
spaceShipRight = pygame.image.load("space-ship-right.png")
star1 = pygame.image.load("star1.png")
star2 = pygame.image.load("star2.png")
star3 = pygame.image.load("star3.png")
star4 = pygame.image.load("star4.png")


initialSpaceShipRect = pygame.Rect(screenRect[2] / 2 - 32, screenRect[3] - 84, 64, 48)
spaceShipRect = pygame.Rect(screenRect[2] / 2 - 32, screenRect[3] - 84, 64, 48)
spaceShipSpeed = 4
spaceShipImage = spaceShip

bullet = pygame.image.load("bullet.png")
bulletSize = (16, 16)
bulletSpeed = 8
bulletOffset = 23

enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")
enemy3 = pygame.image.load("enemy1.png")
enemySize = (64, 64)
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
backgrounds = []

initialTimeToAddEnemy = 120
timeToAddEnemy = initialTimeToAddEnemy

timeToAddBackground = 0

gameState = GAME_STATE_WAIT_FOR_START

level = 1
score = 0
highScore = 0

scoreRect = pygame.Rect(screenRect[2] - 250, screenRect[3] - 30, 64, 64)
highScoreRect = pygame.Rect(20, screenRect[3] - 30, 64, 64)
levelRect = pygame.Rect(screenRect[2] / 2 - 100, screenRect[3] / 2 - 15, 64, 64)



timeInGame = 0
oneSecond = 0
timeToSpeedUp = 0
addEnemies = True

timeForLevel = 40

def moveBackground(backgrounds, screenRect):
    for i in range(len(backgrounds) - 1, -1, -1):
        backgroundObject = backgrounds[i]
        backgroundRect = backgroundObject["rect"]
        backgroundSpd = backgroundObject["speed"]
        backgroundRect[0] = backgroundRect[0] + backgroundSpd[0]
        backgroundRect[1] = backgroundRect[1] + backgroundSpd[1]
        if not backgroundRect.colliderect(screenRect):
            del backgrounds[i]

def moveBullets(bullets, screenRect):
    global spaceShipRect, gameState
    for i in range(len(bullets) - 1, -1, -1):
        bulletObject = bullets[i]
        bulletRect = bulletObject["rect"]
        bulletSpd = bulletObject["speed"]
        bulletRect[0] = bulletRect[0] + bulletSpd[0]
        bulletRect[1] = bulletRect[1] + bulletSpd[1]
        if not bulletRect.colliderect(screenRect):
            del bullets[i]
        else:
            if bulletRect.colliderect(spaceShipRect) and bulletSpd[1] > 0:
                bx = bulletRect[0] + 8
                by = bulletRect[1] + bulletRect[3] - 2
                px = spaceShipRect[0] + 31
                py = spaceShipRect[1]

                if by >= py + spaceShipRect[3] and by < py + spaceShipRect[3] + 12:
                    by = py + spaceShipRect[3] -1

                if by >= py and by <= py + spaceShipRect[3]:
                    i = (by - py) / 3
                    pxe = px + i
                    px = px - i
                    if bx >= px and bx <= pxe:
                        gameState = GAME_STATE_DIED


def moveEnemies(enemies, bullets, screenRect, spaceShipRect):
    global score, gameState
    
    for i in range(len(enemies) - 1, -1, -1):
        enemyObject = enemies[i]
        enemySpd = enemyObject["speed"]

        enemyRect = enemyObject["rect"]

        enemyMovementType = enemyObject["moveLike"]
        if enemyMovementType == MOVEMENT_TYPE_DOWN:
            enemyRect[1] = enemyRect[1] + enemySpd

        elif enemyMovementType == MOVEMENT_TYPE_SIN:
            enemySeedRect = enemyObject["seedRect"]
            sinSpeed = enemyObject["sinSpeed"]
            amplitude = enemyObject["amplitude"]
        
            #enemySeedRect[0] = enemySeedRect[0]
            enemySeedRect[1] = enemySeedRect[1] + enemySpd

            enemyRect[0] = enemySeedRect[0] + math.sin(enemySeedRect[1] / sinSpeed) * amplitude 
            enemyRect[1] = enemySeedRect[1]

        shoot = enemyObject["shoot"]
        if shoot[1] > 0:
            nextShoot = enemyObject["nextShoot"]
            nextShoot = nextShoot - 1
            if nextShoot == 0:
                enemyBulletOffset = enemyObject["bulletOffset"]
                bulletObject = {
                    "sprite": bullet,
                    "rect": pygame.Rect(enemyRect[0] + enemyBulletOffset[0], enemyRect[1] + enemyBulletOffset[1], bulletSize[0], bulletSize[1]),
                    "speed": (0, bulletSpeed)
                    }
                bullets.append(bulletObject)

            elif nextShoot < 0:
                nextShoot = random.randint(shoot[0], shoot[1])

            enemyObject["nextShoot"] = nextShoot

        enemyCollideRect = enemyObject["collideRect"]
        enemyCollideRect[0] = enemyRect[0] + enemyCollideRectSize
        enemyCollideRect[1] = enemyRect[1] + enemyCollideRectSize

        enemyDeleted = False
        if not enemyRect.colliderect(screenRect):
            del enemies[i]
            enemyDeleted = True
            negativeScore = enemyObject["negativeScore"]

            if score >= negativeScore:
                score = score - negativeScore
            
        j = 0
        while not enemyDeleted and j < len(bullets):
            bulletRect = bullets[j]["rect"]
            if bulletRect.colliderect(enemyCollideRect) and bullets[j]["speed"][1] < 0:
                del enemies[i]
                del bullets[j]
                enemyDeleted = True
                enemyScore = enemyObject["score"]

                score = score + enemyScore
            j = j + 1
        if not enemyDeleted and enemyCollideRect.colliderect(spaceShipRect):
            gameState = GAME_STATE_DIED

def movePlayer():
    global spaceShipRect, spaceShipSpeed, spaceShipImage, spaceShipLeft, spaceShipRight
    global gunHeat, bullets, firingSpeed
    
    if key[pygame.K_LEFT]:
        if spaceShipRect[0] - spaceShipSpeed > 0:
            spaceShipRect[0] = spaceShipRect[0] - spaceShipSpeed
            spaceShipImage = spaceShipLeft

    elif key[pygame.K_RIGHT]:
        if spaceShipRect[0] < screenRect[2] - spaceShipRect[2] + spaceShipSpeed:
            spaceShipRect[0] = spaceShipRect[0] + spaceShipSpeed
            spaceShipImage = spaceShipRight

    else:
        spaceShipImage = spaceShip
        
    if key[pygame.K_UP]:
        if spaceShipRect[1] - spaceShipSpeed > 0:
            spaceShipRect[1] = spaceShipRect[1] - spaceShipSpeed
    if key[pygame.K_DOWN]:
        if spaceShipRect[1] < screenRect[3] - spaceShipRect[3] + spaceShipSpeed:
            spaceShipRect[1] = spaceShipRect[1] + spaceShipSpeed
    
def checkBackground():
    global timeToAddBackground, backgrounds
    if timeToAddBackground > 0:
        timeToAddBackground = timeToAddBackground - 1
    else:
        timeToAddBackground = random.randint(0, 15)
        r = random.randint(0, 20)
        if r < 14:
            sprite = star1
        elif r < 17:
            sprite = star2
        elif r < 19:
            sprite = star4
        else:
            sprite = star3

        x = random.randint(0, screenRect.width)
        rect = pygame.Rect(x, 0, 16, 16)
        speedDistribution = random.randint(0, 10)
        if (speedDistribution < 6):
            speed = (0, 1)
        elif (speedDistribution < 9):
            speed = (0, 2)
        else:
            speed = (0, 3)
            

        background = {
            'sprite': sprite,
            'rect': rect,
            'speed': speed
            }
        backgrounds.append(background)

def checkGun():
    global gunHeat
    if gunHeat > 0:
        gunHeat = gunHeat - 1
    else:
        if key[pygame.K_SPACE]:
            if gunHeat == 0:
                bulletObject = {
                    "sprite": bullet,
                    "rect": pygame.Rect(spaceShipRect[0] + bulletOffset, spaceShipRect[1], bulletSize[0], bulletSize[1]),
                    "speed": (0, -bulletSpeed)
                    }
                bullets.append(bulletObject)
                gunHeat = firingSpeed

def checkEnemies():
    global timeToAddEnemy, enemies, timeToAddEnemy, firingSpeed, timeInGame, oneSecond, timeToSpeedUp, enemyMinSpawnTime, enemyMaxSpawnTime
    
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
            if firingSpeed < 5:
                firingSpeed = 5

    if timeToAddEnemy == 0 and addEnemies:
        timeToAddEnemy = random.randint(enemyMinSpawnTime, enemyMaxSpawnTime)
        amplitude = random.randint(0, enemyAmplitude)
        sinSpeed = random.uniform(enemySinSpeed / 2, enemySinSpeed)
        enemyX = random.randint(amplitude, screenRect[2] - enemySize[0] - amplitude)
        enemyY = 0 - enemySize[1]
        if level == 1: # enemy one only
            enemyType = 0
        elif level == 2: # enemy two down only
            enemyType = 1
        elif level == 3: # enemy two down + fast
            enemyType = random.randint(1, 2)
        elif level == 4: # enemy two shoot
            enemyType = 3
        elif level == 5: # enemy two down + fast + shoot
            enemyType = random.randint(1, 3)
        elif level == 6: # enemy one and two only
            enemyType = random.randint(0, 1)
        else: # all
            enemyType = random.randint(0, 3)
            

        if enemyType == 0:
            enemyObject = {
                    "sprite": enemy1,
                    "rect": pygame.Rect(enemyX, enemyY, enemySize[0], enemySize[1]),
                    "collideRect": pygame.Rect(enemyX + enemyCollideRectSize, enemyY + enemyCollideRectSize,\
                                               enemySize[0] - enemyCollideRectSize * 2, enemySize[1] - enemyCollideRectSize * 2),
                    "seedRect": pygame.Rect(enemyX, enemyY, enemySize[0], enemySize[1]),
                    "speed": 2,
                    "moveLike": MOVEMENT_TYPE_SIN,
                    "amplitude": amplitude,
                    "sinSpeed": sinSpeed,
                    "score": 10,
                    "negativeScore": 5,
                    "shoot": (0, 0)
                    }
        elif enemyType >= 1 and enemyType <=3:
            enemyObject = {
                    "sprite": enemy2,
                    "rect": pygame.Rect(enemyX, enemyY, enemySize[0], enemySize[1]),
                    "collideRect": pygame.Rect(enemyX + enemyCollideRectSize, enemyY + enemyCollideRectSize,\
                                               enemySize[0] - enemyCollideRectSize * 2, enemySize[1] - enemyCollideRectSize * 2),
                    "moveLike": MOVEMENT_TYPE_DOWN,
                    "shoot": (0, 0),
                    "bulletOffset": (23, 45),
                    "nextShoot": 0
                    }
            if enemyType == 1: # down only
                enemyObject["speed"] = 4
                enemyObject["score"] = 20
                enemyObject["negativeScore"] = 5
            elif enemyType == 2: # fast down
                enemyObject["speed"] = random.randint(6, 10)
                enemyObject["score"] = 20
                enemyObject["negativeScore"] = 5
            elif enemyType == 3: # shoot
                enemyObject["speed"] = 3
                enemyObject["score"] = 20
                enemyObject["negativeScore"] = 5
                enemyObject["shoot"] = (50, 80)
            

        enemies.append(enemyObject)

def checkLevelEnd():
    global timeInGame, timeForLevel, level, addEnemies

    if timeInGame > timeForLevel:
        addEnemies = False
        if len(enemies) == 0:
            addEnemies = True
            timeInGame = 0
            level = level + 1
        
    
def checkForPause():
    global gameState
    if key[pygame.K_p]:
        gameState = GAME_STATE_PAUSED

def fillBackground():
    global screenRect, backgrounds
    for i in range(0, screenRect.height):
        checkBackground()
        moveBackground(backgrounds, screenRect)
    

def resetGame():
    global score, bullet, enemies, initialTimeToAddEnemy, timeToAddEnemy, spaceShipRect, initialSpaceShipRect
    global enemyMinSpawnTime, initialEnemyMinSpawnTime, enemyMaxSpawnTime, initialEnemyMaxSpawnTime
    global firingSpeed, initialFiringSpeed, timeInGame, oneSecond, timeToSpeedUp
    global level, addEnemies

    level = 1
    score = 0
    for i in range(len(bullets) - 1, -1, -1):
        del bullets[i]
    for i in range(len(enemies) - 1, -1, -1):
        del enemies[i]
    timeToAddEnemy = initialTimeToAddEnemy
    spaceShipRect[0] = initialSpaceShipRect[0]
    spaceShipRect[1] = initialSpaceShipRect[1]


    enemyMinSpawnTime = initialEnemyMinSpawnTime - (level - 1) * 20
    enemyMaxSpawnTime = initialEnemyMaxSpawnTime - (level - 1) * 20
    if enemyMinSpawnTime < 2:
        enemyMinSpawnTime = 2
    if enemyMaxSpawnTime < 4:
        enemyMaxSpawnTime = 4

    firingSpeed = initialFiringSpeed - (level - 1) * 5
    if firingSpeed < 5:
        firingSpeed = 5

    timeInGame = 0
    oneSecond = 0
    timeToSpeedUp = 0
    addEnemies = True


def startScreen():
    global screen
    screen.fill((0, 0, 0))

def endScreen():
        pygame.display.flip()

def drawTextBig(s, x, y):
    global bigFont
    text = bigFont.render(s, 1, (255, 255, 255))
    screen.blit(text, pygame.Rect(x, y, 0, 0))

def drawTextSmall(s, x, y):
    global smallFont
    text = smallFont.render(s, 1, (255, 255, 255))
    screen.blit(text, pygame.Rect(x, y, 0, 0))


def drawBackground():
    global backgrounds, screen
    for backgroundObject in backgrounds:
        screen.blit(backgroundObject["sprite"], backgroundObject["rect"])

def drawEnemies():
    global enemies, screen
    for enemyObject in enemies:
        screen.blit(enemyObject["sprite"], enemyObject["rect"])

def drawBullets():
    global bullets, screen
    for bulletObject in bullets:
        screen.blit(bulletObject["sprite"], bulletObject["rect"])

def drawPlayer():
    global spaceShipImage, spaceShipRect, screen

    screen.blit(spaceShipImage, spaceShipRect)

def drawScore():
    global smallFont, score, screen, scoreRect, highScoreRect
    text = smallFont.render("High Score: " + str(highScore), 1, (255, 255, 255))
    screen.blit(text, highScoreRect)
    text = smallFont.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(text, scoreRect)

def drawLevel():
    global bigFont, level, screen, levelRect, highScoreRect
    text = bigFont.render("Level " + str(level), 1, (255, 255, 255))
    screen.blit(text, levelRect)

def drawInstructions():
    global screenRect

    drawTextBig("Press SPACE for start", 50, screenRect[3] / 2 - 60)
    drawTextSmall("Press I for instructions", 50, screenRect[3] / 2 - 15)
    drawTextSmall("Press W for high score", 50, screenRect[3] / 2 + 30)

def drawYouAreDead():
    global screenRect, score, highScore
    
    drawTextBig("You are dead! Score: " + str(score), 10, screenRect[3] / 2 - 75)
    drawTextSmall("Press RETURN to continue", 50, screenRect[3] / 2 - 30)

    if score > highScore:
        drawTextBig("You have high score!", 50, screenRect[3] / 2 + 15)
        drawTextBig("Well done!!!", 50, screenRect[3] / 2 + 60)
    
        


fillBackground()
resetGame()


while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    key = pygame.key.get_pressed() 
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if key[pygame.K_t]:
        print("Game state =" + str(gameState))
    if key[pygame.K_l]:
        timeInGame = timeForLevel
        if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
            level = level + 1

    if gameState == GAME_STATE_WAIT_FOR_START:
        if key[pygame.K_SPACE]:
            gameState = GAME_STATE_NORMAL
        elif key[pygame.K_i]:
            gameState = GAME_STATE_INSTRUCTIONS
        elif key[pygame.K_w]:
            gameState = GAME_STATE_HIGH_SCORE
            
        checkBackground()
        moveBackground(backgrounds, screenRect)

        startScreen()

        drawBackground()
        drawPlayer()

        drawInstructions()
        drawScore()

        endScreen()

    elif gameState == GAME_STATE_NORMAL:
        checkGun()
        checkBackground()
        checkEnemies()

        moveBackground(backgrounds, screenRect)
        moveBullets(bullets, screenRect)
        moveEnemies(enemies, bullets, screenRect, spaceShipRect)

        movePlayer()
        checkForPause()

        startScreen()

        drawBackground()
        drawEnemies()
        drawBullets()
        drawPlayer()

        if timeInGame < 4:
            drawLevel()

        checkLevelEnd()
        
        drawScore()

        endScreen()
        
    elif gameState == GAME_STATE_DIED:

        if key[pygame.K_RETURN]:
            if score > highScore:
                highScore = score

            resetGame()
            gameState = GAME_STATE_NORMAL

        else:
            checkBackground()
            moveBackground(backgrounds, screenRect)

            startScreen()

            drawBackground()
            drawEnemies()
            drawBullets()
            drawPlayer()
                
            drawScore()
            drawYouAreDead()

            endScreen()

    elif gameState == GAME_STATE_INSTRUCTIONS:
        if key[pygame.K_q]:
            gameState = GAME_STATE_WAIT_FOR_START
            
        checkBackground()
        moveBackground(backgrounds, screenRect)

        startScreen()

        drawBackground()

        endScreen()

    elif gameState == GAME_STATE_HIGH_SCORE:
        if key[pygame.K_q]:
            gameState = GAME_STATE_WAIT_FOR_START

        checkBackground()
        moveBackground(backgrounds, screenRect)

        startScreen()

        drawBackground()

        endScreen()

    elif gameState == GAME_STATE_PAUSED:
        if key[pygame.K_SPACE] or key[pygame.K_RETURN]:
            gameState = GAME_STATE_NORMAL
            
        startScreen()

        drawBackground()
        drawEnemies()
        drawBullets()
        drawPlayer()
            
        drawScore()

        endScreen()


    clock.tick(60)
    

