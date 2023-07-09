#################CONTROLS#############################
#
# WASD or arrow keys - movement
# Left click - shoot
# Aim with mouse
# Right click - grenade
# r - reload
# e - scroll through guns
# space - pick up ammo, med packs or guns
# q - drop gun (only works if you have more than one gun)
##################CHEAT CONTROLS##################### 
# j - respawn enemies
# p - refill ammo 
# k - heal fully
# m - player debug screen (not really a debug screen but its the best way I can describe it)
# n - rect debug screen
# b - enemy debug screen
#################IMPORTING STUFF#############################

import pygame
import Levels as levels
import Classes
import random
import time
import math

pygame.init()

game_running = True
game_state = "GAME"

clock = pygame.time.Clock()
myfont = pygame.font.SysFont("ariel",32)

####################LOADING IMAGES############################

top_or_bottom = pygame.image.load("top or bottom.png")
left_or_right = pygame.image.load("left or right.png")

#########CREATING THE OUTER WAlLS (THESE NEVER CHANGE)########
room = [pygame.Rect(16,16,1248,16),
        pygame.Rect(16,768,1248,16),
        pygame.Rect(16,16,16,768),
        pygame.Rect(1248,16,16,768)
        ]

#########CREATING THE GUNS####################################
gun_options = []
### gun class inits(firerate, dmg,spread,spread_climb,image,loaded ammo,reserve ammo,max loaded,max reserve,type,shot_quantity,bullet speed,recoil)

STAR = Classes.Better_Gun((-32,-32),pygame.image.load("gun.png"),0.2,20,5,0.5,25,100,"Starter AR",1,32,0.25)
Blank_Gun = Classes.Better_Gun((-32,-32),pygame.image.load("blank.png"),0,0,0,0,0,0,"None",0,0,0)
STAR.dropped = False
current_gun = STAR

##############CREATING THE PLAYER#############################

player = Classes.Player(pygame.Rect(704,32,64,64),12,100,10,pygame.image.load("player.png"))
player.inventory.append(STAR)

##############SETTING VARIABLES###############################
recoil = pygame.math.Vector2(0,0)
player_menu = False
rect_menu = False
enemy_menu = False
blown_up_bullet = False
blown_up_enemy = False
blown_up_player = False
shot = False
bullets = []
grenades = []
rockets = []
particles = []
explosion_colour_choices = [(255,102,0),(255,162,0),(255,68,0)]
block_collided_colour_choices = [(150,150,150),(86,86,86),(131,131,131)]
wall_collided_colour_choices  = [(200,200,200),(230,230,230),(255,255,255)]
blood_colour_choices = [(255,0,0),(227,0,0),(200,0,0)]
shoot_colour_choices = [(150,150,150),(86,86,86),(131,131,131),(255,162,0)]
casings_colour_choices = [(255,223,0),(212,175,55)]
Last_damged_by = "Nothing"
curr_inv_slot = 0
gren_slow_down = 0.75
angle = 0
current_level = 0
game_start_time = 0
game_end_time = 0
current_run_time = 0
shoot_time = 0
reload_time = 0
enemy_shoot_time = 0
nade_thrown_time = 0
gun_switch_time = 0
last_gun_switch_time = 0
score = 0
got_reload = False
reload_now = False

#######GRENADE AMMO#############

grenade_ammo = 5

###########GENERATING STARTING LEVEL#######

block_list = levels.load_level(levels.levels[current_level])
enemies = levels.get_enemies(levels.levels[current_level])
gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
ammo_list = levels.get_packs(levels.levels[current_level])
cleared_levels = []


screen = pygame.display.set_mode((1280,800))


