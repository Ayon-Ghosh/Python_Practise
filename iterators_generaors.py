# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:08:51 2019

@author: 140524
"""

#iterators

# iterator protocol is a protocol to work with iterator and iterables
# here list 1 is the iterable on which the iterator functions operates
# the list1 is the iterable - list, sets, dicts, strings,, tuples are all iterables
# the iterables calls the iterator whose work is to return the next element in the list
#
list1 = [1,2,3,4]
for i in list1:
    print(i)

# see how iter fucntion works

listA = [1,2,3,4]
iterate = iter(listA)
next(iterate)    
# returns 1
next(iterate)    

# returns 2 and so on till the elements are finished - then it will raise a exception - stop ietration

# what for loop does internally is given here through iter function

def print_each(iterable):
     iterate = iter(iterable)
     while True:
            try:
                item = next(iterate)
            except StopIteration:
                break
            else:
                print(item)
                
listA = ['apple','orange']
print_each(listA)                
       


# Generator function is a function which returns generator-iteraor with the help of 
#yield keyword

# example to generate fub series

def fib_max(num):
    a,b=0,1
    i=a
    while i<=num:
           c=a+b
           a,b=b,c
           yield c
           i=i+1
# calling one after another values using next function

gen = fib_max(10)
gen   
# returns 1        
next(gen)        
        
next(gen)        
        
next(gen)        

next(gen)        

next(gen)        

next(gen)        

next(gen)        

next(gen)   
next(gen)        
next(gen)        
next(gen)        
# stops iteration here
next(gen)  
      
# we can do the same thing with for loop

for i in gen:
    print(i)     

#modifying the fib series a little bit
    
def fib_max(num):
    a,b=0,1
    while True:
           c=a+b
           if c<=num:  
               yield c
               a,b=b,c
           else:
               break
           
            
gen = fib_max(20)
for i in gen:
     print(i)            
     
lst = [1,2,3,4]
lst1=lst.__iter__()     
lst1
next(lst1)
# or using iter
lst2 = iter(lst)
while i<len(lst):
    print(next(lst2))

