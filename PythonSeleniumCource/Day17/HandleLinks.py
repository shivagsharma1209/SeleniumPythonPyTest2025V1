import time

from driver import find_element
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
# time.sleep(5)

# Find number of links on webpage
# links=driver.find_elements(By.TAG_NAME,'a')
links=driver.find_elements(By.XPATH,'//a')
print("Total number of lnks...", len(links))
for link in links:
    print(link.get_attribute("href"))
    print(link.text)


