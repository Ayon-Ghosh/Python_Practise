# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:58:15 2020

@author: 140524
"""
#https://www.youtube.com/watch?v=kr0mpwqttM0
#passing one function in another function
def square(n):
    x = n*n
    return x
f = square(5)
print(f)
#or
f = square
f
f(5)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result    

squares = my_map(square,[1,2,3,4,5])
print(squares)

def cube(x):
    return x*x*x

cubes = my_map(cube, [1,3,5,7,9])
cubes

#returing a function through another function

def logger(msg):
    def log_message():
        print('log:',msg)
    return log_message

log_hi = logger('hi')
log_hi
log_hi()

# another example

def html_tag(tag):
    def wrap_test(text):
        print('<{0}><{1}><{0}>'.format(tag,text))

    return wrap_test

print_h1 = html_tag('h1')
print(print_h1.__name__)
print_h1('heading1')
print_h1('heading2')
print_h1('heading3')

print_p1 = html_tag('p1')
print_p1('paragraph')

#https://www.youtube.com/watch?v=swU3c34d2NQ
#-----Closures()


def outer_funct():
    message = 'hi'
    def inner_funct():
        print(message)
    return inner_funct
#outer_funct()    
# or
my_func = outer_funct()
my_func
print(my_func.__name__)
print(my_func())
my_func()


# therefore as shown above the variable my_func assigned to the outer function still now
#has access to the inner function even after the outer function has stopped execution

import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__,args))
        print(func(*args))
    return log_func    
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
add_logger= logger(add)
add_logger(3,4)
add_logger(7,8)
sub_logger = logger(sub)
sub_logger(11,7)
sub_logger(11,7)


#https://www.youtube.com/watch?v=FsAPt_9Bf3U
#Decorator

def outer_function(msg):
    message  = msg
    def inner_function():
        print(message)
    return inner_function
hi_func = outer_function('hi')
hi_func()
bye_func = outer_function('bye')
bye_func()

# or

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function
hi_func = outer_function('hi')
hi_func()
bye_func = outer_function('bye')
bye_func()    


# decorator and wrapper function are kind of similar to the outer and inner function

# decorator is a function that takes in another function as an argument and adds 
#some functionality and returns another function - all of these without altering the 
#source code of the inner function

def decorator_function(msg):
    def wrapper_function():
        print(msg)
    return wrapper_function
hi_func = decorator_function('hi')
hi_func()
bye_func = decorator_function('bye')
bye_func()    

# the format below
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

# example
    
def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')
    
decorated_display = decorator_function(display)    
decorated_display
decorated_display()


#decorator functions allows us to easily add functiolaity to our existing functions
# by adding that functionality inside the wrapper

def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}.'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')
    
decorated_display = decorator_function(display)    
decorated_display
decorated_display()

# the above 3 lines can be changed to write

@decorator_function
def display():
    print('display function ran')
display()    

# or

display = decorator_function(display)    
display()


# now adding another function to pass with arg and keyword argument in the decorator 
# function
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}.'.format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')
display()   

@decorator_function
def display_info(name, age):
    print('display_info function ran with arguments {} and {}'.format(name, age))
display_info('Ayon', 40) 


# using a class decorator instead of a decorator function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
    def __call__(self,*args,**kwargs):
        print('call method executed before {}.'.format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)
        
@decorator_class
def display():
    print('display function ran')
display()   

@decorator_class
def display_info(name, age):
    print('display_info function ran with arguments {} and {}'.format(name, age))
display_info('koyel', 39) 


# see a real life exampkle of decorator function for creating trhe loggin file
#the decorator function allows us to add any number of the times the new functionality to
#any number of functions while keeping the code for the functionlity at one place 

#this is a practical examplke of using decorators for logging function
def my_logger(orig_func):
       import logging
       logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
       
       def wrapper(*args,**kwargs):
           logging.info('ran with args {} and kwargs {}'.format(*args,**kwargs))
           return orig_func(*args,**kwargs)
       return wrapper
   

@my_logger
def display_info(name, age):
    print('display_info function ran with arguments {} and {}'.format(name, age))
display_info('koyel', 39) 
display_info('Rivan', 5) 
#this is a practical examplke of calculating time for each function

def my_timer(orig_func):
    import time
    
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result =  orig_func(*args,**kwargs)
        t2 = time.time() - t1
        print('{} ran in {} secs'.format(orig_func.__name__, t2))
        return result
    return wrapper
        
    
@my_timer
def display_info(name, age):
    print('display_info function ran with arguments {} and {}'.format(name, age))
display_info('koyel', 39) 
display_info('Rivan', 5)        