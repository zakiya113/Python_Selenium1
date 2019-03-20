from selenium import  webdriver

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file(".\\Screenshots\Facebook.png")
driver.find_element_by_id("email").send_keys("Selenium Webdriver")
driver.find_element_by_name("pass").send_keys("Python")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file(".\\Screenshots\\Facebook1.png")
driver.quit()
