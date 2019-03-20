from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
browser.get('http://google.com')
time.sleep(5)

elem = browser.find_element_by_link_text('About')
time.sleep(5)
elem.click()
time.sleep(3)
browser.back()