game_start_time = time.time()
while game_running:
    current_run_time = time.time() - game_start_time
    ### MAIN GAME ###

    if game_state == "GAME":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            #####GRENADE DISTACE CHANGING KEYS##############

            #if event.type == pygame.MOUSEWHEEL:
             #   if gren_slow_down <= 1.5 and gren_slow_down >= 0.10:
              #      if event.y == 1:
               #         gren_slow_down -= 0.05

                #    if event.y == -1:
                 #       gren_slow_down += 0.05

                  #  gren_slow_down = round(gren_slow_down,2)
    
            if event.type == pygame.KEYDOWN:
                if gren_slow_down <= 1.5 and gren_slow_down >= 0.10:
                    if event.key == pygame.K_UP:
                        gren_slow_down -= 0.05
                
                    if event.key == pygame.K_DOWN:
                        gren_slow_down += 0.05

                    gren_slow_down = round(gren_slow_down,2)

                ##############CHEAT MENUS############
                if True:
                    if event.key == pygame.K_m:
                        if player_menu:
                            player_menu = False
                        else:
                            player_menu = True
                    
                    if event.key == pygame.K_n:
                        if rect_menu:
                            rect_menu = False
                        else:
                            rect_menu = True
                    
                    if event.key == pygame.K_b:
                        if enemy_menu:
                            enemy_menu = False
                        else:
                            enemy_menu = True
                    
                    if event.key == pygame.K_l:
                        if current_gun.has_laser:
                            if current_gun.laser_on:
                                current_gun.laser_on = False
                            else:
                                current_gun.laser_on = True
                        else:    
                            current_gun.laser_on = False

                    if event.key == pygame.K_o:
                        block_list = levels.load_level(levels.test_level)
                        enemies = levels.get_enemies(levels.test_level)
                        gun_list = levels.get_guns(levels.test_level,player.inventory)
                        ammo_list = levels.get_packs(levels.test_level)

                ###########DROP GUNS KEY###############

                if event.key == pygame.K_q:
                    if player.has_gun:
                        if len(player.inventory) > 1:
                            gun_item = current_gun
                            gun_item.dropped = True
                            gun_item.collider_rect.topleft = gun_item.rect.topleft
                            gun_list.append(gun_item)
                        
                            player.inventory.remove(current_gun)
                            if curr_inv_slot +1  < len(player.inventory):
                                pass
                            else:
                                curr_inv_slot = len(player.inventory)-1

                            current_gun = player.inventory[curr_inv_slot]

                        else:
                            gun_item = current_gun
                            gun_item.dropped = True
                            gun_item.collider_rect.topleft = gun_item.rect.topleft
                            gun_list.append(gun_item)
                            player.inventory.remove(current_gun)
                            player.has_gun = False
              
#################PLAYER BLOOD AND INVENTORY#################
        if True:
            if player.health == 100:
                player.shot = False
                player.shot_angles.clear()

            if player.shot:
                for shot_angle in player.shot_angles:
                    player.health -= 0.005
                    Last_damged_by = "Bleeding out"
                    for i in range(3):
                        angle = player.facing + shot_angle.blit_angle + 180
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.1,0.4)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(blood_colour_choices[colour_choice],lifespan,part_speed,player.rect.center,angle,20,8,8)
                        particles.append(particle)

            if len(player.inventory) == 0:
                player.has_gun = False
                current_gun = Blank_Gun
                
            else:
                player.has_gun = True
                for gun_option in gun_options:
                    if gun_option.type == player.inventory[curr_inv_slot]:
                        current_gun = gun_option
    
######################################ALL INPUTS HERE##########################

##########PLAYER MOVEMENT###############
                    
        keys = pygame.key.get_pressed()
        player.inputs(keys)
        
########CHEAT KEYS####################
        if True:
            if keys[pygame.K_p]:
                current_gun.loaded_ammo = current_gun.max_loaded
                current_gun.reserve_ammo = current_gun.max_reserve
                grenade_ammo = 5

            if keys[pygame.K_k]:
                player.health = 100
            
            if keys[pygame.K_j]:
                enemies = levels.get_enemies(levels.levels[current_level])
                gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
                ammo_list = levels.get_packs(levels.levels[current_level])

########CHANGING GUNS KEY############

        current_time = time.time()
        if keys[pygame.K_e]:
            if current_time - gun_switch_time > 0.25:
                gun_switch_time = time.time()
                if curr_inv_slot + 1 < len(player.inventory):
                    curr_inv_slot += 1
                    current_gun = player.inventory[curr_inv_slot]
                else:
                    curr_inv_slot = 0
                    current_gun = player.inventory[curr_inv_slot]
                    
#########PICK UP STUFF KEY#############

        if keys[pygame.K_SPACE]:
            for ammo_pack in ammo_list:
                if ammo_pack.block_type == "Ammo":
                    can_pick_up_ammo = ammo_pack.check_pick_up(player)
                    if can_pick_up_ammo == True:
                        ammo_pack.use(player.inventory)
                        grenade_ammo = 5

                        if ammo_pack in ammo_list:
                            ammo_list.remove(ammo_pack)
                            
                if ammo_pack.block_type == "Medi":
                    can_pick_up_medi = ammo_pack.check_pick_up(player)
                    if can_pick_up_medi == True:
                        ammo_pack.use(player)
                        if ammo_pack in ammo_list:
                            ammo_list.remove(ammo_pack)
                
                if ammo_pack.block_type == "Upgrade":
                    can_pick_up = ammo_pack.check_pick_up(player)
                    if can_pick_up == True:
                        ammo_pack.use(current_gun)
                        if ammo_pack in ammo_list:
                            ammo_list.remove(ammo_pack)
                        
            for gun_item in gun_list:
                can_pick_up_gun = gun_item.check_pick_up(player)
                if can_pick_up_gun == True:
                    if gun_item.gun_type not in player.inventory:
                        gun_item.dropped = False
                        player.inventory.append(gun_item)
                        if current_gun == Blank_Gun:
                            current_gun = player.inventory[curr_inv_slot]
                        if gun_item in gun_list:
                            gun_list.remove(gun_item)
                        score += 50   
        
