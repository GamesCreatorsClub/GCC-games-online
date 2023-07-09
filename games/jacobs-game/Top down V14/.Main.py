#################IMPORTING STUFF#############################

import pygame
import Levels as levels
import Classes
import random
import time
pygame.init()

#########PRINTING THE CONTROLS################################
print("\nControls:")
print("WASD - movement\nLeft click - shoot\nAim with mouse\nRight click - grenade\nup and down arrows - grenade throwing speed")
print("r - reload\ne - scroll through guns\nspace - pick up ammo, med packs or guns\nq - drop gun\nl - toggle laser\nv - toggle inpact grenades\nf - toggle flash grenades (temporary feature - will be changed)")

##############################################################
game_running = True
game_state = "GAME"

clock = pygame.time.Clock()
myfont = pygame.font.SysFont("ariel",32)

#########CREATING THE GUNS####################################
gun_options = []
### gun class inits(firerate, dmg,spread,spread_climb,image,loaded ammo,reserve ammo,max loaded,max reserve,type,shot_quantity,bullet speed,recoil)

#STAR = Classes.Better_Gun((-32,-32),pygame.image.load("Guns Cropped/AK 47.png"),0.2,20,5,0.5,25,100,"Starter AR",1,32,0.25,"Full Auto",(32,6))
Blank_Gun = Classes.Better_Gun((-32,-32),pygame.image.load("blank.png"),0,0,0,0,0,0,"None",0,0,0,"Unable To Fire",(0,0))
#STAR.dropped = False
current_gun = Blank_Gun

##############CREATING THE PLAYER#############################

player = Classes.Player(pygame.Rect(1194,32,51,51),12,100,10,pygame.image.load("Characters Cropped/Rifle Player.png"))
#player.inventory.append(STAR)

##############SETTING VARIABLES###############################
recoil = pygame.math.Vector2(0,0)
player_menu = False
rect_menu = False
enemy_menu = False
shot = False
cheat_mode = False
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
Last_damaged_by = "Nothing"
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
curr_emy = 0
V1 = V2 = V3 = (0,0)
got_reload = False
reload_now = False

#######GRENADE AMMO#############

grenade_ammo = 5

###########GENERATING STARTING LEVEL#######

block_list = levels.load_level(levels.levels[current_level])
enemies = levels.get_enemies(levels.levels[current_level])
gun_list = levels.get_guns(levels.levels[current_level])
ammo_list = levels.get_packs(levels.levels[current_level])
cleared_levels = []


screen = pygame.display.set_mode((1280,800))
flash_image = pygame.Surface((screen.get_width(),screen.get_height()))
flash_image.fill((255,255,255))
flash_image.set_alpha(255)
##################FOR A HARDER CHALLENGE GET RID OF THE OCTOTHROPE BELOW###############
#pygame.mouse.set_visible(False)
game_start_time = time.time()
while game_running:
    current_run_time = time.time() - game_start_time
    ### MAIN GAME ###
    if game_state == "GAME":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
            #####GRENADE DISTACE CHANGING KEYS##############
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                if player.gren_speed <= 48 and player.gren_speed >= 12:
                    if event.key == pygame.K_UP:
                        player.gren_speed += 2
                
                    if event.key == pygame.K_DOWN:
                        player.gren_speed -= 2

                if current_gun.gun_type == "Grenade Launcher":
                    if player.gren_speed > 48:
                        player.gren_speed = 48
                        
                    elif player.gren_speed < 12:
                        player.gren_speed = 12
                else:
                    if player.gren_speed > 36:
                        player.gren_speed = 36
                        
                    elif player.gren_speed < 12:
                        player.gren_speed = 12
                    
                if event.key == pygame.K_l:
                        if current_gun.has_laser:
                            if current_gun.laser_on:
                                current_gun.laser_on = False
                            else:
                                current_gun.laser_on = True
                        else:    
                            current_gun.laser_on = False

                if event.key == pygame.K_v:
                        if player.bouncy_grenades:
                            player.bouncy_grenades = False
                            
                        else:    
                            player.bouncy_grenades = True

                ##############CHEAT MENUS############
                if cheat_mode:
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
                    
                    if event.key == pygame.K_g:
                        current_level += 1
                        block_list = levels.load_level(levels.levels[current_level])
                        enemies = levels.get_enemies(levels.levels[current_level])
                        ammo_list = levels.get_packs(levels.levels[current_level])
                        gun_list = levels.get_guns(levels.levels[current_level])
                    
                    if event.key == pygame.K_o:
                        block_list = levels.load_level(levels.test_level)
                        enemies = levels.get_enemies(levels.test_level)
                        gun_list = levels.get_guns(levels.test_level)
                        ammo_list = levels.get_packs(levels.test_level)
                    
                    if event.key == pygame.K_0:
                        if curr_emy +1 < len(enemies):
                            curr_emy += 1
                        else:
                            curr_emy = 0
                    

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
                            
                if event.key == pygame.K_f:
                    if player.has_flash:
                        if player.flashbang:
                            player.flashbang = False
                        else:
                            player.flashbang  = True
              
