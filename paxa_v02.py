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
import paxa_cmd
#v02

class anna:
    def __init__(self,root,rt):
        self.root                                   =   root
        self.rt                                     =   rt
        self.on                                     =   1

        self.n_root                                 =   {}
        self.pad                                    =   {}



        self.taile                                  =   0
        
        self.gril_game                              =   {}
        self.but_app                                =   {}#appuit sur button color
        self.but_app["app_cl"]                      =   {}
        self.but_app["app_cl"]['on']                =   0

        self.rac                                    =   None
        self.ra                                     =   None

        self.app_ext                                =   {}
        
    def re_init(self,fl="paxa_config.txt"):
        ""
        

    def joystick(self):
        ""
        for i in anna.pad:
            c_cmd.pi                                    =   i
            c_cmd.rac                                   =   anna.pad[i]["joy"]
            c_cmd.ra                                    =   anna.pad[i]
            c_cmd.rac.direction()
            c_cmd.rac.button()
            if c_cmd.rac.dire_s[0]  =="s" or c_cmd.rac.dire_s[0]=="u":
                c_cmd.cmd_pad()
            if c_cmd.rac.but_s[0]         =="u" and c_cmd.ra['but']['on']==1:
                c_cmd.cmd_pad_plcl()
            #----------------  V  C O L O R    ON/OFF
            if c_cmd.rac.but_s[0] =="s" and c_cmd.rac.but_s[2] ==2:
                c_cmd.cmd_v_color_on()
            if c_cmd.rac.but_s[0]     =="s" and c_cmd.rac.but_s[2] ==1:
                c_cmd.cmd_v_color_off()

            """
            #print rac.but_s
            
            if 1<=rac.dire_s[1]<=4:
                if rac.dire_s[0]    =="s" or rac.dire_s[0]=="u":
                    if ra["on"] ==1:
                        exec(ra['pad_pos'][rac.dire_s[1]])
                        if ra["module"]["n_color"]["on"]   ==1:
                            a,b             =   m_palcl.curseur["ajt"]
                            c,d             =   m_palcl.pal_cl['ajt']
                            e               =   (a+c,b+d)
                            f               =   m_palcl.pal_cl.keys().count(e)
                            m_palcl.curseur['var']=None
                            if f==1:m_palcl.curseur['var'] =m_palcl.pal_cl[e]
                            self.but_app["app_cl"]["on"]        =   1
                            self.but_app["app_cl"]["play"]      =   i
                            self.but_app["app_cl"]["n_butt"]    =   m_palcl.curseur['var']['cl'] 
                            
                            #self.but_app=[ m_palcl.curseur['var']['cl'],i]

                        
            if 0<=rac.but_s[1]<=3:
                if rac.but_s[0]     =="u" and ra['but']['on']==1:
                    #print ra["but"][rac.but_s[1]],i
                    #self.but_app                    =   [rac.but_s[1],i]
                    self.but_app["app_cl"]["on"]        =   1
                    self.but_app["app_cl"]["play"]      =   i
                    self.but_app["app_cl"]["n_butt"]    =  ra["but"][rac.but_s[1]] 
            
                    
    #  ---------------------- V   C O L O R  ---------------------------       
                if rac.but_s[0] =="s" and rac.but_s[2] ==2 and ra["module"]["n_color"]["on"] ==1:
                    ra['but']['on']                     =   1
                    ra["module"]["n_color"]["on"]       =   0
                    
                if rac.but_s[0]     =="s" and rac.but_s[2] ==1 and ra["module"]["n_color"]["on"] ==0:
                    rac.but_s[2] =-1
                    ra['but']['on']                 =   0
                    ra["module"]["n_color"]["on"]   =   1
                
                
                    
                
                if ra["module"]["n_color"]["on"]   ==1:
                    rac0    =   m_palcl.curseur['ajt']
                    
                    
                    if      rac.but_s[:2] ==['u',0]:rac0[0] -=1
                    elif    rac.but_s[:2] ==['u',1]:rac0[1] +=1
                    elif    rac.but_s[:2] ==['u',2]:rac0[0] +=1
                    elif    rac.but_s[:2] ==['u',3]:rac0[1] -=1
                    
                    if      rac.but_s[:2] ==['s',0]:rac0[0] +=1
                    elif    rac.but_s[:2] ==['s',1]:rac0[1] -=1
                    elif    rac.but_s[:2] ==['s',2]:rac0[0] -=1
                    elif    rac.but_s[:2] ==['s',3]:rac0[1] +=1
                    
                    
                    
                    
            
            if rac.but_s[:2] ==["s",5]:
                self.gril_game[0]["ajt"][0] +=8
                ra["ajt"][0]+=8
                
            #---------------S A V E   O P E N----------------------------
            if rac.but_s[:2] ==["s",6]:
                print " ---"*3,"S A V E","--"*3
                svme.save_gril(self.gril_game)
                
            if  rac.but_s[:2]                           ==["s",7]:
                ra_op       =   self.gril_game["OPEN"]  #°°°°°°°°°°°°°
                print " ---"*3,"O P E N","--"*3
                #             ----------------
               

                    
                if  ra_op["on"]                         ==0:
                    #svme.open_on()
                    ""
                    
                    ir                                      =   self.gril_game.keys()
                    ir.remove("OPEN")
                    ra_op["var"]["claque"]                  =   []
                    for i in ir:
                        if self.gril_game[i]["on"]          ==1:ra_op["var"]["claque"].append(i)
                    self.gril_game[i]["on"]             =   0
                    ra_op['on']                         =   1
                    ra_op["var"]["taile"]= self.n_root['n_root']['taile']
                    self.n_root['n_root']['taile']      =   2    
                    si                                  =   100
                    ra_op["var"]["ajt"]=   ra["ajt"]
                    ra["ajt"]                           =   [-10,-12]
                    ra_op["var"]["taile_pad"] =ra['pos'][ra["pos"].keys()[0]]['taile']
                    ra['pos'][ra["pos"].keys()[0]]['taile'] =si*2

                    self.gril_game["OPEN"]["fl"]        =   {}
                    self.gril_game["OPEN"]["old_pos"]   =   None
                
                    op_a                                =   svme.open_gril()
                    ib                                  =   0
                    ic                                  =   0
                    for i in op_a:
                        exec(i)
                        
                        self.gril_game["OPEN"]["fl"][(ic,ib)]=nana[0]
                        
                        op_b                            =   m_selc.couper(nana[0],[0,0,10000,10000])
                        op_c                            =   m_selc.mis_zero(op_b[0],op_b[1][:2],[ic*100,ib*100])
                        self.gril_game["OPEN"].update(op_c)
                        ic +=1
                        if ic>3:
                            ic                          =   0
                            ib                          +=1
                    
                else   :
                    ra_op["on"]        =   0
                    print " ---"*3,"N O","--"*3
                    
                    self.n_root['n_root']['taile']      =   ra_op["var"]['taile']
                    ra["ajt"]                           =   [10,10]#ra_op["var"]['ajt']
                    ra['pos'][ra["pos"].keys()[0]]['taile'] = ra_op["var"]['taile_pad']
                    for i in ra_op["var"]["claque"]:
                        self.gril_game[i]["on"]         =   1
                    

                
    #-----------------------------------------------------------------------
                
    """
    def n_color(self,play):
        if anna.pad[play]["module"]["n_color"]["on"]   ==0:return -1
        rac_p       =   anna.pad[play]
        rac         =   rac_p["module"]["n_color"]
        sur       =     anna.n_root["n_root"]
        
        vivien.blit(sur,rac)  #<<- n_color
        a,b                                         =   rac_p["pos"].keys()[0]
        c,d                                         =   rac_p["ajt"]
        e,f                                         =   [a+c+2,b+d+2]
        rac["pos"]                                  =   (e,f)

        vivien.dr_pix(rac,m_palcl.pal_cl,-1)
        #--- C U R S E U R ----------
        m_palcl.curseur["taile"]    =m_palcl.pal_cl["taile"]
        vivien.dr_pix(rac,m_palcl.curseur,-1)
        

    def f_save_open(self):
        "f fonction"
        
        if self.gril_game["OPEN"]['on'] ==0:return
        ra          =   anna.pad["play0"]
        c,d         =   ra["ajt"]
        a,b         =   ra['pos'].keys()[0]
        pos         =   [a+c,b+d]
        if self.gril_game["OPEN"]["old_pos"] !=pos:
            self.gril_game["OPEN"]["old_pos"] = pos
        vivien.dr_pix(anna.n_root["d_disp"],
                              self.gril_game["OPEN"]['fl'][(a+c,b+d)],4)
        print ra["joy"].but_s
            
        
        
      
        
    def module_conf(self,module):
        ""
        
        for i in self.pad:
            for ib in module:
                self.pad[i]["module"][ib]                   =   {}
                self.pad[i]["module"][ib]                   =   module[ib].make_module()["toor"]
                self.pad[i]["module"][ib]["mod_name_"]      =   module[ib]
                self.pad[i]["module"]["n_color"]["on"]     =   0
                
                
        
                
    def mainloop(self):
        ""
        anna.joystick()
        if self.but_app["app_cl"]["on"] ==1:
            vivien.make_pixel(self.but_app["app_cl"],anna.pad,self.gril_game[0])
           
        
        
    def display(self):
        ""
        rac_r       =   anna.n_root["n_root"]
        vivien.blit(root_s,rac_r)
        vivien.blit(root_s,anna.n_root["d_disp"])
        vivien.draw_pixel(rac_r,self.gril_game,None)
        #vivien.draw_pixel(anna.n_root["d_disp"],self.gril_game,2)
        
        for i in anna.pad:
            
            rac                                     =   anna.pad[i]
            vivien.draw_lib(rac_r['surface'],rac["pos"],rac['ajt'])
            self.n_color(i)
        anna.f_save_open()
        

        

