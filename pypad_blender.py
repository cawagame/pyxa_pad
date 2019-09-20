
import              pygame
from pygame.locals import *

import pyautogui
import pgwidth
import pgrect
import joystick01

class blender_pad:

    def __init__(self):
        "blender2.7"

        self.mcxy                           =   {}
        self.mcxy["vx"]                     =   0
        self.mcxy["vx"]                     =   0
        self.mcxy["fact_vi"]                =   {}
        self.mcxy["fact_vi"]["vi"]          =   [20,40,80,160,250]
        self.mcxy["fact_vi"]["comx"]        =   0
        self.mcxy["fact_vi"]["comy"]        =   0

        self.camvue                         =   {}
        self.camvue["num"]                  =   ['num0','num7','num1','num3']
        self.camvue["n"]                    =   0

    def init_lib(self):
        ""
        self.pad                            =   joystick01.jock(None,None,0)

    def info(self):
        ''
    def selection_object(self):
        "clique droite"
        
        if self.pad.but_s[:2]            ==["u",10]: pyautogui.click(button='right')

    def menu_add(self):
        "menu add, edite menu mesh"
        if self.pad.but_s[:2]           ==['u',6]:pyautogui.hotkey('shift', 'q')

    def edit_mode(self):
        ''
        if self.pad.but_s[:2]           ==['u',4]:pyautogui.press('tab')

    def valide_sele(self):
        ''
        if  self.pad.but_s[:2]          ==['u',1]:pyautogui.click(button='left')
        
        

    def move_mouse(self):
        "axi01 diriger le curseur sur ecran"
        #print self.pad.ax01_s
        self.mcxy["vx"], self.mcxy["vy"]   =0,0
        
        if self.pad.ax01_s[1]   ==1 or self.pad.ax01_s[1]==3:
            self.mcxy["vx"]                 =  self.pad.ax01_s[0]*50
        if self.pad.ax01_s[1]   ==2 or self.pad.ax01_s[1]==4:
            
            self.mcxy["vy"]                 =  self.pad.ax01_s[0]*50
        pyautogui.move(self.mcxy["vx"],self.mcxy["vy"])

    def move_camera(self):
        "axi25"
        
        if self.pad.but_s[:2]            ==["u",11]:
            self.camvue["n"]+=1
            if  self.camvue["n"]>len(self.camvue["num"])-1:self.camvue["n"]=0
           
            pyautogui.press(self.camvue["num"][self.camvue["n"]])
        if self.pad.ax25_s[1]           ==5:        pyautogui.press('num6')
        elif self.pad.ax25_s[1]         ==6:        pyautogui.press('num8')
        elif self.pad.ax25_s[1]         ==7:        pyautogui.press('num4')
        elif self.pad.ax25_s[1]         ==8:        pyautogui.press('num2')

    def zoom_camera(self):
        ""
        
        if      self.pad.dire_s         ==["u",4]:  pyautogui.scroll(5)
        elif    self.pad.dire_s         ==["u",2]:  pyautogui.scroll(-5)
        
            
            
        
            
            
            
            
        
        
    
    def mainloop(self):
        ""
        self.pad.button()
        self.pad.axie()
        self.pad.direction()
        self.move_mouse()
        self.move_camera()
        self.zoom_camera()
        self.selection_object()
        self.menu_add()
        self.edit_mode()
        self.valide_sele()
        #pyautogui.confirm(text='zz', title='eeee', buttons=['OK', 'Cancel'])


    def display(self):
        ""





root                    =   pgwidth.width()
root.ima_papier         =   [0,0,0]
root.size               =   [100,100]
root.width()
pad                     =   blender_pad()
pad.init_lib()
root.mainloop(pad.mainloop)
        
