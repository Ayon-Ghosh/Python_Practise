# -*- coding: utf-8 -*-
"""
Created on Sun May 12 09:42:16 2019

@author: 140524
"""
#---regular expressions - strgs--amuls 74,75,76,77
#--matching patterns in text

# ^ - matches the beginning of the line--^python
# $- matches the end of the line - .com$
# . matches the single char (a-z) or (1-10) or (special chars), anything except new line
# [] - matches any single char within the range [1-9] 
# [^1-9]=matches a single char not within this range that is 1 or 2,3,4,5,6,7,8,9
# * for exzmple'x*'= matches 0 or more occureances of x
#'+' matches 1 or more occuramces of precending exp '+x'=
#'x?;= indicates 0 or 1 occurances of X
# x{2} indictes 2 occrance of X or x{5} - 5 occrance of x 
#or 'x{5,}' matches atleast 5 occrance of x
#x{5,8} matches 5 to 8 occrances of x
#a|b matches either a or b
#() indicates group - helpes to grp the regular exp
#\s matches the space
#\S matches the non space
#\d matches the single digit
#\D matches the single non digit
#\w matches a single word char such as [1-9] or [a-z] or _
#r indicates raw string


# Match
#match(pattern, string,flag=0 are optional)

import re
line = "pet:cat I love cat, pet:dog, also pet:animal"
a = re.match(r"pet:\w\w\w",line)
a
a.group(0)
a.group(1)

# search
#search(pattern, string,flag=0 are optional)
line = "I love cat, pet:dog also pet:animal"
a = re.search(r"pet:\w\w\w",line)
a
a.group(0)
a.group(1)

# match will search only at the begining of the string but search will search 
#the entire string and returns the first match of that pattern

line = "i love cats pet:cats"
b = re.match(r"pet:\w\w\w",line)
b

# no output - nothing return from above

line = "i love oet:cats and cats pet:dog"
c = re.search(r"pet:\w\w\w",line)
c.group(0)

#or..\w\w\w -- replacing with |w+

line = "i love oet:cats and cats pet:dog"
c = re.search(r"pet:\w+",line)
c.group(0)

line = "i love cats pet:cows i love cats pet:cats"
d = re.search(r"pet:\w\w\w",line)
d 

#Concept of Group:
#https://stackoverflow.com/questions/36728729/python-group0-meaning 
    
m = re.search('(?<=abc)(d(e))f','abcdef')
m.group(0)
m.group(1)
m.group(2)
# finadall searchss and matches all occurances of a pattern
#findall(pattern, string,flag=0 are optional)

line = "i love cats pet:cows i love cats pet:cats"
e = re.findall(r"pet:\w\w\w",line)
e

# Replace - one or more word in a string
import re
line = "ayon@xyz.com and koyel@pqr.com"
var = re.sub(r"@\w+","@gmail",line)
var

# encode and decode -- tutorial point

#https://www.youtube.com/watch?v=pv1q0XhuYsM
# encode function encodes a ASCII string to a binary format so its not readable
# decode function decodes it back
import base64
str1 = "ayonghosh"
str2 = base64.b64encode(str1.encode('utf-8'))
str2

str3 = base64.b64decode(str2.decode('utf-8'))
str3




#split(pattern, string,flag=0 are optional)
import re
line = "i love cats pet:cows i love cats pet:cats"
f = re.split(r"pet:\w\w", line)
f


##A website requires the users to input username and password to register. 
#Write a program to check the validity of password input by users.

#Following are the criteria for checking the password:

#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will 
#check them according to the above criteria. Passwords that match the 
#criteria are to be printed, each separated by a comma.

import re

pattern = '^.

import re
pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
password = input("Enter string to test: ")
result = re.findall(pattern, password)
if (result):
    print("valid password:",password.split(','))
else:
    print ("Password not valid" )     
# string format function

#https://www.geeksforgeeks.org/python-format-function/
#https://stackoverflow.com/questions/8234445/python-format-output-string-right-alignment
#https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3