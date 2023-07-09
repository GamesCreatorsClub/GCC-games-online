import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, image,name,type='tile'):
        super().__init__()
        self.image = image
        self.type = type
        self.name = name
        self.rect = pygame.Rect(0,0, size, size)
        self.rect.topleft = pos
        self.can_collide = True

    
