# import pygame
from utils import load_folder

class Images:
    def __init__(self,scale):

        self.items = load_folder('../graphics/items',scale,False,(255,255,255))
        self.characters = load_folder('../graphics/characters',scale,False,(0,0,0))
        self.tiles = load_folder('../graphics/tiles',scale,False,(0,0,0))
        self.ui = load_folder('../graphics/ui',scale)
        
        #self.players
        #self.enemies