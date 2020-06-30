# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:34:24 2020

@author: 140524
"""
#https://medium.com/@raiyanquaium/how-to-web-scrape-using-beautiful-soup-in-python-without-running-into-http-error-403-554875e5abed
from urllib.request import Request,urlopen
my_address = "https://realpython.com/practice/poseidon.html"
req = Request(my_address , headers={'User-Agent': 'Chrome/75.0'})
html_page = urlopen(req).read().decode('utf-8')
print(html_page)

# printing only the title

start_tag = '<title>'
end_tag = '</title>'
start_index = html_page.find(start_tag) + len(start_tag)
print(start_index)
end_index = html_page.find(end_tag)
print(html_page[start_index: end_index])

# Using beautiful soup
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
url = 'https://www.fool.ca/recent-headlines/'
req = Request(url , headers={'User-Agent': 'Chrome/75.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
print(page_soup.prettify())
print(page_soup.get_text().replace('\n ','\n'))


# printing only the titleusing beautiful soup

page_soup = soup(webpage, "html.parser")
title = page_soup.find("title")
print(title)


container = page_soup.findAll("p","promo")
for i in container:
       print(i)
       
       
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
url = 'https://realpython.com/practice/dionysus.html'
req = Request(url , headers={'User-Agent': 'Chrome/75.0'})
req
webpage = urlopen(req).read()
webpage
page_soup = soup(webpage, "html.parser")
print(page_soup.get_text())
print(page_soup.prettify())
page_soup = soup(webpage, "html.parser")
name = page_soup.find("h2")
print(name)

# or

from urllib.request import Request,urlopen
my_address = "https://realpython.com/practice/dionysus.html"
req = Request(my_address , headers={'User-Agent': 'Chrome/75.0'})
html_page = urlopen(req).read().decode('utf-8')
print(html_page)
start_tag = '<h2>'
end_tag = '</h2>'
print(html_page.find(start_tag))
start_index = html_page.find(start_tag) + len(start_tag) + len('Name: ')
end_index = html_page.find(end_tag)
print(html_page[start_index:end_index])       


from urllib.request import Request,urlopen
my_address = "https://realpython.com/practice/dionysus.html"
req = Request(my_address , headers={'User-Agent': 'Chrome/75.0'})
html_page = urlopen(req).read().decode('utf-8')
print(html_page)

Tag = ['Name:','Favorite Color:']
for tag in Tag:
    start_index = html_page.find(tag) + len(tag) 
    end_index = html_page[start_index:].find('<')
    print(html_page[start_index:start_index+end_index])  

import re
Tag = ["Name:.*?[\n<]","Favorite Color:.*?[\n<]"]    
for tag in Tag:
    match_results = re.search(tag, html_page)     
    #result = re.sub(".*: ", "", match_results.group())
    print(match_results.group().strip('\n<'))
    
import re
Tag = ["Name:.*?[\n<]","Favorite Color:.*?[\n<]"]    
for tag in Tag:
    match_results = re.search(tag, html_page)     
    result = re.sub(".*: ", "", match_results.group())
    print(match_results.group().strip('\n<'))    
    
#1    
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
url = 'http://olympus.realpython.org/profiles'
req = Request(url , headers={'User-Agent': 'Chrome/75.0'})

webpage = urlopen(req).read()
page_soup = soup(webpage, "html.parser")
print(page_soup.get_text())
print(page_soup.prettify())


2#
for link in page_soup.find_all('a'):
        #print(link)
        link_address = url + link["href"]
        link_page = urlopen(link_address).read()
        page_soup = soup(link_page, "html.parser")
        print(page_soup.get_text())
        
       
for anchor in page_soup.find_all("a"):
    # Could also have used urlparse.urljoin() to get absolute URL
    
    print(f"--- Fetching {link_address}:")       
    
