import pygame
import random
import math
import time

######DEFINING THE FIND ANGLE FUNCTIONS########

def find_player_angle(player):
    mouse = pygame.mouse.get_pos()
    pos = player.rect.center
    mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
    angle = -(math.degrees(math.atan2(mdif[1],mdif[0])))-90
    return angle

def find_enemy_angle(player,enemy):
    player_pos = player.rect.center  
    enemy_pos = enemy.rect.center
    player_diff = (player_pos[0] - enemy_pos[0],enemy_pos[1] - player_pos[1])
    angle = -(math.degrees(math.atan2(player_diff[1],player_diff[0])))+90
    return angle

#######DEFINING THE LASER FUNCTION############

def laser(gun,room,blocks,player):

    laser_rect = pygame.Rect(gun.rect.center[0],gun.rect.center[1],1,1)
    direction = pygame.math.Vector2(16,0)
    direction = direction.rotate(player.facing+90)
    found_end = False
    while not found_end:
        laser_rect.topleft += direction
        for wall in room:
            if laser_rect.colliderect(wall):
                found_end = True
                return laser_rect.center
        
        for block in blocks:
            if not block.can_move:
                if laser_rect.colliderect(block):
                    found_end = True
                    return laser_rect.center

#########DEFINING THE FUNCTION TO GET CASINGS AFTER SHOOTING ############

def casings(gun,colour_choices,angle):
    if gun.gun_type == "SMG":
        casing_chance = random.randint(0,3)
        if casing_chance == 0:
            colour_choice = colour_choices[random.randint(0,1)]
            particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,12,8)
            return particle

    elif gun.gun_type == "AR":
        casing_chance = random.randint(0,1)
        if casing_chance == 0:
            colour_choice = colour_choices[random.randint(0,1)]
            particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,12,8)
            return particle
    
    if gun.gun_type == "Machine Gun Enemy":
        colour_choice = colour_choices[random.randint(0,1)]
        particle = Particle(colour_choice,0.6,5,gun.rect.center,-angle-90,10,12,8)
        return particle

    else:
        colour_choice = colour_choices[random.randint(0,1)]
        particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,12,8)
        return particle
        
def make_particle(colour_choices,gun,angle):
    lifespan = random.uniform(0.1,0.3)
    part_speed = random.randint(3,5)
    max_choice = len(colour_choices) -1
    colour_choice = colour_choices[random.randint(0,max_choice)]
    particle = Particle(colour_choice,lifespan,part_speed,gun.barrel_pos,-angle+180,10,8,8)                        
    return particle
############DEFINING THE CLASSES###############

class Obstacle():
    def __init__(self,rect,block_type,image,can_move):
        self.rect = rect
        self.image = image
        self.can_move = can_move
        self.block_type = block_type

        
class Mine(Obstacle):
    def __init__(self, rect, block_type,image, can_move,blast_radius,dmg):
        super().__init__(rect, block_type,image, can_move)
        self.blast_radius = blast_radius
        self.dmg = dmg
        self.death_radius = 120
        
    def explode_check(self,collider):
        if self.rect.colliderect(collider.rect):
            return True
        return False

    def explode(self,entity):
        a = self.rect.centerx - entity.rect.centerx
        b = self.rect.centery - entity.rect.centery
        c = math.sqrt(a*a+b*b)
        
        if  c < self.blast_radius:
            entity.health -= self.dmg/(c/6)


class Stairs(Obstacle):
    def __init__(self, rect, block_type, image,can_move,up_or_down):
        super().__init__(rect, block_type, image,can_move)
        self.up_or_down = up_or_down

    def move_to_level(self, player, current_level,levels,load_level):
        if self.block_type == "down stairs":
            if self.rect.colliderect(player):
                player.x = 864
                player.y = 32
                return load_level(levels[current_level+1])

        if self.block_type == "up stairs":
            if self.rect.colliderect(player):
                player.x = 352
                player.y = 32
                return load_level(levels[current_level-1])
        return None
            

