import time
import os
from selenium import webdriver

chromedriver = "C:/Users/minds9/PycharmProjects/Python_Selenium/drivers/chromedriver.exe"
os.environ["webdriver.chrome.driver"]=chromedriver
driver= webdriver.Chrome(chromedriver)


driver.get("http://the-internet.herokuapp.com/upload")


driver.find_element_by_id("file-upload").send_keys('C:/Users/minds9/Downloads/r2.jpg')
driver.find_element_by_id("file-submit").click()

time.sleep(3)

