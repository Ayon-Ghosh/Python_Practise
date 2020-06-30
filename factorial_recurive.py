# -*- coding: utf-8 -*-
"""
Created on Wed May 15 04:30:17 2019

@author: 140524
"""

# factorial program using recursive program

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
n=int(input("enter your number: "))
factorial(n)
    

# examples from edureka - functions

def print_name(str1):
    return print("welcome to edureka", str1)
    
    
n = input("enter your name: ")    
print_name(n)    