import pygame, sys, time

pygame.init()

block_width = 64
block_height = 64

playerSprite = pygame.image.load("Sprite.png")
wallSprite = pygame.image.load("wall.png")
floorSprite = pygame.image.load("floor.png")
npcSprite = pygame.image.load("NPC.png")
exitSprite = pygame.image.load("exit.png")

frameclock = pygame.time.Clock()
fallingSpeed = 1
jumpingTime = 0
restTime = 0

walls = []
floors = []
exits = []
levelone = [
   "###################",
   "#|||||||          #",
   "########          #",
   "#                 #",
   "#               x #",
   "#       # # #   ###",
   "######            #",
   "#     ######      #",
   "#           ####  #",
   "#########        ##",
   "#       ##    #####",
   "#    ##o    #     #",
   "###################",
    ]
leveltwo = [
   "##########",
   "#x       #",
   "######   #",
   "#        #",
   "#  #######",
   "#        #",
   "####    ##",
   "#|o   ####",
   "##########",
    ]
level = levelone

levelloaded = False;

speed = [4, 4]

x_margin = 4
y_margin = 4

onTheGround = 0

move_rect = pygame.Rect(0, 0, block_width - x_margin * 2, block_height - y_margin * 2)
move_rect_test = pygame.Rect(0, 0, block_width - x_margin * 2, block_height - y_margin * 2)
player_rect = pygame.Rect(0, 0, block_width, block_height)
player_start_rect = pygame.Rect(0, 0, block_width, block_height)

text_rect = pygame.Rect(0, 0, block_width, block_height)

#               |
#main game loop V
while True:
   if levelloaded == False:
      screen = pygame.display.set_mode ((level[0].__len__() * block_width, level.__len__() * block_height))

      onTheGround = 0
      floors = []
      walls = []
      x = y = 0
      for row in level:
         for col in row:
            if col == "#":
               walls.append(pygame.Rect(x, y, block_width, block_height))

            elif col == "o":
               floors.append(pygame.Rect(x, y, block_width, block_height))
               player_start_rect = pygame.Rect(x, y, block_width, block_height)
               player_rect[0] = player_start_rect[0]
               player_rect[1] = player_start_rect[1]
               move_rect = pygame.Rect(x, y, block_width - x_margin * 2, block_height - y_margin * 2)

            elif col == "|":
               floors.append(pygame.Rect(x, y, block_width, block_height))
               npc1 = pygame.Rect(x, y, block_width, block_height)
            elif col == "x":
               floors.append(pygame.Rect(x, y, block_width, block_height))
               exit_rect = pygame.Rect(x, y, block_width, block_height)
               
            else:
               floors.append(pygame.Rect(x, y, block_width, block_height))

            x += block_width
         y += block_height
         x = 0
      levelloaded = True
   
   for event in  pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()


   key = pygame.key.get_pressed()

   move_rect[0] = player_rect[0] + x_margin
   move_rect[1] = player_rect[1] + y_margin

   if key[pygame.K_RIGHT]:
      move_rect[0] = move_rect[0] + speed[0]
   if key[pygame.K_LEFT]:
      move_rect[0] = move_rect[0] - speed[0]
   if key[pygame.K_DOWN]:
      move_rect[1] = move_rect[1] + speed[1]
   #if key[pygame.K_UP] and jumpingTime == 0:
   if key[pygame.K_UP] and onTheGround == 1:
      
#      move_rect[1] = move_rect[1] - speed[1]
      fallingSpeed = -16
      jumpingTime = 17
      
   move_rect_test[0] = move_rect[0]
   move_rect_test[1] = player_rect[1]
   if move_rect_test.collidelist(walls) == -1:     
      player_rect[0] = move_rect[0] - x_margin

   move_rect_test[0] = player_rect[0]
   move_rect_test[1] = move_rect[1]
   if move_rect.collidelist(walls) == -1:     
      player_rect[1] = move_rect[1] - y_margin
      

   move_rect[0] = player_rect[0] + x_margin
   move_rect[1] = player_rect[1] + y_margin
      
   move_rect[1] = move_rect[1] + fallingSpeed
   if jumpingTime > 0:
      jumpingTime = jumpingTime - 1

   collidingWall = move_rect.collidelist(walls)
   if collidingWall == -1:
      onTheGround = 0
      player_rect[0] = move_rect[0] - x_margin
      player_rect[1] = move_rect[1] - y_margin
      if fallingSpeed < 16:
          fallingSpeed = fallingSpeed + 1
   else:
      if fallingSpeed > 1:
         move_rect[1] = move_rect[1] - fallingSpeed
         fallingSpeed = fallingSpeed - 1
         move_rect[1] = move_rect[1] + fallingSpeed
         while move_rect.colliderect(walls[collidingWall]):
            move_rect[1] = move_rect[1] - fallingSpeed
            fallingSpeed = fallingSpeed - 1
            move_rect[1] = move_rect[1] + fallingSpeed
         
         player_rect[0] = move_rect[0] - x_margin
         player_rect[1] = move_rect[1] - y_margin
         onTheGround = 1
      elif fallingSpeed > 0:
         fallingSpeed = 1
         onTheGround = 1
      else:
         fallingSpeed = 1

   if player_rect.colliderect(exit_rect):
      if level == levelone:
          level = leveltwo
      elif level == leveltwo:
          level = levelone
      levelloaded = False
   
   frameclock.tick(30)
                               
   screen.fill((100, 100, 100))

   for floor_rect in floors:
      screen.blit(floorSprite, floor_rect)

   for wall in walls:
      screen.blit(wallSprite, wall)

   screen.blit(exitSprite, exit_rect)

   screen.blit(npcSprite, npc1)

   screen.blit(playerSprite, player_rect)
   pygame.display.flip()

