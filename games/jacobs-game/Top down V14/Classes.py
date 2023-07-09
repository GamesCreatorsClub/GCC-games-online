import pygame
import random
import math
import time

######DEFINING THE FIND ANGLE FUNCTIONS########

def find_player_angle(player):
    mouse = pygame.mouse.get_pos()
    pos = player.rect.center
    mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
    angle = math.degrees(math.atan2(mdif[1],mdif[0]))
    return angle

def player_to_enemy_angle(player,enemy):
    mouse = enemy.rect.center
    pos = player.rect.center
    mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
    angle = math.degrees(math.atan2(mdif[1],mdif[0]))
    return angle

def find_enemy_angle(player,enemy):
    player_pos = player.rect.center  
    enemy_pos = enemy.rect.center
    player_diff = (player_pos[0] - enemy_pos[0],enemy_pos[1] - player_pos[1])
    angle = -(math.degrees(math.atan2(player_diff[1],player_diff[0])))+90
    return angle

#######DEFINING THE LASER FUNCTION############

def raycast_to_entity(start,blocks,radius,entity,player):
    mouse = pygame.mouse.get_pos()
    dx = mouse[0] - start[0]
    dy = mouse[1] - start[1]

    raycast_rect = pygame.Rect(0,0,1,1)
    raycast_rect.center = start
    raycast_float = pygame.math.Vector2(raycast_rect.center)

    angle = -player_to_enemy_angle(player,entity)
    angle_gradient = pygame.math.Vector2(1,0)
    angle_gradient = angle_gradient.rotate(angle)
    angle_gradient.scale_to_length(4)

    collided = False
    while not collided:
        dx = abs(raycast_rect.centerx - start[0])
        dy = abs(raycast_rect.centery - start[1])
        length = math.sqrt((dx*dx)+(dy*dy))
        if length >= radius:
            return False
        
        raycast_float.x += angle_gradient.x
        raycast_float.y += angle_gradient.y
        raycast_rect.topleft = raycast_float
        for block in blocks:
            if not block.can_move:
                if raycast_rect.colliderect(block.rect):
                    return False

        if raycast_rect.colliderect(entity.rect):
            return True

def laser2(gun,blocks,player,radius,spread,enemies,check_enemies):
    first_check = False
    if not first_check:
        player1 = (-64,-64)
        mouse = (-128,-128)
        first_check = True

    if player.rect.center != player1 and pygame.mouse.get_pos() != mouse:
        player1 = player.rect.center
        mouse = pygame.mouse.get_pos()
        dx = mouse[0] - gun.barrel_pos[0]
        dy = mouse[1] - gun.barrel_pos[1]

        raycast_rect = pygame.Rect(0,0,1,1)
        raycast_rect.center = gun.barrel_pos
        raycast_float = pygame.math.Vector2(raycast_rect.center)

        angle = -find_player_angle(player)+spread
        angle_gradient = pygame.math.Vector2(1,0)
        angle_gradient = angle_gradient.rotate(angle)
        angle_gradient.scale_to_length(4)

        collided = False
        while not collided:
            dx = abs(raycast_rect.centerx - gun.barrel_pos[0])
            dy = abs(raycast_rect.centery - gun.barrel_pos[1])
            length = math.sqrt((dx*dx)+(dy*dy))
            if length >= radius:
                collided = True
            
            raycast_float.x += angle_gradient.x
            raycast_float.y += angle_gradient.y
            raycast_rect.topleft = raycast_float
            for block in blocks:
                if not block.can_move:
                    if raycast_rect.colliderect(block):
                        collided = True
            
            if check_enemies:
                for enemy in enemies:
                    if raycast_rect.colliderect(enemy):
                        collided = True

        return raycast_rect.center        

def check_gun_collide(gun,block_list):
    check_rect1 = pygame.Rect(gun.rect.center[0],gun.rect.center[1],1,1)
    check_rect2 = pygame.Rect(gun.barrel_pos[0],gun.barrel_pos[1],1,1)
    check_rect3 = pygame.Rect((gun.barrel_pos[0]+gun.rect.center[0])/2,(gun.barrel_pos[1]+gun.rect.center[1])/2,1,1)
    for block in block_list:
        if not block.can_move:
            if check_rect1.colliderect(block):
                return True
            if check_rect2.colliderect(block):
                return True
            if check_rect3.colliderect(block):
                return True
    return False

