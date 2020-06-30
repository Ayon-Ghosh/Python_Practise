# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 00:39:11 2020

@author: 140524
"""

#https://www.youtube.com/watch?v=bD05uGo_sVI&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=36


#class is a blue print based on which each instance of class is built
# method is a function that is associated with a class
#if you dont want to set up any attributes and methods of a class leave it for now
#using the pass
class employee:
    pass
# create instances of a clas    
emp1 = employee()
emp2 = employee()   
#note printing each instance of a class points out towaards a employee object at a 
#memory location 
print(emp1)
print(emp2)

#instance variables contain data that is unique to each instance
#examples below
emp1.first = 'Ayon'
emp1.last = 'Ghosh'
emp1.email = 'ayon.ghosh@company.com'
emp1.pay = 50000

emp2.first = 'koyel'
emp2.last = 'Ghosh'
emp2.email = 'koyel.ghosh@company.com'
emp2.pay = 60000
print(emp1.email)

# now creating the instance varaible of each instances of class is a lot of code
# to avoid that we can use init method inside the class
# the name, pay are all attributes of our class
# the init method are constructors of the instances of a class when the attributes are straightforward
#as shown below ---we will discuss the alternative constructors are class methods
# when the class attributes are not straight forward

class employee:
    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
#emp1 will be passed in as self in the init method
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
print(emp1.email)

# now lets add a method to the class
#lets add a method outside the class first - the method is to print full name

print ('{} {}'.format(emp1.first,emp1.last))

# now lets add the method inside the class

class employee:
    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
print(emp1.fullname())    

# now we call the class method from an instance in which the instance will pass itself
#as self as below

print(emp2.fillname)

#or

#we can call the class mnethod fropm the class itself. In that we will have to pass the 
#instance name - otherwise the class wont know what instance we are calling

print(employee.fullname(emp2))

# both of the above does the same thing

#-----------class variables
# instance variables are unique for each instances but class variables are shared across
# all instances

# lets take an example of annual raise of our company as the class variable - the same 
# to be shared by all the instances of the class


class employee:
    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
# see we have hard coded the raise here
# the problem is every time we will         
    def apply_raise(self):
        self.raised_pay = int(self.pay*1.04)
        return self.raised_pay
    
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
print(emp1.fullname())   
print(emp1.pay)
print(emp1.apply_raise())


# now instead of defining into a class method the 1.04 hard coded
# lets create a class variable raise_amount

class employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
employee.raise_amount
emp1.raise_amount
emp2.raise_amount

#using namespace to know all the attributes of a class
employee.__dict__
emp1.__dict__

#now lets set raise_amount only for emp1. emp2 wll take the raise_amount from the cl;ass

emp1.raise_amount = 1.05
emp1.__dict__
emp2.__dict__
emp1.raise_amount
emp2.raise_amount
employee.raise_amount

# thus using self.raise_amount in the apply_raise function will make it specific to each instance
# rather than employee.raise_amount

emp1.apply_raise()
emp2.apply_raise()

# now lets create a class variable called number of employees
#the number of employees will increase each time you create an instance
class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
emp3 = employee('rivan','ghosh',7000)    
emp1 = employee('X','Y',2000)
emp2 = employee('A','B',8000)
emp3 = employee('PUTUL','ghosh',7000)    
print(employee.num_empl)


# ---------------------Regular method, class methods and static methods

# regular methods are those in which we pass the self (which translate to the name of
#the instance of the class as the first argument example: fullname and apply_raise methods

# if the method takes class as the first argument instead of the instance as the firs,
# it will be called class method

class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    # first add a decorater to initate a class method
    #also the first argument is cls for class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return amount
    
# now setting the raise aount at a class level
        
employee.set_raise_amt(1.06)    
emp1 = employee('ayon','ghosh',5000)
emp2 = employee('koyel','ghosh',6000)
emp3 = employee('rivan','ghosh',7000)  
employee.raise_amount
emp1.raise_amount
emp2.raise_amount

# you can also use class methods as alternative constructors

#lets say u are constantly getting employee information in the form of a string 
#separated by hi-pens -that u have to parse constantly to create attributes

# =============================================================================
# #example: 
# emp_str_1 = 'John-Doe-7000'
# emp_str_2 = 'ayon-ghosh-6000'
# emp_str_3 = 'koyel-ghosh-8000'
# =============================================================================

emp_str_1 = 'John-Doe-7000'
first,last, pay = emp_str_1.split('-')
new_emp1=employee(first,last, pay)
print(new_emp1.email)
# the above works but they will have to parse the strings everytime they will create a 
#new employee
#so lets create an alternative constructor that will parse the string and create an employee for them
class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    # first add a decorater to initate a class method
    #also the first argument is cls for class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return amount    
    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last, pay)
        
emp_str_2 = 'ayon-ghosh-6000'
emp_str_2  = employee.from_string(emp_str_2)
emp_str_2 .email


# static method unlike class or regular method doesnt take self/ instance or cls 
#as a argument. They behave like regular functions but in someway related to the class

class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    # first add a decorater to initate a class method
    #also the first argument is cls for class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return amount    
    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last, pay)
    # first add a decorater to initate a static method, no instance or cls is passed
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        else: 
            return True
        
import datetime
my_date = datetime.date(2020,10,2) 
print(employee.is_workday(my_date))   

# inheritance allows us to inherit into the sub classes the attributes and methods from the parent classes

class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    # first add a decorater to initate a class method
    #also the first argument is cls for class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return amount    
    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last, pay)
    # first add a decorater to initate a static method, no instance or cls is passed
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        else: 
            return True
        
import datetime
my_date = datetime.date(2020,10,2) 
print(employee.is_workday(my_date))   

# creating subclasses
# simply writing pass statement will inherit all the functionalities from employee class


class developer(employee):
    pass
dev_1 = developer('Corey', 'shafer', 5000)
dev_1.fullname()
dev_1.email

print(help(developer))

print(dev_1.pay)
print(dev_1.apply_raise())
print(dev_1.raised_pay)
 # Now customize the subclasses to override the class variable raise_amt
# of the sub classes the attributes and methods from the parent classes

class employee:
    raise_amount = 1.04
    #initializing # of employees
    num_empl = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        #since each time we create a instance the # of employees increases
        #we will have to keep the counter within the init method
        # we dont write the self.num bcoz every time a self as an instance is created the
        #number of employee increases
        employee.num_empl = employee.num_empl+1
        
# creating the class method here        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        # see here the class variable is called using the classname.class variable
        #self.raised_pay = int(self.pay*employee.raise_amount)
        # or we can do self.instance as below
        self.raised_pay = int(self.pay*self.raise_amount)
        return self.raised_pay
    # first add a decorater to initate a class method
    #also the first argument is cls for class
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        return amount    
    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last, pay)
    # first add a decorater to initate a static method, no instance or cls is passed
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() ==6:
            return False
        else: 
            return True
        
import datetime
my_date = datetime.date(2020,10,2) 
print(employee.is_workday(my_date))   
class developer(employee):
     raise_amount = 1.10
dev_1 = developer('Corey', 'shafer', 5000)     
print(dev_1.apply_raise())
print(dev_1.raised_pay)     

# now adding the developer a programming language

class developer(employee):
     raise_amount = 1.10
     def __init__(self,first,last,pay,prog_lang):
#now inheriting the first,last, and pay from the employee class
#can be done in 2 ways
           super().__init__(first,last,pay)
           
#or
#           employee.__init__(self,first,last,pay)      
           self.prog_lang = prog_lang
           
dev1 = developer('corey','shafer',50000,'python') 
dev2 = developer('Ayon','ghosh',60000,'java') 
dev1.email
dev1.prog_lang          
# create another subclass manager

class manager(employee):
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
                self.employees = []
        else:
                self.employees = employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print('--->',emp.fullname())
            
dev1 = developer('corey','shafer',50000,'python') 
dev2 = developer('Ayon','ghosh',60000,'java')             
mgr_1 = manager('Sue_1','Smith',90000,[dev1,dev2])
print(mgr_1.email)
print(mgr_1.print_emp())
dev3 = developer('joy','basu',3000,'.net')
mgr_1.add_emp(dev3)
mgr_1.print_emp()
        
# isinstance or issubclass
#check if an object is an instance of an class

print(isinstance(mgr_1,manager))
print(isinstance(mgr_1,employee))

print(isinstance(mgr_1,developer))

print(issubclass(developer, employee))
print(issubclass(manager, employee))

# special methods - magic methods




