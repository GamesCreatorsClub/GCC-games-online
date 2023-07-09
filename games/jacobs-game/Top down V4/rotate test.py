import pygame as pg
import math
import time

def rotate(surface, angle, pivot, offset):

    if -angle+90 < 270 and -angle +90 > 90:
        surface = pg.transform.flip(surface,True,False)

    rotated_image = pg.transform.rotozoom(surface, -angle, 3)  

    rotated_offset = offset.rotate(angle)

    rect = rotated_image.get_rect(center=pivot+rotated_offset)

    return rotated_image, rect  


class Bullet():
    def __init__(self,angle,origin):
        self.angle = -angle
        self.image = pg.image.load("bullet.png")
        self.image = pg.transform.rotozoom(self.image,angle,1)
        self.speed = 48
        self.origin = pg.math.Vector2(origin)
        self.direction = pg.math.Vector2(0,self.speed)
        self.direction = self.direction.rotate(self.angle)
        self.rect = self.image.get_rect(center = self.origin)
    
    def move(self):
        self.rect.center += self.direction
        dist = pg.math.Vector2(self.rect.center[0]-self.origin[0],self.rect.center[1]-self.origin[1])
        if dist.length() > 1200:
            return True
        else:
            return False        


pg.init()
screen = pg.display.set_mode((1280, 500))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
IMAGE = pg.image.load("sniper for rotate test.png")
pivot = [640, 250]
offset = pg.math.Vector2(0, 10)
angle = 0
shoot_time = 0
bullets = []
running = True
flipped = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    mouse_diff = (mouse_pos[0] - pivot[0],pivot[1] - mouse_pos[1])
    angle = -(math.degrees(math.atan2(mouse_diff[1],mouse_diff[0])))-90

    rotated_image, rect = rotate(IMAGE, angle, pivot, offset)
    if -angle+90 < 270 and -angle +90 > 90:
        barrel_offset = pg.math.Vector2(2,98)
    else:
        barrel_offset = pg.math.Vector2(-12,98)
    rot_barrel_offset = barrel_offset.rotate(angle)
    barrel_pos = rect.center + rot_barrel_offset
    for bullet in bullets:
        del_bullet = bullet.move()
        if del_bullet:
            bullets.remove(bullet)
    current_time = time.time()

    if pg.mouse.get_pressed()[0] == 1:
        if current_time - shoot_time > 1:
            bullet = Bullet(-angle,barrel_pos)
            bullets.append(bullet)
            shoot_time = time.time()
            casing = Casing(rect.center)
        

    screen.fill(BG_COLOR)
    for bullet in bullets:
        screen.blit(bullet.image,bullet.rect)
    screen.blit(rotated_image, rect)  
    pg.draw.circle(screen, (30, 250, 70), pivot, 3)
    pg.draw.circle(screen,(30,250,70),barrel_pos,3)
    pg.draw.rect(screen, (30, 250, 70), rect, 1) 
    pg.display.set_caption('Angle: {}'.format(angle))
    pg.display.flip()
    clock.tick(30)

pg.quit()
