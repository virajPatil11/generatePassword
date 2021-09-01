# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:55:49 2021

@author: viraj
"""

import random
def passwordGenerator():
    
    upperchars = ['A', 'B','C', 'D']
    lowerchars = ['a', 'b','c', 'd']
    specialchars = ['!', '#','$']
    numericchars= ['1', '2' , '3', '4', '5']
    
    password= random.choice(upperchars) + random.choice(lowerchars)+random.choice(specialchars) +random.choice(numericchars) 
    password= password + password  
    print(password)
passwordGenerator()