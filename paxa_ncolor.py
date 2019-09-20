import              pygame
from pygame.locals import *
import time
import pgwidth
import pgrect

import sys

import numpy
import random
import joystick01
import anna01_varaiable

import pavi
import paha


class n_color:
    "couleur pallete"
    "pour paxa"

    def __init__(self,root,rt):
        ""
        self.root                   =   root
        self.rt                     =   rt
        self.on                     =   1
        self.curseur    = {     'ajt':[0,0],'taile':16,'on':1,"var":None,
                                'm_pos':{(0,0):{"w":5,'cl':[0,0,200],"taile":16,"read":None}}}
        self.pal_cl     = {     'ajt':[0,0],'var':None,'taile':32,"on":1,
                                'lim':[3,3]}
        """
        self.pal_cl["m_pos"]={
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
                                (0, 3): {'w': 0, 'cl': [255, 0, 255],'taile':16}
                                }"""
        self.pal_cl["m_pos"]={
                            (0,0):{'w': 0, 'cl': [100, 0, 0],'taile':16},
                            (0,1):{'w': 0, 'cl': [128, 0, 0],'taile':16},
                            (0,2):{'w': 0, 'cl': [255, 0, 0],'taile':16},
                            (0,3):{'w': 0, 'cl': [255, 28, 100],'taile':16},
                            (0,4):{'w': 0, 'cl': [255, 178, 150],'taile':16},
                            (1,0):{'w': 0, 'cl': [0, 100, 0],'taile':16},
                            (1,1):{'w': 0, 'cl': [0, 128, 0],'taile':16},
                            (1,2):{'w': 0, 'cl': [0, 255, 0],'taile':16},
                            (1,3):{'w': 0, 'cl': [28, 255, 100],'taile':16},
                            (1,4):{'w': 0, 'cl': [178, 255, 150],'taile':16},
                            (2,0):{'w': 0, 'cl': [100, 0, 255],'taile':16},
                            (2,1):{'w': 0, 'cl': [128, 0, 255],'taile':16},
                            (2,2):{'w': 0, 'cl': [0, 0, 255],'taile':16},
                            (2,3):{'w': 0, 'cl': [30, 128, 255],'taile':16},
                            (2,4):{'w': 0, 'cl': [50, 198, 255],'taile':16},
                            (3,0):{'w': 0, 'cl': [0, 0, 0],'taile':16},
                            (3,1):{'w': 0, 'cl': [70, 70, 70],'taile':16},
                            (3,2):{'w': 0, 'cl': [140, 140, 140],'taile':16},
                            (3,3):{'w': 0, 'cl': [205, 205, 205],'taile':16},
                            (3,4):{'w': 0, 'cl': [225, 225, 255],'taile':16},
                            (3,5):{'w': 0, 'cl': [255, 255, 255],'taile':16}
                            
            

            }
        
        self.n_root                 =   {}
        self.vivien                 =   pavi.vivien(root,rt)
        self.s_name                 =   "toor"
        self.s_size                 =   [150,150]
        self.s_pos                  =   [1,1]
        self.s_cl                   =   [128,128,128]
        self.s_taile                =   16
        self.s_on                   =   1

        

    def make_module(self):
        return self.vivien.make_surface(self.s_name,self.s_size,self.s_pos,self.s_cl,self.s_taile,self.s_on)




    def re_init(self):
        ""
    def displ_palcl(self,nb_r=0,gril=None):
        
        ""
        #print nb_r
             
        rac         =   self.n_root[self.n_root.keys()[nb_r]]
        if rac['on']                    ==1:
            if gril                     !=None:
                plcl.vivien.draw_pixel(rac['surface'],gril)
                
            if self.curseur["on"]       ==1:
                self.curseur['taile']   =   gril['taile']
                self.vivien.draw_pixel(rac['surface'],self.curseur)
                
            plcl.vivien.blit(self.root,rac)

    def displ_curseur(self,sur,gril):
        ""
        print "disp curseur"
        
        rac         =   sur[self.n_root.keys()[0]]
        if self.curseur["on"]       ==1:
            self.curseur['taile']   =   gril['taile']
            self.vivien.draw_pixel(rac['surface'],self.curseur)
    def commande(self,cmd=None):
        "commade pad pour curseur 1,2,3,4"
        
        #if              cmd ==None: return -1
        if              cmd ==1:self.curseur['ajt'][0] -=1
        elif            cmd ==2:self.curseur['ajt'][1] +=1
        elif            cmd ==3:self.curseur['ajt'][0] +=1
        elif            cmd ==4:self.curseur['ajt'][1] -=1
        a,b                 =   self.pal_cl["ajt"]
        c,d                 =   self.curseur["ajt"]
        e                   =   (c+a,d+b)
        f                   =self.pal_cl["m_pos"].keys().count(e)
        print f,e
        self.curseur['var']= None
        if f ==1:
            print "eee"
            self.curseur['var']=self.pal_cl[e]
        
        
        

    def mainloop(self):
        ""
        self.displ_palcl(0,self.pal_cl)
        

    def display(self):
        ""
        plcl.vivien.blit(self.root,plcl.n_root["toor"])
        self.commande()

if __name__=='__main__':
    ""
    root                            =   pgwidth.width()
    root.size                       =   [600,350]
    root.ima_papier                 =   [255,250,250]
    root.width()
    plcl                            =   n_color(root.root,root)
    
    plcl.n_root.update(plcl.make_module())

    
    root.act.append(plcl)
    root.mainloop()
