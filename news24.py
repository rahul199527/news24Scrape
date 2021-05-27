def news24():
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


    company = input("Enter company name :" )  ## has to taken from user input

    driver = webdriver.Chrome(executable_path=r'C:\\Python\\news24\\chromedriver.exe')
    driver.get('https://www.news24.com/')
    driver.maximize_window()

    driver.implicitly_wait(10)

    ## passing name of the company to search

    inputElement = driver.find_element_by_id("search")
    inputElement.send_keys(company)
    inputElement.send_keys(Keys.ENTER)


    ## basic scroll needs to be improved
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(5)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,1000)")
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,1000)")
    ime.sleep(10)


    a_elements = [] 
    ## contains the filtered list of companies
    matches = [] 
    ## This is the list with all the title
    t_element = [] 
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


    ## number of articles collected
    print (len(matches))


    ## scraping title and body of article, storing to a list of dictionaries
    sample = {'title': [], 'article': []}
    result = []
    for j in matches:
        try: 
            driver.get(j)
            titleElement = driver.find_element_by_tag_name('h1').text
            bodyElement = driver.find_element_by_class_name('article__body').get_attribute("textContent")
            #sample.update({'title' : titleElement})
            #sample.update({'article' : bodyElement})
            sample = {'title': titleElement, 'article': bodyElement}
            result.append(sample)
            
        except:
            print("Needs a Subscriber Account")

    #print(result)

if __name__ == "__main__":
    news24()
