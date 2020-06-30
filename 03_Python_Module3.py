
# coding: utf-8

# # Functions

####[5]:


import os, sys, json


# Now we are good to get started with functions

####[1]:


def process(file_path):
    if os.path.exists(file_path):
        rp = open(file_path, 'r')
        for line in rp:
            print(line)
        rp.close()


####[8]:


def add(n1, n2):
    return n1+n2 if n1 > n2 else n2-n1

# add(10, 30)
n1 = input('Enter first number : ')
n2 = input('Enter second number : ')
n1 = int(n1)
n2 = int(n2)
add(n1, n2)


####[14]:


def new(a,b):
    return b

def third():
    print('Hello world!')
    
new(1,2) 
third()


# # Function Arguments

# #### This is fourth level heading


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


####[10]:


add(3, 4)


####[9]:


add('python', 'anaconda')


####[12]:


add('anaconda', 'python')


# # Built-In Functions

####[6]:

#Python. | dir() function. dir() is a powerful inbuilt function in Python3, 
#which returns list of the attributes and methods of any object 
#(say functions , modules, strings, lists, dictionaries etc.)
dir()


####[7]:


abs(-10)


####[10]:


sum(20, 30)


####[11]:


sum([20,30,40])


####[34]:


chr(65)


####[35]:


chr(97)


####[14]:


int(12.36)


####[58]:

marks = []
any(marks)

marks = [45, 54, 99, 81, 12, -3]
any(marks)


####[60]:


marks.append(0)
all(marks)


####[61]:


list(reversed([10, 40, 30]))


####[63]:


sorted(marks, reverse=False)


####[20]:


names = ['Python', 'Steve', 'Jobs']
all(names)


####[21]:


for x in reversed([10, 40, 30]):
    print(x)


####[14]:

#It allows us to loop over something and have an automatic 
#counter.
    
# when just one var in taken to loop over the iterable with enumerate
#the  it prints indivitual tuples    
for index in enumerate([10, 20, 30],23):
    print(index)

# or
    
for val in enumerate([10, 20, 30],23):
    print(val)  
    
 # but when 2 vars are looped over then it prints the following way

for index,val in enumerate([10, 20, 30],23):
    print(index,val)  
   

####[65]:


bin(2)


####[16]:


oct(40)


####[37]:


hex(4)


####[38]:


int(hex(4))


####[17]:


v = 0x4
print(v)


####[22]:


oc = 0o77
oc


# # Lambda, map, filter and reduce

####[ ]:


def sq_func(x):
    return x**2 if x > 10 else x**3

sq_func(3)

####[42]:

#Python allows you to create anonymous function i.e function having no names 
#using a facility called lambda function. lambda functions are small functions usually 
#not more than a line. ... 
#The result of the expression is the value when the lambda is applied to an argument

sq = lambda x : x**2 if x > 10 else x**3 # def add(x, y)
sq(3)


####[41]:


sq(12)


####[44]:


marks


####[47]:


def categorize_marks(mark):
    if mark > 70:
        return 'Perfect'
    else:
        return 'Needs Improvement'
marks = [45, 54, 99, 81, 12, -3]    
for mark in marks[:-1]:
    print(categorize_marks(mark))


####[57]:


list(map(categorize_marks, marks))


####[48]:


list(map(lambda x: 'Perfect' if x >= 70 else 'Needs Improvement', marks)) # concise way of transforming values


####[49]:


list(filter(lambda x: (x >= 50 and x <= 75) or (x < 10 or x > 80), marks)) # concise way of filtering values


####[50]:


high_marks = []
for x in marks:
    if x >= 50:
        high_marks.append(x)
print(high_marks)


####[51]:


for x in filter(lambda x: x >= 50, marks):
    print(x)


####[30]:


def is_gt_50(mark):
    return mark>=50

list(filter(is_gt_50, marks))


####[50]:

#will give range of values range(1,6) as (1,2,3,4,5)
from functools import reduce
reduce((lambda x, y: x+y), range(1,6))




####[ ]:


# 1,2,3,4,5 = (((1*2)*3)*4)*5 => 1*2 (x) 3(y) = x* y = (1*2*3) saved to x (1 * 2 * 3) y (4) 


####[67]:


####[42]:


# Generator
def elements(int_input):
    for x in range(1, int_input+1):
        return x
    print('Hello')
    
def elementss(int_input):
    for x in range(1, int_input+1):
        print('Hello')
    return x
        
print(elements(5))

print(elementss(5))


# or

def elements(int_input):
    i=1
    while i<=int_input:
                yield i
                i=i+1
gen = elements(5)
next(gen)
#--
next(gen)
# and so on

# or
for i in gen:
     print(i)            

# list(elements(5))
# range(1, 11)
# for value in elements(5):
#     print(value)


