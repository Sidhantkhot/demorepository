# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:24:29 2022

@author: SIDHANT
"""

from selenium import webdriver
#from webdrivermanager import ChromeDriverManager()

import datetime
        
class MoveCharacter:
    def movefwd(self):
        print("move forward 1 step")
        
    def movebwd(self):
        print("move backward 1 step")
        
class JumpCharacter:
    def jump_level1(self):
        print('jump character 1 level')
        
    def jump_level2(self):
        print("jump character 2 level")
        
class Pokemon(MoveCharacter,JumpCharacter):
    def movefwd(self):
        print('pokemon moving')
        
p= Pokemon()

p.movefwd()
p.jump_level1()