def area(V1,V2,V3):
    return abs((V1[0]*(V2[1]-V3[1])+(V2[0]*(V3[1]-V1[1]))+(V3[0]*(V1[1]-V2[1])))/2.0)

def point_in_triangle2(V1,V2,V3,point):
    A=area(V1,V2,V3)
    A1=area(V1,V2,point)
    A2=area(V1,V3,point)
    A3=area(V2,V3,point)
    if (A1)+(A2)+(A3) - A<1:
        return True
    else:
        return False

#########DEFINING THE FUNCTION TO GET CASINGS AFTER SHOOTING ############

def casings(gun,colour_choices,angle):
    if gun.gun_type == "SMG":
        casing_chance = random.randint(0,3)
        if casing_chance == 0:
            colour_choice = colour_choices[random.randint(0,1)]
            particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,6,4,True)
            return particle

    elif gun.gun_type == "AR":
        casing_chance = random.randint(0,1)
        if casing_chance == 0:
            colour_choice = colour_choices[random.randint(0,1)]
            particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,6,4,True)
            return particle
    
    if gun.gun_type == "Machine Gun Enemy":
        colour_choice = colour_choices[random.randint(0,1)]
        particle = Particle(colour_choice,0.6,5,gun.rect.center,-angle-90,10,6,4,True)
        return particle

    else:
        colour_choice = colour_choices[random.randint(0,1)]
        particle = Particle(colour_choice,0.3,5,gun.rect.center,-angle-90,10,6,4,True)
        return particle
        
def make_particle(colour_choices,pos,angle,spread,min_life,max_life,min_ps,max_ps,collide,size):
    lifespan = random.uniform(min_life,max_life)
    part_speed = random.randint(min_ps,max_ps)
    max_choice = len(colour_choices) -1
    colour_choice = colour_choices[random.randint(0,max_choice)]
    particle = Particle(colour_choice,lifespan,part_speed,(int(pos[0]),int(pos[1])),-angle+180,spread,size,size,collide)                        
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
        
    def explode_check(self,bullets,enemies,player):
        if self.rect.colliderect(player.rect):
            return True
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                return True
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                return True
        return False

    def explode(self,enemies,player,blocks,bullets):
        for enemy in enemies:
            enemy_dist = pygame.math.Vector2(abs(enemy.rect.centerx-self.rect.centerx),abs(enemy.rect.centery-self.rect.centery))
            if enemy_dist.length() <= self.blast_radius:
                can_hit = raycast_to_entity(self.rect.center,blocks,self.blast_radius,enemy,self)
                if can_hit:
                    enemy.health -= self.dmg/(enemy_dist.length()/6)
        
        for bullet in bullets:
            bullet_dist = pygame.math.Vector2(abs(bullet.rect.centerx-self.rect.centerx),abs(bullet.rect.centery-self.rect.centery))
            if bullet_dist.length() <= self.blast_radius:
                can_hit = raycast_to_entity(self.rect.center,blocks,self.blast_radius,bullet,self)
                if can_hit:
                    bullets.remove(bullet)
                            
        player_dist = pygame.math.Vector2(abs(player.rect.centerx-self.rect.centerx),abs(player.rect.centery-self.rect.centery))
        if player_dist.length() <= self.blast_radius:
            can_hit = raycast_to_entity(self.rect.center,blocks,self.blast_radius,player,self)
            if can_hit:
                player.health -= self.dmg/(player_dist.length()/6)
        