# # Function arguments - positional, keywords, arbitrary length

####[33]:


# non-default arguments - specify value for every argument
# default arguments - default to value specified

# positional notation - passing and defining arguments
# keyword notation - passing and defining arguments

def fun1(a,b,c,d=60):
    print(a,b,c)
    print(d)

    
# fun1(10, 20, 30) # positional
#fun1(10, 20, 30,40)
# fun1(a=10,c=20,b=45) # keyword notation
#fun1(a=10, c=30, b=20, d=40, e=50)


#Arbitrary
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")

# **Python Function - Variable Length Arguments with *args 
# Keyword arguments and **kwargs

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))



def fun(a,b,c,d=60,*p,**kwargs):
    print(a,b,c)
    print(p)
    print(d)
    print(kwargs)
    
# fun(10, 20, 30) # positional
# fun(a=10,c=20,b=45) # keyword notation
fun(a=10, c=30, b=20, d=40, e=50)
# fun(10, 20)


def myFunction(arg1, arg2, arg3, *args, **kwargs):
     print ('First Normal Argument : ' + str(arg1))
     print ('Second Normal Argument : ' + str(arg2))
     print ('Third Normal Argument : ' + str(arg3))
     print ('Non-keyworded Argument : ' + str(args))
     print ('Keyworded Argument : ' + str(kwargs))


myFunction(1, 2, 3, 4, 5, 6, 7, name='Mandar', country='India', age=25)
#Keyworded Argument : {'country': 'India', 'age': 25, 'name': 'Mandar'}



####[30]:


def pass_the_world(*c):
    print(type(c), c)
    
pass_the_world()
pass_the_world(10,20,30,40,*list(range(10)))

###########################################################################
####[38]:


# non-default arguments
# default arguments
# positional notation - passing and defining arguments
# keyword notation - passing and defining arguments

def format_name(fname, lname, mname=None, reverse=True):
    print(type(fname), type(lname), type(reverse))
    if reverse:
        return lname + ' ' + fname
    else:
        return fname + ' ' + lname

# print(format_name('Python', 'Spark'))

# oracle : username, password, tnsname
# mysql: username, password, host, port, ssl-key, ssl-ca, ssl-cert
def connect(db_type, **kwargs):
    oracle_template = 'jdbc:client:://{username}:{password}/{tnsname}/{host}/{port}'
    if db_type == 'Oracle':
        cxn_str = oracle_template.format(**kwargs) # 'jdbc:client:://{username}:{password}/{tnsname}
        print(cxn_str)
    elif db_type =="mysql":
        cxn_str = oracle_template.format(**kwargs) # 'jdbc:mysql://hist:port/username/password/sslc/sslk'
        print(cxn_str)
    
def add_marks(standard, names=None, **marks):
    return sum(marks)

def master(ndf1, ndf2, df1=2, df2=3, d=3, *args, **kwargs):
    print(ndf1, ndf2, df1, df2)
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)
    
master(10, 20, df1=30, k=10, v=20, d=30, p=50)
print(add_marks('Xth', marks=[10, 20, 30, 40, 90, 100, 45, 54]))
# connect('mysql', username='Python', password='Anaconda', tnsname='Disaster', host='cloudserver', port='3306')


####[59]:


def flexi(*args):
    print(type(args))
    print(args)
    
# flexi()
flexi(10,20,30)
# flexi(10)


####[63]:


def afun(a,b,c=100,*args):
    print(a,b,c)
    print(args)
    print(a+b+c+sum(args))
    print('------')
# afun(10,20)
# afun(10,20,30)
afun(10,20,30,40,50,63,75,81,0,12)


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


# # Classes

####[1]:


class Number():
    pass

x = Number
y = Number()
print(x)
print(y)



##############

# File one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    
    


####[25]:


class EdurekaCustomer(object):
    '''
    This class is used to represent Edureka Customer.
    '''
    DEFAULT_DISC = '3%'
    DISC_STRATEGY = lambda age: '20%' if age <= 40 else '15%'
    
    def __get_default_pwd(cls):
        import random, string
        return ''.join([random.choice(string.ascii_letters + string.digits) for x in range(10)])
    
    def __init__(self, name, email, phone, age, userid):
        print('Inside constructor')
        self.name = name
        self.email = email
        self.phone = phone
        self._age = age
        self.userid = userid
        self.__pwd = self.__get_default_pwd()
        
    @property
    def hashed_pwd(self):
        import base64
        return base64.b64encode(self.__pwd.encode())
        
    def set_phone(self, val):
        self.phone = phone
        
    def get_phone(self):
        return self.phone
        
    def set_pwd(self, pwd):
        self.__pwd = pwd # base64

    @classmethod # decorator
    def owned_by_class(cls, arg1):
        print(cls.DISC_STRATEGY(30))
        print(arg1)
        cls.i_am_static('called from owned_by_class')
        
    def available_discount(self, wealthy_customer=False):
        if not wealthy_customer:
            self.i_am_static('called from available_discount')
            return self.DISC_STRATEGY(self.age)
        else:
            return self.DEFAULT_DISC
        
    def __del__(self):
        print('This is my last breath, interpreter will perform the rites.')
        
    @staticmethod
    def i_am_static(msg):
        print(msg, 'Did you notice, I do not require self/cls as first argument')
        return 'Statically simple'
        
