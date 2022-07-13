# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:30:23 2022

@author: SIDHANT
"""

import unittest

class Login(unittest.TestCase):
    def test_login(self):
        print("This is log in by test")
        self.assertTrue(True)
        
    def test_login_by_Fb(self):
        print("login by facebook")
        self.assertTrue(True)
        
    def test_login_by_inst(self):
        print("log in by instagram")
        self.assertTrue(True)
        
        
if __name__ == "__main__":
    unittest.main()