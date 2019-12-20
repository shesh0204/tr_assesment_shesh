# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:33:03 2019

@author: mshe
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:05:22 2019

@author: mshe
"""

#SAP Logon

import pyautogui
                                
class SapLogon(object):
    
    def __init__(self,user,pwd,inst):
        self.uid = user
        self.pid = pwd
        self.instance = inst
        
    def activate_pre_invoke(self):
        pyautogui.hotkey('win','d')
        
    def activate_SapLogon(self):
        try:
            pyautogui.hotkey('win','r')
            pyautogui.typewrite('saplogon')
            pyautogui.press('enter')
            return True
        except:
            return False
    
    def open_instance(self):
        try:
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.typewrite(self.instance)
            pyautogui.press('enter')
            return True
        except:
            return False
        
    def SapLogin(self):
        pyautogui.typewrite(self.uid)
        pyautogui.press('tab')
        pyautogui.typewrite(self.pid)
        pyautogui.press('enter')
        time.sleep(3)
                   
#####

import time
if __name__ == '__main__':
    mysap = SapLogon('20249670', 'ammu-2727', 'R00')
    mysap.activate_pre_invoke()
    time.sleep(2)
    mysap.activate_SapLogon()
    time.sleep(5)
    time.sleep(2)
    mysap.open_instance()
    time.sleep(5)
    mysap.SapLogin()
    time.sleep(3)
#    pyautogui.press('enter')
   
 