#     def get_pwd(self, pin):
#         pin_from_db = self.__fetch_pin()
#         if pin == pin_from_db:
#             return self.__pwd
#         else:
#             raise Exception('AuthorizationError : pin mismatch')

ob = EdurekaCustomer('Python Enthusiast', 'reachable@gmail.com', '999999999', 30, 'pyenthu')
# print(ob)
print(ob.get_phone())
print(ob.name, ob.email, ob._age, ob.phone)
print(ob._EdurekaCustomer__pwd)
print(ob.hashed_pwd)
# ob.i_am_static('called by object')
# EdurekaCustomer.i_am_static('called by class')
# print(ob.get_pwd())
# del ob
# print(ob)
# ob.owned_by_class('random')
# EdurekaCustomer.owned_by_class('classy')
# print(ob.available_discount())
# print(EdurekaCustomer.__dict__)
# print(EdurekaCustomer.__doc__)
# print(EdurekaCustomer.__bases__)
# print(EdurekaCustomer.__mro__)
# print(EdurekaCustomer.__name__)
# print(EdurekaCustomer.DEFAULT_DISC)
# print(EdurekaCustomer.owned_by_class('abc'))
# print(EdurekaCustomer.i_am_static('Hello'))


####[20]:


import base64
pwd = 'aO4Ly1WlMT'
print()


####[23]:


print(base64.b64encode(pwd.encode()))


####[29]:


SOME_VAR = 'Something'

class Species(object):
    PLANET = 'Any'

    def get_planet(self):
        return self.PLANET
        
class People(Species):
    PLANET = 'Earth'
    
    def __init__(self, name, eth, age):
        print('Inside Init!')
        self._name = name
        self.ethnicity = eth
        self.__age = age
    
    def __str__(self):
        return 'Name, Ethnicity and Age : {}, {}, {}'.format(self._name, self.ethnicity, self.__age)
    
    def get_name(self):
        return self._name
    
    def get_age(self, pretty=True):
        return self.__age if not pretty else '{} yrs old'.format(self.__age)
    
    def __get_db_connection(self):
        return cxn
    
    def __validate_key(self, key):
        return 'pwd'
    
    def get_pwd(self, key):
        # verify the key in a db table and fetch associated pwd if key is correct
        return 'Authenticated. Password is :', ''
    
    def is_old(self):
        return self.__age > 60
    
#     def get_planet(self):
#         return 'Mostly {} if a person is not cosmonaut.'.format(self.PLANET)
        
    def lives_under_water(self):
        return 'Depends. If it is '

x = People('Adam', 'US', 45)
print(x)
x.weight = '60 pounds'
print(x)
is_old = x.is_old()
x._name = 'Brian Adams'
is_old = 'is' if is_old else 'is not'
print('Person {} {} old, age is {}, weight is {}'.format(x._name, is_old, x.get_age(), x.weight))
print('I am on planet : {}'.format(x.get_planet()))


####[ ]:


class Vector(object): # N x 1 or 1 x N
    def __init__(self, *elements):
        self.elements = list(elements)
        
    def get_elements(self):
        return self.elements
    
    # for overloading +
    def __add__(self, other):
        values = []
        for x, y in zip(self.elements, other.get_elements()):
            values.append(x+y)
        return values

    def __sub__(self, other):
        pass
    
    def __len__(self):
        return self.no_of_pages
    
book1 = Book('Author', 'Name', 'No of Pages')
len(book1)


####[32]:


import abc
print(abc.__name__)
print(abc.__doc__)


####[86]:


dir(Number)


####[135]:


# self - a pointer to current object under consideration
# cls - a pointer to the class from which object is derived

class Account():
    account_type = 'Savings'
    
    def __init__(self, account_id, name, password):
        self.id = account_id
        self.name = name
        self.__pwd = password
    
    @classmethod
    def _cls_method(cls):
        print('This is a class method')
    
    def welcome(self):
        print(self.__get_welcome_message())
        
    def __get_welcome_message(self):
        if self.account_type == 'Savings':
            return 'Dear {}, we have some exciting offers for Savings account customers. Please connect with us for more details.'.format(self.name)
        else:
            return 'Dear {}, welcome to bank XYZ.'.format(self.name)
    
    def __del__(self):
        print('Invoking destructor, happy ending {}'.format(self.name))
    
