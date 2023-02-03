from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

job = []
location = []
company = []

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://in.indeed.com/?r=us')
time.sleep(2)

user_input = driver.find_element(by = By.XPATH, value = '//*[@id="text-input-what"]').send_keys(['Data Scientist',Keys.ENTER])
time.sleep(2)
k = 0
for i in range(0,20):
    try:
        driver.find_element(by=By.XPATH, value = '//*[@id="mosaic-modal-mosaic-provider-desktopserp-jobalert-popup"]/div/div/div[1]/div/button').click()
    except:
        pass
    if k != 0:
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[7]').click()
        except:
            driver.find_element(by=By.XPATH,
                            value='//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[6]').click()

    print('loaded page: ',k)
    k += 1

    get_url = driver.current_url
    time.sleep(2)
    html = driver.page_source

    with open('indeed.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # creating data frame
    with open('indeed.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'lxml')
    containers = soup.find_all('div', {'class': 'slider_container css-g7s71f eu4oa1w0'})

    for j in containers:
        location.append(j.find('div', {'class': 'companyLocation'}).text)
        company.append(j.find('span', {'class': 'companyName'}).text)
        job.append(j.find('h2').text)

    time.sleep(2)

df = pd.DataFrame({
        'Role': job,
        'Company': company,
        'Location': location
    })

df.to_csv('Indeed.csv', index=False)