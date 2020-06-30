# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:01:50 2019

@author: 140524
"""

#Question1
#Write a program which will find all such numbers which are divisible by 7 
#but are not a multiple of 5, between 2000 and 3200 (both included).The numbers 
#obtained should be printed in a uma-separated sequence on a single line

listA = [x for x in range(2000,3201)]
listA
listB = list(filter(lambda x:x%7==0 and x%5!=0,listA))
def conv_str(x):
    return str(x)
listC = [conv_str(x) for x in listB]
listC
print(','.join(listC))


# OR in a list

list(filter(lambda x:x%7==0 and x%5!=0, range(2000,3201)))

#Question 2
#Write a program which can compute the factorial of a given numbers.
#Suppose the following input is supplied to the program: 8 Then, the output should be:40320

 

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input('enter the number: '))
fact(n)

#Question 3
#With a given integral number n, write a program to generate a dictionary that 
#contains (i, i x i) such that is an integral number between 1 and n (both included). 
#and then the program should print the dictionary.Suppose the following input is 
#supplied to the program
n = int(input("enter the number of elements: "))
d={}
for i in range(1,n+1):
    d[i] = i**2
d    

#OR---

num = int(input("enter the number of elements: "))
my_dict={}
a = [x**2 for x in range(1,num+1)]
b=[x for x in range(1,num+1)]
for i in range(len(a)):
    my_dict[b[i]]=a[i]
my_dict    
    

#OR

n = int(input("enter the number of elements: "))
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)

#OR
## This is done with dictionary comprehension method
n = int(input("enter the number of elements: "))
ans={i : i*i for i in range(1,n+1)}
print(ans)

#Question 4
#Write a program which accepts a sequence of comma-separated numbers from 
#console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:

n = input("enter the list: ").split(',')
n
tuple(n)
#or

num=input("enter the list: ")
#creates a list
numlist = num.split(',')
numlist
# converts list to tuple
tuple(numlist)

    
#Question 5
#Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class myclass:
    string=input("enter the string:")
    def setstring(self,string):
             self.string=string
    def getstring(self):
             return(self.string.upper())
        
newob = myclass()
print(newob.getstring())    
   
#OR

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("enter the string:")

    def printString(self):
        return self.s.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()    

#Question 6
#Write a program that calculates and prints the value according to the given formula:

#Q = Square root of [(2 * C * D)/H]

#Following are the fixed values of C and H:

#C is 50. H is 30.

#D is the variable whose values should be input to your program in a 
#comma-separated sequence.For example Let us assume the following comma 
#separated input sequence is given to the program:

import math
c=50
h=30
d = input("enter the sequence:").split(',')
result = [str(round(math.sqrt(2*c*int(i)/h))) for i in d]
print(','.join(result))

# or

import math
c=50
h=30
string = input("enter the sequence:")
numlist = string.split(',')
resultlist=[]
for i in numlist:
    temp = round(math.sqrt(2*c*int(i)/h))
    resultlist.append(temp)
resultlist=[str(i) for i in resultlist]    
print(','.join(resultlist))
    
#--  OR---
  
import math
c=50
h=30
string = input("enter the sequence:")
numlist = string.split(',')
resultlist = list(map(lambda x:round(math.sqrt(2*50*int(x)/30)),numlist))
resultlist

#---OR

#  The below process will show how to convert a string list to int list
# The .join mnthod method shows to join only 2 strings
import math
def funct(x):
    return (round(math.sqrt(2*50*x/30)))

string = input("enter the sequence:")
numlist = string.split(',')
intnumlist = [int(x) for x in numlist]
resultlist = [funct(x) for x in intnumlist]
resultlist

# optional step --

strlist = [str(i) for i in resultlist]
print(','.join(strlist))



#Question 7
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i * j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

dim = input("enter the dim of the array:").split(',')
dimnum = [int(x) for x in dim]
dimnum
result = []
for i in range(dimnum[0]):
    rowlist=[]
    for j in range(dimnum[1]):
         rowlist.append(i*j)
    result.append(rowlist)     
result        


# input splitted ','
dim = input("enter the dim of the array:").split(',')
# convert the input to list and convert the list elements to int
dim = [int(x) for x in dim]
resultlist=[]
for i in range(dim[0]):
    rowlist=[]
    for j in range(dim[1]):
                rowlist.append(i*j)
                #rowlist
    resultlist.append(rowlist)  
print(resultlist)          

#  OR

dim = input("enter the dim of the array:").split(',')
# convert the input to list and convert the list elements to int
dim = [int(x) for x in dim]
resultlist=[[0 for row in range(dim[0])] for col in range(dim[1])]
for row in range(dim[0]):
    for col in range(dim[1]):
        resultlist[row][col] = row*col
              
print(resultlist)    

#Question 8      

#Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.

#Suppose the following input is supplied to the program:

string_in = input("enter the string:").split(',')
print(','.join(sorted(string_in)))


#or


string_in = input("enter the string:").split(',')
string_in
print(sorted(string_in))

#or - to not print a list just a string

string_in = input("enter the string:").split(',')
string_in.sort()
print(','.join(string_in))

#Question 9
#Write a program that accepts sequence of lines as input and prints the lines 
#after making all characters in the sentence capitalized
#Suppose the following input is supplied to the program:
# cannot do in above method becoz upper functionality is not applible to list object
#----or

listA = []
string_in = input("enter the string:").split(' ')
for element in string_in:
    listA.append(element.upper())
print(','.join(listA))    


#or



listA=[]
string_in = input("enter the string:").split(' ')
for x in string_in:
    list.append(x.upper())
print(' '.join(list))    

#-----or

list = []
while True:
    string_in = input("enter the number:").split(' ')
    if string_in:
          list.append(string_in.upper())
    else:    
          break
for line in list:
    print(line)       


#Question 10
#Write a program that accepts a sequence of whitespace separated words as input 
#and prints the words after removing all duplicate words and sorting them alphanumerically.    

string_in = input("enter the string:").split(' ')
result = set(string_in)
print(','.join(sorted(result)))

# or

listU=[]
string_in = input("enter the string:").split(' ')
for i in string_in:
    if i not in listU:
        listU.append(i)
print(','.join(sorted(listU)))        
# or
string_in = input("enter the string:").split(' ')
#sentence = [x for x in string_in.split(' ')]
print(' '.join(sorted(set(string_in))))



#---OR
string_in = input("enter the string:")
sentence = [x for x in string_in.split(' ')]
sentence
print(' '.join(sorted(list(set(sentence)))))
 
#--OR
#this method doesnt work if there are more than 2 repeatations
word = input('enter the string: ').split()

for i in word:
    if word.count(i) > 1:  # count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))


#---OR

word = input("Enter:").split()
[word.remove(i) for i in word if word.count(i) > 1 ]
# removal operation with comprehension method
word.sort()
print(" ".join(word))     

#Question 11
#Write a program which accepts a sequence of comma separated 4 digit binary numbers 
#as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.

bin_num=input("enter the decimal number:").split(',')
result = []
for i in bin_num:
      y=int(i,2)
      if y%5==0:
          result.append(y)
result          

# or

bin_num=input("enter the decimal number:").split(',')
dec_list = [x for x in bin_num]
dec_list
int_list = []
for x in dec_list:
   y=int(x,2)
   int_list.append(y)
print(int_list)   
result_list = []
for y in int_list:
    if y%5==0:
        result_list.append(y)
    else:
        continue
result_list     

#---OR--best apprach
bin_num=input("enter the decimal number:").split(',')
result_list = []
for x in bin_num:
   y=int(x,2)
   if y%5==0:
      result_list.append(x)
   else:
       continue
print(result_list)  

#---OR

bin_num=input("enter the decimal number:").split(',')
result_list = []
for x in bin_num:
   y=int(x,2)
   if y%5==0:
      result_list.append(x)
   else:
       continue
print(','.join(result_list))  



#Question 12

#Write a program, which will find all such numbers between 1000 and 3000 
#(both included) such that each digit of the number is an even number.The numbers
# obtained should be printed in a comma-separated sequence on a single line.

resultlist=[]
for num in range(1000,3001):
     temp_str=str(num)   
     if ((int(temp_str[0])%2==0) and (int(temp_str[1])%2==0) and (int(temp_str[2])%2==0) and (int(temp_str[3])%2==0)):
         resultlist.append(temp_str)
print(resultlist)
    
#or-------

resultlist=[]
for num in range(1000,3001):
     temp_str=str(num)   
     if ((int(temp_str[0])%2==0) and (int(temp_str[1])%2==0) and (int(temp_str[2])%2==0) and (int(temp_str[3])%2==0)):
         resultlist.append(temp_str)
         s = ','.join(resultlist)
print(s)  

 # or even more precise - excluding 0's                       
                  
listA=[]
for i in range(1000,3001):
             num = i
             count = 0
             while(num!=0):
                 div = num%10
                 if div!=0:
                     if div%2==0:
                         count = count + 1
                 num = num//10
             if count == 4:
                 listA.append(i)
listA
       

#Question 13
#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:   
str_in=input('enter the string:')
alpha = [x for x in str_in if x.isalpha()]
print("Alpha length:",len(alpha))
print('-----------')
digit = [x for x in str_in if x.isdigit()]
print("Digit length:",len(digit))


#Question 14
#Write a program that accepts a sentence and calculate the number of upper case 
#letters and lower case letters.Suppose the following input is supplied to the program:

sentence = input("enter the sentence:").strip(' ')
upper = []
lower = []
for i in sentence:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    else:
        continue
upper
lower    

# OR
sentence = input("enter the sentence:").strip(' ')

upper = []
lower = []
for x in sentence:
    if x.isupper():
        upper.append(x)
    elif x.islower():
        lower.append(x)
    else:
        continue
print("length upper:", len(upper))
print("length lower:", len(lower))        


#Question 15
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as 
#the value of a. Suppose the following input is supplied to the program:

n = int(input('enter the no:'))
result = 0
for i in range(1,n+1):
    for j in range(0,i):
           result = result + n*10**j
result    


# or


result = 0
str_in = input('enter the number:')
temp = str_in
for i in range(5):
    result = int(str_in)+result
    print(result)
    print('---')
    str_in = str_in+temp
    print(str_in)


#Question 16
#Use a list comprehension to square each odd number in a list. 
#The list is input by a sequence of comma-separated numbers. 
#Suppose the following input is supplied to the program:    

    
list_in = input('enter the sequence:')
#list_in = [int(x) for x in list_in]
result_list=[x for x in list_in.split(',') if int(x)%2!=0]
print(','.join(result_list))

#-----OR---

#Question 17
#Write a program that computes the net amount of a bank account based a transaction 
#log from console input. The transaction log format is shown as following:
   
n = int(input('enter the number of trans:'))
str = input('enter the trans:').split(',')
str
tran=[]
amt =[]
result=0
for element in str:
   str_keys = element.split('-')
   tran.append(str_keys[0])
   amt.append(str_keys[1])
for i in range(len(tran)):
    if tran[i]=='D':
        result=result+int(amt[i])
    else:
        result=result-int(amt[i])
print(result)        

# take input and print in dict
# observed that keys must be unique, more one one W or D such as WWDW will result 
#in WD

d={}
n = int(input('enter the number of trans:'))
str = input('enter the trans:').split(',')
str
tran=[]
amt =[]
for element in str:
   str_keys = element.split('-')
   print(str_keys)
   print('---')
   tran.append(str_keys[0])
   amt.append(str_keys[1])
 
for i in range(0,len(tran)):
    d[amt[i]]=tran[i]
d      

#Question 18
#A website requires the users to input username and password to register. 
#Write a program to check the validity of password input by users.

#Following are the criteria for checking the password:

#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will 
#check them according to the above criteria. Passwords that match the 
#criteria are to be printed, each separated by a comma.


import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter string to test: ")
result = re.findall(pattern, password)
if (result):
    print("valid password:",password.split(','))
else:
    print ("Password not valid" )       

import re
line = "pet:cat I love cat"
a = re.match(r"pet:\w\w\w",line)
a

#---or---uing if-else and forloop
import re  
password = input("Enter string to test: ")

pass_value = []
for i in password:
    if len(password)>6 and len(password)<12: 
              if re.match("[a-z]",password):
                        pass_value.append(i)
              elif re.match("[A-Z]",password):
                        pass_value.append(i)
              elif re.match("[0-9]",password):    
                        pass_value.append(i)
              elif re.match("[@#$%^&+=]",password):
                        pass_value.append(i)
              else:
                        break
    else:
        break
              
pass_value     
print(','.join(pass_value))    
              
              
#Question 19
#You are required to write a program to sort the (name, age, score) tuples by 
#ascending order where name is string, age and score are numbers. The tuples are input 
#by console. The sort criteria is:              
#1: Sort based on name
#2: Then sort based on age
#3: Then sort by score        
#The priority is that name > age > score.


str_in = input('enter name-age-score:').split(',')
info=[]
for element in str_in:
   info.append(tuple(element.split('-')))
print(sorted(info,key=lambda x: (x[0],x[1]))) 

# or
   
from operator import itemgetter
str_in = input('enter name-age-score:').split(',')
info=[]
for element in str_in:
   info.append(tuple(element.split('-')))
   
print(sorted(info,key=itemgetter(0,1,2)))     


#-----OR

from operator import itemgetter, attrgetter

l = []
while True:
    s=input("enter info:").split(',')
    if not s:
        break
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))

#---OR----

listA=[]
while True:
    s=input("enter info:").split(',')
    if not s[0]:
        break
    listA.append(tuple(s))
print(sorted(listA,lambda s:[0],s[1],s[2]))    

#Question 20
#Define a class with a generator which can iterate the numbers, which are divisible by 7, 
#between a given range 0 and n.

class my_class:
    def result(self,num):
        return [x for x in range(num+1) if x%7==0]   
num=int(input('enter the range:'))        
ob1=my_class()   
print(ob1.result(num))    

#Question 21
#A robot moves in a plane starting from the original point (0,0). 
#The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
#The trace of robot movement is shown as the following:

#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2

import math
steps_in=input("enter the steps:").split(',')
dir=[]
for step in steps_in:
     x = step.split(' ')
     dir.append(tuple(x))
dist = [0,0]    
for i in dir:
    if i[0] == 'up':
        dist[1] = dist[1]+int(i[1])
    elif i[0] =='down':
        dist[1] = dist[1]-int(i[1])
    elif i[0] =='left':
        dist[0] = dist[0]-int(i[1])
    else:
        dist[0] = dist[0]+int(i[1])
dist        
print('final distance:',round(math.sqrt(dist[0]**2+dist[1]**2)))    

# or

import math
steps_in=input("enter the steps:").split(',')
dir=[]
for step in steps_in:
    dir.append(tuple(step.split('-')))
print(dir) 
destx=0
desty=0
for step in dir:   
    if step[0]=='UP':
        desty=desty+int(step[1])
    elif step[0]=='DOWN':
        desty=desty-int(step[1])
    elif step[0]=='RIGHT':    
        destx=destx+int(step[1])
    elif step[0]=='LEFT':    
        destx=destx-int(step[1])    
    else:
        break
dist= round(math.sqrt(destx**2+desty**2))
print(dist)   

#---OR
import math
while True:
    step = input("enter the steps:")
    if not step:
          break
    dir=step[0]
    dist =step[1]
    if dir=='UP':
        desty=desty+int(dist)
    elif dir=='DOWN':
        desty=desty-int(dist)
    elif dir=='RIGHT':    
        destx=destx+int(dist)
    elif dir=='LEFT':    
        destx=destx-int(dist)    
    else:
        break
dist= round(math.sqrt(destx**2+desty**2))
print(dist)   


#Question 22
#Write a program to compute the frequency of the words from the input. 
#The output should output after sorting the key alphanumerically.

#Suppose the following input is supplied to the program:


str_in=input("enter the string:").split()
Listkey = []
Listvalue=[]
my_dict={}
for element in str_in:
    if element not in Listkey:
        x = str_in.count(element)
        Listkey.append(element)
        Listvalue.append(x)
        
    else:
        continue
for i in range(len(Listkey)):
     my_dict[Listkey[i]]=Listvalue[i]    
print(my_dict)
print('-------sorted------')
for key in sorted(my_dict.keys()):
    print("%s: %s" % (key, my_dict[key]))
#Question 23
#Write a method which can calculate square value of number

def square(n):
    return n**2

n = int(input('enter the number:'))    
square(n)
    
#Question 24
#Python has many built-in functions, and if you do not know how to use it, 
#you can read document online or find some books. But Python has a built-in document function for every built-in functions.

#Please write a program to print some Python built-in functions documents, 
#such as abs(), int(), raw_input()

#And add document for your own function

print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
def square(num):
    return num**2
print(square(3))
print (square.__doc__)


#Question 25
#Define a class, which have a class parameter and have a same instance parameter.

class Edureka():
#defining class variabe
    def __init__(self):
        self.name = 'Ayon'
# defining instance variable    
    def setname(self,name):
        self.name=name
    
        
        
ob1 = Edureka()
ob2 = Edureka() 
# printing class variable   
print(ob1.name)
print('-----')
# printing instance variabel

ob2.setname('Rivan')
print(ob2.name)
    
    
#Question 26
#Define a function which can compute the sum of two numbers.

def add(x,y):
    return x+y
print(add(3,4))

#Question 27
#Define a function that can convert a integer into a string and print it in console.

def convert(n):
    return str(n)
n = int(input('enter the number:'))
print(convert(n))
print(type(convert(n)))

#Question 28
#Define a function that can receive two integer numbers in string form and 
#compute their sum and then print it in console.

def convertsum(x,y):
    z = int(x)+int(y)
    return z
str_in = input('enter the number:').split(',')
for element in str_in:
    x = str_in[0]
    print(x)
    y = str_in[1]
    print(y)
print('----')
print(convertsum(x,y))    

#Question 29
#Define a function that can accept two strings as input and concatenate them 
#and then print it in console.

def concat_str(x,y):
    z = x+' '+y
    return z
str_in = input('enter the number:').split(',')
for element in str_in:
    x = str_in[0]
    print(x)
    y = str_in[1]
    print(y)
print('----')
print(concat_str(x,y))

#Question 30
#Define a function that can accept two strings as input and print the string 
#with maximum length in console. If two strings have the same length, 
#then the function should print all strings line by line.

def cal_len(x,y):
    if len(x)>len(y):
        print('string'+' '+ x +'has max length')
    elif len(y)>len(y):   
        print('string'+' '+ y +'has max length')
    else:
        print('both strings have same length')
str_in = input('enter the strings:').split(',')        
for element in str_in:
    x = str_in[0]
    print(x)
    y = str_in[1]
    print(y)
print(cal_len(x,y))    

#Question 31
#Define a function which can print a dictionary where the keys are numbers 
#between 1 and 20 (both included) and the values are square of keys.

def my_dict(num):
    d={}
    listkey = [x for x in range(num+1)]
    listvalue = list(map(lambda x:x**2, listkey))
    for i in range(len(listkey)):
        d[listkey[i]] = listvalue[i]
    print(d)    
num=int(input("enter the range:"))    
my_dict(num)

#---or    
def my_dict(num):
    for value,key in enumerate(list(map(lambda x:x**2,range(num+1))), 1):
                print(key,value)
num=int(input("enter the range:"))   
my_dict(num)  

              

# OR
#----or

def my_dict(num):
    dict = {i:i**2 for i in range(num+1)}
    return dict
num=int(input("enter the range:"))   
my_dict(num)                

# ---or

def my_dict(num):
    d={}
    for i in range(num+1):
        d[i]=i**2
    return d
num=int(input("enter the range:"))   
my_dict(num)                

#Question 32
#Define a function which can generate a dictionary where the keys are numbers 
#between 1 and 20 (both included) and the values are square of keys. 
#The function should just print the keys only

def dict_key(num):
    d={}
    for i in range(num+1):
        d[i]=i**2
    print(d.keys())
num=int(input("enter the range:"))   
dict_key(num)

#Question 33
#Define a function which can generate and print a list where the values are 
#square of numbers between 1 and 20 (both included).

def my_list(num):
    return [x**2 for x in range(num+1)]
num=int(input("enter the range:"))   
my_list(num)

#Question 34
#Define a function which can generate a list where the values are square of 
#numbers between 1 and 20 (both included). Then the function needs to print the 
#first 5 elements in the list.

def my_list(num):
    listA= [x**2 for x in range(num+1)]
    listB=[]
    print(listA)
    print('----')
    for i in range(len(listA)):
        if i>5:
            break
        else:
            listB.append(listA[i])
    print(listB)       
            
        
num=int(input("enter the range:"))   
my_list(num)

#---OR
def my_list(num):
    listA= [x**2 for x in range(num+1)]
    print(listA)
    print('----')
    print(listA[:5])       
            
        
num=int(input("enter the range:"))   
my_list(num)

#Question 35
#Define a function which can generate a list where the values are square of 
#numbers between 1 and 20 (both included). Then the function needs to print 
#the last 5 elements in the list.
def my_list(num):
    listA= [x**2 for x in range(num+1)]
    print(listA)
    print('----')
    print(listA[15:])       
            
        
num=int(input("enter the range:"))   
my_list(num)

#Question 36
#Define a function which can generate a list where the values are square of 
#numbers between 1 and 20 (both included). Then the function needs to print all 
#values except the first 5 elements in the list.

def my_list(num):
    listA= [x**2 for x in range(num+1)]
    print(listA)
    print('----')
    print(listA[:15])       
            
        
num=int(input("enter the range:"))   
my_list(num)

#Question 37
#Define a function which can generate and print a tuple where the value are 
#square of numbers between 1 and 20 (both included)

def my_list(num):
    listA= [x**2 for x in range(num+1)]
    tupA = tuple(listA)
    return tupA
            
        
num=int(input("enter the range:"))   
my_list(num)

#Question 38
#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first 
#half values in one line and the last half values in one line.

TupleA = (1,2,3,4,5,6,7,8,9,10)
TupleB = TupleA[:5]
TupleC = TupleA[5:]
TupleB
TupleC

    

TupleB = TupleA[:5]
TupleC = TupleA[5:]
TupleB
TupleC

#Question 39
#Write a program to generate and print another tuple whose values are even 
#numbers in the given tuple 

TupleA = (1,2,3,4,5,6,7,8,9,10)
listA = []
for i in range(len(TupleA)):
    listA.append(TupleA[i])
listA
print('---')
listB = [x for x in listA if x%2==0]  
listB  

# OR--
TupleA = (1,2,3,4,5,6,7,8,9,10)
TupleB = tuple(filter(lambda x:x%2==0,TupleA))
TupleB



#Question 40

#Write a program which accepts a string as input to print "Yes" if the string is 
#"yes" or "YES" or "Yes", otherwise print "No".

str_in = input('enter the string:')
if (str_in =='yes') or (str_in =='YES') or (str_in =='Yes'):
    print('Yes')
else:
    print('No')
    
#Question 41
#Write a program which can map() to make a list whose elements are square of 
#elements in [1,2,3,4,5,6,7,8,9,10]    
listA = [1,2,3,4,5,6,7,8,9,10]     
listB = list(map(lambda x:x**2,listA))
listB
# or
listA = [1,2,3,4,5,6,7,8,9,10]   
[x**2 for x in listA]
# or square only the even #s

listA = [1,2,3,4,5,6,7,8,9,10]   
[x**2 for x in listA if x%2==0]

#Question 42
#Write a program which can map() and filter() to make a list whose elements 
#are square of even number in 

listA = [1,2,3,4,5,6,7,8,9,10]  
print(list(map(lambda x:x**2,filter(lambda x:x%2==0,listA))))

#Question 43
#Write a program which can filter() to make a list whose elements are 
#even number between 1 and 20 (both included).

listA = [1,2,3,4,5,6,7,8,9,10]     
listB = list(filter(lambda x:x%2==0,listA))
listB

#Question 44
#Write a program which can map() to make a list whose elements are square of 
#numbers between 1 and 20 (both included).

# same as question 41

#Question 45
#Define a class named American which has a static method called printNationality.

class American():
    def race(self,nationality):
        self.nationality=nationality
ob1 = American()
nationality='Indian'
print(ob1.race)
        
#OR---

class American():
    @staticmethod
    def nationality():
        print('i am american')
ob1 = American()
ob1.nationality      
        
#Question 46
#Define a class named American and its subclass NewYorker
class American():
        print('i am american')
# INHERITING below
class NewYorker(American):
    def race(self,nationality):
        print("Happy Learning - sub")
# object from subclass
ob1 = American()
ob2 = NewYorker()
ob2.race

#Question 47
#Define a class named Circle which can be constructed by a radius. The Circle 
#class has a method which can compute the area.
import math

class circle():
    def area(self,radius):
        self.radius=radius
        return math.pi*(radius)**2

new_ob = circle()
print(new_ob.area(2))

#--OR

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())

#Question 48
#Define a class named Rectangle which can be constructed by a length and width. 
#The Rectangle class has a method which can compute the area.

class rectangle():
    def area(self,length,breath):
        self.length = length
        self.breath=breath
        return length*breath
arect=rectangle()
print(arect.area(5,6))    

# or

class rectangle():
    def __init__(self,length, breath):    
        self.length = length
        self.breath = breath
    def area(self,length,breath):
        return length*breath
arect=rectangle()
print(arect.area(5,6)) 

#Question 49
#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument. 
#Both classes have a area function which can print the area of the shape where 
#Shape's area is 0 by default.
class shape():
    def area(self,length,breath):
        self.length = length
        self.breath=breath
        return length*breath
class square(shape):   
     def area(self,length):
        self.length = length
        return length*length
asquare = square()
asquare.area(4)
print('----')
ashape = shape()
ashape.area(5,6)

#Question 50
#Please raise a RuntimeError exception
raise RuntimeError('something wrong')

#Question 51 and 52 are for try-exception - will try later

#Question 53
#Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address. Both user names 
#and company names are composed of letters only

str_in = input("enter the email address:").split('@')
print('username:',str_in[0])

# findall returns a list so it doesnt go with group function
#---ORjust for username
import re
str_in = input("enter the email address:")
str_user = re.findall(r'(\w+)@',str_in)
print(str_user)

#--or--returns user name, website

import re
str_in = input("enter the email address:")
str_user = re.findall(r'(\w+)@(\w+)\.(\w+)',str_in)
print(str_user)

#--or match works with group becauae unlike findall it doesnt return a list
import re
emailAddress = input("enter the email address:")
#pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(r'(\w+)@(\w+)\.(\w+)',emailAddress)
print(r2.group(0))
print(r2.group(1))
print(r2.group(2))
print(r2.group(3))

#Question 54
#Assuming that we have some email addresses in the "username@companyname.com" 
#format, please write program to print the company name of a given email address. 
#Both user names and company names are composed of letters only

import re
str_in = input("enter the email address:")
str_user = re.findall(r'@(\w+)\.',str_in)
print(str_user)

#---or

import re
emailAddress = input("enter the email address:")
#pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(r'(\w+)@(\w+)\.',emailAddress)
print(r2.group(0))
print(r2.group(1))
print(r2.group(2))

#Question 55
#Write a program which accepts a sequence of words separated by whitespace as 
#input to print the words composed of digits only.

#Example: If the following words is given as input to the program:

import re
str_in = input("enter the string:")
str_user = re.findall(r'[0-9]',str_in)
print(str_user)

#---or--using match---will give u the first occurance only

import re
str_in = input("enter the string:")
str_user = re.match(r'[0-9]',str_in)
print(str_user.group(0))

str_user = re.match(r'(\w+)',str_in)
print(str_user.group(0))

#---using list comprehnesion

email = input("enter the string:").split()
ans = [word for word in email if word.isdigit()]  
print(ans)

#Question 56
#Print a unicode string "hello world".
import base64
str1 = "hello world"
str2 = base64.b64encode(str1.encode('utf-8'))
str2

#Question 57
#Write a program to read an ASCII string and to convert it to a unicode 
#string encoded by utf-8.

import base64
str1 = input("enter the string:")
str2 = base64.b64encode(str1.encode('utf-8'))
str2

#Question 58
#Write a special comment to indicate a Python source code file is in unicode.

# -*- coding: utf-8 -*-

#Question 59
#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

num=int(input('enter the number:'))
result =0
for i in range(1,num+1):
    temp=float(i/(i+1))
    print(temp)
    print('--')
    result=float(result+temp)
print(round(result,2))    

#Question 60
#Write a program to compute:
#f(n)=f(n-1)+100 when n>0
#and f(0)=1

def my_func(num):
    if num==0:
        return 1
    else:
        return my_func(num-1)+100
num=int(input('enter the number:'))
my_func(num)    

#Question 61
#Please write a program to compute the Fibonacci Sequence value of f(n) with a
# given n input by console.  

def fib_func(num):
    if num==0:
        return 0
    elif num ==1:
        return 1
    else:
        return (fib_func(num-2) + fib_func(num-1))
num=int(input('enter the number:'))
fib_func(num) 

#--or

num=int(input('enter the number:'))

#Question 62
#Please write a program to compute the value of f(n) with a given n input by console 
#and print the sequence

def fib_func(num):
    if num==0:
        return 0
    elif num ==1:
        return 1
    else:
        return(fib_func(num-2) + fib_func(num-1))
list_fib=[]        
num=int(input('enter the number:'))
for i in range(num+1):
    temp = fib_func(i)
    list_fib.append(temp)
print(list_fib)    

#Question 63
#Please write a program using generator to print the even numbers between 0 
#and n in comma separated form while n is input by console.

num=int(input('enter the number:'))
print([x for x in range(num+1) if x%2==0])

#Return sends a specified value back to its caller whereas Yield can produce a 
#sequence of values. We should use yield when we want to iterate over a sequence, 
#but don't want to store the entire sequence in memory. Yield are used in Python generators.
#---or
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input("enter the num:"))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))

#Question 64
#Please write a program using generator to print the numbers which can be divisible 
#by 5 and 7 between 0 and n in comma separated form while n is input by console.
#Example: If the following n is given as input to the program:
      
    
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%35==0:
            yield i
        i+=1


n=int(input("enter the num:"))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))

#---OR

print([x for x in range(100) if x%35==0])


#Question 65
#Please write assert statements to verify that every number in the list [2,4,6,8] is even.
#Use "assert expression" to make assertion.

li = [2,4,6,8]
for i in li:
    assert i%2==0
    
#Question 66
#Please write a program which accepts basic mathematic expression from console and print the evaluation result.

#Example: If the following n is given as input to the program:  35+3=38
#Use eval() to evaluate an expression.    
    
expression = input("enter:")
print(eval(expression))    

#Question 67
#Please write a binary search function which searches an item in a sorted list. 
#The function should return the index of element to be searched in the list.
def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
        index = 0
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	           found = True
               index == midpoint
	        else:
	           if item < alist[midpoint]:
	                last = midpoint-1
	           else:
	                first = midpoint+1
	
	    return index
    
    
alist=[2,5,7,9,11,17,222]
binarySearch(alist, 11)

#Question 68
#Please generate a random float where the value is between 10 and 100 using Python module.

import random
rand_num = random.uniform(10,100)
print(rand_num)

#Question 69
#Please generate a random float where the value is between 5 and 95 using Python module.

import random
rand_num = random.uniform(5,95)
print(rand_num)

#Question 70
#Please write a program to output a random even number between 0 and 10 inclusive 
#using random module and list comprehension.

#Use random.choice() to a random element from a list.

li = [2,4,6,8]
import random
print random.choice([i for i in range(11) if i%2==0])

#Question 71
#Please write a program to output a random number, which is divisible by 5 and 7, 
#between 10 and 150 inclusive using random module and list comprehension.
#Use random.choice() to a random element from a list.

import random
print (random.choice([i for i in range(10,150) if i%35==0]))

#Question 72
#Please write a program to generate a list with 5 random numbers between 
#100 and 200 inclusive.

#Use random.sample() to generate a list of random values.

import random
print(random.sample(range(100,201), 5))

#Question 73
#Please write a program to randomly generate a list with 5 even numbers between 
#100 and 200 inclusive.

import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))

#Question 74
#Please write a program to randomly generate a list with 5 numbers, which are 
#divisible by 5 and 7 , between 1 and 1000 inclusive.
import random
print(random.sample([i for i in range(1,1001) if i%35==0], 5))

#Question 80
#Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

print([x for x in [5,6,77,45,22,12,24] if x%2!=0])

#Question 81
#By using list comprehension, please write a program to print the list after 
#removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
print([x for x in [12,24,35,70,88,120,155] if x%35!=0])

#Question 82
#By using list comprehension, please write a program to print the list after 
#removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
listA = [12,24,35,70,88,120,155]
print([x for x in listA if listA.index(x)%2!=0])

#  OR----

listA = [12,24,35,70,88,120,155]
listB = [x for (i,x) in enumerate(listA) if i%2!=0]
listB

#Question 83
#By using list comprehension, please write a program to print the list after 
#removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

listA = [12,24,35,70,88,120,155]
listB = [x for (i,x) in enumerate(listA) if 2<=i<=4]
listB

#Question 84
#By using list comprehension, please write a program generate a 3*5*8 3D array 
#whose each element is 0.

array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)    

#Question 85    
#By using list comprehension, please write a program to print the list after 
#removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
listA= [12,24,35,70,88,120,155]
print([x for (i,x) in enumerate(listA) if i not in (0,4,5)])   

#Question 86
#By using list comprehension, please write a program to print the list after 
#removing the value 24 in [12,24,35,24,88,120,155].

print([x for x in [12,24,35,24,88,120,155] if x!=24])

#Question 87

#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a 
#program to make a list whose elements are intersection of the above given lists.

listA=set([1,3,6,78,35,55])
listB=set([12,24,35,24,88,120,155])
print(listA.intersection(listB))

#Question 88
#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print 
#this list after removing all duplicate values with original order reserved.

listA = [12,24,35,24,88,120,155,88,120,155]
listB=[]
for i in listA:
    if i not in listB:
        listB.append(i)
    else:
        continue
print(listB)        
    
#---OR

setA = set([12,24,35,24,88,120,155,88,120,155])
print(setA)


#Question 89
#Define a class Person and its two child classes: Male and Female. All classes 
#have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person():
    def getGender(self):
        return 'unknown'
class Male(Person):
    def getGender(self):
        return 'Male'
class Female(Person): 
    def getGender(self):
        return 'Male'
    
M = Male()
print(M.getGender)

F = Female()
print(F.getGender)    
    
    
#Question 90
#Please write a program which count and print the numbers of each character in a 
#string input by console.

#Example: If the following string is given as input to the program:

str_in=input('enter the string:')
listA = []
for i in str_in:
    listA.append(i)
listA
print('---')
listB=[]
for i in listA:
    if i not in listB:
        listB.append(i)
listB
print('****')
listC=[]
for i in range(len(listB)):
    temp=listA.count(listB[i])
    listC.append(temp)
listC
print('$$$$')
d={}   
for i in range(len(listB)):
    d[listB[i]]=listC[i]
d    

        