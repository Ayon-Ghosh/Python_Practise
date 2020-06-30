# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:01:52 2019

@author: 140524
"""

#---amuls academy - videos 18,19,20,21,22,23,24

#list Examples

animals = ['dog','cat', 'monkey']
animals[0]

list2=[[10,20],[30,40]]
list2[1][0]

list1=[10,20,30,40]
for num in list1:
    print(num)
    
#list operation - replace

animals = ['dog','cat', 'monkey']
animals[2] = 'tiger'
animals    


#list operation - insert

animals = ['dog','cat', 'monkey']
animals.insert(1,'tiger')
animals

#list operation - sort for similar type of values

animals = ['dog','cat', 'monkey']
animals.sort()
animals

list1=[10,20,30,40,2,5,6]
list1.sort()
list1

#list operation - delete
list1=[10,20,30,40,2,5,6]
del list1[4]
list1

del list1
list1

#list operation - append 

animals = ['dog','cat', 'monkey']
animals.append('tiger')
animals

#list operation - reverse

animals.reverse()
animals

#-----Tuple----immutable - cant - replace, insert, sort,del, append

animals = ('dog','cat','monkey')
animals[1]

tuple1 = ((10,2,3),(3.5,4))
tuple1[1][0]

tuple2 = ()
tuple2

# sequence operation on list,dict, tuple,sets,str

#len

name = "ayon"
list1=[10,20,3.5,2.3]
tup1 = (10,20,3.5,2.3)

len(name)
len(list1)
len(tup1)

# select

name[1]
list1[3]
tup1[2]

# slice

name[1:4]
list1[2:]
tup1[1:]
name[::-1]

#count - how many times a value is present
list1=[10,20,3.5,2.3]
word = "frickkky"
word.count('k')
list1.count(2.3)

#index - which char's index u want

word.index('c')
tup1.index(3.5)

#membership - whether a char is present in the sequence

'm' in name
'y' in word

#concatenation - join 2 sequence - tup and list wont concatenate or cant list with str

word1 = ' house'
word+word1

list3 = [111,112,113,'hello']
list2+list3
tup2 =(111,112)
tup1+tup2

#Min value
list1=[10,20,30,40,2,5,6]
min(list1)
min(word)

#Max value

max(list2)

#sum - total sum of element - cant use sum ops for string

sum(list1)
sum(tup1)


#List assignment - change in list 1 will also change list2

list1 = [10,20,30,40]
list2 = list1
list2

list1[2] = 'hello'
list2

#list copying  = change in list 1 will also change list2

list3=list(list1)
list3
list1[2]='ayon'
list3

result=[x**2 for x in [1,2,3]]
result

#---end of videos - amuls-----#

#---List comprehension - amuls --132,133,134,148,150---

# [expression for item in iterable]
#[expression for item in iterable if condition]
#[expression if condition else statement for item in iterable]

[x for x in range(1,11)]
[x for x in range (1,11) if x%2==0]
[x if x>2 else x+1 for x in range(1,11)]

num = [1,2,3,4]
[10*x for x in num]

words = ['hello', 'a', 'ayon']
[x.upper() for x in words]
[x.capitalize() for x in words]

str1 = "ayonsonu1234"
str2 = [x for x in str1 if x.isalpha()]
str3 = [x for x in str1 if x.isdigit()]
str2
str3

list1 = [[1,2,3], [4,5,6], ['a','b','c']]

# OR

def firstelement(x):
    return x[0]
[firstelement(x) for x in list1]

[x**2 for x in range(1,11)]

a = [1,2,3,4]
b = [10,1,6]
[x+y for x in a for y in b]

a = [1,2,3,4]
c = [2,2,2,2]
[a[i]+c[i] for i in range(0,len(a))]

# list comprehension to replace lambda and map function

num = [1.2,2.3,4.5]
listA = list(map(lambda x:int(x), num))
listA

#-- alternate

[int(x) for x in num]


# list comprehension to replace filter function

num1 = [1,4,6,9,11,12,13,15,16]
list(filter(lambda x:x%2==0, num1))
del list
#-- alternate

[x for x in num1 if x%2==0]

# list comprehension to replace reduce function
num1 = [1,4,6,9,11,12,13,15,16]
import functools
functools.reduce(lambda x,y:x+y, num1)

#-- alternate

sum([x for x in num1])

# sorting of list,tuples, dict

# using the built in functions first

# sort

num = [10,2,3.4,56,10.11]
num.sort()
num

num.sort(reverse=True)
num

list1 = ['aa','ccc','eee','b','ddd','eeee','ffffff']
list1.sort()
list1
list1.sort(reverse=True)
list1


# using key function to sort based on legth
list1 = ['aa','ccc','eee','b','ddd','eeee','ffffff']
list1.sort(key=len)
list1

# using user defined function to sort based on second element of the list and Key
# sort method ONLY for list

list2 = [[2,9],[1,10],[3,7]]

def second(x):
    return x[1]

list2.sort(key=second)
list2

list3 = [(2,9),(1,10),(3,7)]

def second(x):
    return x[1]

list3.sort(key=second,reverse=True)
list3


# sorted method for list, tuple, dicts

# sorted(iterable, key=None, reverse = false)

list1 = [7,5,6,3,2,1]
tup1 = ((3,8),(2,9),(1,10),(4,7))
d1 = {3:'a',2:'f',6:'d',7:'b'}
sorted(list1,reverse = True)
sorted(tup1,key=second)

sorted(d1)
sorted(d1.values())
sorted(d1.keys())

#---sort dict by keys and retrun in dict form

sorted(d1.items())

#---sort dict by values and retrun in list of tuples

sorted(d1.items(), key = lambda x:x[1])

tup2 = ((1,'a'),(4,'s'),(3,'z'),(2,'r'))
sorted(tup2,key=lambda x:x[1], reverse = True)


#---end of videos - amuls-----#

#---List comprehension - amuls --135,136,137,139,140---


# dictionary - Unordered collection of itesm


# creating dictionaries different way"

dict = {1:'tup'}
if 'list' not in dict:
    dict['list'] = []
dict['list'].append('list_item')
dict.setdefault(2)
print(dict)    

dict = {1:'tup'}
if 'list' not in dict:
    dict['list'] = 'list_item'
dict.setdefault(2)
print(dict)    


dict = {1:'tup'}
dict.setdefault('list','listitem')
print(dict)
    
dict = {2:'tup'}
dict['list'] = 'listitems'
print(dict)


my_d = {}
my_d[1] = 'apple'
my_d[2] = 'banana'
my_d[3] = 'cat'
my_d

# using dic constructor

d = dict([(1,'apple'),(2,'banana'),(3,'cat')])
d

# create dic using 2 parrallel list

a = [1,2,3,4]
b = ['a','b','c','d']

d = {}
for i in range(len(a)):
    d[a[i]]=b[i]
d    
    

# access the elements and insert new elements from dict

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

d[1]

#---Using Get method u can access the values from dict, it will return none when key is not present

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

d.get(3)

# insert at end

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
d[5] = 'f'
d

d[2] = 'ayon'
d

len(d)

# from Keys - create dic using fromkeys

#fromkeys(iterable, value) - value is optional

list1=[1,2,3,4]
dict.fromkeys(list1,None)

# OR

{}.fromkeys(range(1,7),'Ayon')



# setdefault - search for a key in dic. If the key is present it will return 
#the value of the key. If not present it will add the key to the dict

#setdefault(key,value) - value is optional

std = {'jon':20, 'alia':21, 'ayon':40}

std.setdefault('jon')
std.setdefault('koyel')
std
std.setdefault('rivan',4)
std
#---end of videos - amuls-----#

#---Edureka------
dict={1:"Python",2:"Android"}
for i in dict:
    print(i)
    print('---')
    print(dict[i])
print(dict)
print(dict[1])
dict[1]="Javascript"
print(dict)
del(dict[2])
print(dict)

print(len(dict))
print(str(dict))
print(type(dict))

dict = {'Name':'Zara','Age':7}
print(dict)
print(str(dict))

print(dict.copy())
dict.clear()
print(dict)

dict1={1:'Python',2:'Android'}
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.setdefault(1))
print(dict1.setdefault(3))
third_value = dict1.setdefault(3,'code')
print(third_value)
print(dict1)


dic={3:'Python',1:'Java',2:'Big Data'}
k=list(dic.keys())
print(k)

sk=sorted(k)
print(sk)

for k in sk:
    print(k,'=>',dic[k])
    
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],'age': 40.5}
print(rec.get('name'))

#....Dictionary compression

#creating one dictionary from another

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1.keys()
dict1.values()
dict1.items()
#This is the general template you can follow for dictionary comprehension in Python:
#dict_variable = {key:value for (key,value) in dictonary.items()}
#changing the values
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)
#adding conditions

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)

# multiple conditions

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

# triple condition

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict1_tripleCond)

#If-Else Conditions
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
dict1_tripleCond
#changing the keys
dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)


#creating dictionaries from 2 different unrelated list
k_range = range(1,26)
score = range(100,126)
dict(zip(k_range,score))

# creating dict when keys and values are relatable

new_dict_comp = {n:n**2 for n in range(1,10) if n%2 == 0}
new_dict_comp



# symmetric diff and dictionary comparision

d1 = {'fname':'Ayon','lname':'jobs','age':21}    
d2 = {'fname':'Ayon','lname':'Ghosh','age':21}
is_equal=True
# the below returns a empty set bcoz the length of d1 and d2 and the keys of d1 
#and d2 are exatly same
    diff = set(d1.keys()).symmetric_difference(set(d2.keys()))
    print(diff)

#The most common use for break is when some external condition is triggered requiring a 
#hasty exit from a loop. The break statement can be used in both while and for loops. 
#The pass statement in Python is used when a statement is required syntactically but you do 
#not want any command or code to execute.

if len(set(d1.keys()).symmetric_difference(set(d2.keys()))) == 0:
    print("both dicts have same length and same keys")
    for k in d1:
        print('key is:', k)
        if k in d2:
            print(d1[k], d2[k])
            if d1[k]==d2[k]:
                continue
            else:
                is_equal = False
                break
        else:
            is_equal = False
            break
else:
    is_equal = False
print(is_equal)        
            
        

#----------


list=["Hadoop","Python","Android"]
print(list[1])

print(list[0:2])

print(list[-3])

list=["Hadoop","Python","Android"]

list[1]="Java"
print(list)

del(list[2])
print(list)

list=[1,2,3]
list.append("Machine Learning")
print(list)

list.extend(['g','h'])
print(list)

list.insert(1,'Scripting')
print(list)

list.remove(3)
print(list)

lst=[1,4,2,'x','y','z']
type(lst)
if type(lst)==list:
      print("Yes")



list3=[1,2,5,'Python','Haddop']
print(type(list3))

print([x**2 for x in[1,2,3,4,5]])


mylist = ["b", "C", "A"]
mylist2 = mylist.sort()

list4=[5,7,10,2]
sorted(list4)
list6 = list4.sort()
list4_revword = list4[::-1]


print([x**2 for x in[1,2,3,4,5]])

list=[1,2,3,4,5,'a','b','c']
print(list.pop(3))

list.remove('a')
print(list)

list1=['Python','XYZ','ABC','PQR']
print(list1)

print(sorted(list1))

print(list1[::-1])

#----------

list=[(1,2,3),("Python","Java")]
print(list)
print(len(list))
print(list[0][0:1])

list[0][1]=50
print(list)



tup=([1,2,3],[3,4,5],[5,6,7])
print(tup)
print(len(tup))
print(tup[0][1])

#Updating Tuple
tup[0][1]=90
print(tup)

#Deleting element in Tuple
del(tup[1][2])
print(tup)





list=[1,2,'Python','Android']
print(list)

list[2]='Data Science'
print(list)

tup=(1,2,3,'Data Science')
print(tup)

tup[1]='Python'
print(tup)



tuple1=(1,2,3,5,7,'a','b')
lst=list(tuple1)
print(lst)

lst[1]='Python'
print(lst)

tuple2=tuple(lst)
print(tuple2)


tuple1=(1,8,3,5,7)
print(sorted(tuple1))
print(tuple1[::-1])

#---split method

values=input("enter your value: ")
l=values.split(",")
l
t=tuple(l)
print(l)
print(t)

text = 'geeks for geeks'
# Splits at space 
print(text.split()) 
  
word = 'geeks, for, geeks'
  
# Splits at ',' 
print(word.split(', ')) 
  
word = 'geeks:for:geeks'
  
# Splitting at ':' 
print(word.split(':')) 
  
word = 'CatBatSatFatOr'
  
# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 


# ----str operations

str1='Welcome'
str2="to"
str3="""Edureka"""
print(str1)
print(str2)
print(str3)

string="Python"
print(string)
print(len(string))
print(string[1:3])
print('t' in string)

print("Welcome to %s%s%s"%("Python ","learning ","program"))
print("My name is %s and my age is %d and my income is %d"%("Annie",22,10000))
str='edureka'
print(str.capitalize())
print(str.count("ka",0,len(str)))

#--OR

print(str.count("ka"))


#---Encode

s=str.encode('utf-8','strict')
print(s)
str = 'edurekaee'
print(max(str))
print(min(str))
print(str.replace('e','--E--',4))
print(str.upper())
print(str.index('k'))

str1="Happy Learning"

print(str1[::-1])

print(str1[2:7])

print(str1.find('L'))

#---OR

print(str1.index('L'))
str2="Welcome to Edureka"

print(str1+str2)

print(str1*2)

#----set operation--

X=set('Welcome To Edureka')
print(X)

A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A-B)

s={'a','b','c','d','e','f','o','v'}
set1={'a','b','d','o','v'}
set2={'a','c','d','o','e'}
print(s.issuperset(set1))
print(set1|set2)
print(set1&set2)
print(set1-set2)
#add

s={1,2,3,'a','b'}
set1={1,'a','d'}
print(1 in set1)

print(set1.issubset(s))

print(5 not in s)
print(s.issuperset(set1))

#--or

print(s|set1)

#--or

print(s&set1)
print(s.union(set1))

print(s.difference(set1))

#---or

print(s-set1)

print(s.symmetric_difference(set1))
s={1,2,3,'a','b'}
s.pop()
print(s)
s.add('c')
print(s)


print(s.intersection(set1))

s.remove(1)
print(s)
s.discard(3)
print(s)

s.pop()
print(s)


s.clear()
print(s)

# ENUMERATE

a =['eat', 'sleep','drink']
b='code'
a[0]
x = list(enumerate(a))
print(x)

print(list(enumerate(b,2)))
    
for i in enumerate(a):
    print (i)
    
for count,i in enumerate(a,100):
    print(count,i)     
    
 
for i in enumerate(a,100):
    print(i)        
    
#-----------

m = [[1,2],[3,4],[5,6]] 
matrix = []
for i in range(2):
    row = []
    for j in range(3):
         row.append(m[j][i])
    matrix.append(row)

mat = [[m[i][j] for i in range(3)] for j in range(2)]
mat

matrix    
list(zip(*m))

len(m[0])
for row in m : 
    print(row) 
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
rez
print("\n") 
for row in rez: 
    print(row)    
    