from selenium import  webdriver

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element_by_id("u_0_j").send_keys("Anam")
driver.find_element_by_name("lastname").send_keys("Khan")
driver.find_element_by_id("u_0_o").send_keys("anam123khan@gmail.com")
driver.find_element_by_id("u_0_r").send_keys("anam123khan@gmail.com")
driver.find_element_by_id("u_0_v").send_keys("123anam")
driver.find_element_by_id("day").send_keys("14")

#driver.find_element_by_id("day/option[13]").click()

driver.find_element_by_id("month").send_keys("April")
driver.find_element_by_id("year").send_keys("1994")
driver.find_element_by_id("u_0_9").click()
driver.find_element_by_id("u_0_11").click()




#driver.quit()
