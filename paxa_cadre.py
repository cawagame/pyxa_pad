# -*- coding: utf-8 -*-
import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
import sys

#import paxa_ncolor

import numpy
import random
import joystick01
#import anna01_varaiable

import pavi
import paha
import paxa_ncolor
import paxa_save

#v02
class cadre:
    "cadre surface"
    def __init__(self,root,rt,old):
        "                  2²       "
        "               ------      "
        "               -    -      "
        "           1²  -    - 3²   "
        "               ------      "
        "                  4²       "
        
        self.root               =   root
        self.rt                 =   rt
        self.old                =   old
        self.pos                =   [0,0]
        self.size               =   [100,100]
        self.w                  =   1
        self.cl                 =   [0,0,0]
        self.cote               =   None#[0,0,1,0]

    def draw_cadre(self):
        if type(self.old["cadre"]["on"]) == type(1):
            c,d             = self.root.get_size()
            w               = self.old["cadre"]["on"]
            pos             = [0,0]
            pygame.draw.rect(self.root,[255,250,250],pos+[c,d],w+5)
            pygame.draw.rect(self.root,self.cl,pos+[c,d],w)
            
