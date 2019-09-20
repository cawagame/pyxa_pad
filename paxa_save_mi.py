import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
#import pgrentrypy
import sys

import pavi

import paxa_select

class svop:
    def __init__(self,old):
        self.old            =old
        

    def f_open(self,name):
        ""
        "f fonction"
        
        ra_op       =   self.old.gril_open['OPEN'] #<--- raco
        ra          =   self.old.pad[name]
        
        if      ra['ajt'][0]    <   0               :ra['ajt'][0]=ra_op['lim'][0]
        elif    ra['ajt'][0]    >   ra_op['lim'][0] :ra['ajt'][0]=0
        elif    ra['ajt'][1]    <   0               :ra['ajt'][1]=ra_op['lim'][1]
        elif    ra['ajt'][1]    >   ra_op['lim'][1] :ra['ajt'][1]=0
        
        c,d         =   ra['ajt']
        if ra_op['fl'].keys().count((c,d))==0:ra['ajt']=[0,0]

    def f_openp2(self):
        ''
    def menu(self,name):
        ""
        ra_op       =   self.old.gril_open['OPEN'] #<--- raco
        ra          =   self.old.pad[name]
        a,b                                         =   ra['ajt']
        d                                           =   self.old.svme.open_gril()
        c                                           =   ra_op["fl"][(a,b)]['nfl']

        if      ra_op["var"]['home'][-1]==2         :self.menu_2x(c)
        if      ra_op["var"]['home'][-1]==0 and c==1:self.menu_01(name)     #open
        elif    ra_op["var"]['home'][-1]=="save":self.menu_save()         #save

    def menu_01(self,name):
        ra_op       =   self.old.gril_open['OPEN'] #<--- raco
        ra          =   self.old.pad[name]
        a                                           =   ra_op['var']
        #self.old.re_grilopen()
        #ra_op["var"].update(a)
        #ra_op['on']            =   1
        #ra_op['var']['home'].append(2)
        #ra_op['var']['fl']="paxa_save/paxa_sv.txt"
        ra_op['var'][name]['disp']                  =   {'row':8,'size':50,
                                                    'ajt':[0,0],"px_c":[0,0]}
        #ra["pos"][(0,0)]["size"]                    =   [0,0]
        #ra["pos"][(0,0)]["szc"]                     =   [0,0]
        self.old.svme.open_on(self.old.gril_open["OPEN"]['var']['fl'],name)
        

    def menu_save(self):
        ""
        self.old.svme.save_gril(self.old.gril_game)
        self.old.svme.open_off("play0")

    def menu_2x(self,nu):
        print nu,self.old.gril_open["OPEN"]['var']
        lo =self.old.svme.open_gril(self.old.gril_open["OPEN"]['var']['fl'][-1])
        exec(lo[nu])
        self.old.gril_game =nana
        self.old.svme.open_off("play0")
        print 'O P E N fichir','-----------------'
        

        
        
        
