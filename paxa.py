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
#import paxa_save_mi     #mission impossible
import paxa_svop
import paxa_FJoyDire
import paxa_select
import paxa_cadre
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
        self.gril_open                              =   {}
        self.gril_sel                               =   {}
        self.gril_but                               =   {}

        self.gril_                                  =   {}
        self.gril_d                                 =   {}
        self.gril_d["d"]                =   {}
        self.gril_d['d']["g"]           =   self.gril_game
        self.gril_d['d']['v']           =   2
        self.gril_d['d']['c']           =   None
        self.gril_d["n"]                =   {}
        self.gril_d['n']['g']           =   self.gril_game
        self.gril_d['n']['v']           =   None
        self.gril_d['n']['c']           =   None
        self.but_app                                =   {}#appuit sur button color
        self.but_app['app_cl']                      =   {}
        self.but_app['app_cl']['on']                =   0

        self.v_pastel                               =   {}

        self.ima                =   pygame.image.load("paxa_image/sol.png")

        #self.para                                   =   {}

    def init_import(self):
        self.svme                       =   paxa_save.svop(anna)
        self.m_selc                     =   paxa_select.selc(self)
        self.svop                       =   paxa_svop.opensavefl(self)
        self.f_dire                     =   paxa_FJoyDire.funct(self)

    def init_claque(self):
        ''
        self.n_root['cl_']['variable']              = {}
        self.n_root['cl_']['variable']["focus"]     = 0
        self.n_root['cl_']['variable']["atv"]       = 0
        self.n_root['cl_']['variable']["sel"]       = {0:self.n_root['cl0'],
                                                       1:self.n_root['cl1'],
                                                       2:self.n_root['cl2'],
                                                       3:self.n_root['cl3']}
        
        
        self.n_root['cl0']['variable']              = {}
        self.n_root['cl0']['variable']["focus"]     = 0
        self.n_root['cl0']['variable']["atv"]       = 1
        
        self.n_root['cl1']['variable']              = {}
        self.n_root['cl1']['variable']["focus"]     = 0
        self.n_root['cl1']['variable']["atv"]       = 0
        
        self.n_root['cl2']['variable']              = {}
        self.n_root['cl2']['variable']["focus"]     = 0
        self.n_root['cl2']['variable']["atv"]       = 0
        
        self.n_root['cl3']['variable']              = {}
        self.n_root['cl3']['variable']["focus"]     = 0
        self.n_root['cl3']['variable']["atv"]       = 0
        

        
        
    def re_init(self,fl="paxa_config.txt"):
        ""

    
        

    def joystick(self):
        ""
        for i in anna.pad:
            rac                 =   self.pad[i]['joy']
            ra                  =   self.pad[i]
            ra_op               =   self.gril_open['OPEN']
            #ra_op["var"][i]                 =   {}
            #ra_op_pa                        =   ra_op["var"]
            rac.direction()
            rac.button()
            #rac.axie_1()
            #if ra['on'] ==1:self.f_dire.dire(i,rac.dire_s)
        
            #print rac.ax_s
            #if rac.ax_s[0]=="u" or rac.ax_s[0]=="s":print rac.ax_s
            if 1<=rac.dire_s[1]<=4:
                
                if rac.dire_s[0]    =="s" or rac.dire_s[0]=="u":
                #if rac.ax_s[0]=="u" or rac.ax_s[0]=="s":
                    if ra['on'] ==1:
                        v_exec      ="anna."+ra['pad_pos'][rac.dire_s[1]]
                        exec(v_exec)
                        if ra['module']['n_color']['on']   ==1:
                            
                            
                            a,b             =   m_palcl.curseur['ajt']
                            c,d             =   m_palcl.pal_cl['ajt']
                            e               =   (a+c,b+d)
                            f               =   m_palcl.pal_cl['m_pos'].keys().count(e)
                            m_palcl.curseur['var']              =   None
                            if f==1:m_palcl.curseur['var']      =   m_palcl.pal_cl['m_pos'][e]
                            self.but_app['app_cl']['on']        =   1
                            self.but_app['app_cl']['play']      =   i
                            self.but_app['app_cl']['n_butt']    =   m_palcl.curseur['var']['cl'] 
                            
                            #self.but_app=[ m_palcl.curseur['var']['cl'],i]
                
                        

            
            if 0<=rac.but_s[1]<=3:

                if ra["module"]['sele']['on'] ==2 and rac.but_s[0]     =="u":
                    ra["module"]['sele']["but_app"] =rac.but_s[:2][:]
                    
                    
                    
                    
                
                if rac.but_s[0]     =="u" and ra_op['on']==1:
                    ra_op['var'][i]['but_app']          =rac.but_s[:]
                    
                    
                    
                #butt color mode 0
                if rac.but_s[0]     =="u" and ra['but']['on']==1 :
                    self.but_app['app_cl']['on']        =   1
                    self.but_app['app_cl']['joy']       =   i
                    self.but_app['app_cl']['n_butt']    =  ra['but'][rac.but_s[1]] 
                    
                    
    #  ---------------------- V   C O L O R  ---------------------------
                #  V COLOR  ON
                #if rac.but_s[0] =="s" and self.gril_open['OPEN']['on']==0:
                if rac.but_s[0] =="s" and ra['but']['on']==1: 
                    if rac.but_s[2] ==1 and ra['module']['n_color']['on'] ==0 and ra["module"]['sele']['on']==0:
                        rac.but_s[2]                    =   -1
                        ra['but']['on']                 =   0
                        ra['module']['n_color']['on']   =   1
                        

                #  V COLOR  OFF
                if ra['module']['n_color']['on'] ==1:
                    if rac.but_s[2] ==2:
                        ra['but']['on']                     =   1
                        ra['module']['n_color']['on']       =   0

                        a,b             =   m_palcl.curseur['ajt']
                        c,d             =   m_palcl.pal_cl['ajt']
                        e               =   (a+c,b+d)
                        ra['but'][rac.but_s[1]] = m_palcl.pal_cl["m_pos"][e]['cl']
                                        
                    if rac.but_s[0]=='r' and rac.but_s[2]==0:
                        rac.but_s[2]                    = -1
                        
                        exec(m_palcl.curseur['pad_pos']['fm']+m_palcl.curseur['pad_pos'][rac.but_s[1]+1])
                        if      m_palcl.curseur['ajt'][0] <0:m_palcl.curseur['ajt'][0]=m_palcl.pal_cl['lim'][0]
                        elif    m_palcl.curseur['ajt'][0] >m_palcl.pal_cl['lim'][0]:m_palcl.curseur['ajt'][0]=0
                        elif    m_palcl.curseur['ajt'][1] <0:m_palcl.curseur['ajt'][1]=m_palcl.pal_cl['lim'][1]
                        elif    m_palcl.curseur['ajt'][1] >m_palcl.pal_cl['lim'][1]:m_palcl.curseur['ajt'][1]=0


            #------------------ S E L E C T
            if ra["module"]['sele']['on'] ==2 and rac.but_s[:2] ==['u',7]:
                ra["module"]['sele']['on']              =   0
                ra['but']['on']                         =   1
                
                

            if rac.but_s[:2] ==['s',7] and ra["module"]['sele']['on']==0:
               
                ra['but']['on']                         =   0
                ra['module']['n_color']['on']           =   0
                ra["module"]['sele']['on']              =   1
                ra["module"]['sele']['but_app']         =   {}
                ra["module"]['sele']['but_app_act']     =   0
                ra["module"]['sele']['touch']           =   0
                
                ra["module"]['sele']['dp']              = ra["ajt"][:]
            if rac.but_s[:2] !=['r',7] and ra["module"]['sele']['on']==1:
                ra["module"]['sele']['end']             =   ra["ajt"][:]
            if rac.but_s[:2] ==['r',7] and ra["module"]['sele']['on']==1:
                ra["module"]['sele']['on']              =   2
                
                
                
            #------------------ C L A Q U E
            rac_cla     =   self.n_root['cl_']['variable']  #<--- rac
           
            if rac.but_s[:2] ==["s",4]:
                if rac_cla['focus']                     ==0:
                    print 'claque_ ON'
                    rac_cla['focus']                    =   1
                    rac_cla['joy']                      =   i
                    self.n_root['cl_']["ajt"]           =   [0,0]
                    # --- O F F --
                    ra["on"]                            =   0
                    ra['but']['on']                     =   0
                    ra['module']['n_color']['on']       =   0
                    self.n_root['cl_']['cl']            =   [255,255,144]
                elif  rac_cla['focus']==1:
                    print 'claque_ OFF'
                    rac_cla['focus']                    =   0
                    # --- O N --
                    ra["on"]                            =   1
                    ra['but']['on']                     =   1
                    self.n_root['cl_']['cl']            =   [255,255,255]
            if rac_cla['focus']==1:
                if rac.dire_s                           ==["u",1]:
                    rac_cla["sel"][self.n_root['cl_']["ajt"][0]]["cl"]=[255,255,255]                    
                    self.n_root['cl_']["ajt"][0] -=1
                    rac_cla["sel"][self.n_root['cl_']["ajt"][0]]["cl"]=[255,0,0]
                elif rac.dire_s                         ==["u",3]:
                    rac_cla["sel"][self.n_root['cl_']["ajt"][0]]["cl"]=[255,255,255]                    
                    self.n_root['cl_']["ajt"][0] +=1
                    rac_cla["sel"][self.n_root['cl_']["ajt"][0]]["cl"]=[255,0,0]

                elif rac.dire_s                         ==["u",2]:
                    self.n_root['cl_']["ajt"][1] -=1
                elif rac.dire_s                         ==["u",4]:
                    self.n_root['cl_']["ajt"][1] +=1
                    
                
                
                

                
                


                
            #------------------ Z  O O M
            #print rac.but_s[:2]
            
            if rac.but_s[1] ==[5]:
                ""
                #self.gril_game[0]['ajt'][0] +=8
                #ra['ajt'][0]+=8
                #self.gril_d["n"]["v"]=2
           
                
                

