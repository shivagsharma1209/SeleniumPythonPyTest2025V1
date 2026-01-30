import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver.get("https://www.foundit.in/seeker/dashboard")
driver.maximize_window()
driver.implicitly_wait(10)


upload_element = driver.find_element(By.XPATH, "//input[@type='file']")
upload_element.send_keys("C:\\Users\\Admin\\Documents\\testfile.txt")