#################PLAYER BLOOD AND INVENTORY#################
        if True:
            if player.health > 33:
                player.shot = False
                player.shot_angles.clear()
        
            if player.shot:
                for shot_angle in player.shot_angles:
                    player.health -= 0.005
                    Last_damaged_by = "Bleeding out"
                    angle = -player.facing + shot_angle.blit_angle
                    particle = Classes.make_particle(blood_colour_choices,player.rect.center,angle,10,0.1,0.3,3,5,True,8)
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
        if not cheat_mode:
            if keys[pygame.K_BACKSPACE]:
                if keys[pygame.K_RETURN]:
                    if keys[pygame.K_TAB]:
                        print("\nCheat Keys:")
                        print("j - respawn enemies\ng - moves onto next level\np - refill ammo\nk - heal fully(stops bleeding)")
                        print("m - player 'debug screen'\nn - rect 'debug screen'\nb - enemy 'debug screen'\n")
                        cheat_mode = True

        
        if cheat_mode:
            if keys[pygame.K_p]:
                current_gun.loaded_ammo = current_gun.max_loaded
                current_gun.reserve_ammo = current_gun.max_reserve
                grenade_ammo = 5

            if keys[pygame.K_k]:
                player.health = 100
            
            if keys[pygame.K_j]:
                enemies = levels.get_enemies(levels.levels[current_level])
                gun_list = levels.get_guns(levels.levels[current_level])
                ammo_list = levels.get_packs(levels.levels[current_level])

########CHANGING GUNS KEY############

        current_time = time.time()
        if keys[pygame.K_e]:
            if len(player.inventory) > 0:
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
                        ammo_pack.use(current_gun,player)
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
            grenade.update_x(block_list)
            explode = grenade.update_y(block_list)
            if explode:
                health_check = player.health
                grenade.explode(enemies,player,block_list)
                if health_check > player.health:
                    Last_damaged_by = "A Grenade"
                if pygame.math.Vector2(player.rect.x - grenade.rect.x, player.rect.y - grenade.rect.y).length() < grenade.blast_radius:
                    flash_brightness = 255
                    
                    
                for i in range(30):
                    particle = Classes.make_particle(explosion_colour_choices,grenade.rect.center,180,180,0.1,0.3,3,5,True,8)
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
                        enemy.shot_angles.append(Classes.Blood_Angle(player.facing,bullet.angle+90))
                        enemy.health -= bullet.dmg
                        if bullet in bullets:
                            bullets.remove(bullet)

            ### checking for player damage ### 

            if bullet.shot_from == "Enemy" or bullet.shot_from == "Heavy Enemy" or bullet.shot_from == "Machine Gun Enemy":
                collided = bullet.check_collision(player.rect)
                if collided:
                    player.shot = True
                    player.shot_angles.append(Classes.Blood_Angle(player.facing,-bullet.angle))
                    player.health -= bullet.dmg
                    Last_damaged_by = "Getting shot"
                    if bullet in bullets:
                        bullets.remove(bullet)


            ### checking for block and wall collisions ###

            for block in block_list:
                if block.can_move == False:
                    collided = bullet.check_collision(block.rect)
                    if collided:
                        for i in range(10):
                            particle = Classes.make_particle(block_collided_colour_choices,bullet.rect.center,-bullet.angle,20,0.1,0.3,3,5,False,6)
                            particles.append(particle)
                        if bullet in bullets:
                            bullets.remove(bullet)

            if bullet.rect.x < -32 or bullet.rect.x > screen.get_width():
                if bullet in bullets:
                    bullets.remove(bullet)
                    
            if bullet.rect.y < -32 or bullet.rect.y > screen.get_height():
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
                        Last_damaged_by = "A Rocket"
                    for i in range(30):
                        particle = Classes.make_particle(explosion_colour_choices,rocket.rect.center,-rocket.angle,20,0.1,0.3,3,5,False,8)
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
                            Last_damaged_by = "A Rocket"
                        for i in range(30):
                            particle = Classes.make_particle(explosion_colour_choices,rocket.rect.center,rocket.angle,20,0.1,0.3,3,5,False,8)
                            particles.append(particle)
                        if rocket in rockets:
                            rockets.remove(rocket)

