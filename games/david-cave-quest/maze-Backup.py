import pygame, sys, time



def DrawText(text, position):
   global screen, font
   font = pygame.font.SysFont("apple casual" , 50)
   text = font.render(text, 1,(255, 255, 255))
   screen.blit(text, position)
score = 0
pygame.init()
pygame.display.set_caption("Maze")
block_width = 64 
block_height = 64
print("HELLO!")
playerSprite = pygame.image.load("Sprite.png")
wallSprite = pygame.image.load("wall.png")
floorSprite = pygame.image.load("floor.png")
npcSprite = pygame.image.load("NPC.png")
exit_ = pygame.image.load("exit.png")

frameclock = pygame.time.Clock()
fallingSpeed = 1
jumpingTime = 0
restTime = 0

walls = []
floors = []
exits = []
levelone = [
   "################",
   "#o             #",
   "#              #",
   "#########      #",
   "#        #     #",
   "#x        #    #",
   "#######       ##",
   "#       ########",
   "#|      ########",
   "################",
    ]
level = levelone

levelloaded = False;

speed = [4, 4]

x_margin = 4
y_margin = 4


player_rect = pygame.Rect(0, 0, block_width, block_height)
player_start_rect = pygame.Rect(0, 0, block_width, block_height)

text_rect = pygame.Rect(0, 0, block_width, block_height)
#               |
#main game loop V
while True:
   if levelloaded == False:
      screen = pygame.display.set_mode ((level[0].__len__() * block_width, level.__len__() * block_height))

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
   if key[pygame.K_SPACE] and jumpingTime == 0:
      
#      move_rect[1] = move_rect[1] - speed[1]
      fallingSpeed = -16
      jumpingTime = 32
      

   if move_rect.collidelist(walls) == -1:     
      player_rect[0] = move_rect[0] - x_margin
      player_rect[1] = move_rect[1] - y_margin
      

      
   move_rect[1] = move_rect[1] + fallingSpeed
   if jumpingTime > 0:
      jumpingTime = jumpingTime - 1

   if move_rect.collidelist(walls) == -1:     
      player_rect[0] = move_rect[0] - x_margin
      player_rect[1] = move_rect[1] - y_margin
      if fallingSpeed < 16:
          fallingSpeed = fallingSpeed + 1
   else:
      fallingSpeed = 1

   if player_rect.colliderect(npc1):
      DrawText("You reached the exit!", text_rect)
   
      
 
   if player_rect.colliderect(exit_rect):
      player_rect[0] = player_start_rect[0]
      player_rect[1] = player_start_rect[1]

      DrawText("Press Space to jump!", text_rect)
      pygame.display.flip()
      time.sleep(3)
      score = score + 1
      #screen.text(text, 0, 0)

#   if player_rect.colliderect():      
#      screen.fill((100, 100, 100))
   
                               
 
   
   for floor_rect in floors:
      screen.blit(floorSprite, floor_rect)

   for wall in walls:
      screen.blit(wallSprite, wall)
   if player_rect.colliderect(npc1):
        DrawText("Press Space to jump!", text_rect)

   screen.blit(exit_, exit_rect)
   screen.blit(npcSprite, npc1)


   screen.blit(playerSprite, player_rect)
   DrawText("score: " + str(score), (0, 576))
   pygame.display.flip()
   frameclock.tick(30)