#dir(Account)


####[136]:


ob1 = Account(123, 'Python', 'anaconda')
print(ob1.__dict__)
ob1.welcome()
print(Account.account_type)
Account._cls_method()
ob1._cls_method()

# print(Account.__dict__)
# print(Account.__doc__)


####[137]:


del ob1


####[138]:


ob1


####[93]:


print(Account.__name__)


####[111]:


Account.account_type = 'Current'
ob = Account()
#dir(ob)


####[112]:


ob.account_type


####[113]:


ob.welcome()


####[109]:


print(ob.__dict__)


####[110]:


ob.name = 'Bob'
print(ob)


# ####heritance, Encapsulation/Abstraction, Overriding and Polymorphism

####[16]:


class JustForClarity():
    def does_it_eat(self):
        return 'God knows what you expect me to return.'

class Species():
    def does_it_eat(self):
        return 'Depends'
    
    def lives_under_water(self):
        raise NotImplementedError
        
class People(Species):
    def needs_oxygen(self):
        return True
    
    def needs_water(self):
        return True
    
    def does_it_eat(self):
        output = super(People, self).does_it_eat()
        return '{}, as long as the person is not fasting.'.format(output)
    
    def lives_under_water(self):
        return 'Is usually on land unless its too hot when a person would prefer swimming.'
    
class Civilization(People):
    pass
#     def does_it_eat(self):
#         return 'Civilized to eat only well cooked food.'
    
class Asians(Civilization, JustForClarity):
    pass

class Americans(People):
    pass
    
s1 = Species()
#print(s1.does_it_eat())
#print(s1.lives_under_water())
p1 = People()
#print(p1.does_it_eat())
#print(p1.lives_under_water())
a1 = Asians()
#print(a1.does_it_eat())
print(Asians.__mro__)
print(a1.does_it_eat())


####[ ]:


# [<one-position>] - lists, tuples, strings, sets
# [start:stop:step] - lists, tuples, strings, sets
class ConnectToDB():
    def __init__(self, connect_to='Postgres'):
        self._connect_to = connect_to
        self.__establish_cxn()
        
    def __connect_to_postgres(self):
        pass
    
    def __connect_to_mysql(self):
        pass
    
    def __establish_cxn(self):
        if self._connect_to == 'Postgres':
            self.__connect_to_postgres()
        else:
            self.__connect_to_mysql()
            
    def setCxnToMysql(self):
        if self._connect_to != 'MySQL':
            self._connect_to = 'MySQL'
            self.__establish_cxn()
        
    def setCxnToPostgres(self):
        if self._connect_to != 'Postgres':
            self._connect_to = 'Postgres'
            self.__establish_cxn()
            
    def __add__(self):
        pass
    
    def __subtract__(self):
        pass
    
    def __len__(self):
        return self.__no_of_pages


# # Standard Libraries - sys, os, json, random, re, datetime, 
# #                                    string, dateutil, math

####[17]:


import sys
print(sys.argv)


####[4]:


import os
import random
import sys
import string
import datetime
from datetime import datetime, date, timedelta
from dateutil import parser
import json

# l1 = sys.argv
# print('Welcome {} to Python world!'.format(l1[1]))
# print(os.getcwd())
# os.chdir(l1[2])
# print(os.getcwd())

# print(random.randrange(12))
# print(random.randint(10, 13))
# lot = ['abc123', 'def345', 'ghi987']
# print(random.choice(lot))
# random.choice
# list of letters + list of digits
# print(string.ascii_letters + string.digits + string.punctuation)
# print(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(100)]))


####[16]:

import datetime
print(date.today())
print(datetime.today())
print(datetime.utcnow())
print(date.isoweekday(date.today() + timedelta(3)))
print(parser.parse('2018-10-06T20:53:24.999+05:30'))


####[18]:


# print(datetime.date.today())
# print(datetime.date.today() - datetime.timedelta(1))
# print(parser.parse('2018-08-05'))
emp = {'name': 'Steve', 'age': 25, 'salary': 12000,
       'addresses': {'primary': "White House",
                     'secondary': '''Trump Towers'''}
       }
jemp = json.dumps(emp)
print(type(emp), type(jemp))
print(jemp)

# [] () . + {2,3} ? * 


####[19]:


# print('-----------------------------------')
jstr = '{"name": "Steve", "age": 25, "salary": 12000, "addresses": {"primary": "White House", "secondary": "Trump Towers"}}'
jdict = json.loads(jstr)
print(jdict)
print(type(jstr), type(jdict))


####[28]:


import re


####[32]:


s1 = 'Python is wonderful'
m1 = re.findall('ful', s1, re.IGNORECASE)
m1

