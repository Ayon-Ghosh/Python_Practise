# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:53:01 2019

@author: 140524
"""

#Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included). The numbers
# obtained should be printed in a comma-separated sequence on a single line.

result =[]
for i in range(2000,3201):
    num = i
    if num%7==0 and num%5!=0:
        result.append(num)
print(result)        
        
#Write a program which can compute the factorial of a given numbers. 
#Use recursion to find it.

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
        
n=int(input("enter the number: "))    
print(fact(n))


#Write a program which takes 2 digits, X,Y as input and generates a 
#2-dimensional array. The element value in the i-th row and j-th column of the
# array should be i*j.Note: i=0,1.., X-1; j=0,1,¡Y-1.

X = int(input("enter the row: "))
Y = int(input("enter the col: "))
result = []
for i in range(0,X):
    temp=[]
    for j in range(0,Y):
        a=i*j
        temp.append(a)
    result.append(temp)   
print(result)       


#--OR

X = int(input("enter the row: "))
Y = int(input("enter the col: "))
result=[i*j for i in range(0,X) for j in range(0,Y)]
print(result)


#--OR


X = int(input("enter the row: "))
Y = int(input("enter the col: "))
result=[[i*j for j in range(0,Y)] for I in range(0,X)]
print(result)


#Write a program that calculates and prints the value according to the given 
#formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H: C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma- 
#separated sequence.
import math
listA = []
C =50
H =30
n = int(input("enter the length of the list: "))
for i in range(0,n):
    temp = int(input())
    listA.append(temp)
print(listA)    
result = [int(math.sqrt(2) * math.sqrt(C) * math.sqrt(i)/math.sqrt(H)) for i in listA]
print(result)


#Write a program which accepts a sequence of comma separated 4 digit binary 
#numbers as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.
      
#---None comes when forming a bianry list--   inputs in list form  

def decimaltobinary(n):
    if (n>1):
        decimaltobinary(n//2)
    print(n%2,end='')    
value = []
num=int(input('enter the number of binary no: '))
for i in range (0,num):
       temp = input('enter binary: ')
       value.append(temp)
print(value) 
listD=[]
for p in value:
       intp = int(p,2)
       if intp%5==0:
         a = decimaltobinary(intp)  
         listD.append(a)
print(listD)  

#----or---

num = input().split(',')
result = list(filter(lambda x: int(x,2)%5==0,num))
print(result)

#Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

str1 = input("enter your sentence: ")
n = len(str1)
count = 0
for i in str1:
    if i.isupper():
        count = count+1
print("UpperCase: ",count)
print("Lowercase: ",n-count)
    
#---OR
str1 = input("enter your sentence: ")
listA=[x for x in str1 if x.isupper()]
print(listA, "all uppercase and the length is:",len(listA))
listN=[x for x in str1 if x.islower()]
print(listN, "all lowercase and the length is",  len(listN))

#Write a program that accepts a comma separated sequence of words as input and 
#prints the words in a comma-separated sequence after sorting them 
#alphabetically.

str1 = input("enter your sentence: ").split(',')
str2  = sorted(str1)
str2

#Write a program that accepts sequence of lines as input and prints the lines
# after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:

words = input("enter your sentence: ").split(' ')
        
caps = [x.capitalize() for x in words]
print("".join(caps)
