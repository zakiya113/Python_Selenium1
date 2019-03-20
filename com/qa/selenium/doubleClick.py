from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.get('https://www.google.com/intl/en-GB/gmail/about/#')

element=driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[5]/ul[1]/li[3]/a[1]').click()

driver.implicitly_wait(30)

action_chains = ActionChains(driver)
action_chains.double_click(element).perform()
