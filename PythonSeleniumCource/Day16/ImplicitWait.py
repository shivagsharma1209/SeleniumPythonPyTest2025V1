import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com")

driver.maximize_window()

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

time.sleep(5)

driver.find_element(By.XPATH,"//h3[@id='_Hps3acDZFtic4-EPraPX2Qo_122']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Downloads']").click()








