# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:09:26 2019

@author: 140524
"""

#A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, 
#DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
#UP 5
#DOWN 3
#LEFT 3
#RIGHT 2
#The numbers after directions are steps. Write a program to compute the distance current position 
#after sequence of movements.
#Hint: Use math module.

dir = input('enter the dir:').split(',')
dir
step = input('enter the steps:').split(',')
step
d = {}
for i in range(len(dir)):
    d[dir[i]]=step[i]
d    
x = 0
y = 0
for i in d:
    if i == 'up':
                  y=int(d[i])+y
    elif i =='down':
                  y=y-int(d[i])
    elif i =='right':
                  x=int(d[i])+x
    else:
                 x=x-int(d[i])
print(x,y) 

print(((x)**2 + (y)**2)**0.5)                
              

#Weather forecasting organization wants to show is it day or night. So, write 
#a program for such organization to find whether is it dark outside or not.
import time
ltime = time.localtime()
ltime
current_hour = ltime.tm_hour
print(current_hour)

if (current_hour<=7 or current_hour>=19):
    print("Its dark out side")
else:
    print("its day now")
    
                      
##Design a software for bank system. There should be options like cash withdraw,
# cash credit and change password. According to user input, 
#the software should provide required output. 
   
pin =int(input('enter PIN:'))
if pin!=1980:
    print('Incorrect PIN')  
else:  
    tran = input('enter the tran:')
    bal=1000
    if tran=='withdraw':
        amt = int(input('enter amt:',))
        print('final balance:',bal-amt)
    elif tran=='deposit':
        amt = int(input('enter amt:',))
        print('final balance:',bal+amt)
    else:
        pass1 = input('change password:',)
        pass2 = input('enter password again:',)
        if pass1 == pass2:
            print('password changed')
        else:
            print('password entered wrong')
           
#Write a program which can compute the factorial of a given numbers.
#Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
fact(8)    

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
result=[]
listD = list(map(lambda x:int(x),d))
for D in listD:
    Q =round(math.sqrt(2*c*D/h))
    result.append(str(Q))
print(','.join(result))    

#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 

#The element value in the i-th row and j-th column of the array should be i * j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


row_col=input('enter row and col:').split(',')
row_col
row=int(row_col[0])
col=int(row_col[1])
result=[]

for i in range(row):
    sub=[]
    for j in range(col):
        sub.append(i*j)
    result.append(sub)
    
result    

#Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.


words = input('enter the words:').split(',')
sort_words=[]
for word in words:
    sort_words.append(word.upper())
print(','.join(sorted(sort_words)))    

# 

words = input('enter the words:').split(',')

sorted(list(map(lambda x:x.upper(),words)))    

#---------------

import pandas as pd
bank_data=pd.read_csv('C:\\edureka\\PRClass_3\\Data_set\\bank-data.csv')
bank_data.head()
job = set(bank_data.job.unique())
prof = input('enter job:')
prof1=prof.lower()
prof1

if prof1 in job:
    print('client elligible')
else:
    print('dont call')    


bank_data.columns
bank_data.age.min()
bank_data.age.max()
#------
import pandas as pd
usecols = ['Last_Name','First Name', 'Flag']
df=pd.read_csv('C:\\edureka\\PRClass_3\\Data_set\\FairDealCustomerData.csv',header= None, names=usecols)
df.head()

df[['Title','First_Name']]=df['First Name'].str.split('.',expand = True)
df.head()
df.drop('First Name', inplace=True)
df

      
# OR---

Title = []
First_Name=[]
for i in df['First Name']:
    c = i.split('.')
    Title.append(c[0])
    First_Name.append(c[1])
Title
First_Name    
df['First_Name'] = pd.Series(First_Name)
df
df['Title']=pd.Series(Title)
df.columns
df.drop('First Name', inplace=True)
df
df_exception = df[df['Flag'] == 0] 
df_exception        

#---or-----

import pandas as pd
import numpy as np
df=pd.read_csv('C:\edureka\PR_class_4\Data_Set\SalaryGender.csv')
df.head()
sal=np.array(df['Salary'])
Gen = np.array(df['Gender'])

df_MPHD = df[(df.Gender==1) & (df.PhD==1)]
df_MPHD

df_PHD = df[df.PhD==1]
df_PHD[['Age','PhD']]
df_PHD[['Age','PhD']].count()

# or
df.loc[0,'Gender']
       
count=0
for index, row in df.iterrows():
    Male= row['Gender']
    PhD = row['PhD']
    if Male==1 and PhD==1:
        print(row)
        count=count+1
print(count)        

num_arr = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
list_cnt= []
for i in range(10):
    j = num_arr.count(i)
    list_cnt.append(j)
list_cnt    
    
import numpy as np
arr = np.arange(0,12,1).reshape(4,3)
arr[arr<6].reshape(2,3)

arr = np.random.randn(10,10)

print('min:',arr.min())
print('---')
print('max:',arr.max())

arr=np.arange(0,11)

def fun(x):
    if x<4:
        return x
    elif x<9:
        return -x
    else:
        return x
listA=list(map(lambda x:fun(x),list(arr)))
np.array(listA)


arr=np.arange(0,11)
arr[(arr>3) &(arr<9)]*-1
m=(arr>3) &(arr<9)
m
print(m.astype(int))
arr=arr[m]*-1
arr

import numpy as np
import pandas as pd
usecols = ['col1','col2','col3']
df=pd.DataFrame(np.random.randn(3,3), columns=usecols)
df.sort_values('col1')
df.sort_values('col2')

   
import pandas as pd
drink = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/drinks.csv')  
drink.head(5)

temp=drink.loc[2,:]
drink.loc[2,:]=drink.loc[3,:]
drink.loc[3,:]=temp

drink.head(5)



import numpy as np
import pandas as pd
usecols=['col1','col2','col3']
df=pd.DataFrame(np.random.randn(3,3),columns=usecols,index=['row1','row2','row3'])
df
df['Sum_rows'] = pd.Series([df.loc['row1',:].sum(),df.loc['row2',:].sum(),df.loc['row3',:].sum()], index = ['row1','row2','row3'])
print(df)
usecols.append('Sum_rows')
usecols
row=pd.DataFrame([[df.col1.sum(),df.col2.sum(),df.col3.sum(),df.Sum_rows.sum()]],columns=usecols,index=['row4'])
df.append(row,sort=False)
df














 