class Door(Obstacle):
    def __init__(self,rect,block_type,image,can_move):
        super().__init__(rect,block_type,image,can_move)

    def check_win(self,player):
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False

        
class Enemy():
    def __init__(self, rect, type, speed, health, dmg, image):
        self.rect = rect
        self.speed = speed
        self.health = health
        self.dmg = dmg
        self.image = image
        self.type = type
        self.shoot_time = 0
        self.text = ""
        self.gun = Better_Gun((-32,-32),pygame.image.load("gun.png"),1,20,5,0.5,25,100,"Enemy",1,32,0)
        self.rotimg = self.gun.image
        self.rorect = self.gun.rect
        self.shot = False
        self.shot_angles = []
        self.blit_shot_angles = []
        self.rotenimg = self.image 
        self.rotenrect = self.rect
        self.facing = 0

    def rotate(self, angle, pivot, offset,gun):
        rotated_image = pygame.transform.rotozoom(gun.image, -angle, 1)  
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect
        
    def rotate_gun(self,player):
        angle = find_enemy_angle(self,player)
        pivot = self.rect.center
        offset = self.gun.rotational_offset
        rotated_image, rect = self.rotate(angle, pivot, offset,self.gun)
        self.gun.rect = rect
        return rotated_image, rect

    def shoot(self,player):
        angle = -(find_enemy_angle(self,player))-90
        spread = random.randint(-self.gun.spread,self.gun.spread)
        bullet = Bullet(angle + spread,self.gun)
        return bullet

    def rotate_self(self,player):
        pivot = self.rect.center
        offset = pygame.math.Vector2(0,0)
        angle = find_enemy_angle(self,player)
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,self)
        ### changing self.facing for the enemies ###
        self.facing = angle
        return rotated_image, blit_rect


class Heavy_Enemy(Enemy):
    def __init__(self, rect, type, speed, health, dmg, image):
        super().__init__(rect, type, speed, health, dmg, image)
        self.gun = Better_Gun((-32,-32),pygame.image.load("assault rifle.png"),1.5,50,1,0.5,25,100,"Heavy Enemy",1,32,0)
           
        
class Grenade_Enemy(Enemy):
    def __init__(self, rect, type, speed, health, dmg, image):
        super().__init__(rect, type, speed, health, dmg, image)
        self.gun = Better_Gun((-32,-32),pygame.image.load("grenade launcher.png"),1,0,0,0,5,10,"Grenade Launcher",1,24,0.3)         

    def shoot(self,player):
        gren_dist = random.uniform(0.5,1.0)
        angle = -(find_enemy_angle(self,player))-90
        spread = random.randint(-self.gun.spread,self.gun.spread)
        grenade = Grenade(self.gun.speed,angle + spread,self.gun.rect.center,1500,180,gren_dist)
        grenade.death_radius = 60
        return grenade


class Machine_Enemy(Enemy):
    def __init__(self, rect, type, speed, health, dmg, image):
        super().__init__(rect, type, speed, health, dmg, image)
        base_image = pygame.image.load("machine gun base.png")
        gun_image = pygame.image.load("machine gun.png")
        self.gun = Machine_Gun((-32,-32),base_image,gun_image,0.25,25,5,0.5,25,100,"Machine Gun Enemy",1,32,0)
        self.gun.base_rect = self.gun.base_image.get_rect(center = self.rect.center)
        self.gun.rect.center = self.rect.center
        self.image = pygame.image.load("enemy.png")


