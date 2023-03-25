import pygame, random

pygame.init()
#pygame.font.init()
total = 0
hoopsh = 0
hoopsc = 0
score = 0
score2 = 0

font = pygame.font.SysFont("Arial", 30)

width = 400
height = 400

screen = pygame.display.set_mode((width, height))

boy = pygame.image.load("player_down_0.png")
boy_rect = boy.get_rect()

hedgehog = pygame.image.load("ball_down0.png")
hedgehog_rect = hedgehog.get_rect()

background = pygame.image.load("flippyboard.png")
hoop_image = pygame.image.load("hoop.png")

mouse_position = [0,0]
hedgehog_position = [200,200]
hedgehog_direction = [1,0]

dims = (17, 17)

hoop_positions = [pygame.Rect((167, 56), dims), pygame.Rect((78, 127), dims), pygame.Rect((55, 55), dims), pygame.Rect((350, 270), dims)]

game_running = True

while game_running:
    pygame.time.Clock().tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:

            if hedgehog_rect.collidepoint(event.pos):
                hedgehog_direction[0] = hedgehog_position[0] - event.pos[0]
                hedgehog_direction[1] = hedgehog_position[1] - event.pos[1]
                score2 = score2 +1
                #print(score2)
            
                if hedgehog_direction[0] > 1:
                    hedgehog_direction[0] = 1
                if hedgehog_direction[0] < -1:
                    hedgehog_direction[0] = -1
                if hedgehog_direction[1] > 1:
                    hedgehog_direction[1] = 1
                if hedgehog_direction[1] < -1:
                    hedgehog_direction[1] = -1

    screen.blit(background, (0,0))

    boy_rect.center = mouse_position
    screen.blit(boy, boy_rect)

    hedgehog_position[0] += hedgehog_direction[0]
    if hedgehog_rect.left < 0 or hedgehog_rect.right > width:
        # Yes - touching sides of screen so reverse X
        # velocity value
        hedgehog_direction[0] = -hedgehog_direction[0]
    if hedgehog_rect.top < 0 or hedgehog_rect.bottom > height:
        # Yes - touching top/bottom of screen so
        # reverse the Y velocity value
        hedgehog_direction[1] = -hedgehog_direction[1]
 
    hedgehog_position[1] += hedgehog_direction[1]
    if hedgehog_position[0] > screen.get_width() or hedgehog_position[0] < 0:
        hedgehog_position[0] = 0
        score -= 5
        hedgehog_position[1] = random.randint(0, screen.get_height())
        hedgehog_direction = [1,0]
        
    if hedgehog_position[1] > screen.get_height() or hedgehog_position[1] < 0:
        hedgehog_position[0] = 0
        score -= 5
        hedgehog_position[1] = random.randint(0, screen.get_height())

    hedgehog_direction[0] = hedgehog_direction[0] * 0.99
    hedgehog_direction[1] = hedgehog_direction[1] * 0.99
        
    hedgehog_rect.center = hedgehog_position
    screen.blit(hedgehog, hedgehog_rect)
        
    for hoop in hoop_positions:
        screen.blit(hoop_image, hoop)

    for hoop in hoop_positions:
        if hedgehog_rect.colliderect(hoop):
            score = score + 10 - score2
            hoop_positions.remove(hoop)

    #if pygame.MOUSEBUTTONDOWN == True:
        #score2 = score2 +1
        #print(score2)
        
       
    font_surface = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(font_surface, (10, 10))
        
    pygame.display.flip()

#pygame.quit()
    
