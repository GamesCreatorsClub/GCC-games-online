import pygame, sys
pygame.init()

screen = pygame.display.set_mode ((512, 512))
size = width, hieght = 1024, 1024
sprite = pygame.image.load("Sprite.png")

while True:

   for event in  pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    
       screen.fill((255, 255, 255))
       screen.blit(sprite, (200, 200))
       pygame.display.flip()

    