if __name__ == '__main__':
    root                            =   pgwidth.width()
    root.size                       =   [1200,700]
    root.ima_papier                 =   [255,250,200]
    
    
    root.width()
    root_s                          =   {}
    root_s["taile"]                 =   1
    root_s["surface"]               =   root.root
    
    anna                            =   anna(root.root,root)
    hana                            =   paha.hana(root.root,root)
    vivien                          =   pavi.vivien(root.root,root)
    m_palcl                         =   paxa_ncolor.n_color(root.root,root)
    m_selc                          =   paxa_select.selc(None,None)
    c_cmd                           =   paxa_cmd.cmd(anna)
    anna.n_root.update(vivien.make_surface("n_root",[1000,700],[280,0],[250,255,250],16,1))
    anna.n_root.update(vivien.make_surface("d_disp",[280,200],[20,10],[255,255,255],2,1))
    anna.pad.update(hana.nez())
    anna.gril_game.update(vivien.make_gril(0,16))
    anna.gril_game.update(vivien.make_gril("OPEN",100))
    anna.gril_game["OPEN"]["on"]    =   0
    

    anna.module_conf({"n_color":m_palcl})

    svme        =paxa_save.svop(anna)
    
        
    
        
    anna.app_ext["hana"]        =   hana
    anna.app_ext["vivien"]      =   vivien
    anna.app_ext["m_palcl"]     =   m_palcl
    
    root.act.append(anna)
    root.mainloop()
        

        

    
        
        
        
        
