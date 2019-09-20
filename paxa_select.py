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

class selc:
    "selection element"
    def __init__(self,old):
        ""
        self.old        =   old

    def couper(self,g_g,pos_end=[0,0,10000,10000]):
        "pos_end [0,100,0,100]"
        out5                        =   {}
        j,k,l,m                     =   10000,10000,0,0
        a,b,c,d                     =   pos_end
        for i in g_g:
            if type(i)==type(()):
                e,f                 =   i
                if a<e<c and b<f<d:
                    out5[(e,f)]     =   g_g[i]
                    if e<j:     j   =   e
                    if f<k:     k   =   f
                    if e>l:     l   =   e
                    if f>m:     m   =   f

        return out5,[j,k,l,m]
        
                
        

    def mis_zero(self,data,pos_mz,pos_n=[0,0]):
        out5                        =   {}
        a,b                         =   pos_mz
        e,f                         =   pos_n
    
        for i in data:
            ""            
            c,d                     =   i
            out5[c-a+e,d-b+f]       =   data[i]
        return out5

    def selct_rect(self):
        ax,bx     =vivien.pos_table(ra_m['dp'],anna.n_root['n_root'])[0]
        cx,dx     =vivien.pos_table(ra_m['end'],anna.n_root['n_root'])[0]
        dx,ex     =   cx-ax,dx-bx
        pygame.draw.rect(anna.n_root['n_root']['surface'],[0,0,0],[ax,bx]+[dx,ex],5)
        
