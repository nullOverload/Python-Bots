from pyautogui import *
import pyautogui
import time
import keyboard
import random
import mouse
from win32 import win32api
import win32.lib.win32con as win32con

num = 1

#1st collumn coor = 
#2nd collumn coor = 
#3rd collumn coor = 
#4th collumn coor = 

def clickk(x, y):
    win32api.SetCursorPos((x,y+90))
    mouse.click('left')

while True:
    
    if keyboard.read_key() == 's':
        num = 2
    
    while num == 2:
            
            if pyautogui.pixel(758, 500)[0] == 0 or pyautogui.pixel(758, 500)[0] == 16:
                clickk(758, 500)
            if pyautogui.pixel(894, 500)[0] == 0 or pyautogui.pixel(894, 500)[0] == 16:
                clickk(894, 500)
            if pyautogui.pixel(1015, 500)[0] == 0 or pyautogui.pixel(1015, 500)[0] == 16:
                clickk(1015, 500)
            if pyautogui.pixel(1138, 500)[0] == 0 or pyautogui.pixel(1138, 500)[0] == 16:
                clickk(1138, 500)
