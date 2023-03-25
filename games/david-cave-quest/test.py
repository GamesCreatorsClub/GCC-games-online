import pygame, sys
pygame.init()

class Hello:
    def doSomeThing():
       screen = pygame.display.set_mode ((512, 512))
       # #size = width, hieght = 1024, 1024
       sprite = pygame.image.load("Sprite.png")
       screen.fill((255, 255, 255))
       screen.blit(sprite, (200, 200))
       pygame.display.flip()
