import pygame
import math
import time
import random
import item_funcs as itf
from bullets import Bullet

class Gun(pygame.sprite.Sprite):
    def __init__(self, image,bimage,pos,handle, shoot_point,rate_of_fire, inaccuracy,mag_size,reload_speed,shots, ammo_type,bullet_mat):
        super().__init__()
        self.shoot_time = 0
        self.reload_time = 0
        self.mag_size = mag_size
        self.bullet_mat = bullet_mat
        self._reload = False
        self.mag = self.mag_size
        self.reload_speed = reload_speed
        self.loaded = False
        self.timer = 0
        self.dropped = True
        self.momentum = pygame.math.Vector2()
        self.type = 'item'
        self.name = 'gun'
        self.shots = shots
        self.ammo_type = ammo_type
        self.flip = False
        self.base_handle = handle
        self.base_shoot_point = shoot_point
        self.inaccuracy = inaccuracy
        self.rateof = rate_of_fire
        self.base_img = image.copy()
        self.flipped = image
        self.image = image
        self.b_image = bimage
        self.base_rect = self.image.get_rect(midbottom = pos)
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pygame.math.Vector2(self.rect.center)

    def rotate(self,pos, originPos,barrel, image, angle):
        image_rect = image.get_rect(topleft = (pos[0]- originPos[0],pos[1] - originPos[1]))
        ptc = pygame.math.Vector2(pos[0] - image_rect.center[0], pos[1] - image_rect.center[1])
        ptb = pygame.math.Vector2(barrel[0] -originPos[0],barrel[1]- originPos[1])

        rptc = ptc.rotate(-angle)
        rptb = ptb.rotate(-angle)

        rc = (pos[0]-rptc[0],pos[1] - rptc[1])
        muzzle = (pos[0]+rptb[0],pos[1] + rptb[1])

        new_image = pygame.transform.rotate(image, angle)
        rorect = new_image.get_rect(center = rc)

        return new_image, rorect,muzzle
    
    def reset(self,level):
        if self.flip:
            self.image = pygame.transform.flip(self.base_img,True,False)
        else:
            self.image = self.base_img
        self.rect = self.image.get_rect(center = self.rect.center)
        self.pos = pygame.math.Vector2(self.rect.midbottom)

        if self._reload:
            self._reload = False
            self.timer = 0
            delattr(self,'reload_time')
            level.finish_bar = False

    def reload(self,ammo,current):
        reloaded = False
        if self.reload_time == 0:
            self.reload_time = time.time()
            
        self.timer = current - self.reload_time
        if current - self.reload_time >= self.reload_speed:
            diff = self.mag_size - self.mag
            if diff > ammo[self.ammo_type][0]:
                amount = ammo[self.ammo_type][0]
                ammo[self.ammo_type][0] -= amount
                self.mag += amount
                reloaded = True
            else:
                self.mag += diff
                ammo[self.ammo_type][0] -= diff
                reloaded = True
        if reloaded:
            self.reload_time = 0
        return reloaded

    def update(self,projectiles, dt, pos,level,ammo = None):
        if not self.dropped:  
            mouse = pygame.mouse.get_pos()
            mdif = (mouse[0] - (pos[0]-level.scroll.x),(pos[1]-level.scroll.y) - mouse[1])
            angle = math.degrees(math.atan2(mdif[1],mdif[0]))
            if self.flip:
                self.flipped = pygame.transform.flip(self.base_img,False,True)
                self.handle = (self.base_handle[0],self.flipped.get_height()- self.base_handle[1])
                self.shoot_point = (self.base_shoot_point[0], self.flipped.get_height() - self.base_shoot_point[1])
            else:
                self.flipped = self.base_img
                self.handle = self.base_handle
                self.shoot_point = self.base_shoot_point

            self.image,self.rect,self.barrel = self.rotate(pos, self.handle, self.shoot_point, self.flipped, angle)
            
            current = time.time()
            
            if self._reload:
                reloaded = self.reload(ammo, current)
                if reloaded == True:
                    self._reload = False

            if pygame.mouse.get_pressed() == (1,0,0) and (current - self.shoot_time > self.rateof) and not self._reload and self.mag>0 and not level.show_wheel:
                self.shoot_time = time.time()
                for i in range(self.shots):
                    offset = random.randint(-self.inaccuracy,self.inaccuracy)
                    new_bullet = Bullet(angle+offset, self.barrel,self.b_image,self.bullet_mat)
                    projectiles.add(new_bullet)
                self.mag -= 1
            elif (pygame.MOUSEBUTTONDOWN,1) in level.keyed and self.mag==0:
                if self.mag < self.mag_size and ammo[self.ammo_type][0] > 0:
                    self._reload = True
        else:
            itf.is_loaded(level,self)
            if not self.unloaded:
                itf.move(level,self,dt)

        
            
        
        
        
