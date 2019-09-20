# -*- coding: utf-8 -*-
import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
import sys

import paxa_ncolor

import numpy
import random
import joystick01
import anna01_varaiable

import pavi
import paha
import paxa_ncolor

#v02

class anna:
    def __init__(self,root,rt):
        self.root                               =   root
        self.rt                                 =   rt
        self.on                                 =   1

        self.n_root                             =   {}
        self.pad                                =   {}



        self.taile                             =   0
        
        self.gril_game                          =   {}
        self.but_app                            =   None#appuit sur button color
        """
        self.pal_cl     = {     'ajt':[0,0],'var':None,'taile':16,"on":1,
                                (0, 1): {'w': 0, 'cl': [128, 0, 0],'taile':16},
                                (1, 2): {'w': 0, 'cl': [0, 255, 0],'taile':16},
                                (3, 2): {'w': 0, 'cl': [255, 255, 0],'taile':16},
                                (0, 0): {'w': 0, 'cl': [0, 0, 0],'taile':16},
                                (3, 3): {'w': 0, 'cl': [255, 255, 255],'taile':16},
                                (3, 0): {'w': 0, 'cl': [128, 128, 128],'taile':16},
                                (3, 1): {'w': 0, 'cl': [128, 128, 0],'taile':16},
                                (1, 1): {'w': 0, 'cl': [0, 128, 0],'taile':16},
                                (2, 1): {'w': 0, 'cl': [128, 0, 128],'taile':16},
                                (0, 2): {'w': 0, 'cl': [255, 0, 0],'taile':16},
                                (2, 0): {'w': 0, 'cl': [0, 0, 128],'taile':16},
                                (1, 3): {'w': 0, 'cl': [0, 255, 255],'taile':16},
                                (2, 3): {'w': 0, 'cl': [192, 192, 192],'taile':16},
                                (2, 2): {'w': 0, 'cl': [0, 0, 255],'taile':16},
                                (1, 0): {'w': 0, 'cl': [128, 0, 128],'taile':16},
                                (0, 3): {'w': 0, 'cl': [255, 0, 255],'taile':16}}        

        
        """
    def re_init(self,fl="paxa_config.txt"):
        ""

    def joystick(self):
        ""
        for i in anna.pad:
            rac                                     =   anna.pad[i]["joy"]
            ra                                      =   anna.pad[i]
            rac.direction()
            rac.button()
            if 1<=rac.dire_s[1]<=4:
                if rac.dire_s[0]    =="s" or rac.dire_s[0]=="u":
                    exec(ra['pad_pos'][rac.dire_s[1]])
            if 0<=rac.but_s[1]<=3:
                if rac.but_s[0]     =="u" and ra['but']['on']==1:
                    self.but_app                    =   [rac.but_s[1],i]

    #  ---------------------- V   C O L O R  ---------------------------       
                if rac.but_s[0]     =="s" and ra["module"]["n_color"]["on"] ==0:
                    ra['but']['on']                 =   0
                    ra["module"]["n_color"]["on"]   =   1
            
            if rac.but_s[:2] ==["u",4]:
                ra['but']['on']                     =   1
                ra["module"]["n_color"]["on"]       =   0
    #-----------------------------------------------------------------------
                

    def n_color(self,play):
        if anna.pad[play]["module"]["n_color"]["on"]   ==0:return -1
        rac =anna.pad[play]["module"]
        sur_r   =anna.n_root["n_root"]["surface"]
        
        vivien.blit(sur_r,rac["n_color"])
        a,b                                         =   anna.pad[play]["pos"].keys()[0]
        c,d                                         =   anna.pad[play]["ajt"]
        e,f                                         =   [a+c+2,b+d+2]
        anna.pad[play]["module"]["n_color"]["pos"]  =   (e,f)
        vivien.draw_pixel(rac["n_color"]["surface"],self.pal_cl)
        
        

        
                
        
                    
                    
                
                    
                    

                
    def mainloop(self):
        ""
        anna.joystick()
        if self.but_app         !=None:
            vivien.make_pixel(self.taile,self.but_app,anna.pad,self.gril_game)
            self.but_app                            =   None
        
        
    def display(self):
        ""
        vivien.blit(root.root,anna.n_root["n_root"])
        vivien.draw_pixel(anna.n_root["n_root"]['surface'],self.gril_game[0])
        for i in anna.pad:
            rac                                     =   anna.pad[i]
            vivien.draw_lib(anna.n_root["n_root"]['surface'],rac["pos"],rac['ajt'])
            self.n_color(i)        
        

        

if __name__ == '__main__':
    root                            =   pgwidth.width()
    root.size                       =   [600,350]
    root.ima_papier                 =   [255,250,200]
    
    
    root.width()
    anna                            =   anna(root.root,root)
    hana                            =   paha.hana(root.root,root)
    vivien                          =   pavi.vivien(root.root,root)
    anna.n_root.update(vivien.make_surface("n_root",[500,300],[1,0],[250,255,250],16,1))
    
    anna.pad.update(hana.nez())

    anna.gril_game.update(vivien.make_gril(0,16))
    
        
    
        
    
    root.act.append(anna)
    root.mainloop()
        

        

    
        
        
        
        
