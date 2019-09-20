#!/usr/bin/env python
# -*-coding:utf-8-*-
import pygame
from pygame.locals import *
import copy
import pgwidth
import time
import pggame_key
class rect:

    def __init__(self,root=None,rt=None,ima_ima=None):
        ""
        self.   rt                      =       rt
        self.   root                    =       root
        r                               =   str(self)
        self.key    =pggame_key.rect()
        self.   name                    =       r.split(" ")[-1][:-1]
        self.   n_cola                  =       None
        
        self.xy                        =   0#toucher element
        self.   color                   =       [20,30,40]
        self.   pos                     =       [70,70]
        self.   size                    =       [50,50]
        self.   w                       =       1
        self.   w0                      =       2
        self.   w1                      =       7 #toucher
        self.   unappuit                =       0
        self.   nu_ftouch               =       0   #nombre fois toucher activer
        #option ---------------------------------
        self.   on                      =       1
        self.   on_dis                  =       None
        self.   ms_touch                =       1
        #option mouse -----------------------------
        self.   move                    =       (1,0,0)
        self.v_mouse                    =       0
        self.   ms_cl1                  =       None
        self.   ms_cl2                  =       None
        self.   ms_cl3                  =       None
        #option font ----------------------------
        #self.   font_text               =       "VAVA" #ou None
        self.font_text              =           None
        self.   font_size               =       50
        self.   font_color              =       [0,128,0]
        self.   font_font               =       "comicsansms"
        
        #option image -----------------------
        #self.   ima_load                =       "tux.jpg"
        self.   ima_ima                 =       ima_ima
        self.ima_load               =           None
        self.ima_pos                    =       [0,0]
        #print self.ima_ima
        self.   re_rect                         ()


        #-----------  rserver a game
        self.   focus                   =       0 #0/1
        self.   act_focus               =       None


        self.       act_pad             =       1
        self.       act_pad_tt          =       .3
        self.       act_pad_t0          =       0
        #---___  sprite
        self.ima_sprite                 =       []
        self.ima_sprite_n               =       0
        self.sprite_n                   =       10
        self.sprite_nv                  =       0

    def sprite(self):
        "activer sprite"
        self.sprite_nv                  =   self.sprite_nv+1
        if self.sprite_nv>self.sprite_n:
            self.sprite_nv              =   0
            self.ima_sprite_n           =   self.ima_sprite_n+1
        if self.ima_sprite_n>len(self.ima_sprite)-1:
            self.ima_sprite_n       =   0
        self.ima_ima            =   self.ima_sprite[self.ima_sprite_n]
        return self.ima_sprite[self.ima_sprite_n]
        
        
    def re_rect                                 (self):
    
        if self.ima_load !=  None and self.ima_ima ==None    :   self.re_ima()
        if self.    font_text       !=  None    :   self.re_font()
    def re_font                                 (self):
        "re_init option font "
        self.   font                    =       pygame.font.SysFont(self.font_font, self.font_size)
        self.   di_tx                   =       self.font.render(self.font_text, True, self.font_color)

    def re_ima                                  (self):
        "re_init option ima"
        self.   ima_ima                 =       pygame.image.load(self.ima_load).convert_alpha()
        self.   ima_ima                 =       pygame.transform.scale(self.ima_ima,self.size)
        
        
        
    

    def display                         (self,w=1):
   
        if self.on_dis                  ==  1       :
            pygame.draw.rect(self.root,self.color,self.pos+self.size,self.w)
        if self.ima_load            !=  None    or self.ima_ima !=None:
            ai,bi                       =self.pos
            ci,di                       =self.ima_pos
            impos                       =   [ai+ci,bi+di]
            self.root.blit(self.ima_ima,impos)
        if self.font_text           !=  None    :
            self.root.blit(self.di_tx,(self.pos))

  



   

    def touch(self):
        "mouse touch"
        
        a,b                         =           self.pos[0],self.pos[1]
        c,d                         =           self.size[0],self.size[1]
        x,y                         =           pygame.mouse.get_pos()
        if a<x<a+c and b<y<+b+d             :   self.xy =15
        #if self.xy                  ==  15  :   self.display(w=self.w+1)
        if self.xy                  ==  15  :self.w =self.w1
        else:self.w =self.w0


    def ms_clx(self,act=None):
        "ms_cl auto"
        if act                  !=None      :
            if type(act)        ==type("")  :exec(act)
            else                            :act()


                
    def mainloop(self):
        ""
        self.xy                     =           0

        #a,b     =pygame.mouse.get_rel()
        
        if self.ms_touch            ==  1   :   self.touch()
        if self.focus           ==  1 and self.act_focus !=None:
            self.act_focus()
        
        #move mouse
        if self.xy                  ==  15 :
            #if self.rt.ms_touch.count(self) ==0:
            self.rt.ms_touch.append(self)
            
            if pygame.mouse.get_pressed()   ==self.move:
                #self.v_move         =           1

                c,d                 =           pygame.mouse.get_rel()
                if c>20 or -20>c            :   c,d =0,0
                if d>20 or -20>d            :   c,d =0,0
                self.pos            =           [self.pos[0]+c,self.pos[1]+d]

                """
                o,p     =pygame.mouse.get_pos()
                q,r     =self.pos
                s,t     =o-q,p-r
                print o,p,"  ",q,r, "    ",s,t
                self.pos    =[q+s,r+t]
        
                """
        #-------------------- FIN move ------------
            #code ms_clx
            
            
            if self.key.mouse()==2          :self.ms_clx(self.ms_cl1)
            if self.key.mouse()==4          :self.ms_clx(self.ms_cl2)
            if self.key.mouse()==8          :self.ms_clx(self.ms_cl3)
                
        
                
                

            
        if self.act_pad     !=1:
            if self.act_pad_t0+self.act_pad_tt <time.time():
                self.act_pad =1
        
    def bye(self):
        "quit effacer tuer"
        try:
            self.rt.act.remove[self]
        except:
            ""
            
        

if __name__ == '__main__':

    
    
    def bb():
        global a
        z   =copy.copy(b)
        z.pos =[10,20]
        a.act.append(z)

        
    a   =pgwidth.width()
    a.on_dis       =   None
    a.width()
    
    im =pygame.image.load("vavi/im_vide.png").convert_alpha()
    im =pygame.transform.scale(im,[12,25])


    
    b   =rect(a.root,a)
    b.size =[12,25]
    b.ms_cl3 = "print 'essai_cl.py'"
    b.ms_cl2 =bb
    #b.ima_load="tux.jpg"
    b.pos   =[20,100]
    b.ima_ima=im
    #b.re_ima()
    c   =rect(a.root,a)
    c.color =[255,0,255]
    c.font_text ="anna"
    c.re_font()
    c.pos   =[200,100]
    #b.display()
    a.act.append(c)
    a.act.append(b)
    a.mainloop()
