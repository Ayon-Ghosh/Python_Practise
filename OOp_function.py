# -*- coding: utf-8 -*-
"""
Created on Wed May 15 05:09:00 2019

@author: 140524
"""

#--edureka examples --functions

grocery=['bread', 'milk','oil']
g=enumerate(grocery)

# converting to a list with the default counter
print(list(g))

# changing the default counter 

g = enumerate(grocery,10)
print(list(g))

# ---examples of maop, reduce, filter functions

ans=(lambda z:z*4)
print(ans(7))
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (int((9)/5)*x) + 32, C))
print(F)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

number_list = range(-5, 5)
more_than_zero = list(filter(lambda x: x > 0, number_list))
print(more_than_zero)

from functools import reduce
product = reduce((lambda x, y: x + y), [1, 2, 3, 4,5,6,7])
print(product)


#--- variable length argumentc --this is used when numbers of arguments 
#cannot be decided when function is created


def info(*users):
    for var in users:
        print("welcome to python")
        print(var)

info('Ayon', 'Koyel', 'rivan')    


def func(arg1,arg2,arg3,*arg4,**kwargs):
    print('first argument is:' + str(arg1))
    print('second argument is:', str(arg2))
    print('third argument is:', str(arg3))
    for var in arg4:
        print("the variableargument is:", var)
    print('keyworded argument is:',kwargs)

func(1,2,3,4,5,6,7,8,'hello', name='Rivan', country = 'USA', age = 4)    

# scope of a variable--Global and local

a = 50
def num(n):
    n = 30
    return (print(n))
num(20)
print(a)

def info1(name, age=50):
   print('Name:',name)
   print('Age:',age)
   return()
info1('Ayon',40)
info1(age=38,name = 'koyel')
info1('Dummy')
    
#---OOPS-------------

#--creating a class---

class num():
    pass

x=num()
print(x)

# self points to the object of the class 

class edureka():
    def hello(self):
        print('happy learning')
a = edureka()
a.hello()

a = 50
class edureka():
   b = 50
   return b

x = edureka()
x         

#..buit in attributes

# dict contains class's namespace

class Edureka:
    empcount=0
    
print("Edureka.__dict__:",Edureka.__dict__)
 

#class documentation string or none if undefined


print("Edureka.__doc__:",Edureka.__doc__)

# class name

print("Edureka.__name__",Edureka.__name__)    

# module name in which edureka is defined


print("Edureka.__module__:",Edureka.__module__)    

# attributes defined by user
# Private attrbutes can only be accessed inside a class definition
# public attributes can be accessed freely everywhere
# protected attributes can be accessed only within classes and sub classes

class edureka():
    def __init__(self):
        self.__a =('i am private')
        self._b=('i am protected')
        self.c=('i am public')
X = edureka()
print(X.c)
print(X.__c)
print(X._b)
       
class  myclass():
    def publicmethod(self):
          print("my public object")
    def __privatemethod(self):
          print("my private method")
a = myclass()
a.publicmethod()
a.__privatemethod()
a._myclass__privatemethod()     



# class variable and instance variable

class myclass():
    domain = 'Data Science'
    def course(self,name):
        self.name=name
        
a=myclass()
b=myclass()

a.course('python')
print(a.name)
print(a.domain)
b.course('R')
print(b.name)
print(b.domain)

#---class variable and instance variable--
# instance variable is unique to each instance of the class

class Edureka():
    domain = 'Data Science'
    def setcourse(self,name):
        self.name=name
x=Edureka()
y=Edureka()
print(x.domain)
print(y.domain)

x.setcourse('python')
y.setcourse('R')
print(x.name)
print(y.name)
        

#...constructor and destructor--
#..The constructor is implemented using __init__(self) which you can define 
# parameters that follow self
#..The destructor is implemented using __del__(self) in which object is created
# and manually deleted so both messages will be displayed

class testclass():
    def __init__(self):
        method = 'constructor'
        print(method)
    def __del__(self):
        method1 = 'destructor'
        print(method1)
        
a = testclass()
del a
b = testclass()
b.method       


#multiple constructors

class Date:
    def __init__(self, Day, month, year):
        self.day=day
        self.month-month
        self.year=year
# print init

    
    def ymd(cls,year,month, day):
        cls.day = day
        cls.month = month
        cls.year=year
# order of return should be the same as init
    return cls(cls.year, cls.month, cls.day)
     
    def mdy(cls,month,day,year):
        cls.day = day
        cls.month = month
        cls.year=year
# order of return should be the same as init        
    return cls(cls.month, cls.day, cls.year)
a = Date(30,11,1978)
print(a)
print(a.day)
print(a.year)
print(a.month)
 
b = Date.ymd(1980,10,28)
print(b.ymd)
print(b.year)
print(b.month)
print(b.day)

c = Date.mdy(04,28,2015)
print(b.mdy)
print(c.month)
print(c.day)
print(c.year)

# inheritane --

class base1:
    def fun(self):
        print("in class base1")

class sub(base1):
        pass

a=sub()
a.fun()        

# muti level inheritancr

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")
class Second(object):    
    def __init__(self):
        super(Second, self).__init__()
        print("second")
class Third(Second,First):
    def __init__(self):
        super(Third,self).__init__()
        print("third")
        
Third();


# Multi level inheritence

class animal(object):
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")  
class babydog(dog):
    def run(self):
        print("running")         
        
boxer = babydog()
boxer.bark()
boxer.eat()
boxer.run()


#Overriding method

#Parent clas method can always be overriden. One reason for overriding parent's
#class method is because you want special or different functionality for your
#sub class

class Parent:
    def mymethod(self):
        print("calling parent method")
class Child(Parent):
    def child(self):
        print("calling child method")         

c=Child()
c.mymethod()        

#Example -class overriding

class rectangle:
    def __init__self(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(self.length*self.breadth, "is the area of the rectangle")
class square(rectangle):
    def __init__self(self,side):
        self.side=side
        rectangle. init (self,side,side)
    def area(self):
        print(self.side*self.side,"is the area of the square")
        
s=square(4)
s.area()
r = rectangle(4,2)
r.area()            
        

#----OS Module---DIR

import os

print(os.name)
print(os.environ)
print(os.getlogin())
print(os.getppid)
print(os.getcwd())
print(os.chdir('C:\python'))
print(os.mkdir('C:\\python\\ayon'))
print(os.rmdir('C:\\python\\ayon'))
print(os.listdir('C:\\'))


# JOIN method

import os
files = os.listdir('C:\\')
new = os.getcwd()
for file in files:
    print(os.path.join(file,new))
    