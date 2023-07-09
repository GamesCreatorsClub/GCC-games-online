import pygame as pg
import random
from settings import *
from sprites import *
from img import *
from levels import *

vec = pg.math.Vector2

class Game(object):
    def __init__(self):
        # Initialise game window, etc.
        pg.init()
#        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.levels = Level()
        self.camera_offset = vec(0, 0)
        self.camera_rect = pg.Rect(384, 384, 768, 384)
        self.camera_target_rect = pg.Rect(384, 384, 768, 384)
        self.debug = True
        
        
    def new(self):
        # Start a new game, reinitialise constants
        # Create lists
        self.blocks = []
        self.enemies = []
        # Instantiate the player and add to group
        self.player = Player(self)
        # Instatiate blocks and add them to groups
        self.create_level(self.levels.level00)
        # Put enemies in the list
        self.enemies.append(Enemy(self))
        # .run() starts game
        self.run()
        

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    # This function detects if player is outside of camera rect and moves it accordingly
    # It then updates the camera offset
    def camera_update(self):
        width = len(self.levels.active_level[0]) * BLOCK_WIDTH
        height = len(self.levels.active_level) * BLOCK_HEIGHT
        minx = 384
        maxx = width - 384
        miny = 384
        maxy = height - 384
        if self.player.pos.x > minx and self.player.pos.x < maxx:
            if self.player.pos.x > self.camera_rect.right:
                vx = abs(self.camera_rect.right - self.player.pos.x)
                self.camera_target_rect.x += vx
            elif self.player.pos.x < self.camera_rect.left:
                vx = abs(self.camera_rect.left - self.player.pos.x)
                self.camera_target_rect.x -= vx
        if self.player.pos.y < maxy:
            if self.player.pos.y > self.camera_rect.bottom:
                vy = abs(self.camera_rect.bottom - self.player.pos.y)
                self.camera_target_rect.y += vy
            elif self.player.pos.y < self.camera_rect.top:
                vy = abs(self.camera_rect.top - self.player.pos.y)
                self.camera_target_rect.y -= vy

        # Find dx and dy difference between start and target rect
        dx = abs(self.camera_target_rect.x - self.camera_rect.x)
        dy = abs(self.camera_target_rect.y - self.camera_rect.y)
        
        if dx < 1:
            self.camera_rect.x = self.camera_target_rect.x
        if dy < 1:
            self.camera_rect.y = self.camera_target_rect.y
        # X camera offset 
        if self.camera_rect.x < self.camera_target_rect.x:
            self.camera_offset.x -= dx
            self.camera_rect.x += dx
        if self.camera_rect.x > self.camera_target_rect.x:
            self.camera_offset.x += dx
            self.camera_rect.x -= dx
        # Y camera offset 
        if self.camera_rect.y > self.camera_target_rect.y:
            self.camera_offset.y += dy
            self.camera_rect.y -= dy
        if self.camera_rect.y < self.camera_target_rect.y:
            self.camera_offset.y -= dy
            self.camera_rect.y += dy


        

    def update(self):
        # Debug quit game
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            pg.quit()
        # Game Loop - Update
        self.player.update()

        # Check if player hits a platform
        collision = False
        for block in self.blocks:
            if block.stand_on:
                if self.player.vel.y < 20:
                    if block.surface_rect.colliderect(self.player.foot_rect):
                        collision = True
                else:
                    if block.rect.colliderect(self.player.foot_rect):
                        collision = True
                if collision == True:
                    if self.player.vel.y > 0 and self.player.pos.y < block.rect.bottom:
                        self.player.pos.y = block.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False

        # Insert some code that goes through everything and adds the offset to their coords
        self.camera_update()

    def events(self):
        # Game Loop - Events
        for event in pg.event.get():
            # Check for closing the window
            if event.type == pg.QUIT:
                if self.playing == True:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_t:
                    if self.debug == True:
                        self.debug = False
                    else:
                        self.debug = True
                if event.key == pg.K_r:
                    self.player.pos = vec(448, (len(self.levels.active_level)* BLOCK_HEIGHT) - 386)
                    self.player.vel = vec(0, 0)
                    self.player.acc = vec(0, 0)

  
    def draw(self):
        # Game Loop - Draw
        self.screen.fill(BLACK)
        # Draw blocks
        for block in self.blocks:
            block.draw(self.screen, self.camera_offset)
        # Draw enemies
        for enemy in self.enemies:
            enemy.draw(self.screen, self.camera_offset)
        # Draw player
        self.player.draw(self.screen, self.camera_offset)
        # Draw the debug infographics
        camera_rect = offset_rect(self.camera_rect, self.camera_offset)
        if self.debug == True:
            pg.draw.rect(self.screen, BLUE, camera_rect, 1)

        pg.display.flip()

    def show_start_screen(self):
        # Game splash/start screen
        self.screen.fill(RED)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Let the Physics begin!", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3/ 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        # Game over/continue
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("The Physics came to an end", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3/ 4)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False
                    
    def create_level(self, level):
        # This function reads the level txt file and creates blocks in the required locations
        x = y = 0
        i = j = 0
        for row in level:
            for col in row:
                if col == "#":
                    if level[j][i+1] == " ":
                        block_num = 7
                    elif level[j][i-1] == " ":
                        block_num = 3
                    else:
                        block_num = 1
                    new_block = Block(self, x, y, block_num)
                    self.blocks.append(new_block)
                elif col == "X":
                    if level[j][i+1] == " ":
                        block_num = 12
                    elif level[j][i-1] == " ":
                        block_num = 8
                    else:
                        block_num = 5
                    new_block = Block(self, x, y, block_num, False)
                    self.blocks.append(new_block)
                elif col == "-":
                    if level[j][i+1] == " ":
                        block_num = 11
                    elif level[j][i-1] == " ":
                        block_num = 9
                    else:
                        block_num = 10
                    new_block = Block(self, x, y, block_num)
                    self.blocks.append(new_block)
                x += BLOCK_WIDTH
                i += 1
            y += BLOCK_HEIGHT
            j += 1
            x = 0
            i = 0

    def draw_text(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
