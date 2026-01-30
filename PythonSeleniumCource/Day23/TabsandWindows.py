import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab') #opens a new webpage in the same broweser windows..
# driver.get("https://www.orangehrm.com/")

driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window') #opens a new window switches to new broweser windows..
driver.get("https://www.orangehrm.com/")
driver.quit()