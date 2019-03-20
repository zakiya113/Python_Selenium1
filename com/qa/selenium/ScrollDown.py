from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
browser.get('http://wikipedia.org')
time.sleep(5)

elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(7)
elm.send_keys(Keys.HOME)
