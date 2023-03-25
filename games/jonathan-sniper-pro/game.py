import pygame, random

pygame.init()
#pygame.font.init()

score = 0
health = 100

font = pygame.font.SysFont("Arial", 30)

screen = pygame.display.set_mode((400, 400))

cross_hair = pygame.image.load("sniper scope.png")
cross_hair_rect = cross_hair.get_rect()

enemy_sprite = pygame.image.load("enemy_32.png")
enemy_rect = enemy_sprite.get_rect()

background = pygame.image.load("Grass background 640x640_2.png")

heart_sprite = pygame.image.load("Heart.png")
heart_rect = heart_sprite.get_rect()

low_health = pygame.image.load("Low Health Indicator.png")

map_speed = 5

map_position = [0,0]
mouse_position = [0,0]

enemy_position = [0,100]
enemy_screen_position = [0,100]

enemies = []

game_running = True
low_health_2 = False

def createEnemy(enemies, map_position, screen):

    enemy = {
        "position" : [0, 100],
        "screen_position" : [0, 100],
        "rect" : enemy_sprite.get_rect()
        }
    enemy["position"][0] = map_position[0]
    enemy["position"][1] = random.randint(0, screen.get_height()) + map_position[1]
    enemies.append(enemy)

#================================================================================
#Game Code
#================================================================================

createEnemy(enemies, map_position, screen)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(enemies) -1, -1, -1):
                enemy = enemies[i]
                if enemy['rect'].collidepoint(event.pos):
                    createEnemy(enemies, map_position, screen)
                    score += 10
                    del enemies[i]
                    if score == 100:
                        createEnemy(enemies, map_position, screen)
                    if score == 200:
                        createEnemy(enemies, map_position, screen)
                    if score == 300:
                        createEnemy(enemies, map_position, screen)
        if health == 25:
            low_health_2 = True
        if health == 0:
            game_running = False
                        


    #Moving Map                
    if mouse_position[0]<= 20:
        if map_position[0] > 0:
            map_position[0] = map_position[0]-4
        
        
    if mouse_position[0]>= (400-84):
        if map_position[0] < 400:
            map_position[0] = map_position[0]+4
        

    if mouse_position[1]<= 20:
        if map_position[1] > 0:
            map_position[1] = map_position[1]-4
        

    if mouse_position[1]>= (400-84):
        if map_position[1] < 400:
            map_position[1] = map_position[1]+4
        
           
    screen.blit(background, (-map_position[0]/map_speed,-map_position[1]/map_speed))
    screen.blit(background, (-map_position[0]/map_speed + 512,-map_position[1]/map_speed))
    screen.blit(background, (-map_position[0]/map_speed,-map_position[1]/map_speed + 512))
    screen.blit(background, (-map_position[0]/map_speed + 512,-map_position[1]/map_speed + 512))

    #Moving Enemy
    #enemy_position[0] += 1
    #if enemy_position[0] > 800:
    #    enemy_position[0] = 0
    #    score -= 5
    #    enemy_position[1] = random.randint(0, screen.get_height())
    #    
    #enemy_screen_position[0] = enemy_position[0] - map_position[0]
    #enemy_screen_position[1] = enemy_position[1] - map_position[1]
    #enemy_rect.center = enemy_screen_position
    #screen.blit(enemy, enemy_rect)

    for i in range(len(enemies) -1, -1, -1):
        enemy = enemies[i]
        enemy["position"][0] += 1
        if enemy["position"][0] > 800:
            createEnemy(enemies, map_position, screen)
            del enemies[i]
            #enemy["position"][0] = 0
            #enemy["enemy_position"][1] = random.randint(0, screen.get_height())
            health -= 5
            
        enemy["screen_position"][0] = enemy["position"][0] - map_position[0]
        enemy["screen_position"][1] = enemy["position"][1] - map_position[1]
        enemy["rect"].center = enemy["screen_position"]
        screen.blit(enemy_sprite, enemy["rect"])


    cross_hair_rect.center = mouse_position
    screen.blit(cross_hair, cross_hair_rect)

    font_surface = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(font_surface, (10, 10))
    font_surface = font.render("Health: " + str(health), 1, (255, 255, 255))
    screen.blit(font_surface, (250, 10))
    if low_health_2 == True:
        screen.blit(low_health,(0, 0))

    heart_rect[0] = 240
    for i in range(0, int(health / 10)):
        heart_rect = heart_rect.move(10, 0)
        screen.blit(heart_sprite, heart_rect)
    
    pygame.display.flip()

#pygame.quit()
    

