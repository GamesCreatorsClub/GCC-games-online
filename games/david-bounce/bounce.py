import pygame, sys
pygame.init()

frameclock = pygame.time.Clock()

screen = pygame.display.set_mode ((512, 512))
size = width, hieght = 1024, 1024

ball = {
    "image": pygame.image.load("Ball.png"),
    "position": [200,500]

    }

while True:
   print (ball["position"][1])

   for event in  pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

   if ball["position"][1] < 1:
       ball["position"][1] = ball["position"][1] + 10
       print (ball["position"][1])

   
   screen.fill((0, 240, 255))
   screen.blit(ball["image"], ball["position"])
   frameclock.tick(30)
   pygame.display.flip()
   