class Stairs(Obstacle):
    def __init__(self, rect, block_type, image,can_move,up_or_down):
        super().__init__(rect, block_type, image,can_move)
        self.up_or_down = up_or_down

    def move_to_level(self, player, current_level,levels,load_level):
        if self.block_type == "down stairs":
            if self.rect.colliderect(player):
                player.x = 1216
                player.y = 32
                return load_level(levels[current_level+1])

        if self.block_type == "up stairs":
            if self.rect.colliderect(player):
                player.x = 32
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
    def __init__(self, rect, enemy_type, speed, health, dmg, image):
        self.rect = rect
        self.speed = speed
        self.health = health
        self.max_health = health
        self.dmg = dmg
        self.image = image
        self.type = enemy_type
        self.shoot_time = 0
        self.text = ""
        self.gun = Better_Gun((-32,-32),pygame.image.load("Guns Cropped/Bad Guy Rifle.png"),1,20,5,0.5,25,100,"Enemy",1,32,0,"Full Auto",(32,0))
        self.rotimg = self.gun.image
        self.rorect = self.gun.rect
        self.shot = False
        self.shot_angles = []
        self.blit_shot_angles = []
        self.rotenimg = self.image 
        self.rotenrect = self.rect
        self.facing = 0
        self.bouncy_grenades = False
        self.gren_speed = 24
        self.blinded = False
        self.blinded_at = 0

    def rotate(self, angle, pivot, offset,gun):
        rotated_image = pygame.transform.rotozoom(gun.image, -angle, 1)  
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect
        
    def rotate_gun(self,player):
        angle = self.facing
        pivot = self.rect.center
        offset = self.gun.rotational_offset
        rotated_image, rect = self.rotate(angle, pivot, offset,self.gun)
        self.gun.rect = rect
        return rotated_image, rect

    def rotate_self(self,player):
        pivot = self.rect.center
        offset = pygame.math.Vector2(0,0)
        if not self.blinded:
            angle = find_enemy_angle(self,player)
        else:
            angle = self.facing
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,self)

        ### changing self.facing for the enemies ###
        self.facing = angle
        
        ### checking self.blinded for the enemies ###
        if self.blinded:
            if time.time() - self.blinded_at > 2:
                self.blinded = False
        return rotated_image, blit_rect
    
    def shoot_check(self,player,blocks):
        player_diff = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        if not self.blinded:
            if player_diff.length() < 720:
                can_see = raycast_to_entity(player.rect.center,blocks,720,self,player)
                return can_see
            else:
                return False
        else:
            return True
    
    def shoot(self,player):
        angle = -(find_enemy_angle(self,player))-90
        spread = random.randint(-self.gun.spread,self.gun.spread)
        bullet = Bullet(angle + spread,self.gun)
        return bullet

    def drop_item(self):
        if self.type == "machine enemy":
            item = Better_Gun(self.gun.rect.center,pygame.image.load("Guns Cropped/MP40.png"),0.001,20,20,2,50,100,"MP40",1,32,0.25,"Full Auto",(32,0))
        elif self.type == "grenade enemy":
            item = Better_Gun(self.rect.center,pygame.image.load("Guns Cropped/grenade launcher.png"),1,0,0,0,5,10,"Grenade Launcher",1,32,0.3,"Semi Auto",(54,0))
        else:
            item = None
        return item


class Heavy_Enemy(Enemy):
    def __init__(self, rect, enemy_type, speed, health, dmg, image):
        super().__init__(rect, enemy_type, speed, health, dmg, image)
        self.gun = Better_Gun((-32,-32),pygame.image.load("Guns Cropped/Bad Guy Heavy.png"),1.5,30,1,0.5,25,100,"Heavy Enemy",1,32,0,"Burst Fire",(28,-6))
        self.gun.burst_quantity = 2
    
    
class Grenade_Enemy(Enemy):
    def __init__(self, rect, enemy_type, speed, health, dmg, image):
        super().__init__(rect, enemy_type, speed, health, dmg, image)
        self.gun = Better_Gun((-32,-32),pygame.image.load("Guns Cropped/grenade launcher.png"),1,0,0,0,5,10,"Grenade Launcher",1,31,0.3,"Full Auto",(54,0))         

    def shoot(self,player):
        
        
        angle = -(find_enemy_angle(self,player))-90
        spread = random.randint(-self.gun.spread,self.gun.spread)
        grenade = Grenade(self.gren_speed,angle + spread,self.gun.rect.center,1500,180,False,False)
        grenade.death_radius = 60
        return grenade


