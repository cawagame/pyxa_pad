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
import pavi
import pali

class hana:
    def __init__(self,root,rt):
        self.root                                       =   root
        self.rt                                         =   rt
        self.on                                         =   1
        self.sur                                        =   {}
        self.pad                                        =   {}
        self.vivien                      =   pavi.vivien(root,rt)
        self.pad_ij             =[{'pos': [10, 12], 'cl': [12, 120, 23],'w':1},
                                  {'pos': [10, 15], 'cl': [120, 12, 23],'w':1}]
        self.gril_game                                  =   {}
        self.gril_game[16]                              =   {}
        self.gril_game[16]                              =   {
                                (12, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (11, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (13, 10): {'w': 0, 'cl': [250, 0, 250]},
                                 (10, 10): {'w': 0, 'cl': [250, 0, 250]}}
        self.gril_game[16]['on']                        =   1
        self.gril_game[16]['ajt']                       =   [0,0]
        self.gril_game[16]['var']                       =   {}
        self.gril_game[16]['taile']                     =   16
        self.gril_game[8]                               =   {}
        self.gril_game[8]                               =   {
                                (21, 19): {'w': 1, 'cl': [20, 0, 250]},
                                 (11, 11): {'w': 1, 'cl': [20, 0, 250]},
                                 (13, 11): {'w': 1, 'cl': [20, 0, 250]},
                                 (10, 11): {'w': 1, 'cl': [20, 0, 250]}}
        self.gril_game[8]['on']                         =   1
        self.gril_game[8]['ajt']                        =   [0,0]
        self.gril_game[8]['var']                        =   {}
        self.gril_game[8]['taile']                      =   8

    def nez(self):
        ''
        if self.pad !={}:return -1
        a= pygame.joystick.get_count()
        for i in range(a):
            self.pad.update(self.ne2(i))
        return self.pad
    def ne2(self,i):
            pos                                         =   self.pad_ij[i]["pos"]
            w                                           =   self.pad_ij[i]["w"]
            cl                                          =   self.pad_ij[i]["cl"]
            return self.conf_pad(i,pos,w,cl)        

    def conf_pad(self,i,pos,w,cl):
        out5                                            =   {}
        out5["play"+str(i)]                             =   {}
        out5["play"+str(i)]["n_pad"]                    =   i
        out5["play"+str(i)]["on"]                       =   1
        out5["play"+str(i)]['joy']                      =   joystick01.jock(None,None,i)
        out5["play"+str(i)]['taile']                    =   16
        out5["play"+str(i)]['ajt']                      =   pos
        out5["play"+str(i)]['pos']                      =   {}
        out5["play"+str(i)]['pos'][(0,0)]               =   {}
        out5["play"+str(i)]['pos'][(0,0)]['size']       =   [0,0] 
        out5["play"+str(i)]['pos'][(0,0)]['szc']        =   [0,0]
        out5["play"+str(i)]['pos'][(0,0)]['cl']         =   cl
        out5["play"+str(i)]['pos'][(0,0)]["w"]          =   3
        #out5["play"+str(i)]['pos'][(0,0)]["taile"]      =   16
        
        out5["play"+str(i)]["afa"]                      =   100
        out5["play"+str(i)]["but"]                      =   {}
        out5["play"+str(i)]["but"]['app']               =   {}
        out5["play"+str(i)]["but"]["on"]                =   1
        out5["play"+str(i)]["but"][0]                   =   [255,0,0]
        out5["play"+str(i)]["but"][1]                   =   [0,0,255]
        out5["play"+str(i)]["but"][2]                   =   [0,255,0]
        out5["play"+str(i)]["but"][3]                   =   [0,0,0]
        out5["play"+str(i)]["but"]['w']                 =   0
        out5["play"+str(i)]["surface"]                  =   None
        out5["play"+str(i)]["pad_dir"]                  =   'pad_pos'
        out5["play"+str(i)]["pad_pos"]                  =   {}
        out5["play"+str(i)]["pad_pos"][1]  =   "pad['play"+str(i)+"']['ajt'][0]-=1"
        out5["play"+str(i)]["pad_pos"][2]  =   "pad['play"+str(i)+"']['ajt'][1]+=1"
        out5["play"+str(i)]["pad_pos"][3]  =   "pad['play"+str(i)+"']['ajt'][0]+=1"
        out5["play"+str(i)]["pad_pos"][4]  =   "pad['play"+str(i)+"']['ajt'][1]-=1"
        out5["play"+str(i)]["module"]                   =   {}
        #out5["play"+str(i)]["module"].update(self.vivien.make_surface("n_color",[70,70],[10,0],[2,255,250],16,0))

        return out5

                                  

    def mainloop(self):
        ''
        vivien.blit(root_s,hana.sur["n_root"])
        self.nez()
        for i in self.pad:
            vivien.draw_lib(hana.sur["n_root"]['surface'],self.pad[i]['pos'],self.pad[i]['ajt'])
        vivien.draw_pixel(hana.sur["n_root"]["surface"],self.gril_game[16])
        vivien.draw_pixel(hana.sur["n_root"]["surface"],self.gril_game[8])
       

    def display(self):
        ''
        for i in self.pad:
            rac= self.pad[i]["joy"]
            rac.direction()
            rac.button()
            if rac.but_s[:2]==["u",1]:
                lib.sv_lib(self.gril_game)
 
            


if __name__=='__main__':
    root                        =   pgwidth.width()
    root.size                   =   [600,400]
    root.ima_papier             =   [120,120,120]

    root.width()
    root_s                    =   {}
    root_s["taile"]             =16
    root_s["surface"]       =root.root

    hana                        =   hana(root.root,root)
    vivien                      =   pavi.vivien(root.root,root)
    lib                         =   pali.lib()
    
    hana.sur.update(vivien.make_surface('n_root',[500,400],[0,0],[255,255,255],16,1))
    

    root.act.append(hana)
    root.mainloop()
    
        