#####################PLAYER SHOOTING####################
        current_gun.place_barrel(player,clock)
        can_shoot = current_gun.check_shoot()
        if can_shoot:
            if player.has_gun:
                gun_wall_clip = Classes.check_gun_collide(current_gun,block_list)
                if not gun_wall_clip:
                    angle = -Classes.find_player_angle(player)
                    if current_time - gun_switch_time > 0.1:
                        if current_gun.loaded_ammo > 0:
                            if current_gun.gun_type == "Grenade Launcher":
                                grenade = current_gun.shoot(-angle,player)
                                grenades.append(grenade)
                                current_gun.loaded_ammo -= 1

                            elif current_gun.gun_type == "Rocket Launcher":
                                rocket = current_gun.shoot(-angle,player)
                                rockets.append(rocket)
                                current_gun.loaded_ammo -= 1
                                for i in range(15):                        
                                    particle = Classes.make_particle(explosion_colour_choices,current_gun.barrel_pos,angle,20,0.1,0.3,3,5,True,8)
                                    particles.append(particle)

                            elif current_gun.gun_type == "Flamethrower":
                                current_gun.shoot2(block_list,player,enemies)
                                current_gun.loaded_ammo -= 0.125
                                for i in range(20):
                                    particle = Classes.make_particle(explosion_colour_choices,current_gun.barrel_pos,-angle+180,current_gun.max_spread,0.3,0.7,12,20,True,8)
                                    particles.append(particle)
                                
                            else:
                                for i in range(current_gun.shot_quantity):
                                    bullet = current_gun.shoot(angle,player)
                                    bullets.append(bullet)
                                current_gun.loaded_ammo -= 1
                                for i in range(15):                        
                                    particle = Classes.make_particle(shoot_colour_choices,current_gun.barrel_pos,-angle+180,20,0.1,0.3,3,5,True,4)
                                    particles.append(particle)
                                casing = Classes.casings(current_gun,casings_colour_choices,-angle+180)
                                particles.append(casing)

################GRENADE THROWNING#################
        if True:
            current_nade_time = time.time()
            if pygame.mouse.get_pressed()[2] == 1:
                if grenade_ammo >= 1:
                    if current_nade_time - nade_thrown_time > 1:
                        nade_thrown_time = time.time()
                        angle = Classes.find_player_angle(player)-180
                        spread = random.randint(-2,2)
                        grenade = Classes.Grenade(player.gren_speed,angle+spread+180,player.rect.center,1500,180,player.bouncy_grenades,player.flashbang)
                        grenade.rect.center = player.rect.center
                        grenade.death_radius = 60
                        grenades.append(grenade)
                        grenade_ammo -= 1

##############PLAYER MOVEMENT (including level changing and win condition)###########

        player.update_x(block_list)
        
        player.update_y(block_list)
                     
        #####################MOVING BETWEEN LEVELS#########################
        if len(enemies) == 0:
            cleared_levels.append(levels.levels[current_level])
            
        for block in block_list:
            if block.block_type == "down stairs" or block.block_type == "up stairs":
                if player.rect.colliderect(block.rect):
                    bullets.clear()
                    grenades.clear()
                    if block.block_type == "down stairs":
                        cleared_levels.append(levels.levels[current_level])
                        current_level += 1
                        if current_level < len(levels.levels):
                            block_list = levels.load_level(levels.levels[current_level])
                            player.rect.x = 1184
                            if levels.levels[current_level] not in cleared_levels:
                                enemies = levels.get_enemies(levels.levels[current_level])
                                ammo_list = levels.get_packs(levels.levels[current_level])
                                gun_list = levels.get_guns(levels.levels[current_level])
                            else:
                                enemies = levels.get_enemies(levels.blank_level)
                                ammo_list = levels.get_packs(levels.blank_level)
                                gun_list = levels.get_guns(levels.levels[current_level])

                        else:
                            game_state = "VICTORY"
                            
                    if block.block_type == "up stairs":
                        current_level -= 1
                        if current_level < len(levels.levels):
                            block_list = levels.load_level(levels.levels[current_level])
                            player.rect.x = 32
                            if levels.levels[current_level] not in cleared_levels:
                                enemies = levels.get_enemies(levels.levels[current_level])
                                ammo_list = levels.get_packs(levels.levels[current_level])
                                gun_list = levels.get_guns(levels.levels[current_level])
                            else:
                                enemies = levels.get_enemies(levels.blank_level)
                                ammo_list = levels.get_packs(levels.blank_level)
                                gun_list = levels.get_guns(levels.levels[current_level])
                        