class Player():
    def __init__(self,rect,speed,health,dmg,image):
        self.rect = rect
        self.speed = speed
        self.health = health
        self.dmg = dmg
        self.image = image
        self.direction = pygame.math.Vector2()
        self.inventory = []
        self.shot = False
        self.shot_angles = []
        self.has_gun = True

    def inputs(self, keys):
        if keys[pygame.K_a]:
            self.direction.x = -1
            
        elif keys[pygame.K_d]:
            self.direction.x = 1
            
        else:
            self.direction.x = 0
            

        if keys[pygame.K_w]:
            self.direction.y = -1
          
        elif keys[pygame.K_s]:
            self.direction.y = 1
        
        else:
            self.direction.y = 0
        
        check_length = self.direction.length()
        if check_length > 0:
            self.direction = self.direction.normalize()
    
        ### updating facing variable for player ###
        player_pos = pygame.mouse.get_pos()  
        player_diff = (player_pos[0] - self.rect.center[0],self.rect.center[1] - player_pos[1])
        self.facing = -(math.degrees(math.atan2(player_diff[1],player_diff[0])))-90

    def update_x(self,room,block_list):
        self.rect.x += self.direction.x * self.speed
        for wall in room:
            if self.rect.colliderect(wall):
                if self.direction.x < 0:
                    self.rect.left = wall.right
                elif self.direction.x > 0:
                    self.rect.right = wall.left

        for block in block_list:
            if block.can_move == False:
                if self.rect.colliderect(block):
                    if self.direction.x < 0:
                        self.rect.left = block.rect.right
                    elif self.direction.x > 0:
                        self.rect.right = block.rect.left

    def update_y(self,room,block_list):
        self.rect.y += self.direction.y * self.speed
        for wall in room:
            if self.rect.colliderect(wall):
                if self.direction.y < 0:
                    self.rect.top = wall.bottom
                elif self.direction.y > 0:
                    self.rect.bottom = wall.top

        for block in block_list:
            if block.can_move == False:
                if self.rect.colliderect(block):
                    if self.direction.y < 0:
                        self.rect.top = block.rect.bottom
                    elif self.direction.y > 0:
                        self.rect.bottom = block.rect.top

    def rotate(self, angle, pivot, offset,current_gun):
        rotated_image = pygame.transform.rotozoom(current_gun.image, -angle, 1)  
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect
        
    def rotate_gun(self,current_gun):
        pivot = self.rect.center
        offset = current_gun.rotational_offset
        angle = find_player_angle(self)
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,current_gun)
        current_gun.rect = blit_rect
        return rotated_image, blit_rect
    
    def shoot(self,current_gun):
        angle = find_player_angle(self)+90
        spread = random.uniform(-current_gun.spread,current_gun.spread)
        bullet = Bullet(-angle+spread,current_gun)
        current_gun.last_shot_time = time.time()
        return bullet

    def rotate_self(self):
        pivot = self.rect.center
        offset = pygame.math.Vector2(0,0)
        angle = find_player_angle(self)
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,self)
        return rotated_image, blit_rect


class Better_Gun():
    def __init__(self,pos,image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil):
        self.pos = pygame.math.Vector2(pos)
        self.fire_rate = fire_rate
        self.dmg = dmg
        self.spread = 0
        self.spread_climb = spread_climb
        self.max_spread = spread
        self.image = image
        self.loaded_ammo = max_loaded
        self.reserve_ammo = max_reserve
        self.gun_type = gun_type
        self.max_loaded = max_loaded
        self.max_reserve = max_reserve
        self.shot_quantity = shot_quantity
        self.rotational_offset = pygame.math.Vector2(-8, 20)
        self.speed = speed
        self.rect = self.image.get_rect(center = pos)
        self.collider_rect = self.image.get_rect(center = pos)
        self.last_shot_time = 0
        self.recoil = pygame.math.Vector2(recoil,0)
        self.dropped = True
        self.has_laser = False
        self.laser_on = False
        self.stock = False
        self.used_mag = False
        self.barrel_offset = pygame.math.Vector2(0,0)
        if self.gun_type == "AR":
            self.barrel_offset = pygame.math.Vector2(48,2)

        elif self.gun_type == "SMG":
            self.barrel_offset = pygame.math.Vector2(48,2)

        elif self.gun_type == "Starter AR":
            self.barrel_offset = pygame.math.Vector2(32,6)

        elif self.gun_type == "Pistol":
            self.barrel_offset = pygame.math.Vector2(24,0)

        elif self.gun_type == "Shotgun":
            self.barrel_offset = pygame.math.Vector2(48,2)
        
        elif self.gun_type == "Sniper":
            self.barrel_offset = pygame.math.Vector2(64,0)

        elif self.gun_type == "Grenade Launcher":
            self.barrel_offset = pygame.math.Vector2(54,0)

        elif self.gun_type == "Rocket Launcher":
            self.barrel_offset = pygame.math.Vector2(63,0)
        
        elif self.gun_type == "Enemy":
            self.barrel_offset = pygame.math.Vector2(32,6)

        elif self.gun_type == "Heavy Enemy":
            self.barrel_offset = pygame.math.Vector2(48,2)
        
        elif self.gun_type == "Machine Gun Enemy":
            self.barrel_offset = pygame.math.Vector2(60,0)

        self.rot_barrel_offset = self.barrel_offset
        self.barrel_pos = self.rect.center + self.rot_barrel_offset

    def check_pick_up(self,player):
        if self.dropped == True:
            if self.collider_rect.colliderect(player.rect):
                return True
            else:
                return False

    def place_barrel(self,player):
        if self.gun_type == "Rocket Launcher":
            if self.loaded_ammo == 1:
                self.barrel_offset = pygame.math.Vector2(63,0)
            else:
                self.barrel_offset = pygame.math.Vector2(36,0)

        self.rot_barrel_offset = self.barrel_offset.rotate(player.facing+90)
        self.barrel_pos = self.rect.center + self.rot_barrel_offset#

               
