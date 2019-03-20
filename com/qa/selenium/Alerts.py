from selenium import webdriver

import time
driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
#driver = webdriver.Chrome()
driver.get("http://demo.guru99.com/test/delete_customer.php")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_name("cusid").send_keys("53920")
driver.find_element_by_name("submit").click()


#driver.execute_script("window.alert('This is alert');")
#time.sleep(5)

alert = driver.switch_to.alert()
alert.dismiss()