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

inputElement = driver.find_element_by_id("search")
inputElement.send_keys(company)
inputElement.send_keys(Keys.ENTER)

#driver.execute_script("window.scrollBy(0,20000)")
#time.sleep(10)

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

#for i in matches:
#    driver.get(i)
#    titleElement = driver.find_element_by_tag_name('h1').text
 #   t_element.append(titleElement)
 #   driver.implicitly_wait(1)
 #   driver.back
for j in matches:
    driver.get(j)
    page = requests.get('https://www.news24.com/')
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find( class_ ="article__body")
    print(data)
    #p_data = data.find_all
    #data_text = data.strip()
    #p_element.append(data_text)
    

#for j in p_element:
#    print(j)
 #   print('\n')

