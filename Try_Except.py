# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:02:41 2020

@author: 140524
"""

# =============================================================================
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass
# =============================================================================

try:
    f = open('ayon.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('finally executing')    
    
# =============================================================================
#     
# Dock Typing and Easier to ask forgiveness than permission (EAFP)    
# Python treats that any objects that can do the same things must be treated the same
# for example if we have 2 classes - duck and person and in each of the classes if we have :
# 2 functions fly and walk then we treat both classes the same way
# =============================================================================
    
#https://www.youtube.com/watch?v=x3v9zMX1s4s&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=32    
class Person:
    def quack(self):
        print('i am quacking like a duck')
    def fly(self):
        print('i am flying like a duck')

class duck:
    def quack(self):
        print('quck quack')
    def fly(self):
        print('fly fly')

# the below is the check so people dont  misuse ducktyping -EAFP
def quack_and_fly(thing):
    try:
       thing.fly()
       thing.quack()  
       #this will raise attribute error
       thing.bark()
         
    except AttributeError as e:
        print(e)
        
d = duck()
quack_and_fly(d)     

p = Person()
quack_and_fly(p)        
           
        