###########RELAOD KEY##################

        start_time = time.time()
        if keys[pygame.K_r]:
            reload_now = True
            if current_gun.loaded_ammo < current_gun.max_loaded:
                if got_reload == False:
                    got_reload = True
                    reload_time = time.time()
        
        if start_time - reload_time > 0.5 and reload_now == True:
            loaded_diff = current_gun.max_loaded - current_gun.loaded_ammo
            current_gun.loaded_ammo = current_gun.max_loaded
            current_gun.reserve_ammo -= loaded_diff
            if current_gun.reserve_ammo < 0:
                current_gun.loaded_ammo += current_gun.reserve_ammo
                current_gun.reserve_ammo = 0
            got_reload = False
            reload_now = False
            
############GRENADE AND ROCKET MOVEMENT AND DAMAGE CHECKING################
        
        for grenade in grenades:
            for block in block_list:
                if block.can_move == False:
                    collided = grenade.check_collision(block.rect)
                    if collided:
                        check_health = player.health
                        grenade.explode(enemies,player)
                        if player.health < check_health:
                            Last_damged_by = "A Grenade"
                        for i in range(30):
                            colour_choice = random.randint(0,2)
                            lifespan = random.uniform(0.2,0.7)
                            part_speed = random.randint(6,10)
                            particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,grenade.rect.center,0,180,8,8)
                            particles.append(particle)
                        if grenade in grenades:
                            grenades.remove(grenade)

            for wall in room:
                collided = grenade.check_collision(wall)
                if collided:
                    check_health = player.health
                    grenade.explode(enemies,player)
                    if player.health < check_health:
                        Last_damged_by = "A Grenade"
                    for i in range(30):
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.2,0.7)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,grenade.rect.center,0,180,8,8)
                        particles.append(particle)
                    if grenade in grenades:
                        grenades.remove(grenade)

            new_length = grenade.update()
            if new_length <= 0:
                check_health = player.health
                grenade.explode(enemies,player)
                if player.health < check_health:
                    Last_damged_by = "A Grenade"
                for i in range(30):
                    colour_choice = random.randint(0,2)
                    lifespan = random.uniform(0.2,0.7)
                    part_speed = random.randint(6,10)
                    particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,grenade.rect.center,0,180,8,8)
                    particles.append(particle)
                if grenade in grenades:
                    grenades.remove(grenade)

        for bullet in bullets:
            bullet.move()
            bullet.dmg_reduce()
        
            ### checking for enemy damage ###

            if bullet.shot_from != "Enemy" and bullet.shot_from != "Heavy Enemy" and bullet.shot_from != "Machine Gun Enemy":
                for enemy in enemies:
                    collided = bullet.check_collision(enemy.rect)
                    if collided:
                        enemy.shot = True
                        enemy.shot_angles.append(Classes.Blood_Angle(player.facing,bullet.angle+180))
                        enemy.health -= bullet.dmg
                        if bullet in bullets:
                            bullets.remove(bullet)

            ### checking for player damage ### 

            if bullet.shot_from == "Enemy" or bullet.shot_from == "Heavy Enemy" or bullet.shot_from == "Machine Gun Enemy":
                collided = bullet.check_collision(player.rect)
                if collided:
                    player.shot = True
                    player.shot_angles.append(Classes.Blood_Angle(player.facing,bullet.angle+180))
                    player.health -= bullet.dmg
                    Last_damged_by = "Getting shot"
                    if bullet in bullets:
                        bullets.remove(bullet)


            ### checking for block and wall collisions ###

            for block in block_list:
                if block.can_move == False:
                    collided = bullet.check_collision(block.rect)
                    if collided:
                        for i in range(5):
                            colour_choice = random.randint(0,2)
                            lifespan = random.uniform(0.1,0.4)
                            part_speed = random.randint(6,10)
                            particle = Classes.Particle(block_collided_colour_choices[colour_choice],lifespan,part_speed,bullet.rect.center,bullet.angle+180,20,8,8)
                            particles.append(particle)
                        if bullet in bullets:
                            bullets.remove(bullet)

            for wall in room:
                collided = bullet.check_collision(wall)
                if collided:
                    for i in range(5):
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.1,0.4)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(wall_collided_colour_choices[colour_choice],lifespan,part_speed,bullet.rect.center,bullet.angle+180,20,8,8)
                        particles.append(particle)
                    if bullet in bullets:
                        bullets.remove(bullet)

        for rocket in rockets:
            rocket.update()
            
            for enemy in enemies:
                collided = rocket.check_collision(enemy.rect)
                if collided:
                    check_health = player.health
                    rocket.explode(enemies,player)
                    enemy.health -= rocket.dmg
                    if player.health < check_health:
                        Last_damged_by = "A Rocket"
                    for i in range(30):
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.2,0.7)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,rocket.rect.center,rocket.angle,20,8,8)
                        particles.append(particle)
                    if rocket in rockets:
                        rockets.remove(rocket)
            
            for wall in room:
                collided = rocket.check_collision(wall)
                if collided:
                    check_health = player.health
                    rocket.explode(enemies,player)
                    if player.health < check_health:
                        Last_damged_by = "A Rocket"
                    for i in range(30):
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.2,0.7)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,rocket.rect.center,rocket.angle,20,8,8)
                        particles.append(particle)
                    if rocket in rockets:
                        rockets.remove(rocket)
            
            for block in block_list:
                if not block.can_move:
                    collided = rocket.check_collision(block)
                    if collided:
                        check_health = player.health
                        rocket.explode(enemies,player)
                        if player.health < check_health:
                            Last_damged_by = "A Rocket"
                        for i in range(30):
                            colour_choice = random.randint(0,2)
                            lifespan = random.uniform(0.2,0.7)
                            part_speed = random.randint(6,10)
                            particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,rocket.rect.center,rocket.angle,20,8,8)
                            particles.append(particle)
                        if rocket in rockets:
                            rockets.remove(rocket)

