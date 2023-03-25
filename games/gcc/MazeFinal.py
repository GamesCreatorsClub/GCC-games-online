import pygame, sys, random
screen = pygame.display.set_mode((640, 480))
pygame.init()

# Create map
walls = []
level = [
"####################",
"#       E#         #",
"# ###### # ####### #",
"# #              # #",
"#   ############   #",
"# # #          # # #",
"#     ### ####     #",
"# ### #     x# ### #",
"#   # ######## #   #",
"# #              # #",
"#   ############   #",
"# #              # #",
"# ####### # ###### #",
"#o        #        #",
"####################",
]

block_size = 32
player_start_rect = pygame.Rect(0,0, block_size, block_size)
exit_rect = pygame.Rect(0,0, block_size, block_size)
enemy_start_rect = pygame.Rect(0,0, block_size, block_size)
enemy2_start_rect = pygame.Rect(0,0, block_size, block_size)
player_sprite = pygame.image.load("sprite_32.png")
wall_sprite = pygame.image.load("wall_32.png")
exit_sprite = pygame.image.load("exit_32.png")
enemy_sprite = pygame.image.load("enemy_32.png")

# Fill the walls array with rectangles for each '#'
x = 0
y = 0
for row in level:
    for col in row:
        if col == "#":
            walls.append(pygame.Rect(x, y, block_size, block_size))

        # Set the player position if we find an 'o'
        if col == "o":
            player_start_rect = pygame.Rect(x, y, block_size - 10, block_size - 10)

        # Set the exit position if we find an 'x'
        if col == "x":
            exit_rect = pygame.Rect(x, y, block_size, block_size)

        # Set the enemy position if we find an 'E'
        if col == "E":
            enemy_start_rect = pygame.Rect(x, y, block_size, block_size)
            
        x += block_size
    y += block_size
    x = 0

game_state = 0;
enemy_direction = [0,1]
player_rect = player_start_rect
enemy_rect = enemy_start_rect
font = pygame.font.SysFont("jingjing", 50)

while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    key = pygame.key.get_pressed()

    if game_state == 0:
        # Make a temporary marker of the player position        
        player_move_rect = player_rect

        speed = 4
        enemy_speed = 4

        # update the enemy move rectangle according to direction & speed
        enemy_move_rect = enemy_rect.move(enemy_direction[0] * enemy_speed, enemy_direction[1] * enemy_speed)

        # Read the keyboard input and move the marker
        if key[pygame.K_LEFT]:
            player_move_rect = player_move_rect.move(-speed, 0)
        if key[pygame.K_RIGHT]:
            player_move_rect = player_move_rect.move(speed, 0)
        if key[pygame.K_UP]:
            player_move_rect = player_move_rect.move(0, -speed)
        if key[pygame.K_DOWN]:
            player_move_rect = player_move_rect.move(0, speed)

        # Only if the marker has not hit a wall do we update the player
        if player_move_rect.collidelist(walls) == -1:
            player_rect = player_move_rect

        # If the enemy has hit a wall, generate a new direction
        if enemy_move_rect.collidelist(walls) != -1:
            random_direction = random.randint(0, 3)
            if random_direction == 0:
                enemy_direction = [0,1] # down
            elif random_direction == 1:
                enemy_direction = [0,-1] # up
            elif random_direction == 2:
                enemy_direction = [1,0] # right
            elif random_direction == 3:
                enemy_direction = [-1,0] # left
        
        else:
            enemy_rect = enemy_move_rect
        
        # Check if we have reached the exit
        if player_rect.colliderect(exit_rect):
            game_state = 1;

        if player_rect.colliderect(enemy_rect):
            game_state = 2;

        # Draw the screen
        # Background
        screen.fill((70, 70, 190))

        # Walls
        for wall in walls:
            # shadow first...
            pygame.draw.rect(screen, (50, 50, 170), wall.move(20, 20))
            # now the walls
            screen.blit(wall_sprite, wall)
            
        # Player
        screen.blit(player_sprite, player_rect)

        # Exit
        screen.blit(exit_sprite, exit_rect)

        # Enemy
        screen.blit(enemy_sprite, enemy_rect)
        screen.blit(enemy_sprite, enemy_rect)
    elif game_state == 1:
        text = font.render("You Made It!", 1, (255, 255, 128))

        screen.fill((0, 128, 0))
        screen.blit(text, (130, 100))
        if key[pygame.K_SPACE]:
            game_state = 0
            player_rect = player_start_rect
            enemy_rect = enemy_start_rect

    elif game_state == 2:
        text = font.render("Oh No - You Lose!", 1, (255, 255, 128))

        screen.fill((128, 0, 0))
        screen.blit(text, (90, 100))
        if key[pygame.K_SPACE]:
            game_state = 0
            player_rect = player_start_rect
            enemy_rect = enemy_start_rect

    pygame.display.flip()
    # End of the while loop


