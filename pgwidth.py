#!/usr/bin/env python
# -*-coding:utf-8-*-
import              pygame
from pygame.locals import *
import              copy
import              time

class width:
    "2017"
    def __init__(self):
        ""
        pygame.init()
        self.rt                     =           None
        self.size                   =           [800,400]
        self.title                  =           "WIDTH 2017"
        self.ima_papier             =           [200,150,250]
        self.ima_papier             =          "payssage.jpg"
        
        self.ima_pos                =           [0,0]
        self.unappuit               =           0
        self.py_image               =           ""
        #----------------        
        self.time                   =           .02
        self.ms_touch               =           []
        self.ms_touch_old           =           []
        self.focus                  =           None #donne le focus a entry
        self.ms_app                 =           []
        self.act0                   =           []
        self.act                    =           []
        self.act1                    =           []

        self.ms_down_up             =           None
        self.tt                     =           time.time()

        self.dis_update             =           1   #display update activer
        
        

    def re_init                         (self)  :
        ""


    
    def pos_case(self,n_case,surface):
        "sorti 3"
        taile   =surface['taile']
        size    =surface["size"]
        ref                 =   size[0]/float(taile)
        a                   =   n_case/ref
        b                   =   int(a)*ref
        c                   =   n_case-b
        d                   =   b/ref
    
        ref,a,c                 =  int(ref),int(a),int(c)
        return (c*taile,a*taile),[a,c],a*ref+c


    def pos_gril(self,g,surface):
        "g =[123,12]"
        taile   =surface['taile']
        size    =surface["size"]
        ref                 =   size[0]/taile
        a =g[0]/taile
        b =g[1]/taile
        c =a*taile
        d =b*taile
        return (c,d),[b,a],b*ref+a

    def pos_table(self,t,surface):
        "t =[20,40]"
     
        taile   =surface['taile']
        size    =surface["size"]
        ref                 =   size[0]/taile
        a,c                 =t

        return  (a*taile,c*taile),[a,c],a*ref+c            
            
        
        

    def image(self):
        "load image"
        self.ima_ima                =           pygame.image.load(self.ima_papier)
        
    def width(self):
        ""
        self.root                   =           pygame.display.set_mode(self.size)
        
        self.fond_ecran()


    def fond_ecran(self):
        if type(self.ima_papier)     ==  type("")    :
            ""
            self.ima_ima                =           pygame.image.load(self.ima_papier)
            #if self.ima_move        ==1:self.ima_pos[1] =self.ima_pos[1]-1
            self.root.blit(self.ima_ima,self.ima_pos)
                
        else:
            self.root.fill(self.ima_papier)
   
        
    def l_act(self,i):
        "act liste"
        if i.on ==1:
            i.display()
            i.mainloop()
            if self.focus !=i:i.focus =None

    def mainloop(self,act=None):
        ""
        while 1:
           
            #print time.time()
            #self.mouse          =pygame.mouse
            
            
            for self.event in pygame.event.get()    :
                if(self.event.type==pygame.QUIT or (self.event.type==pygame.KEYDOWN and self.event.key==pygame.K_ESCAPE)):
                    #pygame.quit()
                    return
             
            if act!=None:act()
            if self.act0        !=None:
                for i in self.act0:self.l_act(i)
            if self.act         !=None:
                for i in self.act:self.l_act(i)
            if self.act1         !=None:
                for i in self.act1:self.l_act(i)
            
                
            #print self.ms_touch  <---
       
            #pygame.time.wait(self.time)
              
            #if time.time()-self.tt          >(self.time):
            pygame.time.wait(20)
                #print time.time()-self.tt
            self.tt                     =   time.time()
            if self.dis_update ==1:pygame.display.update()
            self.fond_ecran()
            self.ms_touch_old           =   self.ms_touch[:]
            self.ms_touch               =   []

                
            
            

if __name__ == '__main__':
    a =width()
    a.width()
    a.mainloop()