#####################PLAYER SHOOTING####################
        current_gun.place_barrel(player)
        current_time = time.time()
        if pygame.mouse.get_pressed()[0] == 1:
            if player.has_gun:
                angle = -(Classes.find_player_angle(player))+90
                if current_time - gun_switch_time > 0.1:
                    if current_gun.loaded_ammo > 0:
                        
                        #### INCREASING SPREAD ####
                        if current_gun.gun_type != "Shotgun":
                            if current_gun.spread < current_gun.max_spread:
                                current_gun.spread += current_gun.spread_climb
                            else:
                                current_gun.spread = current_gun.max_spread
                        else:
                            current_gun.spread = current_gun.max_spread

                        if current_time - shoot_time > current_gun.fire_rate:    
                            if current_gun.gun_type == "Grenade Launcher":
                                ##### firing grenade launchers #####
                                grenade = Classes.Grenade(24,angle+180,current_gun.barrel_pos,1500,180,gren_slow_down)
                                grenade.death_radius = 60
                                grenades.append(grenade)
                                shot = True

                            elif current_gun.gun_type == "Rocket Launcher":
                                ##### firing rocket launchers #####
                                for i in range(15):
                                    ##### making the particles from firing #####
                                    lifespan = random.uniform(0.1,0.3)
                                    part_speed = random.randint(3,5)
                                    colour_choice = explosion_colour_choices[random.randint(0,2)]
                                    particle = Classes.Particle(colour_choice,lifespan,part_speed,current_gun.barrel_pos,-angle+180,10,8,8)
                                    particles.append(particle)
                                ##### making the rocket #####
                                rocket = Classes.Rocket(32,angle+180,current_gun.barrel_pos,1800,300)
                                rockets.append(rocket)
                                shot = True

                            elif current_gun.gun_type == "Sniper":
                                if player.direction == (0,0):
                                    for i in range(5):
                                        ##### making the particles from firing #####
                                        particle = Classes.make_particle(shoot_colour_choices,current_gun,angle)
                                        particles.append(particle)
                                    
                                    particle = Classes.casings(current_gun,casings_colour_choices,angle)
                                    if particle is not None:
                                        particles.append(particle)

                                    bullets.append(player.shoot(current_gun))
                                    shot = True
                            else:
                                ##### shooting for all other guns ##### 
                                for i in range(5):
                                    ##### making the particles from firing #####
                                    particle = Classes.make_particle(shoot_colour_choices,current_gun,angle)
                                    particles.append(particle)
                                
                                particle = Classes.casings(current_gun,casings_colour_choices,angle)
                                if particle is not None:
                                    particles.append(particle)
                                
                                for i in range(current_gun.shot_quantity):
                                    bullets.append(player.shoot(current_gun))
                                shot = True
                            
                            if shot == True:
                                shoot_time = time.time()
                                current_gun.loaded_ammo -= 1
                        
                                recoil = current_gun.recoil
                                recoil = recoil.rotate(-angle)
                                player.direction += recoil
                                shot = False

        else:
            current_shot_time = time.time()
            if current_shot_time - current_gun.last_shot_time > 0:
                if current_gun.spread > 0:
                    current_gun.spread -= 0.125

