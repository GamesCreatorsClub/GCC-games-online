import pygame, random, time, sys, math

pygame.init()

frameclock = pygame.time.Clock()

width = 1024
height = 700

screensize = (width, height)

screen = pygame.display.set_mode(screensize)

tankImage = pygame.image.load('tank.png')
selectedImage = pygame.image.load('selected.png')

units = []

MOUSEDOWN = False

def createUnit(unit):
    global units, key, tankImage, mouse_position

    rect = tankImage.get_rect().move((mouse_position[0], mouse_position[1]))

    ok = True
    i = 0
    while ok and i < len(units):
        u = units[i]
        if u['rect'].colliderect(rect):
            ok = False
        i = i + 1

    if ok and unit == 'tank':
        tank = {
            'unitName': 'tank',
            'image': tankImage,
            'rect': rect,
            'selected': False,
            'destRect': tankImage.get_rect().move((mouse_position[0], mouse_position[1])),
            
            }
        units.append(tank)

def controlUnits():
    global units, MOUSEDOWN, mouse_position, key

    selectedUnit = False
    
    for unit in units:
        if MOUSEDOWN:
            if unit['rect'].collidepoint(mouse_position):
                unit['selected'] = not unit['selected']
#                print(unit['selected'])
                time.sleep(0.05)
#                unit['selected'] = True
                selectedUnit = True
#            else:
#                print("not selected (" + str(mouse_position[0]) + "," + str(mouse_position[1]) + ") vs (" \
#                      + str(unit['rect'][0]) + "," + str(unit['rect'][1]) \
#                      + str(unit['rect'][2]) + "," + str(unit['rect'][3]) + ")")
#        if unit['selected']:
#            if key[pygame.K_SPACE]:
#                unit['destRect'][0] = mouse_position[0]          
#                unit['destRect'][1] = mouse_position[1]
#                unit['selected'] = not unit['selected']
                

        rect = pygame.Rect(unit['rect'][0], unit['rect'][1], unit['rect'][2], unit['rect'][3])
#        rect = unit['rect'].copy()
        destRect = unit['destRect']
        
        if destRect[0] > rect[0]:
            rect[0] += 1
        elif destRect[0] < rect[0]:
            rect[0] -= 1
        else:
            rect[0] = destRect[0]

        if destRect[1] > rect[1]:
            rect[1] += 1
        elif destRect[1] < rect[1]:
            rect[1] -= 1
        else:
            rect[1] = destRect[1]

        ok = True
        i = 0
        while ok and i < len(units):
            u = units[i]
            if u != unit and u['rect'].colliderect(rect):
                ok = False
            i = i + 1

        if ok:
            unit['rect'][0] = rect[0]
            unit['rect'][1] = rect[1]

    if MOUSEDOWN and not selectedUnit:
        for unit in units:
            if unit['selected']:
                unit['selected'] = False
                unit['destRect'][0] = mouse_position[0]          
                unit['destRect'][1] = mouse_position[1]

def drawUnits():
    for unit in units:
        screen.blit(unit['image'], unit['rect'])
        if unit['selected']:
            screen.blit(selectedImage, unit['rect'])


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

    if key[pygame.K_a]:
        createUnit('tank')

    controlUnits()


    screen.fill((100, 0, 0))
    drawUnits()

    pygame.display.flip()
    frameclock.tick(30)
