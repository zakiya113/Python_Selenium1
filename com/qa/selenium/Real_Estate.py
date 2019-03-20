from selenium import  webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(10)
driver.get("http://real-estate.itechscripts.com/agent_login.php")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id("login_email").clear()
driver.find_element_by_id("login_email").send_keys("agentdemo@yourmail.com")

driver.find_element_by_id("login_password").clear()
driver.find_element_by_id("login_password").send_keys("userdemo")

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)

#Mouse Hover
element=driver.find_element_by_xpath("//a[contains(text(),'Agent Zone')]")
hover = ActionChains(driver).move_to_element(element)
hover.perform()
time.sleep(1)

#Select from Drop down
driver.find_element_by_xpath("//a[contains(text(),'Post Property Free')]").click()
time.sleep(1)

#Scroll Down
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

#Property info
#Property For
driver.find_element_by_xpath("//*[@id='post_prprty']/div[1]/div/button").click()
time.sleep(1)
# Rent
driver.find_element_by_xpath("html/body/div[2]/div/ul/li[3]/a").click()
time.sleep(1)

#Select Property Type
driver.find_element_by_xpath("//*[@id='property_type_div']/div/button").click()
time.sleep(1)
#Residential House
driver.find_element_by_xpath("html/body/div[3]/div/ul/li[2]/a/span").click()
time.sleep(1)

#Select Country
driver.find_element_by_xpath("//*[@id='post_prprty']/div[3]/div/button").click()
time.sleep(1)
#India
driver.find_element_by_xpath("html/body/div[4]/div/ul/li[2]/a/span").click()
time.sleep(1)

#Select City
driver.find_element_by_xpath("//*[@id='city']").click()
time.sleep(1)
#Mumbai
driver.find_element_by_xpath("//*[@id='city']/option[2]").click()
time.sleep(1)

#Locality
driver.find_element_by_xpath("//*[@id='locality']").send_keys("Worli")
time.sleep(1)

# About
driver.find_element_by_xpath("//*[@id='about']").send_keys("This is a Residential House located in Mumbai")
time.sleep(1)

#Scroll Down
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(1)

#Scroll Down
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.PAGE_DOWN)
time.sleep(1)


#Upload WebElement
driver.find_element_by_id("app_photo").send_keys('C:/Users/minds9/Downloads/r2.jpg')
driver.find_element_by_name("submit").click()



#driver.quit()
