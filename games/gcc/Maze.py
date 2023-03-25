import pygame, sys
screen = pygame.display.set_mode((640, 480))
pygame.init()
clock = pygame.time.Clock()

# Create map
walls = []
level = [
"##########",
"#x#      #",
"# # #### #",
"# # #    #",
"#   # ## #",
"##### ## #",
"#o       #",
"##########",
]

block_size = 64
player_rect = pygame.Rect(0,0, block_size, block_size)
exit_rect = pygame.Rect(0,0, block_size, block_size)

sprite = pygame.image.load("sprite.png")
wall_sprite = pygame.image.load("wall.png")
exit_sprite = pygame.image.load("exit.png")

font = pygame.font.SysFont("jingjing", 50)

# Fill the walls array with rectangles for each '#'
x = 0
y = 0
for row in level:
    for col in row:
        if col == "#":
            walls.append(pygame.Rect(x, y, block_size, block_size))

        # Set the player position if we find an 'o'
        if col == "o":
            player_rect = pygame.Rect(x, y, block_size, block_size)

        # Set the exit position if we find an 'x'
        if col == "x":
            exit_rect = pygame.Rect(x, y, block_size, block_size)
            
        x += block_size
    y += block_size
    x = 0

game_running = True;

while game_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Make a temporary marker of the player position        
    move_rect = player_rect

    # Read the keyboard input and move the marker
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        move_rect = move_rect.move(-2, 0)
    if key[pygame.K_RIGHT]:
        move_rect = move_rect.move(2, 0)
    # Only if the marker has not hit a wall do we update the player
    if move_rect.collidelist(walls) == -1:
        player_rect = move_rect

    move_rect = player_rect
    if key[pygame.K_UP]:
        move_rect = move_rect.move(0, -2)
    if key[pygame.K_DOWN]:
        move_rect = move_rect.move(0, 2)

    # Only if the marker has not hit a wall do we update the player
    if move_rect.collidelist(walls) == -1:
        player_rect = move_rect

    # Check if we have reached the exit
    if player_rect.colliderect(exit_rect):
            pygame.quit()
            sys.exit()

    # Draw the screen
    # Background
    screen.fill((70, 70, 190))
    
    # Walls
    for wall in walls:
        # shadow first...
        #pygame.draw.rect(screen, (50, 50, 170), wall.move(20, 20))
        # now the walls
        screen.blit(wall_sprite, wall)
        
    # Player
    screen.blit(sprite, player_rect)

    # Exit
    screen.blit(exit_sprite, exit_rect)

    text = font.render("Score " + str(clock.get_fps()), 1, (255, 255, 128))
    screen.blit(text, (130, 100))
    
    pygame.display.flip()

    # End of the while loop

