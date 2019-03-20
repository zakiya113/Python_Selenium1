from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")

#driver = webdriver.Firefox("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\geckodriver.exe")

driver.get("https://classic.crmpro.com/login.cfm")

title = driver.title

print(title)

# assert "CRMPRO Log In Screen" in title

driver.find_element_by_name("username").send_keys("zakiya")
driver.find_element_by_name("password").send_keys("Minds123")

driver.quit()
