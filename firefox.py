# Open google.com
# search campusx
# learnwith.campusx.in
# dsmp course page

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service('geckodriver.exe')

webdriver.Firefox(service=s)

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