####################UPDATING PARTICLES###################

        for particle in particles:
            delete_particle = particle.update(block_list)
            if delete_particle == True:
                if particle in particles:
                    particles.remove(particle)

######################CHANGING THE IMAGE FOR THE ROCKET LAUNCHER###################

        if current_gun.gun_type == "Rocket Launcher":
            if current_gun.loaded_ammo == 0:
                current_gun.image = pygame.transform.rotate(pygame.image.load("Guns Cropped/Rocket Launcher Unloaded.png"),45)
                current_gun.rotational_offset = pygame.math.Vector2(-4, 6)
            else:
                current_gun.image = pygame.image.load("Guns Cropped/Rocket Launcher Loaded.png")
                current_gun.rotational_offset = pygame.math.Vector2(1, 6)
        
        elif current_gun.gun_type == "Flamethrower":
            current_gun.rotational_offset = pygame.math.Vector2(-5,28)
        
        else:
            current_gun.rotational_offset = pygame.math.Vector2(-5, 21)

#############CHANGING PLAYER IMAGE DEPENDING ON THE GUN############################
        if current_gun.gun_type == "Rocket Launcher" or current_gun.gun_type == "Flamethrower":
            player.image = pygame.image.load("Characters Cropped/Heavy Player.png")
        
        else:
            player.image = pygame.image.load("Characters Cropped/Rifle Player.png")

#############CHECKING ENEMY HEALTH ENEMY SHOOTING AND ENEMY BLOOD##################
        enemy_current_time = time.time()
        for enemy in enemies:
            if enemy.type == "patrol enemy":
                enemy.move()
            enemy.gun.place_barrel(enemy,clock)
            if enemy.health <= 0:
                if enemy in enemies:
                    enemies.remove(enemy)
                    gun = enemy.drop_item()
                    if gun is not None:
                        gun_list.append(gun)
            
            enemy.gun.spread = enemy.gun.max_spread
            enemy_can_see = enemy.shoot_check(player,block_list)
            if enemy_can_see:
                enemy_gun_wall_clip = Classes.check_gun_collide(enemy.gun,block_list)
                if not enemy_gun_wall_clip:
                    if enemy_current_time - enemy.shoot_time > enemy.gun.fire_rate:
                        enemy.shoot_time = time.time()
                        if enemy.type == "grenade enemy":
                            enemy.gren_speed = random.randint(18,30)
                            grenades.append(enemy.gun.shoot(-enemy.facing-90,enemy))
                        else:
                            for i in range(5):
                                particle = Classes.make_particle(shoot_colour_choices,enemy.gun.barrel_pos,-enemy.facing+90,10,0.1,0.3,3,5,False,4)
                                particles.append(particle)

                            particle = Classes.casings(enemy.gun,casings_colour_choices,-enemy.facing+90)
                            if particle is not None:
                                particles.append(particle)
                            if enemy.gun.gun_type == "Heavy Enemy":
                                if enemy.gun.fire_rate == 1:
                                    enemy.gun.fire_rate = 0.1
                                    enemy.gun.barrel_offset = pygame.math.Vector2(28,-6)
                                else:
                                    enemy.gun.fire_rate = 1
                                    enemy.gun.barrel_offset = pygame.math.Vector2(28,6)
                            bullets.append(enemy.gun.shoot(enemy.facing+90,enemy))

            if enemy.shot:
                for shot_angle in enemy.shot_angles:
                    enemy.health -= 0.01
                    angle = -enemy.facing + shot_angle.blit_angle + 90
                    particle = Classes.make_particle(blood_colour_choices,enemy.rect.center,angle,20,0.1,0.3,3,5,True,8)
                    particles.append(particle)
                    particles.append(particle)

            if enemy.health == 100:
                enemy.shot = False
                enemy.shot_angles.clear()