#---------------S A V E   O P E N----------------------------
                
            if rac.but_s    ==  ["s",13,2] and ra_op['on'] ==0:
                
                
                self.svme.sv_parametre(i)
                
                ra_op['var']["p"]                   =   i
                ra_op['var']["home"]                =   [0]
                ra_op['var']["fl"]                  =   "paxa_save/menu.txt"
                ra_op['on']                         =   1
                ra['module']['n_color']['on']       =   0


                ra_op["m_pos"][(5,4)]       ={"type":"img",
                                              "img":pygame.image.load("paxa_image/menu/save.png")}
                ra_op["m_pos"][(5,5)]       ={"type":"img",
                                              "img":pygame.image.load("paxa_image/menu/open.png")}
                ra_op["m_pos"][(5,6)]       ={"type":"img",
                                              "img":pygame.image.load("paxa_image/menu/lib.png")}

                ra['ajt']                           =   [5,4]
                ra['taile']                         =   64
                ra["pos"][(0,0)]["size"]            =   [200,0]
                ra["pos"][(0,0)]["szc"]             =   [-20,-10]
                self.gril_d["n"]["g"] =anna.gril_open
                self.gril_d['n']['v']=None
                
            if rac.but_s    ==  ["s",13,1] and ra_op['on'] ==1:
                ra_op['on']                         =   0
                print " ---"*3,"OPEN F I N","--"*3
                self.svme.open_off()
                
            
            
           
    def on_onoff(self,mm):
        ""                             
                
    #-----------------------------------------------------------------------


    def claque(self):
        if self.n_root['cl_']['variable']['focus']!=1:
            #self.n_root['cl_']['cl']=[255,144,144]
            self.n_root['cl_']['cl']=[255,255,255]
            return
        if self.n_root['cl_']['on']!=1:return

        name            =    self.n_root['cl_']['variable']['joy']
        print self.n_root['cl_']["ajt"]
        
    def m_sele(self):
        ''
        for i in anna.pad:
            ra                                      =   anna.pad[i]
            ra_m                                    =   ra['module']['sele']
            if  ra["module"]["sele"]['on']        ==0:return
            
            #ra["module"]['sele']['dp']
            ax,bx     =vivien.pos_table(ra_m['dp'],anna.n_root['n_root'])[0]
            cx,dx     =vivien.pos_table(ra_m['end'],anna.n_root['n_root'])[0]
            dx,ex     =   cx-ax,dx-bx
            pygame.draw.rect(anna.n_root['n_root']['surface'],[0,0,0],[ax,bx]+[dx,ex],5)

            
            a,b             =ra_m['dp']
            c,d             =ra_m['end']
            e,f             =ra["ajt"]
            
            if a-1<e<c and b-1<f<d:
                ra["module"]['sele']['touch']       =   1
                pygame.draw.rect(anna.n_root['n_root']['surface'],[205,120,250],[ax,bx]+[dx,ex],5)
            else:ra["module"]['sele']['touch']      =   0

            if ra_m['but_app_act']                  ==1:
                pygame.draw.rect(anna.n_root['n_root']['surface'],[255,180,250],[ax,bx]+[dx,ex],5)
                
            
            if ra_m["but_app"]                      !=None:
                if ra_m["but_app"] ==['u',1] and ra_m['touch']==   1 and ra_m['but_app_act'] ==0:
                    ra_m['but_app_act']             =   1
                    ra_m["but_app"]                 =   None
                    aa,ab                           =   ra_m['dp']
                    a                               =   [aa-1,ab-1]
                    b                               =   ra_m['end']
                    op_b                            =   self.m_selc.couper(self.gril_game[0]["m_pos"],a+b)
                    op_bb                           =   op_b[1]
                    px,py                           =   0,0
                    op_c                            =   self.m_selc.mis_zero(op_b[0],op_bb[:2],[0,0])
                   
                        
                        
                    self.v_pastel[i]                =   {}
                    self.v_pastel[i].update(op_c)
                
                if ra_m['but_app_act'] ==1 and ra_m["but_app"] ==['u',1]:
                    ajx,ajy     =   ra["ajt"][:]
                    for ii in self.v_pastel[i]:
                        sx,sy   =ii
                        self.gril_game[1]["m_pos"][(ajx+sx,ajy+sy)] =self.v_pastel[i][ii]
                           
                #print ra["module"]['sele']['dp'],ra["module"]['sele']['end'],
                #print ra["ajt"],ra["module"]['sele']["but_app"]
                ra_m["but_app"] =None
                

    def n_color(self,play):
        if anna.pad[play]['module']['n_color']['on']   ==0:return -1
        rac_p                                       =   anna.pad[play]
        rac                                         =   rac_p['module']['n_color']
        sur                                         =   anna.n_root['n_root']
        
        vivien.blit(sur,rac)  #<<- n_color
        a,b                                         =   rac_p['pos'].keys()[0]
        c,d                                         =   rac_p['ajt']
        e,f                                         =   [a+c+2,b+d+2]
        rac['pos']                                  =   (e,f)

        vivien.dr_pix(rac,m_palcl.pal_cl,-1)
        #--- C U R S E U R ----------
        m_palcl.curseur['taile']                    =   m_palcl.pal_cl['taile']
        vivien.dr_pix(rac,m_palcl.curseur,-1)
        

    def f_save_open(self):
        "f fonction"
        
        
        
        if self.gril_open["OPEN"]['on']             ==0:return
        name        =   self.gril_open['OPEN']["var"]['p']
        ra_op       =   self.gril_open['OPEN']  #<--- raco
        ra          =   self.pad[name]          #<--- raco


        if ra_op['var']["home"][-1]                    =="open":
             self.svop.op_d()
             
        if ra_op['var'][name]['but_app']            !={}:
            
            if ra['ajt']==[5,4]:
                "save"
                self.svop.op_save("paxa_save/paxa_sv.txt")
                
            elif ra['ajt']==[5,5]:
                "OPEN"
                self.svop.op_disp()
                

            elif ra_op['var']["home"][-1]                 =="open":
                self.svop.op_dire()

            ra_op['var'][name]['but_app']               =   {}
        
            
                    
            
        

    def re_grilopen(self):
        anna.gril_open.update(vivien.make_gril("OPEN",100))
        anna.gril_open['OPEN']['on']                        =   0
            
        
        
      
        
    def module_conf(self,module):
        ""
        for i in self.pad:
            self.pad[i]['module']['sele']                   =   {}
            self.pad[i]['module']['sele']['on']             =   0
            self.pad[i]['module']['sele']['dp']             =   [0,0]
            self.pad[i]['module']['sele']['end']            =   [0,0]
            
            for ib in module:
                self.pad[i]['module'][ib]                   =   {}
                self.pad[i]['module'][ib]                   =   module[ib].make_module()['toor']
                self.pad[i]['module'][ib]['mod_name_']      =   module[ib]
                self.pad[i]['module']['n_color']['on']      =   0

    def disp_but(self):
        ""
        rac_b       =   anna.gril_but['d_but']["m_pos"]
        for i in self.pad:
        
            ra_b        =   anna.pad[i]['but']
            rac_b[(0,1)]['cl'] =ra_b[0]
            rac_b[(1,2)]['cl'] =ra_b[1]
            rac_b[(2,1)]['cl'] =ra_b[2]
            rac_b[(1,0)]['cl'] =ra_b[3]
        
            
        
        
                
        

    def metres_zero(self,nzero):
        ""
        
        
        
    def mainloop(self):
                                                           
        ""
        anna.joystick()
        if self.but_app['app_cl']['on'] ==1 and self.gril_open['OPEN']['on']==0:
            vivien.make_pixel(self.but_app['app_cl'],anna.pad,self.gril_game[0])
        self.disp_but()
        
        
    def display(self):
        ""
        rac_r       =   anna.n_root
        vivien.blit(root_s,rac_r['cl_'])
        vivien.blit(self.n_root['cl_'],rac_r['cl0'])
        vivien.blit(self.n_root['cl_'],rac_r['cl1'])
        vivien.blit(self.n_root['cl_'],rac_r['cl2'])
        vivien.blit(self.n_root['cl_'],rac_r['cl3'])
        
        vivien.blit(root_s,rac_r['n_root'])
        vivien.blit(root_s,rac_r['d_but'])
        vivien.blit(root_s,rac_r['d_disp'])
        vivien.blit(root_s,rac_r['d_lib'])
        
              
        vivien.draw_pixel(rac_r['d_disp'],self.gril_d['d']["g"],self.gril_d['d']['v'])
        vivien.draw_pixel(rac_r['n_root'],self.gril_d['n']['g'],self.gril_d['n']['v'])

        vivien.draw_pixel(anna.n_root['d_but'],self.gril_but,None)

        rac_r['d_lib']['surface'].blit(self.ima,[0,0])
        #rac_r['d_lib']['surface'].blit(self.ima,[65,0])

        #self.gril_sel[0]["m_pos"][(0,0)]={"type":"img","data"}
        
        
        
        
        for i in anna.pad:
            rac                                     =   anna.pad[i]
            vivien.draw_lib(rac_r['n_root']['surface'],rac,rac['ajt'])
            self.n_color(i)
        anna.f_save_open()
        anna.m_sele()
        anna.claque()
        

        

