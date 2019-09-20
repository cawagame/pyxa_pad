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
import paxa_select
import paxa_cadre

class cmd:
    ""
    def __init__(self,old=None):
        "Nouvelle format de root"

        self.old        =   old
        self.rac        =   None
        self.ra         =   None
        self.pi         =   None#player n
        
        


    def cmd_pad(self):
        ""
        
        if self.ra["on"] ==0:return
        if 1<=self.rac.dire_s[1]<=4:
            v_ex= "self.old."+self.ra['pad_pos'][self.rac.dire_s[1]]
            exec(v_ex)
            
            rac_mp  =   self.old.app_ext['m_palcl']
            if self.ra["module"]["n_color"]["on"]   ==1:
                a,b             =   rac_mp.curseur["ajt"]
                c,d             =   rac_mp.pal_cl['ajt']
                e               =   (a+c,b+d)
                f               =   rac_mp.pal_cl.keys().count(e)
                rac_mp.curseur['var']=None
                if f==1:self.rac_mp.curseur['var']          =   self.rac_mp.pal_cl[e]
                self.old.but_app["app_cl"]["on"]        =   1
                self.old.but_app["app_cl"]["play"]      =   i
                self.old.but_app["app_cl"]["n_butt"]    =   self.rac_mp.curseur['var']['cl']
         
                    
                            #self.but_app=[ m_palcl.curseur['var']['cl'],i]
    def cmd_pad_plcl(self):
        if self.ra['but']['on']==0:return
        if 0<=self.rac.but_s[1]<=3:
            self.old.but_app["app_cl"]["on"]            =   1
            self.old.but_app["app_cl"]["play"]          =   self.pi
            self.old.but_app["app_cl"]["n_butt"]        =   self.ra["but"][self.rac.but_s[1]]
    def cmd_v_color_0N(self):
        if self.ra["module"]["n_color"]["on"]   ==0:      return
        self.ra['but']['on']                            =   1
        self.ra["module"]["n_color"]["on"]              =   0
    def cmd_v_color_off(self):
        if self.ra["module"]["n_color"]["on"] ==1: return
        self.rac.but_s[2]                               =   -1
        self.ra['but']['on']                            =   0
        self.ra["module"]["n_color"]["on"]              =   1

