# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:35:03 2019

@author: 140524
"""

# Itertools

from itertools import chain

x='abc'
y='def'
z='ghi'
for i in x,y,z:
    print(i)

# now with chain method - it even breaks down the string to single char
    
x='abc'
y='def'
z='ghi'
for i in chain(x,y,z):
    print(i)    
    
# or

x='abc'
y='def'
z='ghi'
arr=[x,y,z]
for i in chain.from_iterable(arr):
    print(i)    

#itertools combinations method -USING this u can write all combinations that can be
# done using this method
from itertools import combinations as com    
letter = 'ABCDEF'    
x = com(letter,3)
y=[''.join(i) for i in x]
y


# Accumulate function
import operator
from itertools import accumulate
x = list(range(5))
y= list(accumulate(x,operator.add))
y

# counters are subclass of dictionary
#There are 3 ways to initialize counters

from collections import Counter
#with sequence of itemns containing repeated values

print(Counter(['A','A','B','B','C','C','C','C','A','B']))

#with keyword

print(Counter({'A':3,'B':2,'C':6}))

#with keyword arguments
print(Counter(A=3,B=7,C=2))

# itertools.product -------
import itertools
p=d=q=range(0,5)
pdq = list(itertools.product(p,d,q))
pdq


#Update function to update counter

#initialize a variable for the counter function. This initialize and empty counter
#To add a data into it, we use the update function with data in the parenthesis
#first update the counter with data1 and then update with data2

from collections import Counter
count = Counter()
count.update([1,2,2,3,3,1,1,2,2])
print(count)
count.update([1,2,4])
print(count)
    
#example 2:
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv')
data.head()
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))
language_counter   

# we can use subtract function to find the difference between 2 counters

from collections import Counter
C1 = Counter(A=3,B=7,C=2)
C2 = Counter(A=10,B=2,C=8)
C1.subtract(C2)
print(C1)

import pandas as pd
a = pd.Series([1])
a
b = pd.Series([2,3,4])
b
a.add(b)
