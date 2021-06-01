import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import random
import re
import csv
import urllib
import requests

from tensorflow import keras
import pickle
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences



company = input("Enter company name :" )  ## has to taken from user input


driver = webdriver.Firefox(executable_path=r'C:\Python\geckodriver.exe')
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
time.sleep(10)


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
titleList = []
bodyList = []
for j in matches:
    try: 
        driver.get(j)
        titleElement = driver.find_element_by_tag_name('h1').text
        bodyElement = driver.find_element_by_class_name('article__body').get_attribute("textContent")
        #sample.update({'title' : titleElement})
        #sample.update({'article' : bodyElement})
        titleList.append(titleElement)
        bodyList.append(bodyElement)
        sample = {'title': titleElement, 'article': bodyElement}
        result.append(sample)
        
    except:
        print("Needs a Subscriber Account")

#print(result)

json_file = open(r"C:\Python\Scrapper\Model_ker\Model_ker\model.json",'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights(r"C:\Python\Scrapper\Model_ker\Model_ker\model.h5")
print("Loaded model")

with open(r'C:\Python\Scrapper\tokenizer.pickle' , 'rb') as handle :
        new_tok = pickle.load(handle)
    
classes = ['negative','positive','unclear']
max_features = 5000 # takin the top most occuring 5k words
maxlen = 200  # padding the length of review to 200 tokens

seq_test_1 = new_tok.texts_to_sequences(titleList)
pad_test_1 = pad_sequences(seq_test_1, padding='post', maxlen=maxlen)
y_prob_1 = loaded_model.predict(pad_test_1)

returnArray = []
for n,prediction in enumerate(y_prob_1):
    sent_pred = y_prob_1.argmax(axis=-1)[n]
    print("\n ==============\n")
    print(titleList[n],"\nPrediction: ",classes[sent_pred])
    textAndSentiment = [titleList[n], classes[sent_pred]]
    returnArray.append(textAndSentiment)