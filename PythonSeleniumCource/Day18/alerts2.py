import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
alert = driver.switch_to.alert
time.sleep(5)
alert.accept()
time.sleep(5)