if __name__ == '__main__':
                                                           
    root                            =   pgwidth.width()
    root.size                       =   [1300,700]
    root.ima_papier                 =   [192,192,192]
    
    
    root.width()
    root_s                          =   {}
    root_s['taile']                 =   1
    root_s['surface']               =   root.root
    
    anna                            =   anna(root.root,root)
    hana                            =   paha.hana(root.root,root)
    vivien                          =   pavi.vivien(root.root,root,anna)
    m_palcl                         =   paxa_ncolor.n_color(root.root,root)
    #m_selc                          =   paxa_select.selc(None,None)
    #anna.n_root.update(vivien.make_surface("cl_",[260,70],[0,0],[255,144,144],1,1))
    anna.n_root.update(vivien.make_surface("cl_",[260,70],[5,5],[255,255,255],1,1))
    anna.n_root.update(vivien.make_surface("cl0",[60,30],[5,20],[255,255,255],16,1))
    anna.n_root.update(vivien.make_surface("cl1",[60,30],[67,20],[255,255,255],16,1))
    anna.n_root.update(vivien.make_surface("cl2",[60,30],[129,20],[255,255,255],16,1))
    anna.n_root.update(vivien.make_surface("cl3",[60,30],[191,20],[255,255,255],16,1))
    
    anna.n_root.update(vivien.make_surface("n_root",[1000,700],[280,0],[255,255,255],16,1))
    anna.n_root.update(vivien.make_surface("d_disp",[280,200],[20,85],[255,255,255],2,1))
    anna.n_root.update(vivien.make_surface("d_but",[300,100],[0,290],[255,255,255],30,1))
    anna.n_root.update(vivien.make_surface("d_lib",[300,300],[0,400],[255,255,255],30,1))        

    anna.pad.update(hana.nez())
    anna.gril_      .update(vivien.make_gril(0,8))
    anna.gril_game  .update(vivien.make_gril(0,8))
    anna.gril_game  .update(vivien.make_gril(1,8))
    anna.gril_sel   .update(vivien.make_gril(0,100))
    anna.gril_but.update(vivien.make_gril("d_but",16))
    anna.gril_open.update(vivien.make_gril("OPEN",100))
    anna.gril_open['OPEN']['on']               =   0



    g_but =anna.gril_but['d_but']["m_pos"]
    
    g_but[(0,1)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(1,0)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(2,1)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(1,2)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}

    g_but[(4,1)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(5,0)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(6,1)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}
    g_but[(5,2)]            =   {'taile': 16, 'w': 0, 'cl': [0, 0, 255]}

    m_palcl.curseur['pad_pos'] ={}
    m_palcl.curseur['pad_pos']['fm']    ="m_palcl."
    
    m_palcl.curseur['pad_pos'][1]       ="curseur['ajt'][0]-=1"
    m_palcl.curseur['pad_pos'][2]       ="curseur['ajt'][1]+=1"
    m_palcl.curseur['pad_pos'][3]       ="curseur['ajt'][0]+=1"
    m_palcl.curseur['pad_pos'][4]       ="curseur['ajt'][1]-=1"
    

    anna.module_conf({"n_color":m_palcl})

    #svme        =paxa_save.svop(anna)
    #svmemi      =paxa_save_mi.svop(anna)
    
        
    
    anna.init_claque()
    anna.init_import()
    root.act.append(anna)
    root.mainloop()
        

        

    
        
        
        
        
