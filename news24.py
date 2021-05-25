import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from bs4 import BeautifulSoup
import random
import re
import csv
import urllib
import requests


company = 'santam' ## has to taken from user input

driver = webdriver.Chrome(executable_path=r'C:\\Python\\news24\\chromedriver.exe')
driver.get('https://www.news24.com/')
driver.maximize_window()

driver.implicitly_wait(10)

#url = urllib.urlopen('https://www.news24.com/')
#content = url.read()
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
H = driver.execute_script("return document.documentElement.scrollHeight")
#print(H)

#time.sleep(5)
#n = range(0, 14000, 1000)

#driver.execute_script("window.scrollBy(0,'n')")
#time.sleep(10)

inputElement = driver.find_element_by_id("search")
inputElement.send_keys(company)
inputElement.send_keys(Keys.ENTER)

time.sleep(5)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(5)
#driver.execute_script("window.scrollBy(0,1000)")
#time.sleep(10)
#driver.execute_script("window.scrollBy(0,1000)")
#time.sleep(10)
#driver.execute_script("window.scrollBy(0,1000)")
#time.sleep(10)
#driver.execute_script("window.scrollBy(0,1000)")
#time.sleep(10)
#driver.execute_script("window.scrollBy(0,1000)")
#ime.sleep(10)


a_elements = []
matches = [] ## contains the filtered list of companies
t_element = [] ## This is the list with all the title
p_element = []

content_blocks = driver.find_elements_by_class_name("article-list--container")

for block in content_blocks:
    elements = block.find_elements_by_tag_name("a")
    #elements.get_Text()
    for el in elements:
        a_elements.append(el.get_attribute("href"))      

for match in a_elements:
            if company in match:
                matches.append(match)

## This is title scarping part t_element is the list.
#for i in matches:
#    driver.get(i)
#    titleElement = driver.find_element_by_tag_name('h1').text
#    t_element.append(titleElement)
#    driver.implicitly_wait(1)
 #   driver.back


#print (len(matches))
sample = {'title': None, 'article': None}
for j in matches:
    try: 
        driver.get(j)
        titleElement = driver.find_element_by_tag_name('h1').text
        bodyElement = driver.find_element_by_class_name('article__body').get_attribute("textContent")
        sample.update({'title' : titleElement})
        sample.update({'article' : bodyElement})
        #print(titleElement)
        #print('\n')
        #print(bodyElement)
    except:
        print("Needs a Subscriber Account")


print(sample)



## trying with Beautifulsoup

#for i in matches:
#    try:
#        r = requests.get(i).text
#        soup = BeautifulSoup(r,'html5lib')
#
 #       p_tags1 = soup.find_all('p',class_ = "article__body")
        
#
#        for p in p_tags1:
#            print(p.text.strip())

#        print("\n")

#    except:
#        print("Subscriber")