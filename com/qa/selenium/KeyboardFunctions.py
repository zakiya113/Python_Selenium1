from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
#act.send_keys(Keys.CONTROL).send_keys("a").perform()
#act.send_keys(Keys.SPACE).perform()
act.send_keys(Keys.BACKSPACE).perform()



