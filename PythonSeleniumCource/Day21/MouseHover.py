import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://naveenautomationlabs.com/opencart/")
driver.maximize_window()

desktop = driver.find_element(By.XPATH, "//a[normalize-space()='Desktops']")
pc = driver.find_element(By.XPATH, "//a[normalize-space()='PC (0)']")
mac= driver.find_element(By.XPATH, "//a[normalize-space()='Mac (1)']")

#Mouse hover actions on individual elements......................
# actions = ActionChains(driver)
# actions.move_to_element(desktop).perform()
# time.sleep(2)
# actions.move_to_element(pc).perform()
# time.sleep(2)
# actions.move_to_element(mac).perform()
# time.sleep(2)

#We can do the same using below single statement
actions = ActionChains(driver)
actions.move_to_element(desktop).move_to_element(pc).move_to_element(mac).perform()
time.sleep(2)