class Machine_Gun(Better_Gun):
    def __init__(self,pos,base_image,gun_image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil):

        super().__init__(pos,gun_image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil)
        self.base_image = base_image
        self.rotational_offset = pygame.math.Vector2(0,0)
        self.rot_barrel_offset = self.barrel_offset
        self.barrel_pos = self.rect.center + self.rot_barrel_offset
        

class Bullet():
    def __init__(self,angle,shot_from):
        self.image = pygame.image.load("bullet.png")
        self.pos = pygame.math.Vector2(shot_from.barrel_pos)
        self.origin = shot_from.barrel_pos
        self.rotated_image = pygame.transform.rotate(self.image,angle+90)
        self.rect = self.rotated_image.get_rect(center = self.pos)
        self.speed = pygame.math.Vector2(shot_from.speed,0)
        self.speed = self.speed.rotate(-angle)
        self.dmg = shot_from.dmg
        self.shot_from = shot_from.gun_type
        self.shot_time = time.time()
        self.in_max_range = True
        self.health = 1
        self.angle = -angle

    def move(self):
        self.rect.center += self.speed

    def dmg_reduce(self):   
        if self.shot_from == "Starter AR":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center


        if self.shot_from == "AR":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "Shotgun":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "SMG":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "Pistol":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (15*32): # 15 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "Enemy":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

    def check_collision(self,entity):
        if self.rect.colliderect(entity):
            return True
        else:
            return False


class Rocket():
    def __init__(self,speed,angle,pos,dmg,blast_radius):
        self.image = pygame.image.load("rpg ammo.png")
        self.pos = pygame.math.Vector2(pos)
        self.rotated_image = pygame.transform.rotate(self.image,angle+90)
        self.rect = self.rotated_image.get_rect(center = self.pos)
        self.speed = pygame.math.Vector2(speed,0)
        self.speed = self.speed.rotate(-angle)
        self.dmg = dmg
        self.blast_radius = blast_radius
        self.angle = -angle
        self.dmg_cone = 30
    
    def update(self):
        self.rect.center += self.speed

    def check_collision(self,entity):
        if self.rect.colliderect(entity):
            return True
        else:
            return False
    
    def explode(self,enemies,player):
        for enemy in enemies:
            mouse = enemy.rect.center
            pos = self.rect.center
            mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
            enemy_angle = -(math.degrees(math.atan2(mdif[1],mdif[0])))
            if enemy_angle < self.angle + self.dmg_cone and enemy_angle > self.angle - self.dmg_cone:
                a = self.rect.centerx - enemy.rect.centerx
                b = self.rect.centery - enemy.rect.centery
                c = math.sqrt(a*a+b*b)
                if  c < self.blast_radius:
                    enemy.health -= self.dmg/(c/4)

        mouse = player.rect.center
        pos = self.rect.center
        mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
        enemy_angle = -(math.degrees(math.atan2(mdif[1],mdif[0]))+90)
        if enemy_angle < self.angle + self.dmg_cone and enemy_angle > self.angle - self.dmg_cone:
            a = self.rect.centerx - enemy.rect.centerx
            b = self.rect.centery - enemy.rect.centery
            c = math.sqrt(a*a+b*b)
            if  c < self.blast_radius:
                player.health -= self.dmg/(c/4)


