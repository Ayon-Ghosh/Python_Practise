# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:43:39 2020

@author: 140524
"""

import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
W
H = model.components_



cars = ['ford focus', 'honda civic', 'chevy truck',]
parts = ['ignition', 'head light']

for car in cars:
    for part in parts:
        print(car + " "+ part)
        
        
mylist = [1,3,6.10]
a = (x**2 for x in mylist)
a
print(next(a),next(a))        

def Foo(n):
    def mul(x):
        return x*n
    return mul

a = Foo(5)
b = Foo(5)
a(b(2))

def make_pretty(func):
    def inner():
        print('i am decorated')
        func()
    return inner

def ordinary():
       print('i am ordinary')
       
pretty = make_pretty(ordinary)
pretty()       


def outerfunc():
    global a
    a = 20
    def innerfunc():
        global a
        a = 30
        print('a=',a)
a = 10
outerfunc()
print('a=',a)

class Foo:
    def printline(self,line='Python'):
        print(line)
a = Foo()
a.printline('Java')        

class Point:
    def __init__(self,x=0,y=0):
             self.x=x+1
             self.y=y+1
pl = Point(2,2)
pl.x
pl.y


class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __sub__(self,other):
        self.x = self.x+other.x
        self.y = self.y+other.y
p1 = Point(3,4)
p2 = Point(1,2)  
result= p1-p2
print(result.x)
           