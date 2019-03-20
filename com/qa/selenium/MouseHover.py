from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("http://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(30)

element=driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
hover = ActionChains(driver).move_to_element(element)
hover.perform()
driver.implicitly_wait(40)
driver.quit()
