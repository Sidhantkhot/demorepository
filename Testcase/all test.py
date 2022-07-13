# -*- coding: utf-8 -*-
"""
Created on Sat May 28 23:35:00 2022

@author: SIDHANT
"""

import unittest
from Package1.Login import Login
from Package2.Paymentmethod import Paymentmethod


Tc1 = unittest.TestLoader().loadTestsFromModule(Login)
Tc2 = unittest.TestLoader().loadTestsFromModule(Paymentmethod)

test_suite = unittest.TestSuite([Tc1,Tc2])

unittest.TextTestRunner().run(test_suite)