class Machine_Enemy(Enemy):
    def __init__(self, rect, enemy_type, speed, health, dmg, image):
        super().__init__(rect, enemy_type, speed, health, dmg, image)
        base_image = pygame.image.load("Guns Cropped/machine gun base.png")
        gun_image = pygame.image.load("Guns Cropped/machine gun.png")
        self.gun = Machine_Gun((-32,-32),base_image,gun_image,0.25,25,5,0.5,25,100,"Machine Gun Enemy",1,32,0,"Full Auto",(60,0))
        self.gun.base_rect = self.gun.base_image.get_rect(center = self.rect.center)
        self.gun.rect.center = self.rect.center

class Patrol_Enemy(Enemy):
    def __init__(self, rect, enemy_type, speed, health, dmg, image,horizontal):
        super().__init__(rect, enemy_type, speed, health, dmg, image)
        self.horizontal = horizontal
        self.origin = pygame.math.Vector2(self.rect.x,self.rect.y)

    def move(self):
        current_pos = pygame.math.Vector2(self.rect.x,self.rect.y)
        current_distance = abs(pygame.math.Vector2(self.rect.x-self.origin.x,self.rect.y-self.origin.y).length())
        if current_distance > 160:
            self.speed *= -1
        if self.horizontal:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed


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
        self.gren_speed = 24
        self.bouncy_grenades = True
        self.has_flash = False
        self.flashbang = False
        self.blinded = False
        self.blinded_at = 0

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
        
        if self.blinded:
            pass
    
        ### updating facing variable for player ###
        player_pos = pygame.mouse.get_pos()  
        player_diff = (player_pos[0] - self.rect.center[0],self.rect.center[1] - player_pos[1])
        self.facing = -(math.degrees(math.atan2(player_diff[1],player_diff[0])))-90
        if self.blinded:
            if time.time() - self.blinded_at > 10:
                self.blinded = False

    def update_x(self,block_list):
        self.rect.x += self.direction.x * self.speed
        
        for block in block_list:
            if block.can_move == False:
                if self.rect.colliderect(block):
                    if self.direction.x < 0:
                        self.rect.left = block.rect.right
                    elif self.direction.x > 0:
                        self.rect.right = block.rect.left

    def update_y(self,block_list):
        self.rect.y += self.direction.y * self.speed
        
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
        angle = -find_player_angle(self)-90
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,current_gun)
        current_gun.rect = blit_rect
        return rotated_image, blit_rect
    
    def shoot(self,current_gun):
        angle = -find_player_angle(self)
        bullet = current_gun.shoot(angle)
        return bullet

    def rotate_self(self):
        pivot = self.rect.center
        offset = pygame.math.Vector2(0,0)
        angle = -find_player_angle(self)-90
        rotated_image, blit_rect = self.rotate(angle, pivot, offset,self)
        return rotated_image, blit_rect


