import pygame, sys, random

# class for the player ship sprite
class ShipSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface.convert_alpha(pygame.image.load("Magna.png"))
        self.rect = self.image.get_rect()
        self.position = [30,384]
        self.velocity = [0, 1]
        
    def Draw(self, screen):
        screen.blit(self.image, self.position)     
   
    def Update(self, seconds):
        self.position += self.velocity * seconds
        

class ScrollingMap:
    def __init__(self, sprite_sheet_filename, sprite_size):
        self.map_array = []
        self.tile_array = []
        self.sprite_sheet = pygame.Surface.convert_alpha(pygame.image.load(sprite_sheet_filename))
        self.sprite_size = sprite_size
        self.sprite_tile_rectangles = []
        total_tiles = int(self.sprite_sheet.get_width() / self.sprite_size) * int(self.sprite_sheet.get_height() / self.sprite_size)
        for tiles in range(total_tiles):
            self.sprite_tile_rectangles.append(self.GetMapTileRectangle(tiles))
        self.tile_lookup = {
            "____" : 0,
            "___#" : 1,
            "__#_" : 2,
            "__##" : 3,
            "_#__" : 4,
            "_#_#" : 5,
            "_##_" : 6,
            "_###" : 7,
            "#___" : 8,
            "#__#" : 9,
            "#_#_" : 10,
            "#_##" : 11,
            "##__" : 12,
            "##_#" : 13,
            "###_" : 14,
            "####" : 15
            }
        self.current_pixel_offset = 0
        self.current_map_origin = 0

    def GetMapTileRectangle(self, cell_index):
        column_count = self.sprite_sheet.get_width() / self.sprite_size
        column = int(cell_index % column_count)
        row = int(cell_index / column_count)
        x = column * self.sprite_size
        y = row * self.sprite_size
        return pygame.Rect(x, y, self.sprite_size, self.sprite_size)

    def LoadMapData(self, filename):
        file = open(filename)
        raw_array = []
        for index, line in enumerate(file):
            #self.map_array.append([])
            raw_array.append([])
            line = line.rstrip()
            for letter in line:
                raw_array[index].append(letter)
                #if letter in self.tile_lookup:
                #    self.map_array[index].append(self.sprite_tile_rectangles[self.tile_lookup[letter]])
                #else:
                #    self.map_array[index].append(None)
        file.close()
        # read the raw array in blocks of 4 and populate tile array accordingly#
        row = 0
        #for y in range(0, int(len(raw_array)), 2):
        for y in range(0, int(len(raw_array))):
            self.map_array.append([])
            for x in range(0, int(len(raw_array[y]))):
                if raw_array[y][x] == '#':
                    # Up, Right, Down, Left
                    if x == 0:
                        right = raw_array[y][len(raw_array[y]) - 1]
                    else:
                        right = raw_array[y][x - 1]

                    if y == 0:
                        up = '#'
                    else:
                        up = raw_array[y - 1][x]

                    if x == len(raw_array[y]) - 1:
                        left = raw_array[y][0]
                    else:
                        left = raw_array[y][x + 1]

                    if y == len(raw_array) - 1:
                        down = '#'
                    else:
                        down = raw_array[y + 1][x]                    
                        
                    tile_string = up + left + down + right
             
                    # look up sprite sheet rectangle according to tile_string
                    if tile_string in self.tile_lookup:
                        self.map_array[row].append(self.sprite_tile_rectangles[self.tile_lookup[tile_string]])
                    else:
                        self.map_array[row].append(None)
                else:
                    self.map_array[row].append(None)
            row += 1  
    
    def Draw(self, screen):
        for x in range(11):
            map_column = (x + self.current_map_origin) % len(self.map_array[0]) # wrap around the column
            for y in range(8):
                if self.map_array[y][map_column] != None:
                    screen.blit(self.sprite_sheet, (x * self.sprite_size - self.current_pixel_offset, y * self.sprite_size), self.map_array[y][map_column])
    
    def Update(self):
        self.current_pixel_offset += 1
        if self.current_pixel_offset > 64:
            self.current_map_origin += 1
            self.current_pixel_offset = 0

        self.current_map_origin = self.current_map_origin % len(self.map_array[0]) # wrap around the origin
    
#def main():
pygame.init()
screen = pygame.display.set_mode((640,480))

game_map = ScrollingMap("s9s_map_tile_sheet2.png", 64)
game_map.LoadMapData("s9s_map.txt")

magna_ship = ShipSprite()

#time is specified in milliseconds
#fixed simulation step duration
desired_frame_duration = 20
#max duration to render a frame
max_frame_duration = 100

last_frame_time = pygame.time.get_ticks()
game_running = True
pygame.key.set_repeat(250, 30)
pygame.event.set_allowed((pygame.QUIT, pygame.KEYDOWN))
while(game_running):
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                magna_ship.position[1] += 1
            if event.key == pygame.K_UP:
                magna_ship.position[1] -= 1

    #get the current real time
    current_frame_time = pygame.time.get_ticks()

    #if elapsed time since last frame is too long...
    if current_frame_time - last_frame_time > max_frame_duration:
        #slow the game down by resetting clock
        last_frame_time = current_frame_time - desired_frame_duration
        #alternatively, do nothing and frames will auto-skip, which
        #may cause the engine to never render!

    #this code will run only when enough time has passed, and will
    #catch up to wall time if needed.
    while(current_frame_time - last_frame_time >= desired_frame_duration):
        #save old game state, update new game state based on step_size
        last_frame_time += desired_frame_duration
    else:
        pygame.time.wait(1)

    #render game state. use 1.0/(desired_frame_duration/(last_frame_time - current_frame_time)) for interpolation
    game_map.Update()
    #magna_ship.Update(current_frame_time)
    screen.fill((50,50,50))
    game_map.Draw(screen)
    magna_ship.Draw(screen)
    pygame.display.flip()
        
#    pygame.quit()
#    sys.exit()
#
#if __name__ == "__main__":
#    main()