######################MINE EXPLOSION CHECKING AND EXPLODING########################
    
        for block in  block_list:
            if block.block_type == "Mine":
                explode_check = block.explode_check(bullets,enemies,player)
                if explode_check:
                    check_health = player.health
                    block.explode(enemies,player,block_list,bullets)
                    for i in range(20):
                        particle = Classes.make_particle(explosion_colour_choices,block.rect.center,0,180,0.3,0.6,3,5,False,8)
                        particles.append(particle)
                    if player.health < check_health:
                        Last_damaged_by = "A Mine"                    
                    block_list.remove(block)

####################CHECKING PLAYER HEALTH#######################

        if player.health <= 0:
            game_state = "DEAD"
            player.health = 0

##########################DRAWING SECTION########################

        ### making the screen and making it brown ###

        screen.fill((125, 74, 46))
        
        ### blitting the blocks, guns and packs ###

        for block in block_list:    
            screen.blit(block.image,block.rect)

        for gun_item in gun_list:
            screen.blit(gun_item.image,gun_item.rect)

        for ammo_pack in ammo_list:
            screen.blit(ammo_pack.image,ammo_pack.rect)

        ### creating the on-screen text ###
        
        mytext = myfont.render("Ammo: "+str(int(current_gun.loaded_ammo))+"   Reserve ammo: "+str(current_gun.reserve_ammo)+"   Gun type: "+current_gun.gun_type+"   Current Level: "+str(current_level+1),1,(255,255,255))
        mytext.set_alpha(128)
        grenade_text = myfont.render("Grenades: "+str(grenade_ammo)+"   Grenade speed: "+str(player.gren_speed)+"   Flashbang: "+str(player.flashbang),1,(255,255,255))
        timer_text = myfont.render("Current time: "+str(round(current_run_time,2)),1,(255,255,255))
        FPS = myfont.render("FPS: "+str(round(clock.get_fps(),2)),1,(255,255,255))
        
        ### blitting the HUD ### 

        screen.blit(mytext,(1,1))
        screen.blit(grenade_text,(1,9+mytext.get_height()))
        screen.blit(timer_text,(1,9+mytext.get_height()+grenade_text.get_height()))
        screen.blit(FPS,(1,9+mytext.get_height()+timer_text.get_height()+grenade_text.get_height()))
        
        for enemy in enemies:
            image1 = pygame.Surface((1,8))
            if enemy.health > 66:
                image1.fill((0,255,0))
            elif enemy.health <= 66 and enemy.health > 33:
                image1.fill((255,215,0))
            else:
                image1.fill((255,0,0))
            image1 = pygame.transform.scale(image1,(int(75*(enemy.health/enemy.max_health)),8))
            rect1 = pygame.Rect(enemy.rect.centerx-(38.5),enemy.rect.centery-49,77,10)
            screen.blit(image1,(enemy.rect.centerx-(37.5),enemy.rect.centery-48))
            pygame.draw.rect(screen,(0,0,0),rect1,3)
           
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

          
        ###  blitting the player, their gun and their health text ###
        
        if current_gun.gun_type != "Flamethrower":
            rotplimg, rotplrect = player.rotate_self()
            screen.blit(rotplimg, rotplrect)

        if current_gun.has_laser and current_gun.laser_on:
            laser_end_point = Classes.laser2(current_gun,block_list,player,1000000,0,enemies,True)
        
        if player.has_gun:    
            rotimg, rotrect = player.rotate_gun(current_gun)
        
        if current_gun.has_laser and current_gun.laser_on:
            pygame.draw.line(screen,(215,0,0),current_gun.rect.center,laser_end_point,2)

        if player.has_gun:    
            screen.blit(rotimg,rotrect)
        
        if current_gun.gun_type == "Flamethrower":
            rotplimg, rotplrect = player.rotate_self()
            screen.blit(rotplimg, rotplrect)
            
        image1 = pygame.Surface((1,8))
        if player.health > 66:
            image1.fill((0,255,0))
        elif player.health <= 66 and player.health > 33:
            image1.fill((255,215,0))
        else:
            image1.fill((255,0,0))
        image1 = pygame.transform.scale(image1,(int(75*(player.health/100)),8))
        rect1 = pygame.Rect(player.rect.centerx-(38.5),player.rect.centery-49,77,10)        
        screen.blit(image1,(player.rect.centerx-(37.5),player.rect.centery-48))
        pygame.draw.rect(screen,(0,0,0),rect1,3)
        
        if curr_emy +1 > len(enemies):
            curr_emy = 0
        
        if player.blinded:
            flash_image.set_alpha(flash_brightness)
            screen.blit(flash_image,(0,0))
            if time.time() - player.blinded_at > 1:
                flash_brightness -= 1
            
        if player_menu:
            if current_gun.gun_type == "Flame thrower":
                V1 = current_gun.barrel_pos
                V2 = Classes.laser2(current_gun,block_list,player,300,-current_gun.max_spread,enemies,False)
                V3 = Classes.laser2(current_gun,block_list,player,300,current_gun.max_spread,enemies,False)#leftmost on bottom
                pygame.draw.line(screen,(100,0,10),V1,V2,1)
                pygame.draw.line(screen,(100,0,10),V1,V3,1)
                pygame.draw.line(screen,(100,0,10),V2,V3,1)
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
            check_rect1 = pygame.Rect(current_gun.rect.center[0],current_gun.rect.center[1],1,1)
            check_rect2 = pygame.Rect(current_gun.barrel_pos[0],current_gun.barrel_pos[1],1,1)
            check_rect3 = pygame.Rect((current_gun.barrel_pos[0]+current_gun.rect.center[0])/2,(current_gun.barrel_pos[1]+current_gun.rect.center[1])/2,1,1)
            screen.blit(pygame.image.load("barrel test.png"),check_rect1)
            screen.blit(pygame.image.load("barrel test.png"),check_rect2)
            screen.blit(pygame.image.load("barrel test.png"),check_rect3)
            if len(enemies) != 0:      
                pygame.draw.rect(screen,(10,200,0),enemies[curr_emy].rect,2)

            for enemy in enemies:
                pygame.draw.rect(screen,(200,0,0),enemy.rect,1)
                pygame.draw.rect(screen,(255,255,255),enemy.gun.rect,1)
                check_rect1 = pygame.Rect(enemy.gun.rect.center[0],enemy.gun.rect.center[1],1,1)
                check_rect2 = pygame.Rect(enemy.gun.barrel_pos[0],enemy.gun.barrel_pos[1],1,1)
                check_rect3 = pygame.Rect((enemy.gun.barrel_pos[0]+enemy.gun.rect.center[0])/2,(enemy.gun.barrel_pos[1]+enemy.gun.rect.center[1])/2,1,1)
                screen.blit(pygame.image.load("barrel test.png"),check_rect1)
                screen.blit(pygame.image.load("barrel test.png"),check_rect2)
                screen.blit(pygame.image.load("barrel test.png"),check_rect3)
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
                    pass
                pygame.draw.rect(screen,(255,255,255),block.rect,1)

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
        deathtext = myfont.render("You died by: "+Last_damaged_by,1,(255,0,0))
        screen.blit(deathtext,((screen.get_width()/2)-(deathtext.get_width()/2),(screen.get_height()/2)-(deathtext.get_height()/2)))
        pygame.display.flip()
        time.sleep(2.5)
        game_running = False

    ### VICTORY SCREEN ###
        
    if game_state == "VICTORY":
        game_end_time = time.time()
        time_taken = round(game_end_time - game_start_time,2)
    
        
        file = open("times.txt","a")
        file.write(str(time_taken) + "\n")
        file.close()

        file1 = open("times.txt","r")
        file_times = file1.readlines()
        file1.close()

        fastest_time = 100000000
        for file_time in file_times:
            file_time = file_time.rstrip("\n")
            fastest_time = min(fastest_time,float(file_time))

        timevictorytext = myfont.render("You Win! Time: "+str(time_taken)+"s"+ " Fastest time: "+str(fastest_time)+"s",1,(0,255,0))
        screen.blit(timevictorytext,((screen.get_width()/2)-(timevictorytext.get_width()/2),(screen.get_height()/2)-(timevictorytext.get_height()/2)))
        pygame.display.flip()
        time.sleep(2.5)
        game_running = False

    #######SETTING THE FRAMERATE#########
    clock.tick(30)
    
########UPDATING THE DISPLAY#########
    pygame.display.flip()

pygame.quit()
