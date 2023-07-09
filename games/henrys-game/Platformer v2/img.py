import pygame as pg

def resize_player_img(img_list):
    # This function should be used to shrink all player sprites by same ratio
    resized_img = []
    for image in img_list:
        new_img = pg.transform.scale(image, (256, 233))
        resized_img.append(new_img)
    return resized_img

def load_p_img_running_r():

    p_img_running_r = [
        pg.image.load("images/ProfX/Running/Running_000.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_001.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_002.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_003.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_004.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_005.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_006.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_007.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_008.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_009.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_010.png").convert_alpha(),
        pg.image.load("images/ProfX/Running/Running_011.png").convert_alpha()
        ]
    
    final_images = resize_player_img(p_img_running_r)
    
    return final_images


def create_left_images(right_images):
    left_images = []

    for image in right_images:
        left_images.append(pg.transform.flip(image, True, False))

    return left_images

def load_p_img_jump_loop_r():

    load_p_img_jump_loop_r = [
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_000.png").convert_alpha(),
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_001.png").convert_alpha(),
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_002.png").convert_alpha(),
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_003.png").convert_alpha(),
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_004.png").convert_alpha(),
        pg.image.load("images/ProfX/Jump Loop/Jump Loop_005.png").convert_alpha()
        ]
    
    final_images = resize_player_img(load_p_img_jump_loop_r)
    
    return final_images

def load_p_img_idle():
    p_img_idle = [
        pg.image.load("images/ProfX/Idle/Idle_000.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_001.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_002.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_003.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_004.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_005.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_006.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_007.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_008.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_009.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_010.png").convert_alpha(),
        pg.image.load("images/ProfX/Idle/Idle_011.png").convert_alpha()
        ]
    final_images = resize_player_img(p_img_idle)
    
    return final_images

def load_block_images():
    lst = [
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 01.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 02.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 03.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 04.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 05.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 06.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 07.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 08.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 09.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 10.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 11.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 12.png"),
        pg.image.load("images/Tile/Cartoon Jungle Game Tileset_Platformer - Ground 13.png")
        ]
    
    return lst

    
