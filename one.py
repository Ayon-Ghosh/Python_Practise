# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:48:13 2019

@author: 140524
"""

def func():
    print("func() in one.py")
    
print("top level is one.py")

if __name__=="__main__":
    print("one.py is run directly")
else:
    print("one.py is run from another function")     
    
    
    