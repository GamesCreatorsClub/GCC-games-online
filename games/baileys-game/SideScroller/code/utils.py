from os import walk
import pygame
import time
pygame.init()

def load_folder(path,scale,convert_alpha = False,colour_key= None,_list=False):
    files = list(walk(path))
    names = files[0][2]
    if not _list:
        arg = {}
    else:
        arg = []
    for i in names:
        if convert_alpha:
            new_image = pygame.image.load(path +'/'+ i).convert_alpha()
        else:
            new_image = pygame.image.load(path +'/'+ i).convert()
        new_image = pygame.transform.scale(new_image,(new_image.get_width()*scale,new_image.get_height()*scale))
        if colour_key != None:
            new_image.set_colorkey(colour_key)
        name = i.split('.')[0]
        if not _list:
            arg[name] = new_image
        else:
            arg.append(new_image)

    return arg

def check_holding(key, level, current):
    holding = False
    if key not in level.keys_time:
        level.keys_time[key] = 0
    for event in level.keyed: 
        if event[0] == pygame.KEYDOWN and event[1] == key:
            level.keys_time[key] = time.time()
        if event[0] == pygame.KEYUP and event[1] == key:
            level.keys_time[key] = 0
    if level.keys_time[key] != 0:
        if current - level.keys_time[key]>= 0.5:
            holding = True

    return holding