class Particle():
    def __init__(self,colour,lifespan,speed,pos,angle,spread,width,height):
        self.colour = colour
        self.image = pygame.Surface((width,height))
        self.image.fill(colour)
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center = self.pos)
        self.direction = pygame.math.Vector2(speed,0)
        self.spread = random.randint(-spread,spread)
        self.direction = self.direction.rotate(angle + self.spread)
        self.lifespan = lifespan
        self.spawned = time.time()
        
    def update(self):
        self.rect.center += self.direction
        self.current_time = time.time()
        if self.current_time - self.spawned > self.lifespan:
            return True
        return False


class Blood_Angle():
    def __init__(self,player_angle,shot_angle):
        self.blit_angle = shot_angle - player_angle + 180


class Grenade():
    def __init__(self,speed,angle,pos,dmg,blast_radius,gren_dist):
        self.pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos[0],self.pos[1],24,24)
        self.image = pygame.image.load("grenade.png")
        self.speed = pygame.math.Vector2(speed,0)
        self.speed = self.speed.rotate(-angle)
        self.thrown_time = time.time()
        self.health = 1
        self.dmg = dmg
        self.blast_radius = blast_radius
        self.gren_dist = gren_dist
        self.death_radius = 0

    def update(self):
        self.rect.center += self.speed
        new_length = self.speed.length() - self.gren_dist
        if new_length > 0:
            self.speed.scale_to_length(new_length)
        return new_length

    def check_collision(self,entity):
        if self.rect.colliderect(entity):
            return True
        else:
            return False

    def explode(self,enemies,player):
        for enemy in enemies:
            a = self.rect.centerx - enemy.rect.centerx
            b = self.rect.centery - enemy.rect.centery
            c = math.sqrt(a*a+b*b)
        
            if  c < self.blast_radius:
                enemy.health -= self.dmg/(c/4)
                            
        a = self.rect.centerx - player.rect.centerx
        b = self.rect.centery - player.rect.centery
        c = math.sqrt(a*a+b*b)
        
        if  c < self.blast_radius:
            player.health -= self.dmg/(c/4)


class Takeable_Object():
    def __init__(self,rect):
        self.rect = rect
    
    def check_pick_up(self,player):
        if self.rect.colliderect(player.rect):
            return True
        else:
            return False
    

class Ammo_pouch(Takeable_Object):
    def __init__(self,rect):
        super().__init__(rect)
        self.can_move = True
        self.block_type = "Ammo"
        self.image = pygame.image.load("ammo pouch.png")

    def use(self,gun_options):
        for gun_option in gun_options:
            gun_option.loaded_ammo = gun_option.max_loaded
            gun_option.reserve_ammo = gun_option.max_reserve


class Medi_pouch(Takeable_Object):
    def __init__(self,rect):
        super().__init__(rect)
        self.can_move = True
        self.block_type = "Medi"
        self.image = pygame.image.load("medi pouch.png")

    def use(self,player):
        if player.rect.colliderect(self.rect):
            player.health = 100


class Upgrade(Takeable_Object):
    def __init__(self,upgrade_type,pos,image):
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.block_type = "Upgrade"
        self.type = upgrade_type
    
    def use(self,current_gun):
        if self.type == "Laser":
            current_gun.has_laser = True

        elif self.type == "Stock":
            if not current_gun.stock:
                current_gun.stock = True
                current_gun.recoil /= 1.5
                current_gun.max_spread /= 1.5
                current_gun.spread_climb /= 2

        elif self.type == "Mag":
            if current_gun.gun_type != "Shotgun" and current_gun.gun_type != "Grenade Launcher" and current_gun.gun_type != "Rocket Launcher":
                if not current_gun.used_mag:
                    current_gun.max_loaded *= 2
                    current_gun.max_reserve = int(current_gun.max_reserve * 2)
                    current_gun.used_mag = True
                current_gun.loaded_ammo = current_gun.max_loaded
                current_gun.reserve_ammo = current_gun.max_reserve

