import pygame

pygame.init()


screen = pygame.display.set_mode((1644,1000), 0, 32)


screen.fill((255, 255, 255))

game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
			
	pygame.display.update()
pygame.quit()
