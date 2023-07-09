# Sprite classes for platform game
import pygame as pg
from settings import *
from img import *

vec = pg.math.Vector2

def offset_rect(rect, offset):
    new_rect = pg.Rect(rect.x, rect.y, rect.w, rect.h)
    new_rect.x += offset.x
    new_rect.y += offset.y

    return new_rect

def offset_vec(vector, offset):
    new_vec = vec(vector.x, vector.y)
    new_vec.x += offset.x
    new_vec.y += offset.y

    return new_vec

class Enemy(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load("images/Enemies/H.png")
        self.e_image = pg.image.load("images/Enemies/e.png")
        self.pos = vec(0, 0)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        
    def draw(self, screen, offset):
        screen.blit(self.image, self.rect)
        

class Player(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.load_images()
        self.image = self.running_frames_r[0]
        self.img_rect = self.image.get_rect()
        self.pos = vec(448, (len(self.game.levels.active_level)* BLOCK_HEIGHT) - 386)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect = pg.Rect(850,0,60,160)
        self.foot_rect = pg.Rect(0,0, 60, 10)        
        self.rect.midbottom = self.pos
        
        # Animation and motion states
        self.jumping = False
        self.running = False
        self.facing_right = True
        # Animation data
        self.current_frame = 0
        self.last_update = 0

    def draw(self, screen, offset):
        # Create the offset rects and vec for drawing
        img_rect = offset_rect(self.img_rect, offset)
        rect = offset_rect(self.rect, offset)
        foot_rect = offset_rect(self.foot_rect, offset)
        pos = offset_vec(self.pos, offset)

        # Draw player image
        screen.blit(self.image, img_rect)
        # Debug draw for pos and rect of player
        if self.game.debug == True:
            pg.draw.rect(screen, GREEN, rect, 1)
            pg.draw.rect(screen, RED, foot_rect, 1)
            pg.draw.circle(screen, RED, (int(pos.x),int(pos.y)), 3)

    def load_images(self):
        self.idle_frames = load_p_img_idle()
        self.jump_loop_frames_r = load_p_img_jump_loop_r()
        self.jump_loop_frames_l = create_left_images(self.jump_loop_frames_r)
        self.running_frames_r = load_p_img_running_r()
        self.running_frames_l = create_left_images(self.running_frames_r)
    
    def jump(self):
        # Jump only if standing on blocks
        self.can_jump = False
        self.rect.y += 2
        for block in self.game.blocks:
            if block.stand_on:
                if block.surface_rect.colliderect(self.rect):
                    self.can_jump = True
                    
        self.rect.y -= 2
        if self.can_jump: 
            self.vel.y -= PLAYER_JUMP
            self.jumping = True

        
    def update(self):
        # Set vertical acceleration
        self.acc = vec(0, PLAYER_GRAV)
        # Check for horizontal acceleration from the player
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC

        # Apply Friction
        self.acc.x += self.vel.x * -PLAYER_FRICTION
        # Equations of motion
        self.vel += self.acc
        # Set vel x to 0 when very small
        if abs(self.vel.x) < 0.9:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        
        # Align the bottom of the players rect with the position coordinate
        self.rect.midbottom = self.pos
        # Align the img rect with the player rect
        self.img_rect.center = self.rect.center
        if self.facing_right:
            self.img_rect.x -= 6
        else:
            self.img_rect.x += 6
        self.img_rect.y += 12
        # Align the foot rect with the player rect
        self.foot_rect.midbottom = self.pos
        # Looks at the state of the player and in game time to decide which image to use
        self.animate()

    def animate(self):
        current_time = pg.time.get_ticks()
        if self.vel.x != 0:
            self.running = True
        else:
            self.running = False
        # IDLE ANIMATION
        if not self.jumping and not self.running:
            if current_time - self.last_update > 40:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]
        # RUNNING ANIMATION
        if self.running and not self.jumping:
            if current_time - self.last_update > 40:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.running_frames_r)
                if self.vel.x >= 0:
                    self.image = self.running_frames_r[self.current_frame]
                else:
                    self.image = self.running_frames_l[self.current_frame]
        # JUMPING ANIMATION
        if self.jumping:
            if current_time - self.last_update > 40:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.jump_loop_frames_r)
                if self.vel.x >=0:
                    self.image = self.jump_loop_frames_r[self.current_frame]
                else:
                    self.image = self.jump_loop_frames_l[self.current_frame]
       

class Block(pg.sprite.Sprite):

    def __init__(self, game, x, y, block_num, stand_on = True):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.block_num = block_num
        self.rect = pg.Rect(0, 0, BLOCK_WIDTH, BLOCK_HEIGHT)
        self.rect.x = x
        self.rect.y = y
        self.stand_on = stand_on
        if self.stand_on == True:
            self.surface_rect = pg.Rect(self.rect.x, self.rect.y, self.rect.width, 10)
    
    def realign_rects(self):
        if self.stand_on == True:
            self.surface_rect.midtop = self.rect.midtop
        
    
    def draw(self, screen, offset):
        rect = offset_rect(self.rect, offset)
        screen.blit(BLOCK_IMAGES[self.block_num], rect)
        if self.game.debug == True:
            pg.draw.rect(screen, GREEN, rect, 1)
            if self.stand_on == True:
                surface_rect = offset_rect(self.surface_rect, offset)
                pg.draw.rect(screen, BLUE, surface_rect, 1)
