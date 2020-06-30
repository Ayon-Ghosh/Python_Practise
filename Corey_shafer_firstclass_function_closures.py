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
log_hi()

# another example

def html_tag(tag):
    def wrap_test(text):
        print('<{0}><{1}><{0}>'.format(tag,text))

    return wrap_test

print_h1 = html_tag('h1')
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




