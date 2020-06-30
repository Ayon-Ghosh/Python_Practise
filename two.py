# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:54:06 2019

@author: 140524
"""

import one

print("top level is two.py")
one.func()

if __name__=="__main__":
    print("two.py is run directly")
else:
    print("two.py is run from another function") 