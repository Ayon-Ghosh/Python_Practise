# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:59:58 2019

@author: 140524
"""

#separate digits
listA = []
num = int(input('enter your num:'))
i = num
while(i!=0):
    div = i%10
    listA.append(str(div))
    i=i//10
strA = ','.join(listA)     
print(strA[::-1])    
    
    

# amstrong number by user input

num = int(input("enter your num: "))
i = num
n = len(str(i))
result = 0
while(num!=0):
   div = num%10
   result = result + div**n
   num = num//10
if i==result:
    print("Bingo:",i)
else:
    print("Sorry:",i)

# amnstrong number in a range
listA=[]
for i in range(1001):
    num = i
    n = len(str(num))
    result = 0
    while(i!=0):
            div = i%10
            result = result + div**n
            i = i//10
    if num==result:
            #print(num)
            listA.append(str(num)) 
listA
print(','.join(listA))
#user inputs the range and the amstrong #s are printed in a list
            
low = int(input("enter your low bar: "))
high = int(input("enter your high bar: "))
ListA = list()
for i in range(low, high+1):
    num = i
    n = len(str(num))
    result = 0
    while(i!=0):
            div = i%10
            result = result + div**n
            i = i//10
    if num==result:
            ListA.append(num)
print(ListA)          
 