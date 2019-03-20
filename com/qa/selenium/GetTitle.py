from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")

driver.get('http://www.theTestingWorld.com/testings')

driver.maximize_window()
#Fetching Title
print("Title of Page is " + driver.title)

#Fetch URL of Page
print("Page URL is " + driver.current_url)

#Fetch Complete Page HTML
print("******************************************************************************************")
print(driver.page_source)