################GRENADE THROWNING#################
        if True:
            current_nade_time = time.time()
            if pygame.mouse.get_pressed()[2] == 1:
                if grenade_ammo >= 1:
                    if current_nade_time - nade_thrown_time > 1:
                        nade_thrown_time = time.time()
                        mouse = pygame.mouse.get_pos()
                        pos = player.rect.center
                        mdif = (mouse[0] - pos[0],pos[1] - mouse[1])
                        angle = math.degrees(math.atan2(mdif[1],mdif[0]))
                        spread = random.randint(-2,2)
                        grenade = Classes.Grenade(24,angle+spread,player.rect.center,1500,180,gren_slow_down)
                        grenade.rect.center = player.rect.center
                        grenade.death_radius = 60
                        grenades.append(grenade)
                        grenade_ammo -= 1

            ### grenade distance checking ###
            if current_gun.gun_type == "Grenade Launcher":
                gren_slow_down = min(gren_slow_down,1.50)
            else:
                gren_slow_down = min(gren_slow_down,1.00)

            if current_gun.gun_type == "Grenade Launcher":
                gren_slow_down = max(gren_slow_down,0.10)
            else:
                gren_slow_down = max(gren_slow_down,0.50)

            gren_speed = 24
            gren_dist = 0
            while gren_speed > 0:
                gren_dist += gren_speed
                gren_speed -= gren_slow_down
            gren_dist = round(gren_dist/32,2)

##############PLAYER MOVEMENT (including level changing and win condition)###########

        player.update_x(room,block_list)
        
        player.update_y(room,block_list)
                     
        #####################MOVING BETWEEN LEVELS#########################
        for block in block_list:
            if player.rect.colliderect(block.rect):
                if block.block_type == "down stairs" or block.block_type == "up stairs":
                    b = block.move_to_level(player.rect,current_level,levels.levels,levels.load_level)
                    if b is not None:
                        block_list = b
                        bullets.clear()
                        grenades.clear()
                        if block.block_type == "down stairs":
                            cleared_levels.append(levels.levels[current_level])
                            current_level += 1
                            if levels.levels[current_level] not in cleared_levels:
                                enemies = levels.get_enemies(levels.levels[current_level])
                                ammo_list = levels.get_packs(levels.levels[current_level])
                                gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
                            else:
                                enemies = levels.get_enemies(levels.blank_level)
                                ammo_list = levels.get_packs(levels.blank_level)
                                gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
                            
                        if block.block_type == "up stairs":
                            current_level -= 1
                            if levels.levels[current_level] not in cleared_levels:
                                enemies = levels.get_enemies(levels.levels[current_level])
                                ammo_list = levels.get_packs(levels.levels[current_level])
                                gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
                            else:
                                enemies = levels.get_enemies(levels.blank_level)
                                ammo_list = levels.get_packs(levels.blank_level)
                                gun_list = levels.get_guns(levels.levels[current_level],player.inventory)
                        
                if block.block_type == "Door":
                    check_win = block.check_win(player)
                    if check_win == True:
                        game_state = "VICTORY"

####################UPDATING PARTICLES###################

        for particle in particles:
            delete_particle = particle.update()
            if delete_particle == True:
                if particle in particles:
                    particles.remove(particle)

######################CHANGING THE IMAGE FOR THE ROCKET LAUNCHER###################

        if current_gun.gun_type == "Rocket Launcher":
            if current_gun.loaded_ammo == 0:
                current_gun.image = pygame.image.load("rpg unloaded.png")
                current_gun.rotational_offset = pygame.math.Vector2(-8, 6)
            else:
                current_gun.image = pygame.image.load("rpg loaded.png")
                current_gun.rotational_offset = pygame.math.Vector2(-8, 21)
        
        else:
            current_gun.rotational_offset = pygame.math.Vector2(-8, 20)

