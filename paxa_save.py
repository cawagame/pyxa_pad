# -*- coding: utf-8 -*-
import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
#import pgrentrypy
import sys

import pavi

import anna01_varaiable
import paxa_select


class svop:
    def __init__(self,old):
        ""
        self.old                =   old
        #self.m_selc             =   paxa_select.selc(None,None)

        
        

    def re_init(self):
        ""

    def save_gril(self,g_g=None,fl="paxa_save/paxa_sv.txt"):
        ""
        for i in g_g:
            g_g[i]['on']=1
    
        lo =open(fl,"a")
        lo.write("nana="+str(g_g)+"\n")
        lo.close()
        

    def open_gril(self,fl="paxa_save/paxa_sv.txt"):
        lo                  =   open(fl,'r')
        lof                 =   lo.readlines()
        lo.close()
        
        return lof

    def open_on(self,fl="paxa_save/paxa_sv.txt",name=None):
        ""
        
       
        ra                  =   self.old.pad["play0"]       #--- raco
        ra_op               =   self.old.gril_open['OPEN']  #--- raco
        para                =   ra_op['var'][name]["disp"]
        #ra_op['var']['claque']                  =   []
        for i in self.old.gril_game:self.old.gril_game[i]['on'] =   0
        self.old.n_root['n_root']['taile']      =   2    
        ra['ajt']                               =   para["ajt"]
        ra['pos'][ra['pos'].keys()[0]]['taile'] =   para['size']*2
           
        

    
        ra_op['fl']                             =   {}
        op_a                                    =   self.open_gril(fl)
        op_a.reverse()
        ib                                      =   0
        ic                                      =   0
        l_op_a                                  =   len(op_a)
        for i in range(l_op_a):
            exec(op_a[i])
            
            ra_op['fl'][(ic,ib)]                =   {}
            ra_op['fl'][(ic,ib)]['nfl']         =   l_op_a-i-1
            ra_op['fl'][(ic,ib)]['nana']        =   nana
            

            
            op_b                                =   self.old.m_selc.couper(nana[0]['m_pos'],[0,0,10000,10000])
            op_bb                               =   op_b[1]
            px,py                               =   para["px_c"]
            #op_bb =[-100,-25,None,None]
            
            op_c=   self.old.m_selc.mis_zero(op_b[0],op_bb[:2],[ic*para["size"]+px,ib*para["size"]+py])
            self.old.gril_open['OPEN']["m_pos"].update(op_c)
            ic              +=1
            if ic>para['row']:
                ic                              =   0
                ib          +=1
        self.old.gril_open['OPEN']['lim']       =   [para['row'],ib]   
        

        
    def open_off(self,name=None):
        ""
        ra                  =   self.old.pad["play0"]       #--- raco
        ra['but']['on']                         =1
        name                ='play0'
        rac_op_pa           =   self.old.gril_open['OPEN']['var'][name]['sv_para']
        ra['module']['n_color']['on'] =0
        self.old.n_root['n_root']['taile']      =   rac_op_pa['taile']
        ra['ajt']                               =   rac_op_pa['ajt']
        ra['pos'][(0,0)]["size"]                =   rac_op_pa['size']  
        ra['taile']                             =   rac_op_pa['taile_pad']
        ra['pos'][(0,0)]["szc"]                 =   rac_op_pa['szc']
        for i in self.old.gril_game:self.old.gril_game[i]['on'] =   1
        self.old.gril_d["n"]["g"]               = self.old.gril_game
        self.old.gril_d["d"]["g"]               = self.old.gril_game 
        self.old.gril_d['d']['v']               =   rac_op_pa["dv"]
        self.old.gril_d['n']['v']               =   rac_op_pa["nv"]
        
        self.old.re_grilopen()
    def sv_parametre(self,name="sv"):
        ""
        ra                  =   self.old.pad["play0"]       #--- raco
        ra['but']['on']                         =   0
        ra["module"]['sele']['on']              =   0
        
        self.old.gril_open['OPEN']['var'][name]     ={}
        rac_op                                  =   self.old.gril_open['OPEN']['var'][name]

        rac_op['but_app']                       =   {}
        rac_op['sv_para']                       =   {}
        rac_op_pa                               =   rac_op['sv_para']   #--- raco
        rac_op_pa['taile']                      =   self.old.n_root['n_root']['taile']
        rac_op_pa['ajt']                        =   ra['ajt']
        rac_op_pa['size']                       =   ra['pos'][(0,0)]["size"]
        rac_op_pa['szc']                        =   ra['pos'][(0,0)]["szc"]
        rac_op_pa["taile_pad"]                  =   ra['taile']

        #rac_op_pa["dg"]                         =   self.old.gril_d['d']['g']
        rac_op_pa["dv"]                         =   self.old.gril_d['d']['v']
        #rac_op_pa["ng"]                         =   self.old.gril_d['n']['g']
        rac_op_pa["nv"]                         =   self.old.gril_d['n']['v']

        
        
