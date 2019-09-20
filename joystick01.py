import pgwidth
import pgrect
#import pggame_key
import              pygame
from pygame.locals import *
import time
#import pgrentrypy
import sys


"""
axis

0   gauche -1 gauche        0
0   gauche 1 droite         1
1   gauche -1 haud          2
1   gauche 1 bas            3
2   droite  -1 gauche       4
2   droite 1 droite         5
3   /!\
4   /!\
5   droite -1 haut
5   droite 1 bas


    """

    
        
#import joystick
class jock:
    "2019 jocki"
    def __init__(self,root,rt,n):
        ""
        self.root   =root
        self.rt     =rt
        pygame.joystick.init()
        self.pad    =pygame.joystick.Joystick(n)
        self.pad.init()
        self.but            =   [0]*14
        self.but_c          =   [10]*14
        self.but_d          =   []   #dmupltiple button
        self.but_dc         =   [0,10,0]
        self.but_ds         =   [0]*8
        self.but_s          =   [None,None,0]#button solo
        
        #---------------------------------------------
        self.dire           =   [0]*8
        self.dire_c         =   [10]*8
        self.dire_d         =   []
        self.dire_s         =   [None,None]
        #--------------------------------------------
        self.ax             =   [0]*10
        self.ax_c           =   [10]*10
        self.ax_d           =   []
        self.ax01_s           =   [None,None]
        self.ax25_s           =   [None,None]
        self.ax_u           =   [0]*10

        self.p0             =   {}#valeur poubelle 
        



    #_________________B U T T O N ____________________________

    def button(self):
        for i in range(14):
            
            if self.pad.get_button(i)!=0:self.pad_button(i)
            else:self.but[i]=0
        if self.but.count(0)==14:
            self.but_ds =[None,None]
            self.but_s[0]='r'
            #self.but_s=[None,None]
        

    def pad_button(self,n):
        ""
                    
        self.but_d_ =self.but_d
        #print self.but_s,n,'----'
        if self.but.count(0)<14:
            
            self.but_s  =[None,None,0]
            
            #self.but[n] +=1
            #if self.but[n] ==self.but_c[n]:self.but[n]=1
            self.pad_but_plus()
        else:
            
            self.but_dc[0]=0
            self.pad_but_solo(n)

    def pad_but_solo(self,n):
        if self.pad.get_button(n) !=0:
            self.but_s[0]           =   "a"
            self.but_s[1]           =   n
            if self.but[n]==0:
                self.but_s[0]       =   "u"
                self.but_s[2]       =   0
            self.but[n] +=1
            if self.but[n] ==self.but_c[n]:
                self.but_s[0]       =   "s"
                self.but_s[2] +=1
                self.but[n]=1
        

    def pad_but_plus(self):
        "appuits sur plussieur a la foix"
        self.but_ds =[None,None]
        #print self.but_dc,self.but_ds,'ttttttttttt'
        if self.but_dc[0] ==1:
            self.but_ds =["u",self.but_d]
        
            #print 'rrrrrrr',self.but_ds,'================='
            
        if self.but_dc[0] ==self.but_dc[1]:
            #print 'ttttt'
            self.but_dc[0] =1
            self.but_ds =["s",self.but_d]
        
            #print '________','gggggg',self.but_ds
            
        self.but_dc[0]   +=1
        self.but_d        =   []
        #print self.but_dc
        
        
        for i in range(len(self.but)):
            if self.but[i] !=0:self.but_d.append(i)
        
        #print self.but,'_________________',self.but_d
        #self.but_ds=self.but_d
        #print self.but_d,self.but,self.but_dc

    #___________________ F I N __ B U T T O N _______________________



        
    #___________________ D I R E C T I O N _____________________________
    def direction(self):
        n                   =   self.pad.get_hat(0)
        if n==(0,0):self.dire_s=[None,None]
        if      n ==(0,0)   :d=None
        elif    n ==(-1,0)  :d=1    #<--
        elif    n ==(0,-1)  :d=2    #^
        elif    n ==(1,0)   :d=3    #--->
        elif    n ==(0,1)   :d=4    #bas
        elif    n ==(-1,-1) :d=5    #<--- ^
        elif    n ==(-1,1)  :d=6    #<---- bas
        elif    n ==(1,1)   :d=7    #---> bas
        elif    n ==(1,-1)  :d=8    #---> ^

        #if d !=0:self.croix_dire(d)
        
        for i in range(8):
            if i==d:self.croix_dire(d)
            else:self.dire[i]=0
        if self.dire.count(0)==8:
            ""
            #self.dire_s =[0]*8
            self.dire_s =[None,None]
        #print self.dire,self.dire.count(0)
        
    def croix_dire(self,d):
        self.dire_s         =   ["a",d]
        if self.dire[d] ==0:self.dire_s =["u",d]
        self.dire[d] +=1
        if self.dire[d] ==self.dire_c[d]:
            self.dire_s =["s",d]
            self.dire[d]=1

    def manette_info(self,act=None):
        
        if act[0] =='u':print ' '*2,act
        elif act[0] =='s':print " "*4,act,self.pad.get_hat(0)
        elif act[0] =='r':print " "*6,act,self.pad.get_hat(0)


    #___________________ F I N ______ D I R E C T I O N _____________________

    #______________________________ A X E __________________________


    def axie(self):
        ''
        self.ax01_s   =[None,None]
        self.ax25_s   =[None,None]

        
        
        for i in [0,1]:
            if int(self.pad.get_axis(i)*10) !=0:
                
                if      self.pad.get_axis(i)<0 and i==0:    da=1
                elif    self.pad.get_axis(i)<0 and i==1:    da=4
                elif    self.pad.get_axis(i)>0 and i==0:    da=3
                elif    self.pad.get_axis(i)>0 and i==1:    da=2
                self.ax01_s   =[self.pad.get_axis(i),da]
                
        da =0
        for i in [2,5]:
            if int(self.pad.get_axis(i)*10) !=0:
                
                if      self.pad.get_axis(i)<0 and i==2:    da=5
                elif    self.pad.get_axis(i)<0 and i==5:    da=8
                elif    self.pad.get_axis(i)>0 and i==2:    da=7
                elif    self.pad.get_axis(i)>0 and i==5:    da=6
                self.ax25_s   =[self.pad.get_axis(i),da]
                
            
            
                

    """
    def axie(self):
        ''
        da =[0,-1]
        for i in [0,1,2,5]:
          
            if self.pad.get_axis(i) !=0.0:
                if      self.pad.get_axis(i)<0 and i==0:    da=[1,0]
                elif    self.pad.get_axis(i)<0 and i==1:    da=[4,0]
                elif    self.pad.get_axis(i)>0 and i==0:    da=[3,0]
                elif    self.pad.get_axis(i)>0 and i==1:    da=[2,0]
            
                #elif    self.pad.get_axis(i)<0 and i==1:    da=5
                #elif    self.pad.get_axis(i)<0 and i==1:    da=6
                #elif    self.pad.get_axis(i)<0 and i==1:    da=7
                #elif    self.pad.get_axis(i)<0 and i==1:    da=8
        for i in range(1,5):
            if i ==da[0]:
                self.ax_comd(da)
            else:
                #print "no",da
                self.ax[i] =0
    def ax_comd(self,dai):
        
        da,i                =   dai
        self.ax_s=["a",da]
        a =abs(self.pad.get_axis(i))
        self.ax[da] +=a
        #print da,i,self.ax[da],a
        if .1<self.ax[da]<.6:
            self.ax_s= ["u",da]
            self.ax[da]=.7
        if self.ax[da]>self.ax_c[da]:
            self.ax[da]=.7
            self.ax_s= ["s",da]
        if self.ax_s[0]=="u" or self.ax_s[0]=="s":
            ""
            #print self.ax_s
            #print " "*10,self.ax[da],a,self.ax_s
    """
        
        
    """
    def axie(self):
        da                      =0
        old                     =None
        old_1                   =None
        #ge_axi                  =self.pad.get_axis(i)
        for i in range(6):
            ge_axi                  =self.pad.get_axis(i)
            if  ge_axi!=0.0:return
        
                #if      self.pad.get_axis(i)<0 and i==0:    da=1
                
            if    self.pad.get_axis(i)<0 and i==1:    da=2
                #elif    self.pad.get_axis(i)>0 and i==0:    da=3
                #elif    self.pad.get_axis(i)>0 and i==1:    da=4
            
                elif    self.pad.get_axis(i)<0 and i==1:    da=5
                elif    self.pad.get_axis(i)<0 and i==1:    da=6
                elif    self.pad.get_axis(i)<0 and i==1:    da=7
                elif    self.pad.get_axis(i)<0 and i==1:    da=8
                
            old             =self.ax[da]
            self.ax         =[0]*10
            self.ax[da]     =old
            #old_1           =self.ax_u[da]
            #self.ax_u       =[0]*10
            #self.ax_u[da]   =old_1
            #print da,self.pad.get_axis(i)
            print ge_axi,i
            if da !=0 and ge_axi !=0.0:
                print "=====",i,self.pad.get_axis(i),"-----------",da
                #self.axie_comd(ge_axi,da,i)

       
               
    def axie_comd(self,ge,d,i):
        #print "jujujuuuuuu"
        print d,i
        
        self.ax_s=["a",d]
        self.ax[d]  =self.ax[d]+abs(ge)
        if 2<abs(int(self.ax[d]*10))<20 :
            print 'tttt'
            self.ax_s           =["u",d]
            self.ax[d] =30
        print " "*10,self.ax[d],+abs(ge)
        if self.ax[d] >self.ax_c[d]:
            self.ax_s           =["s",d]
            self.ax[d]          =30
           
        #if self.ax_s[0]=="s":self.ax_u           =   0
        if self.ax_s[0]=="u" or self.ax_s[0]=="s":
            
            print '----------------------------------'
        print d,i,"____",self.ax_s,ge," ",self.ax[d]
        
            
        #print self.pad.get_axis(0) 
        
        for i in range(6):
            if self.pad.get_axis(i) !=0.0:print i,self.pad.get_axis(i)
                  
    """
    def mainloop(self):
        ""
        self.button()       
        self.direction()
        self.axie()
        #print self.ax01_s,self.ax25_s
        
        #print self.but_ds
        
        self.manette_info(self.but_s)
        #self.manette_info(self.but_ds)

        #self.manette_info(self.dire_s)
        #self.manette_info(self.ax_s)
        

        
        
    
if __name__ == '__main__':
    ""
    
    root    =pgwidth.width()
    root.ima_papier =[0,0,0]
    root.size=[100,100]
    root.width()
    a =jock(root.root,root,0)
    root.mainloop(a.mainloop)
    