#############CHECKING ENEMY HEALTH ENEMY SHOOTING AND ENEMY BLOOD##################

        enemy_current_time = time.time()
        for enemy in enemies:
            enemy.gun.place_barrel(enemy)
            if enemy.health <= 0:
                if enemy in enemies:
                    enemies.remove(enemy)
                    if enemy.type == "enemy":
                        score += 100
                    elif enemy.type == "heavy enemy":
                        score += 250
                    else:
                        score += 120

            enemy.gun.spread = enemy.gun.max_spread
            if enemy_current_time - enemy.shoot_time > enemy.gun.fire_rate:
                enemy.shoot_time = time.time()
                if enemy.type == "grenade enemy":
                    grenades.append(enemy.shoot(player))
                else:
                    for i in range(5):
                        lifespan = random.uniform(0.1,0.3)
                        part_speed = random.randint(3,5)
                        colour_choice = shoot_colour_choices[random.randint(0,3)]
                        particle = Classes.Particle(colour_choice,lifespan,part_speed,enemy.gun.barrel_pos,enemy.facing+90,10,8,8)
                        particles.append(particle)

                    particle = Classes.casings(enemy.gun,casings_colour_choices,-enemy.facing+90)
                    if particle is not None:
                        particles.append(particle)
                    bullets.append(enemy.shoot(player))

            if enemy.shot == True:
                for shot_angle in enemy.shot_angles:
                    enemy.health -= 0.01
                    for i in range(3):
                        angle = enemy.facing + shot_angle.blit_angle
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.1,0.4)
                        part_speed = random.randint(6,10)
                        particle = Classes.Particle(blood_colour_choices[colour_choice],lifespan,part_speed,enemy.rect.center,angle,5,8,8)
                        particles.append(particle)

            if enemy.health == 100:
                enemy.shot = False
                enemy.shot_angles.clear()

######################MINE EXPLOSION CHECKING AND EXPLODING########################
    
        for block in  block_list:
            if block.block_type == "Mine":
                for enemy in enemies:
                    blown_up_enemy = block.explode_check(enemy)

                for bullet in bullets:
                    blown_up_bullet = block.explode_check(bullet)

                blown_up_player = block.explode_check(player)

                if blown_up_bullet == True or blown_up_enemy == True or blown_up_player == True:
                    for enemy in enemies:
                        block.explode(enemy)

                    for bullet in bullets:
                        block.explode(bullet)
                        if bullet.health <= 0:
                            if bullet in bullets:
                                bullets.remove(bullet)
                    check_health = player.health
                    block.explode(player)
                    for i in range(20):
                        colour_choice = random.randint(0,2)
                        lifespan = random.uniform(0.2,0.7)
                        part_speed = random.randint(5,12)
                        particle = Classes.Particle(explosion_colour_choices[colour_choice],lifespan,part_speed,block.rect.center,0,180,8,8)
                        particles.append(particle)
                    if player.health < check_health:
                        Last_damged_by = "A Mine"

                    tile = Classes.Obstacle(pygame.Rect(block.rect.x,block.rect.y,32,32),"floor",pygame.image.load("floor.png"),True)
                    block_list.remove(block)
                    block_list.append(tile)
                    blown_up_bullet = False
                    blown_up_enemy = False
                    blown_up_player = False

####################CHECKING PLAYER HEALTH#######################

        if player.health <= 0:
            game_state = "DEAD"

