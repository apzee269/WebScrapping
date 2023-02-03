from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://in.indeed.com/?r=us')
time.sleep(2)

user_input = driver.find_element(by = By.XPATH, value = '//*[@id="text-input-what"]').send_keys(['Data Scientist',Keys.ENTER])


html = driver.page_source

with open('indeed.html','w',encoding = 'utf-8') as f:
    f.write(html)

#creating data frame
with open('indeed.html','r',encoding = 'utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html,'lxml')
containers = soup.find_all('div',{'class':'slider_container css-g7s71f eu4oa1w0'})

for i in containers:
    location.append(i.find('div',{'class':'companyLocation'}).text)
    company.append(i.find('span',{'class':'companyName'}).text)
    job.append(i.find('h2').text)

df = pd.DataFrame({
    'Role':job,
    'Company':company,
    'Location':location
})

driver.find_element(by = By.XPATH, value='//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]/a').click()
time.sleep(20)


