from selenium import  webdriver


driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.implicitly_wait(20)
