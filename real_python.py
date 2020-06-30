# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:14:42 2020

@author: 140524
"""

weight = '0.2 kg'
animal = 'newt'
print('{0} is the weight	of	the	{1}.'.format(weight, animal))

weight = '0.2 kg'
animal = 'newt'
print(f'{weight} is the weight	of	the	{animal}.')

phrase = 'the surprise is here somewhere.'
print(phrase.find('surprise'))

s = 'AAA'
print(s.find('a'))

s = 'version 2.0'
x = float(s.find('2.0'))
x
str(x)

s_in = input('enter:')
print(s_in.find('Vx'))

def cube(num):
    return num*num*num
print(cube(5))

def mul(n,m):
    return n*m
n = int(input('enter num1:'))
m = int(input('enter num2:'))
print(mul(n,m))

c = float(input('enter temp in celcius:'))
f = round((c*9)/5 + 32,2)
print('{} is the temp in fahrenheit'.format(str(f)))


for i in range(1,4):
    for j in ['a','b','c']:
        print('i=',i, 'j=',j)
        
        
for i in range(2,11):
    print (i)

i = 2
while(i<11):
    print(i)
    i = i+1           
    
#Generator - yield    
def double(num):
   for i in range(1,4):
           num =  num*2
           yield num
           
for i in double(2):
     print(i)    
     
#Another example of generator:

#A Python program to generate squares from 1 
# to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num)      
    
    
def invest(prin, rate, time):
    for i in range(1, time+1):
                interest = prin*rate*i
                amt = prin+interest
                yield amt
                
        
print('principal amount: $100 ')    
print('annual rate of return: 0.05 ')  
i=1  
for amt in invest(100,0.05,8):
    print('year',i,':', amt)        
    i= i+1
    
    
for	i in range(1,4):				
    j=	i*2				
    print("i is",i,	"and j is",	j)
    
    
def add_underscore(word):
          
          temp = ''
          for i in range(0,len(word)):
                 temp = temp+word[i] +'_'
                 
          return temp

print(add_underscore('Ayon'))    
        
i =1
while True:
    if (i==1) or (i%3==0):
        continue
    elif (i==50):
        break
    else:
        print(i)
    i =i +1