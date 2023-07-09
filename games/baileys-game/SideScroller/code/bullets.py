import pygame
import math
import time


class Bullet_mat:
    def __init__(self,**kwargs):
        self.life_time = kwargs.pop('lifetime')
        self.damage = kwargs.pop('dmg')
        self.speed = kwargs.pop('speed')
        self.props = kwargs
        #physics, explodes, bouncy, hitscan

class Bullet(pygame.sprite.Sprite):
    def __init__(self,angle,pos,img,bullet_mat):
        super().__init__()
        self.baseimg = img
        self.props = bullet_mat.props
        self.type = 'particle'
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.baseimg.get_rect(center = self.pos)
        self.image = pygame.transform.rotate(self.baseimg, angle)
        self.rect = self.image.get_rect(center = self.rect.center)
        self.speed = pygame.math.Vector2(bullet_mat.speed,0)
        self.speed = self.speed.rotate(-angle)
        self.life = time.time()
        self.life_time = bullet_mat.life_time
        self.damage = bullet_mat.damage

    def explode(self,level):
        entites = level.enemies.sprites()
        entites.extend(level.players.sprites())
        
        for p in entites:
            x_offset = p.rect.centerx - self.rect.centerx
            y_offset = p.rect.centery - self.rect.centery
            distance = pygame.math.Vector2(x_offset,y_offset).length()
            if distance > 60*level.scale:
                pass
            elif distance > 42*level.scale:
                p.health -= self.damage/2**2
            elif distance > 24*level.scale:
                p.health -= self.damage/2
            elif distance != None:
                p.health -= self.damage

        self.kill()
        

        
    def update(self,level,dt):
        current = time.time()
        if current - self.life >= self.life_time:
            if 'explode' in self.props:
                self.explode()
            else:
                self.kill()

        for i in level.enemies:
            if self.rect.colliderect(i.rect):
                if 'explode' in self.props:
                    self.explode(level)
                else:
                    i.health -= self.damage
                    self.kill()

        for i in level.tiles:
            if self.rect.colliderect(i.rect):
                if 'explode' in self.props:
                    self.explode(level)
                else:
                    self.kill()

        self.pos += self.speed*dt
        self.rect.center = self.pos

