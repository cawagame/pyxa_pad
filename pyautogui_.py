import              pygame
from pygame.locals import *

import pyautogui
import pgwidth
import pgrect
import joystick01
"""
differente act blender
vue 1 2 3
"""

def mainloop():
    #global mx,my
    mx,my =0,0
    a.button()
    a.direction()
    a.axie()
    
    
    print a.ax25_s
    if a.ax01_s[1]==1 or a.ax01_s[1]==3:
        mx=a.ax01_s[0]*50
    if a.ax01_s[1]==2 or a.ax01_s[1]==4:
        my=a.ax01_s[0]*50
    if a.but_s[:2]==["u",4]:
        pyautogui.moveTo(10,10,1)
    if a.but_s[:2]          ==["u",0]:      pyautogui.click(button='left')
    elif a.but_s[:2]        ==["u",2]:      pyautogui.click(button='middle')
    elif a.but_s[:2]        ==["u",3]:      pyautogui.press('num1')

    if a.dire_s             ==["u",4]:      pyautogui.scroll(10)
    elif a.dire_s           ==["u",2]:      pyautogui.scroll(-10)
    #vue haut
    if a.ax25_s[1]          ==7:            pyautogui.press('num4')
    elif a.ax25_s[1]        ==8:            pyautogui.press('num2')
    elif a.ax25_s[1]        ==5:            pyautogui.press('num6')
    elif a.ax25_s[1]        ==6:            pyautogui.press('num8')
    
        #alert(text='', title='', button='OK')
         #pyautogui.scroll(10)
        #pyautogui.click(button='right')
    pyautogui.move(mx,my)
root    =pgwidth.width()
root.ima_papier =[0,0,0]
root.size=[100,100]
root.width()
a =joystick01.jock(0,0,0)
mx,my= pyautogui.position()
root.mainloop(mainloop)
    