class Better_Gun():
    def __init__(self,pos,image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil,fire_mode,barrel_offset):
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
        self.rotational_offset = pygame.math.Vector2(-5, 21)
        self.speed = speed
        self.rect = self.image.get_rect(center = pos)
        self.collider_rect = self.image.get_rect(center = pos)
        self.last_shot_time = 0
        self.recoil = pygame.math.Vector2(recoil,0)
        self.shot_counter = 0
        self.fire_mode = fire_mode
        self.shot = False
        self.can_shoot = False
        self.dropped = True
        self.has_laser = False
        self.laser_on = False
        self.stock = False
        self.used_mag = False
        self.barrel_offset = pygame.math.Vector2(barrel_offset)
        self.rot_barrel_offset = self.barrel_offset
        self.barrel_pos = self.rect.center + self.rot_barrel_offset
        self.burst_quantity = 3

    def check_shoot(self):
        can_shoot = False
        if pygame.mouse.get_pressed()[0] == 1:
            if self.gun_type != "Shotgun":
                if self.spread < self.max_spread:
                    self.spread += self.spread_climb
                else:
                    self.spread = self.max_spread
            else:                        
                self.spread = self.max_spread

            current_time = time.time()
            if self.fire_mode == "Full Auto":
                if current_time - self.last_shot_time > self.fire_rate:
                    can_shoot = True

            if self.fire_mode == "Semi Auto":
                if current_time - self.last_shot_time > self.fire_rate:
                    if self.shot == False:
                        can_shoot = True
            self.shot = True

            if self.fire_mode == "Burst Fire":
                if current_time - self.last_shot_time > self.fire_rate:
                    if self.shot_counter < self.burst_quantity:
                        can_shoot = True
                        self.shot_counter += 1
            
        else:
            self.shot_counter = 0
            self.shot = False
            current_shot_time = time.time()
            if current_shot_time - self.last_shot_time > 0:
                if self.spread > 0:
                    self.spread -= 0.125
                else:
                    self.spread = 0
        
        return can_shoot

    def shoot(self,angle,player):

        spread = random.uniform(-self.spread,self.spread)
        if self.gun_type == "Grenade Launcher":
            bullet = Grenade(player.gren_speed,angle,self.barrel_pos,1500,180,player.bouncy_grenades,False)
        elif self.gun_type == "Rocket Launcher":
            bullet = Rocket(48,angle,self.barrel_pos,1800,300)
        else:
            bullet = Bullet(-angle+spread,self)
        self.last_shot_time = time.time()
        return bullet

    def check_pick_up(self,player):
        if self.dropped == True:
            if self.collider_rect.colliderect(player.rect):
                return True
            else:
                return False

    def place_barrel(self,player,clock):
        if self.gun_type == "Rocket Launcher":
            if self.loaded_ammo == 1:
                self.barrel_offset = pygame.math.Vector2(32,0)
            else:
                self.barrel_offset = pygame.math.Vector2(16,-16)

        self.rot_barrel_offset = self.barrel_offset.rotate(player.facing+90)
        self.barrel_pos = self.rect.center + self.rot_barrel_offset


class Flamethrower(Better_Gun):
    def __init__(self,pos,image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil,fire_mode,barrel_offset):

        super().__init__(pos,image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil,fire_mode,barrel_offset)

    def check_shoot(self):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        return False

    def shoot2(self,blocks,player,enemies):
        for enemy in enemies:
            enemy_dist = pygame.math.Vector2(abs(enemy.rect.centerx-self.barrel_pos[0]),abs(enemy.rect.centery-self.barrel_pos[1]))
            if enemy_dist.length() <= 300:
                enemy_angle = player_to_enemy_angle(player,enemy)
                player_angle = find_player_angle(player)
                angle_diff = abs(enemy_angle - player_angle)
                if  angle_diff <= self.max_spread or angle_diff >= 360 - self.max_spread:
                    hit = raycast_to_entity(self.barrel_pos,blocks,300,enemy,player)
                    if hit: 
                        enemy.health -= 5
  
        
class Machine_Gun(Better_Gun):
    def __init__(self,pos,base_image,gun_image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil,fire_mode,barrel_offset):

        super().__init__(pos,gun_image,fire_rate,dmg,spread,spread_climb,
            max_loaded,max_reserve,gun_type,shot_quantity,speed,recoil,fire_mode,barrel_offset)
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
        if self.shot_from == "AK 47":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "M4":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (10*32): # 10 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "Pump Action Shotgun":
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

        if self.shot_from == "M1911":
            diffx = self.rect.centerx - self.origin[0]
            diffy = self.rect.centery - self.origin[1]
            self.dist = pygame.math.Vector2(diffx,diffy)
            if self.dist.length() > (15*32): # 15 blocks
                self.in_max_range = False
            if self.in_max_range == False:
                if self.dist.length() > (1*32): # 1 block
                    self.dmg -= 0.5
                    self.origin = self.rect.center

        if self.shot_from == "Pass":
            pass





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
        self.image = pygame.image.load("Guns Cropped/Rocket.png")
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
    def __init__(self,colour,lifespan,speed,pos,angle,spread,width,height,collision):
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
        self.can_collide = collision
        
    def update(self,blocks):
        self.rect.center += self.direction
        if self.can_collide:
            for block in blocks:
                if not block.can_move:
                    if self.rect.colliderect(block.rect):
                        return True
        self.current_time = time.time()
        if self.current_time - self.spawned > self.lifespan:
            return True
        return False


