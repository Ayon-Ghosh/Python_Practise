# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# first star program
num = int(input("enter the number of rows: "))
for i in range(1, num+1):
    for j in range(0, i):
        print("*", end = '')
    print()    
    
# second star program

num = int(input("enter the number of rows: "))
for i in range(1, num+1):
    for j in range(num+1, i,-1):
        print("*", end = '')
    print()    

# third star program   
    
row = int(input("enter the number of rows: "))
col = 2*row
for i in range(1, row+1):
    for j in range(row+1, i,-1):
          print(" ", end = '')
    for j in range(0,i):
          print("*", end ='')
    for j in range(1,i):
          print("*", end ='')
    print()      
    
    
# create a number pyramid

row = int(input("enter the number of rows: "))
col = 2*row
for i in range(1, row+1):
    for j in range(row+1, i,-1):
          print(" ", end = '')
    for j in range(1,i+1):
          print(j, end ='')
    for j in range(1,i):
          print(j, end ='')
    print()      

# create another number pyramid

row = int(input("enter the number of rows: "))
col = 2*row
for i in range(1, row+1):
    for j in range(row+1, i,-1):
          print(" ", end = '')
    for j in range(1,i+1):
          print(j, end ='')
    for j in range(i-1,0,-1):
          print(j, end ='')
    print() 




# create another number pyramid

row = int(input("enter the number of rows: "))
col = 2*row
for i in range(1, row+1):
    for j in range(row, i,-1):
          print(" ", end = '')
    for j in range(1,i+1):
          print(i, end ='')
    for j in range(1,i):
          print(i, end ='')
    print()      
    


# create another number pyramid

row = int(input("enter the number of rows: "))
col = 2*row
count = 1
for i in range(1, row+1):
    for j in range(row, i,-1):
          print(" ", end = '')
    for j in range(1,i+1):
          print(count, end ='')
          count = count+1
    for j in range(1,i):
          print(count, end ='')
          count = count+1
    print()          
    
    
for i in range(1,10):
    if i<=5:
        for j in range(i):
            print('*',end = '')    
        print('\n')    
    else:
        for j in range(10,i,-1):
            print('*',end = '')    
        print('\n')      
        
        
user_inp = input('enter a word:')
print(user_inp[::-1])        