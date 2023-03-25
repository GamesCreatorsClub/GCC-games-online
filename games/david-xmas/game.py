import pygame, random, time, sys, math

pygame.init()


frameclock = pygame.time.Clock()

width = 1024
height = 600

screensize = (width, height)

screen = pygame.display.set_mode(screensize)

score = 0

angle = 0

present_image = pygame.image.load("presents.png")
present_stndrd_rect = present_image.get_rect()
presents = []

flake_image = pygame.image.load("snowflakesmall.png")
flake_stndrd_rect = flake_image.get_rect()
flakes = []

santa = {
    'santaRight' : pygame.image.load("santaSleigh_right.png"),
    'santaLeft' : pygame.image.load("santaSleigh_left.png"),
    'rect': pygame.Rect(0, height - 32, 64, 32),
    'speedR': 0,
    'speedL': 0,
    'direction': 1
    }
def DrawText(text, position):
   global screen, font
   font = pygame.font.SysFont("apple casual" , 50)
   text = font.render(text, 1,(0, 0, 0))
   screen.blit(text, position)


def dropFlakes():
    global flakes, flake_stndrd_rect, santa, score


    # create new flake if needed
    if random.randint(1, 40) <= 2:
        flake_stndrd_rect[0] = random.randint(0, 1024)
        flakes.append(flake_stndrd_rect.copy())
        #print('+1 flake')

    for i in range(len(flakes) -1, -1, -1):
        flake_rect = flakes[i]
        flake_rect[1] += 1
        if random.randint(1, 40) <= 2:
            flake_rect[0] += random.randint(1, 3) - 1
        if flake_rect[1] > height:
            del flakes[i]


def dropPresents():
    global presents, present_stndrd_rect, santa, score


    # create new present if needed
    if random.randint(1, 100) <= 2:
        present_stndrd_rect[0] = random.randint(0, height)
        presents.append(present_stndrd_rect.copy())
        #print('+1 present')


#    for present_rect in presents:
    for i in range(len(presents) -1, -1, -1):
        present_rect = presents[i]
        present_rect[1] += 3
        if presents[i].colliderect(santa['rect']):
            del presents[i]
            score += 1
        if present_rect[1] > height:
            del presents[i]
#                presents.remove(present_rect)
#                print('-1 present')

def drawPresents(angle):
    global presents, present_image
    
    for present_rect in presents:
        
        rotatedPresent = pygame.transform.rotate(present_image, angle)
        screen.blit(rotatedPresent, present_rect)

def drawFlakes(angle):
    global flakes, flake_image
    
    for flake_rect in flakes:
        
        rotatedPresent = pygame.transform.rotate(flake_image, angle)
        screen.blit(rotatedPresent, flake_rect)

def moveSanta():
    global key, santa

    santa['rect'][0] += santa['speedR']
    santa['rect'][0] -= santa['speedL']

    if key[pygame.K_RIGHT]:
        santa['direction'] = 1
        if santa['speedR'] < 10:
            santa['speedR'] += 1
    else:
        if santa['speedR'] > 0:
            santa['speedR'] -= 1

    if key[pygame.K_LEFT]:
        santa['direction'] = 0
        if santa['speedL'] < 10:
            santa['speedL'] += 1
    else:
        if santa['speedL'] > 0:
            santa['speedL'] -= 1

def drawSanta():
    global santa
    if  santa['direction'] == 1:
        screen.blit(santa['santaRight'], santa['rect'])
    if  santa['direction'] == 0:
        screen.blit(santa['santaLeft'], santa['rect'])


while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
           MOUSEDOWN = True
        else:
           MOUSEDOWN = False


    dropPresents()
    dropFlakes()
    moveSanta()

    screen.fill((255,255,255))
    DrawText(str(score), (0,0))
    angle = angle + 1
    drawPresents(angle)
    drawSanta()
    drawFlakes(angle)
    #print(presents)
    pygame.display.flip()
    frameclock.tick(30)

