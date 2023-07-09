import pygame as pg
from settings import *
from sprites import *



class Level(object):

    def __init__(self):
        
        self.load_levels()
        self.active_level = self.level00


    def load_levels(self):

        self.level00 = [
            "                                                                                                                                                                                                         ",
            "       --                                                                                                                                                                                                ",
            "                                                                                                                                                                                                         ",
            "    --                                                                                                                                                                                                   ",
            "                                                                                                                                                                                                         ",
            "--          ---                                                                                                                                                                                          ",
            "                                                                                                                                                                                                         ",
            "                                                                                                                                                                                                         ",
            "    ---   ###                                                                                                                                                                                            ",
            "          XXX                                                                                                                                                                                            ",
            "          XXX ##                                                                                                                                                                                         ",
            "############# XX #################################                                                                                                                                                       ",
            "XXXXXXXXXXXXX XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                                                                       ",
            "XXXXXXXXXXXXX XX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                                                                                       "
            ]

        self.level01 = [
            "               ",
            "               ",
            "               ",
            "              #",
            "  #          #X",
            "            #XX",
            "           #XXX",
            "###########XXXX",
            "XXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXX"
            ]
