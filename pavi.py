# -*- coding: utf-8 -*-
import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
#import pgrentrypy
import sys

import numpy
import random
import joystick01
import paxa_cadre
#import anna01_varaiable
#import paxa_01   suprimer

class vivien:
    def __init__(self,root,rt,old=None):
        ""
        self.root                               =   root
        self.rt                                 =   rt
        self.old                                =   old
        self.on                                 =   1
        self.sur                                =   {}
        self.gril_game                          =   {}
        self.gril_game[16]                      =   {}
        self.gril_game[16]                      =   {
                                (12, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (11, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (13, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (10, 10): {'w': 0, 'cl': [250, 0, 250]}}
        self.gril_game[16]['on']                =   1
        self.gril_game[16]['ajt']               =   [0,0]
        self.gril_game[16]['var']               =   {}
        self.gril_game[16]['taile']             =   16
        self.gril_game[8]                       =   {}
        self.gril_game[8]                       =   {
                                (23, 19): {'w': 1, 'cl': [20, 0, 250]},
                                 (11, 11): {'w': 1, 'cl': [20, 0, 250]},
                                 (13, 11): {'w': 1, 'cl': [20, 0, 250]},
                                 (10, 11): {'w': 1, 'cl': [20, 0, 250]}}
        self.gril_game[8]['on']                 =   1
        self.gril_game[8]['ajt']                =   [0,0]
        self.gril_game[8]['var']                =   {}
        self.gril_game[8]['taile']              =   8
        
        

    def blit(sefl,papa,sur):
        ""
        #print papa
        if sur["on"]                            ==1:
            a,b                 =   sur['pos']
            t                   =   papa['taile']
            pos                 =   [a*t,b*t]
            sur["pos_r"]        =   pos
            
            papa["surface"].blit(sur["surface"],pos)
            sur["surface"].fill(sur['cl'])
            
        if sur['cadre']['on'] !=0:sur['cadre']["dr"].draw_cadre()
        

    def pos_table(self,ta,gg,taile=None):
        "gi =[10,15] gg=gril_game"
        if taile ==None:taile=gg["taile"]
        x,y                                    =   ta
        c,d                                     =   gg["ajt"]
        e                                       =  taile
        return  [(x+c)*e,(y+d)*e],[x+c,y+d]

    def pos_gril(self,gr,gg):
        "gr =[101,103] gg=gril_game"
        a,b                                     =   gr
        c,d                                     =   gg["ajt"]
        e                                       =   gg["taile"]
        f,g                                     =   a/e,b/e
       
        return [(f+c)*e,(g+d)*e],[f+c,g+d]
        
    def draw_lib(self,sur_r,data_,ajt):
        ""
        
        ib ={}
        data =data_["pos"]
        for i in data:
            
            data[i]["ajt"]                      =   ajt
            sca,scb                             =   data[i]['szc']            
            rect                                =   self.pos_table(i,data[i],data_['taile'])[0]
            rect                                =   [rect[0]+sca,rect[1]+scb]
            
            sz                                  =   [data_['taile']]*2
            
            sza,szb                             =   data[i]['size']
            sz                                  =   [sz[0]+sza,sz[1]+szb]
            pygame.draw.rect(sur_r,data[i]["cl"],rect+sz,data[i]["w"])

    def make_pixel(self,but_app,pad,g_r):
        
        cl                                      =   but_app["n_butt"]
        i                                       =   but_app['joy']
        fa,fb                                   =   g_r["ajt"]
        g_g                                     =   g_r["m_pos"]   #rac
        
        ra                                      =   pad[i]
        a,b                                         =   ra["pos"].keys()[0]
        c,d                                         =   ra["ajt"]
        e                                           =   (a+c-fa,b+d-fb)
        #cl                                          =   ra['but'][but_app[0]]
        if g_g.keys().count(e)                      ==0:
            g_g[e]                                  =   {}
            g_g[e]["w"]                             =   0
            g_g[e]["cl"]                            =   cl
        elif g_g[e]["cl"]                           ==cl:g_g.pop(e)
        elif g_g[e]["cl"]                           !=cl:g_g[e]["cl"]=cl
        but_app['on'] =0
            

    
    def draw_pixel(self,sur,g_g,taile=-1):
        "taile = None taile de surface taile =5 valeur du taile  taile =-1 taile de la grile"
        for i in g_g:
   
            if g_g[i]!={}:
                self.dr_pix(sur,g_g[i],taile)
    def dr_pix(self,sur,g_g,taile=-1):
        "taile  None surface[taile] -1 taile origine >0 taile maisson  "
        
        t_old                                       =   g_g['taile']
        sur_r                                       =   sur["surface"]
        if taile                        ==  None:g_g['taile'] =sur["taile"]
        elif taile                      ==  -1:""
        elif taile                      >0 or type(taile)==type([]):
            g_g['taile'] = taile
        if type(taile)==type([]):       posa_s      =   g_g['taile']
        else:                           posa_s      =   [g_g['taile']]*2
        

        
        if g_g['on']                                ==1:            
            for i in g_g['m_pos']:
                
                if g_g['m_pos'][i].keys().count('img')==0:
                    
                    rac_g                           =   g_g['m_pos'][i]
                    posa                            =   self.pos_table(i,g_g)[0]
                    rect                            =   posa+posa_s
                    pygame.draw.rect(sur_r,rac_g['cl'],rect,rac_g["w"])
                else:
                    posa                            =   self.pos_table(i,g_g)[0]
                    self.old.n_root["n_root"]["taile"] =64
                    self.old.n_root['n_root']['surface'].blit(g_g['m_pos'][i]['img'],posa)
                    
        g_g['taile'] =t_old                    
    def make_surface(self,nom,size,pos,cl,taile=16,on=0):
        "sortir OUT5  pos (10,10) def taile 16   on=0"
        out5                                        =   {}
        out5[nom]                                   =   {}
        out5[nom]["on"]                             =   on
        out5[nom]["papa"]                           =   None                        
        out5[nom]["surface"]                        =   pygame.surface.Surface((size))
        out5[nom]["variable"]                       =   None
        out5[nom]["pos"]                            =   pos
        out5[nom]["pos_r"]                          =   None
        out5[nom]["taile"]                          =   taile
        out5[nom]["ajt"]                            =   [0,0]
        out5[nom]["size"]                           =   size
        out5[nom]["lim"]                            =   None
        out5[nom]["cl"]                             =   cl
        out5[nom]["atc_"]                           =   "surface"
        out5[nom]["cadre"]                          =   {}
        out5[nom]["cadre"]["on"]                    =   1 # 0 off, 1 ,[0,0,1,0]
        out5[nom]["cadre"]["dr"]=   paxa_cadre.cadre(out5[nom]["surface"],None,out5[nom])
        return out5

    def make_gril(self,nom,taile):
        "nom =str ou int"
        out5                                            =   {}
        out5[nom]                                       =   {}
        out5[nom]['taile']                              =   taile
        out5[nom]['ajt']                                =   [0,0]
        out5[nom]["on"]                                 =   1
        out5[nom]["size"]                               =   [100,100]
        out5[nom]['var']                                =   {}
        out5[nom]['m_pos']                              =   {}
        return out5

    

    def key_nooui(self,gril,key):
        ""
        out5    ={}
        a =gril.keys()
        b =a.count(key)
        if b==0:return -1
        return 1
        
        

    def mainloop(self):
        ""
        self.blit(root_s,vivien.sur["n_root"])
    

    def display(self):
        ""
        self.dr_pix(vivien.sur["n_root"],self.gril_game[16])
        self.dr_pix(vivien.sur["n_root"],self.gril_game[8])

if __name__=="__main__":
    root                        =   pgwidth.width()
    root.size                   =   [600,400]
    root.ima_papier             =   [120,120,120]

    root.width()
    root_s                      =   {}
    root_s["taile"]             =16
    root_s["surface"]           =root.root
    

    vivien                      =   vivien(root.root,root)
    vivien.sur.update(vivien.make_surface('n_root',[500,200],[0,0],[255,255,255],16,1))
    vivien.sur["n_root"]['cadre']['on'] =3
    root.act.append(vivien)
    root.mainloop()
