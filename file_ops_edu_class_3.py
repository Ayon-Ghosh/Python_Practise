# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:43:55 2019

@author: 140524
"""

d1 = {1:'ayon',2:'koyel',3:'rivan'}
print(d1.items())
print(d1.keys())
print(d1.values())

a = [1,2,3]
b = ['mom','pop','baby']
d={}
for i in range(len(a)):
         d[a[i]]=b[i]
print(d)         

print(d.setdefault(2))
x = print(d.setdefault(2,'baba'))
d
y = print(d.setdefault(4,'kaka'))
d
d[1]='Ma'
d[5] = 'chele'
print(d)

d.get(4)
d.get(5)

# fromkeys assigns only one valye to all the keys - that is a limitation

list1 = [1,2,3,4,5]
{}.fromkeys(list1,'dumb')

list1 = [1,2,3,4,5]
{}.fromkeys(list1,['a','b','c','d'])

# enumerate

list1=['milk','fruits','veg']
list2=list(enumerate(list1,11))
print(list2)

d = {}

for i in range(len(list1)):
    d[list2[i][0]] = list1[i]
d    
    
# or
list3 = []
d={}

for i in range(len(list2)):
         list3.append(list2[i][0])
         d[list3[i]] = list1[i]
d         

list1=['milk','fruits','veg']
list2=set(enumerate(list1,11))
print(list2)

a = {11:'a',12:'b',13:'c',14:'d',15:'e'}
b = {11:'A',12:'B',13:'C',14:'D',15:'E'}
c=list(set(a.keys()).symmetric_difference(set(b.keys())))
c
flag = True
if len(c) ==0:
      print('both a and b has same keys and length')
      for i in a:
          print('keys:',i)
          if i in b:
              print(a[i],b[i])
              if (a[i]==b[i]):
                        pass
              else:
                  flag = False
          else:
              flag = False
else:
    flag = False
print(flag)              
          
# or

a = {1:'a',2:'b',3:'c',4:'d',5:'e'}
b = {1:'A',2:'B',3:'C',4:'D',5:'E'}
c = list(set(a.keys()).symmetric_difference(set(b.keys())))
c
is_equal=True
if len(c)==0:
    print('both a and b has same keys and length')
    for k in a:
        print('key:',k)
        if k in b:
            print(a[k],b[k])
        else:
            is_equal=False
else:
    is_equal = False
print(is_equal)            


a = {1:'a',2:'b',3:'c',4:'d',5:'e'}
b = {1:'a',2:'b',3:'c',4:'d',5:'e'}
c = list(set(a.keys()).symmetric_difference(set(b.keys())))
c
is_equal=True
if len(c)==0:
    print('both a and b has same keys and length')
    for k in a:
        print('key:',k)
        if k in b:
            print(a[k],b[k])
            if a[k]==b[k]:
                pass
            else:
                is_equal=False
                break
        else:
            is_equal=False
else:
    is_equal = False
print(is_equal)            
        


# FILE OPERATIONS

import os
os.chdir('C:\\python\\files\\')
new_file=open('ayon.txt','w+')
for i in range(50):
    new_file.write('sonu putul\n')
new_file.close()    
new_file=open('ayon.txt','r')
for i in range(50):
    print(new_file.read())
new_file.close()    
os.rename('ayon.txt','putul.txt')
new_file.close()  


import os
os.chdir('C:\\python\\files\\')
new_file = open("edureka_py1.txt","w+")
for i in range(10):
    new_file.write("Hello code\n")
new_file.close()
new_file = open("edureka_py.txt","r")
for i in range(10):
    print(new_file.read())
new_file.close()    
os.rename("edureka_py.txt","Edureka_Py.txt")   
new_file.close()    


# GETCWD - get currewnt work directory

help(os.getcwd)

os.getcwd()

# LISTDIR - list directory

help(os.listdir)

os.listdir()

help(os.chdir)

path = os.getcwd()
files = os.listdir()
files
os.path
for file in files:
    print(os.path.join(path,file))
    
    



#fp = codecs.open(os.path.join('C:\edureka\PRClass_3\Data_set','worldcities.csv'), 'r')
os.chdir('C:\\python\\files\\')
new_file= open('worldcities.csv','r')
cnt = 0
for line in new_file:
    if cnt <= 10:
        print(line)
    else:
        break
    cnt += 1
new_file.close()




# join - same functionality as above but printing within a speified range and the heading

fp = open(os.path.join('C:\edureka\PRClass_3\Data_set','worldcities.csv'), 'r')
fp
cnt = 0
for line in fp:
    if cnt==0:
        print(line) # printing heading
    elif cnt<=9:
        pass
    elif cnt<=19:
        print(line) # pinting within a range (10-20 here)
    else:
        break
    cnt += 1
fp.close()

# same program as abive using codecs

import codecs

fp = codecs.open(os.path.join('C:\edureka\PRClass_3\Data_set','worldcities.csv'), 'r')
cnt = 0
for line in fp:
    if cnt <= 10:
        print(line)
    else:
        break
    cnt += 1
fp.close()

os.rename(('C:\edureka\PRClass_3\Data_set\\worldcities.csv'), 
          os.path.join('C:\edureka\PRClass_2\Data_set','country.csv'))

# copying first 1o lines from worldcities.cvs to buli.txt
fr = open('C:\\python\\files\\worldcities.csv','r+')
fw = open('C:\\python\\files\\buli.txt','w+')
cnt=0
for line in fr:
    if cnt<=10:
        fw.write(line)
    else:
        break
    cnt=cnt+1
fr.close()
fw.close()    

fr = open('C:\edureka\PRClass_3\Data_set\\worldcities.csv','r')
fw = open('C:\edureka\PRClass_3\Data_set\\Rivan.csv','w+')

count = 0

for line in fr:
    if count<=10:
        fw.write(line)
       # fw.write('\n')
    else:
        break
    count = count+1
fr.close()
fw.close()    

# another process of copying using chdir (files in 2 different directories)

wf = os.chdir("C:\\edureka\\PRClass_3\\Data_set\\")
new_file=open("Koyel.csv","w+")
rf = open('C:\edureka\PRClass_2\Data_set\\worldcities.csv','r')
line_count=0
for line in rf:
    if line_count<=10:
       new_file.write(line)
       new_file.write('\n')
    else:
        break
    line_count=line_count+1
new_file.close()
rf.close()
   

fw = open('C:\\edureka\\PRClass_3\\Data_set\\Koyel.csv','r')

for line in fw:
    print(fw.read())
    
## another process of copying using chdir (files in 2 different directories)
# using just open    

fr = open('C:\edureka\PRClass_3\Data_set\\worldcities.csv','r')
fw = open('C:\edureka\PRClass_2\Data_set\\country.csv','w+')

count = 0

for line in fr:
    if count<=10:
        fw.write(line)
       # fw.write('\n')
    else:
        break
    count = count+1
fr.close()
fw.close()    

fw = open('C:\\edureka\\country.csv','r')

for line in fw:
    print(fw.read())
    

## another process of copying using chdir (files in 2 different directories)
# using os.path.join    

fr = open('C:\edureka\PRClass_3\Data_set\\worldcities.csv','r')
fw = open(os.path.join('C:\\edureka\\', 'country.csv'), 'w+')
count = 0

for line in fr:
    if count<=10:
        fw.write(line)
       # fw.write('\n')
    else:
        break
    count = count+1
fr.close()
fw.close()    

fw = open('C:\\edureka\\country.csv','r')

for line in fw:
    print(fw.read())

    
 # ---working with JSON files--create and write on json file



d1 = {'fname': 'Steve', 'lname': 'Jobs'}
d2 = {'fname': 'Steve', 'lname': 'Jobs', 'age': 21}

import json
wp = open(os.path.join('C:\\edureka\\PRClass_2\\Data_set\\', 'test_new.json'), 'w+')
for x in range(5):
    if x == 0:
        wp.write(json.dumps(d1))
    elif x == 1:
        wp.write(json.dumps(d2))
    else:
        wp.write(json.dumps({'age':24, 'salary':10000}))
    wp.write('\n')
wp.close()  
wp = open(os.path.join('C:\\edureka\\PRClass_2\\Data_set\\', 'test_new.json'), 'r')
for line in wp:
    print(wp.read())
 

# ---working with JSON files--read json file

rp = open(os.path.join('C:\\edureka\\PRClass_2\\Data_set\\', 'test_new.json'), 'r')
# content = json.loads(rp.read())
for line in rp:
    #print(line)
    rec = json.loads(line)
    #print(rec, type(rec))
    print(rec.get('salary', 'Not found'))
    
rp.close()

# copying all lines till a key word match

from itertools import islice

with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list1.csv','w+') as fwrite:
     for line in fread:
        if 'Decan' in line:
            break
        else:
            fwrite.write(line)



# find a match and copying 200 lines from then on - this is the best way


with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list3.csv','w+') as fwrite:
     for num, line in enumerate(fread, 1):
        if num==1:
            fwrite.write(line) # copying the heading
            
        #print(line)
        #print(num)
        elif 'Kolkata' in line: #finding the match
          print(line)
          x = num
          break
        else:
            pass
        listA = list(islice(fread,x-2,x+199)) # copying 200 lines from the match
        chunk = ''.join(listA)
        fwrite.write(chunk)
       # chunk = line + ''.join(islice(fread, x, x+200))
        #fwrite.write(chunk)






# copying 200 lines from a key word match----- this code will copy line kolkata for 200 times
# which is not the requirement    
     
with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list4.csv','w+') as fwrite:
 count = 0     
for line in fread:
       if 'Kolkata' in line:
               print(count)
               y=count
       count = count+1   
       if count<=y-1:
           pass
       elif count<=y+200:
           fwrite.write(line)
       else:
           pass

# OR the below ode also doesnt work
          
with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list4.csv','w+') as fwrite:
      for num, line in enumerate(fread,1):
          if num==1:
              fwrite.write(line) # copying the heading
     
          elif 'Kolkata' in line:
                       print(line)
                       x = num
                       print(x)
                       fwrite.write(line)
                       
with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list7.csv','w+') as fwrite:
      for num, line in enumerate(fread,1):
              if 'Kolkata' in line:
                       print(line)
                       x = num
                       print(x)
      for num, line in enumerate(fread,x):
                       fwrite.write(line)
                  
          
                       
# or it works but I am not happy
from itertools import islice
with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list2.csv','w+') as fwrite:  
      for num, line in enumerate(fread,1):
         if 'Kolkata' in line:
                 x = num
                 print(x)
                 num=1
                 chunk = ''.join(islice(fread,200))  
                 fwrite.write(chunk)
          
# finding a match and copying 200 lines before that and the heading
                 
with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list5.csv','w+') as fwrite:
      for num, line in enumerate(fread,1):
         if 'Kolkata' in line:
                 x = num
                 print(x)
                 num=1
                 chunk = ''.join(islice(fread,200))  
                 fwrite.write(chunk)

with open('C:\\python\\files\\worldcities.csv','r') as fread, open('C:\\python\\files\\citi_short_list6.csv','w+') as fwrite:
     for num, line in enumerate(fread, 1):
        if num==1:
            fwrite.write(line) # copying the heading
        elif 'Kolkata' in line: #finding the match
          x = num
          break
        else:
          pass
        listA = list(islice(fread,x-200,x-1)) # copying 200 lines from the match
        chunk = ''.join(listA)
        fwrite.write(chunk)
# Refer to the following links for interesting problems
                 
# https://www.computerhope.com/issues/ch001721.htm

# https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file                 
                 
                 
# FUNCTION-----------------------

import os
def process(file_path):
    if os.path.exists(file_path):
        rp = open(file_path, 'r')
        for line in rp:
            print(line)
        rp.close()

process('C:\edureka\PRClass_3\Data_set\FairDealCustomerData.csv') 

# or 

with open('C:\edureka\PRClass_3\Data_set\FairDealCustomerData.csv','r') as fread: 
 for line in fread:
    print(line)
 fread.close()    

# WITHOUT FUNCTION BELOW - 

with open('C:\edureka\PRClass_3\Data_set\FairDealCustomerData.csv','r')  as new_file:

 for line in new_file:
       print(line)        
# FUNCTION EXmple       
       
       
def math_oper(n1, n2):
    return n1+n2 if n1 > n2 else n2-n1

n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))
math_oper(n1, n2)

# example - nothing is executed

X = 30

def add(a, b):
    global X
    X = X + 1
    c = a + b
    #if c > 10:
    #    print(c)
    return c

add(10,20)
print(X)
print(c)
       

# any and all

marks = []
any(marks)
all(marks)

marks = [45, 54, 99, 81, 12, -3]
any(marks)
marks.append(0)
marks
all(marks)
any(marks)
new_marks = list(reversed(marks))
new_marks

# using function

def categorize_marks(mark):
    if mark > 70:
        return 'Perfect'
    else:
        return 'Needs Improvement'
marks = [45, 54, 99, 81, 12, -3]    
for mark in marks[:-1]:
    print(categorize_marks(mark))
    
    # or
    
def categorize_marks(mark):
    if mark > 70:
        return 'Perfect'
    else:
        return 'Needs Improvement'
marks = [45, 54, 99, 81, 12, -3]    
for mark in sorted(marks, reverse = True):
    print(categorize_marks(mark))    

# list using map function
marks = [45, 54, 99, 81, 12, -3]      
list(map(categorize_marks,sorted(marks,reverse=True)))    

# using map and lambda functions

marks = [45, 54, 99, 81, 12, -3]  
list(map(lambda x:'perfect' if x>70 else 'improve',marks))

# using filter and lambda

marks = [45, 54, 99, 81, 12, -3]  
list(filter(lambda x:(x>50 and x<=100),marks))

# using function and filter

def grt_marks(x):
    if x>60:
        return x
list(filter(grt_marks,marks))    
# example if REDUCE and lambda

from functools import reduce
reduce(lambda x,y:x+y, marks)


def sq_func(x):
    return x**2 if x > 10 else x**3

sq_func(3)
sq_func(11)

# lambda

sq = lambda x: x**2 if x<10 else x**3
sq(6)
sq(34)



#------------------KEYWORD arguments and positional parameters

def func1(a,b,c,d=60):
    print(a,b,c,d)
    
    
# --------positional parameters    
func1(10,20,30)    
func1(10,20,30,40)

# ----------------keyword argument

func1(b=24,c=34,a=14,d=17)

#---------arbitary arguments

def greet(*names):
    for name in names:
        print("hello ", name)

greet('Ayon','Rivan', 'Koyel')  
   
   
# **Python Function - Variable Length Arguments with *args 
# Keyword arguments and **kwargs


def bar(first, second, third, **options):
    if options.get('action') == 'sum':
        print ("the sum is:%d" %(first+second+third))
    if options.get('number') == 'first':
        return first
result = bar(1,2,3,action='sum', number='first')    
print("result:%d" %(result))  

# or
def bar(first, second, third, **options):
    if options['action'] == 'sum':
        print ("the sum is:%d" %(first+second+third))
    if options['number'] == 'first':
        return first
result = bar(1,2,3,action='sum', number='first')    
print("result:%d" %(result))  

#----------

def fun(a,b,c,d=60,*p,**kwargs):
    print(a,b,c)
    print(p)
    print(d)
    print(kwargs)
    

fun(10, 30, 20, 45, 70, 80, s = 60, e=50)
 # positional    
fun(10, 20, 30)
## keyword notation
fun(a=10,c=20,b=45) 

# fun(10, 20)
fun(a=10, c=30, b=20, d=40, e=50)

fun(a=10, c=30, b=20, d = 45, 70, 80, s = 60, e=50)

#--------------

def myfunct(arg1,arg2,arg3,*args,**kwargs):
     print ('First Normal Argument : ' + str(arg1))
     print ('Second Normal Argument : ' + str(arg2))
     print ('Third Normal Argument : ' + str(arg3))
     print ('Non-keyworded Argument : ' + str(args))
     print ('Keyworded Argument : ' + str(kwargs))
     
myfunct(1,2,3,4,5,6,7,name='Ayon',country = 'US', age = '40')   

#-----------


def pass_the_world(*c):
    print(type(c), c)
    
pass_the_world()
pass_the_world(10,20,30,40,*list(range(10)))

# --------------

def lang_name(fname,lname,mname = None, reverse = True):
    print(type(fname), type(lname), type(reverse))
    if reverse:
        return lname + ' '+ mname +' '+fname
    else:
        return fname + ' '+ mname +' '+lname
#TypeError: can only concatenate str (not "NoneType") to str
#lang_name('python', 'SQL')    
        
lang_name('python', 'SQL', 'R')

#--------------





def add_marks(standard, names=None, **marks):
    return sum(marks)

print(add_marks(standard = 'Xth', marks = [10, 20, 30, 40, 90, 100, 45, 54]))

#-----------------


def master(ndf1, ndf2, df1=2, df2=3, d=3, *args, **kwargs):
    print(ndf1, ndf2, df1, df2)
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)
    
master(10, 20, df1=30, k=10, v=20, d=30, p=50)


#------

def flexi(*args):
    print(type(args))
    print(args)
    
flexi()
flexi(10,20,30)

#-----

def afun(a,b,c=100,*args):
    print(a,b,c)
    print(args)
    print(a+b+c+sum(args))
    print('------')
# afun(10,20)
# afun(10,20,30)
afun(10,20,30,40,50,63,75,81,0,12)

#----

####[65]:


def afun(a,b,c=45,*args,**kwargs):
    print(a,b,c)
    print(args)
    print(kwargs)
    print('------')
# afun(10,20)
# afun(10,20,30)
# afun(10,20,30,40,50,63,75,81,0,12)
afun(10,20,30,40,50,63,75,81,0,12,d=40,e=50,f=60)


#--------------

class edureka():
     def hello(self):
         print("happy learning")
ob = edureka()
ob
ob.hello()         

#-----

a = 50
class number():
    b = 30
    print(b)
print(a)
print(b)
number()    


# private, protected, and public attributes

class Edureka():
    def __init__(self):
        self.__priv=('i am private')
        self._prot = ('i am protected')
        self.pub = ('i am public')
        
ob = Edureka()
ob.pub
ob._prot()
ob.__priv()        


# private, protected, and public attributes

class Edureka():
    def __init__(self):
        self.__priv=('i am private')
        self._prot = ('i am protected')
        self.pub = ('i am public')
        
ob = Edureka()
ob.pub
ob._prot()
ob.__priv()        


#--pubic and private methods

class Edureka():
    def mypublicmethod(self):
        print('i am public')
    def __myprivatemethod(self):
        print('i am private')
ob = Edureka()
ob.mypublicmethod()
ob._Edureka__myprivatemethod()       


# ---class variable and instance variable

class Edureka():
# defining class variable    
    
    domain = 'Data Science'
# defining instance variable    
    def course(self,name):
        self.name=name
# defining 2 class instance or 2 objects of class        
ob1 = Edureka()
ob2 = Edureka()     
# printing class varianble - accessed by all instances   
print(ob1.domain)
print(ob2.domain)
print("-------")
# printing instances varianble - accessed by specific instances in which name is passed
ob1.course('python')
ob2.course('R')
ob1.name
ob2.name

#cannot over riding class variable outside class - shared by both objects/ instances

ob1.domain = 'ML'
ob1.domain
ob2.domain

# ----class variable and attributes

class Edureka():
# defining class variable   and attrrbutes  (priv, protected, public)
    def __init__(self):
       self.domain_pub = 'Data Science'
       self.name = 'Data Science'
       self._domain_prot ='R'
       self.__domain_priv = 'ML'
# defining instance variable    
    def pubcourse(self,name):
         self.name=name+self.domain_pub+'+'+self._domain_prot
    def __privcourse(self,name):    
        self.name=name+self.__domain_priv
        
        
ob1 = Edureka()
ob2 = Edureka() 
# printing class variable pub and private    
print(ob1.domain_pub)
print(ob1.name)
print(ob2._domain_prot)

# Cannot printing class variable pub and private
print(ob2.__domain_priv)
        
# printing instance variable and attributes

ob2.pubcourse('SQL+')
print(ob2.name)


ob2.pubcourse('Haddop +')
print(ob2.name)
ob3 = Edureka()

# this doesnt work for private method with private attibutes
#ob3._Edureka.__privcourse('NOSQL+')
#print(ob3.name)

# contructor and destructor

class Testclass():
# cibstructor is implemented that follows self    
    
    def __init__(self):
        print('constructor')
        
# destructor to delete        
    def __del__(self):
        print('destructor')
ob1 = Testclass()
del ob1        

# multiple constructors

class Date():
# cibstructor is implemented that follows self    
    
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
 # classmethod

    def dmy(cls,day,month,year):
        cls.year = year
        cls.month = month
        cls.day = day   
        return cls(cls.year,cls.month,cls.day)  
 
 # classmethod

    def mdy(cls,month,day,year):
        cls.year = year
        cls.month = month
        cls.day = day   
        return cls(cls.year,cls.month,cls.day)        
      
# destructor to delete        
a = Date(2016, 12, 26)
print(a.year)   

b = Date.dmy(28, 10, 2015)
print(b.year)

c = Date.mdy(11, 20, 2019)
print(c.year)

#-----

# INHERITANCE

# SINGLE INHERITANCE

# A(CLAASS)--------->B(SUBCLASS)

class BASE():
    def fun(self):
        print("Happy Learning - base")
# INHERITING below
class sub(BASE):
        print("Happy Learning - sub")
# object from subclass
ob1 = sub()
ob1.fun()

# Multiple inheritance -- inherit from 2 or more classes

#A           B
#------------
#    |
#    C

class BASEA():
    def funA(self):
        print("Happy Learning - baseA")
        
class BASEB():
    def funB(self):
        print("Happy Learning - baseB")
        
# INHERITING below
class sub(BASEA,BASEB):
        print("Happy Learning - SUB")
# object from subclass
a = sub()

#----Mul

import os
fpath = input('enter the path:')

for dirs,_, files in os.walk(fpath):
    for file in files:
        path = os.path.join(dirs, file)
        print(path)
        
import pandas as pd
df = pd.read_csv(path)  
df.head()      