##########################DRAWING SECTION########################

        ### making the screen and making it light blue ###

        screen.fill((43, 252, 242))

        ### blitting (drawing) the room walls ###

        screen.blit(top_or_bottom,room[0]) #top wall
        screen.blit(top_or_bottom,room[1]) #bottom wall
        screen.blit(left_or_right,room[2]) #left wall
        screen.blit(left_or_right,room[3]) #right wall

        ### blitting the blocks, guns and packs ###

        for block in block_list:    
            screen.blit(block.image,block.rect)

        for gun_item in gun_list:
            screen.blit(gun_item.image,gun_item.rect)

        for ammo_pack in ammo_list:
            screen.blit(ammo_pack.image,ammo_pack.rect)

        ### creating the on-screen text ###
        
        mytext = myfont.render("Ammo: "+str(current_gun.loaded_ammo)+"   Reserve ammo: "+str(current_gun.reserve_ammo)+"   Gun type: "+current_gun.gun_type+"   Grenades: "+str(grenade_ammo)+"   Grenade throwning distance: "+str(gren_dist),1,(0,0,0))
        timer_text = myfont.render("Current time: "+str(round(current_run_time,2)),1,(0,0,0))
        myhealth = myfont.render("Health: "+ str(int(player.health)),1,(255,0,0))
        FPS = myfont.render("FPS: "+str(round(clock.get_fps(),2)),1,(0,0,0))
        
        for enemy in enemies:  
            enemy.enemy_text = myfont.render("Health: "+str(int(enemy.health)),1,(255,0,0))

        ### blitting the HUD ### 

        screen.blit(mytext,(0,0))
        screen.blit(timer_text,(33,8+mytext.get_height()))
        screen.blit(FPS,(33,8+mytext.get_height()+timer_text.get_height()))
        
        ### blitting the bullets, grenades and rockets ###

        for bullet in bullets:
            screen.blit(bullet.rotated_image,bullet.rect)

        for grenade in grenades:
            screen.blit(grenade.image,grenade.rect)

        for rocket in rockets:
            screen.blit(rocket.rotated_image,rocket.rect)

        ### blitting the particles ###

        for particle in particles:
            screen.blit(particle.image,particle.rect)

        ### blitting the enemies, their guns and their health text ###

        for enemy in enemies:
            if enemy.type == "machine enemy":
                enemy.rotimg, enemy.rotrect = enemy.rotate_gun(player)
                enemy.rotenimg,enemy.rotenrect = enemy.rotate_self(player)
                enemy.rect.center = enemy.gun.base_rect.center + pygame.math.Vector2(0,-80).rotate(enemy.facing)
                enemy.gun.rect.center = enemy.gun.base_rect.center
                screen.blit(enemy.gun.base_image,enemy.gun.base_rect)             
                screen.blit(enemy.rotimg,enemy.rotrect)
                screen.blit(enemy.rotenimg,enemy.rotenrect)                

            else:
                enemy.rotimg, enemy.rotrect = enemy.rotate_gun(player)
                enemy.rotenimg,enemy.rotenrect = enemy.rotate_self(player)
                screen.blit(enemy.rotenimg,enemy.rotenrect)
                screen.blit(enemy.rotimg,enemy.rotrect)

            screen.blit(enemy.enemy_text,(enemy.rect.centerx-(enemy.enemy_text.get_width()/2),enemy.rect.centery-64))

        ###  blitting the player, their gun and their health text ###
        
        
        rotplimg, rotplrect = player.rotate_self()
        screen.blit(rotplimg, rotplrect)

        if current_gun.has_laser and current_gun.laser_on:
            laser_end_point = Classes.laser(current_gun,room,block_list,player)
        
        if player.has_gun:    
            rotimg, rotrect = player.rotate_gun(current_gun)
        
        if current_gun.has_laser and current_gun.laser_on:
            pygame.draw.line(screen,(215,0,0),current_gun.rect.center,laser_end_point,2)

        if player.has_gun:    
            screen.blit(rotimg,rotrect)

        
        screen.blit(myhealth,(player.rect.centerx-(myhealth.get_width()/2),player.rect.centery-64))
        ### blitting the player,rect and enemy menus ###

        if player_menu:
            for block in block_list:
                if block.block_type == "Mine":
                    pygame.draw.circle(screen,(0,255,0),block.rect.center,block.blast_radius,1)
                    pygame.draw.circle(screen,(0,0,255),block.rect.center,block.death_radius,1)
            
            if current_gun.gun_type == "Pistol":
                pygame.draw.circle(screen,(255,0,0),player.rect.center,480,1)
            else:
                pygame.draw.circle(screen,(255,0,0),player.rect.center,320,1)

            for grenade in grenades:
                pygame.draw.circle(screen,(255,255,255),grenade.rect.center,grenade.blast_radius,1)
                pygame.draw.circle(screen,(0,0,255),grenade.rect.center,grenade.death_radius,1)

            for rocket in rockets:
                vectr1 = pygame.math.Vector2(rocket.blast_radius,0)
                vectr1 = vectr1.rotate(rocket.angle)
                vectr2 = vectr1.rotate(rocket.dmg_cone)
                vectr3 = vectr1.rotate(-rocket.dmg_cone)
                pygame.draw.line(screen,(0,0,255),rocket.rect.center,rocket.rect.center+vectr1,2)
                pygame.draw.line(screen,(0,0,255),rocket.rect.center,rocket.rect.center+vectr2,2)
                pygame.draw.line(screen,(0,0,255),rocket.rect.center,rocket.rect.center+vectr3,2)
            
            pygame.draw.line(screen,(255,255,255),player.rect.center,player.rect.center+(recoil*32),2)

            pygame.draw.circle(screen,(255,255,0),player.rect.center,int(gren_dist*32),1)
            mouse_pos = pygame.mouse.get_pos()
            vecto1 = pygame.math.Vector2(mouse_pos[0]-current_gun.barrel_pos[0],mouse_pos[1]-current_gun.barrel_pos[1])
            vecto2 = vecto1.rotate(current_gun.spread)
            vecto3 = vecto1.rotate(-current_gun.spread)
            pygame.draw.line(screen,(255,0,255),current_gun.barrel_pos,current_gun.barrel_pos+vecto1,2)
            pygame.draw.line(screen,(255,0,255),current_gun.barrel_pos,current_gun.barrel_pos+vecto2,2)
            pygame.draw.line(screen,(255,0,255),current_gun.barrel_pos,current_gun.barrel_pos+vecto3,2)
        
        if rect_menu:
            pygame.draw.rect(screen,(255,255,255),player.rect,1)
            pygame.draw.rect(screen,(255,255,255),current_gun.rect,1)
            
            for enemy in enemies:
                pygame.draw.rect(screen,(200,0,0),enemy.rect,1)
                pygame.draw.rect(screen,(255,255,255),enemy.gun.rect,1)
                if enemy.type == "machine enemy":
                    pygame.draw.rect(screen,(255,255,255),enemy.gun.base_rect,1)  
            
            for bullet in bullets:
                pygame.draw.rect(screen,(0,0,255),bullet.rect,1)
            
            for rocket in rockets:
                pygame.draw.rect(screen,(0,0,255),rocket.rect,1)
            
            for grenade in grenades:
                pygame.draw.rect(screen,(0,0,255),grenade.rect,1)

            for block in block_list:
                if block.block_type == "Mine":
                    pygame.draw.rect(screen,(0,0,0),block.rect,1)

            for pack in ammo_list:
                pygame.draw.rect(screen,(0,255,0),pack.rect,1)    
            
            for gun in gun_list:
                pygame.draw.rect(screen,(0,255,0),gun.collider_rect,1)

        if enemy_menu:
            for enemy in enemies:
                mouse_pos = player.rect.center
                vecto1 = pygame.math.Vector2(mouse_pos[0]-enemy.gun.rect.centerx,mouse_pos[1]-enemy.gun.rect.centery)
                vecto2 = vecto1.rotate(enemy.gun.spread)
                vecto3 = vecto1.rotate(-enemy.gun.spread)
                pygame.draw.line(screen,(255,0,100),enemy.gun.rect.center,enemy.gun.rect.center+vecto1,2)
                pygame.draw.line(screen,(255,0,100),enemy.gun.rect.center,enemy.gun.rect.center+vecto2,2)
                pygame.draw.line(screen,(255,0,100),enemy.gun.rect.center,enemy.gun.rect.center+vecto3,2)
                pygame.draw.line(screen,(0,0,0),enemy.gun.rect.center,player.rect.center,1)
     
    ### DEATH SCREEN ###

    if game_state == "DEAD":
        deathtext = myfont.render("You died by: "+Last_damged_by,1,(255,0,0))
        screen.blit(deathtext,((screen.get_width()/2)-(deathtext.get_width()/2),(screen.get_height()/2)-(deathtext.get_height()/2)))
        pygame.display.flip()
        time.sleep(2.5)
        game_running = False

    ### VICTORY SCREEN ###
        
    if game_state == "VICTORY":
        game_end_time = time.time()
        time_taken = round(game_end_time - game_start_time,2)
        score = int(score *player.health)
        score = round(score,0)
        
        file = open("times.txt","a")
        file.write(str(time_taken) + "\n")
        file.close()

        file1 = open("times.txt","r")
        file_times = file1.readlines()
        file1.close()

        file2 = open("scores.txt","a")
        file2.write(str(score) + "\n")
        file2.close()

        file3 = open("scores.txt","r")
        file_scores = file3.readlines()
        file3.close()

        fastest_time = 100000000
        for file_time in file_times:
            file_time = file_time.rstrip("\n")
            fastest_time = min(fastest_time,float(file_time))


        highest_score = 0
        for file_score in file_scores:
            file_score = file_score.rstrip("\n")
            highest_score = max(highest_score,int(float(file_score)))

        timevictorytext = myfont.render("You Win! Time: "+str(time_taken)+"s"+ " Fastest time: "+str(fastest_time)+"s",1,(0,255,0))
        scorevictorytext = myfont.render("Score: "+str(score)+" Highest Score: "+str(highest_score),1,(0,255,0))
        screen.blit(timevictorytext,((screen.get_width()/2)-(timevictorytext.get_width()/2),(screen.get_height()/2)-(timevictorytext.get_height()/2)))
        screen.blit(scorevictorytext,((screen.get_width()/2)-(scorevictorytext.get_width()/2),(screen.get_height()/2)-(scorevictorytext.get_height()/2)+timevictorytext.get_height()))
        pygame.display.flip()
        time.sleep(2.5)
        game_running = False

    #######SETTING THE FRAMERATE#########
    clock.tick(30)

########UPDATING THE DISPLAY#########
    pygame.display.flip()

pygame.quit()