class Blood_Angle():
    def __init__(self,player_angle,shot_angle):
        self.blit_angle = shot_angle - player_angle + 180


class Grenade():
    def __init__(self,speed,angle,pos,dmg,blast_radius,bounce,flashbang):
        self.pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos[0],self.pos[1],24,24)
        self.image = pygame.image.load("grenade.png")
        self.speed = pygame.math.Vector2(speed,0)
        self.speed = self.speed.rotate(-angle)
        self.thrown_time = time.time()
        self.health = 1
        self.dmg = dmg
        self.blast_radius = blast_radius
        self.death_radius = 0
        self.bounce = bounce
        self.flashbang = flashbang

    def update_x(self,block_list):
        self.rect.x += self.speed.x
        
        for block in block_list:
            if block.can_move == False:
                collided = self.check_collision(block.rect)
                if collided:
                    if self.speed.x > 0:
                        self.rect.right = block.rect.left
                    elif self.speed.x < 0:
                        self.rect.left = block.rect.right
                    if self.bounce:
                        self.speed.x *= -1
                    else:
                        self.speed = pygame.math.Vector2(0,0)

    def update_y(self,block_list):
        self.rect.y += self.speed.y

        for block in block_list:
            if block.can_move == False:
                if self.rect.colliderect(block):
                    if self.speed.y < 0:
                        self.rect.top = block.rect.bottom
                    elif self.speed.y > 0:
                        self.rect.bottom = block.rect.top
                    if self.bounce:
                        self.speed.y *= -1
                    else:
                        self.speed = pygame.math.Vector2(0,0)
        
                
        new_length = self.speed.length() - 0.5
        if new_length > 0:
            self.speed.scale_to_length(new_length)
            return False
        elif new_length < 0:
            self.speed = pygame.math.Vector2(0,0)
            return True
        else:
            return True
                  
    def check_collision(self,entity):
        if self.rect.colliderect(entity):
            return True
        else:
            return False

    def explode(self,enemies,player,blocks):
        for enemy in enemies:
            enemy_dist = pygame.math.Vector2(abs(enemy.rect.centerx-self.rect.centerx),abs(enemy.rect.centery-self.rect.centery))
            if enemy_dist.length() <= self.blast_radius:
                can_hit = raycast_to_entity(self.rect.center,blocks,self.blast_radius,enemy,self)
                if can_hit:
                    if not self.flashbang:
                        enemy.health -= self.dmg/(enemy_dist.length()/4)
                    else:
                        enemy.blinded = True
                        enemy.blinded_at = time.time()
                            
        player_dist = pygame.math.Vector2(abs(player.rect.centerx-self.rect.centerx),abs(player.rect.centery-self.rect.centery))
        if player_dist.length() <= self.blast_radius:
            can_hit = raycast_to_entity(self.rect.center,blocks,self.blast_radius,player,self)
            if can_hit:
                if not self.flashbang:
                    player.health -= self.dmg/(player_dist.length()/4)
                else:
                    player.blinded = True
                    player.blinded_at = time.time()


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
        self.image = pygame.image.load("Environment/ammo pouch.png")

    def use(self,gun_options):
        for gun_option in gun_options:
            gun_option.loaded_ammo = gun_option.max_loaded
            gun_option.reserve_ammo = gun_option.max_reserve


class Medi_pouch(Takeable_Object):
    def __init__(self,rect):
        super().__init__(rect)
        self.can_move = True
        self.block_type = "Medi"
        self.image = pygame.image.load("Environment/medi pouch.png")

    def use(self,player):
        if player.rect.colliderect(self.rect):
            player.health = 100


class Upgrade(Takeable_Object):
    def __init__(self,upgrade_type,pos,image):
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.block_type = "Upgrade"
        self.type = upgrade_type
    
    def use(self,current_gun,player):
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
                
        elif self.type == "Flashbang":
            player.has_flash = True

