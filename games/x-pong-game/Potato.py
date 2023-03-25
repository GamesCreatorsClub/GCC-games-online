import sys, pygame
pygame.init()

alpha=0

size = width, height = 700, 600

player_left_score=0
player_right_score=0

velocity = [5, -3 ]


black = (255, 255, 255)

pygame.mixer.init(frequency=22050, size=-16, channels=8, buffer=4096)
pygame.mixer.set_num_channels(8)
music_sound = pygame.mixer.Sound("song.wav")

screen = pygame.display.set_mode(size)

score_font=pygame.font.SysFont("badaboombb",40)

background = pygame.image.load("background.png")

sprite = pygame.image.load("sprite.png")

spriterect = sprite.get_rect()

music_sound.play(loops=-1, maxtime=0, fade_ms=0)

paddle1 = pygame.image.load("paddle.png")
paddle1rect = paddle1.get_rect()

paddle2 = pygame.image.load("paddle2.png")
paddle2rect = paddle2.get_rect()
paddle2rect.right=width

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        paddle1rect = paddle1rect.move(0, -10)
    if pressed_keys[pygame.K_s]:
        paddle1rect = paddle1rect.move(0, 10)


    if paddle1rect.top < 0:
        paddle1rect.top = 0     
    if paddle1rect.bottom > height:
        paddle1rect.bottom = height

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_w]:
        paddle2rect = paddle2rect.move(0, -10)
    if pressed_keys[pygame.K_s]:
        paddle2rect = paddle2rect.move(0, 10)


    if paddle2rect.top < 0:
        paddle2rect.top = 0     
    if paddle2rect.bottom > height:
        paddle2rect.bottom = height


    score_txt=score_font.render("score is over 9000!!!!!",1,(0,0,0))

    spriterect = spriterect.move(velocity)

    if spriterect.left < 0:
        player_right_score = player_right_score + 1

    if spriterect.right > width:
        player_left_score = player_right_score + 1

    if spriterect.left < 0 or spriterect.right > width or spriterect.colliderect(paddle1rect):
        velocity[0] = -velocity[0]
    if spriterect.top < 0 or spriterect.bottom > height:
        velocity[1] = -velocity[1]

    screen.blit(background, (0,0))
    screen.blit(sprite, spriterect)
    screen.blit(paddle1, paddle1rect)
    screen.blit(paddle2, paddle2rect)
    screen.blit(score_txt,(0,0))
    pygame.display.flip()
# end of while loop - go round the loop again!
