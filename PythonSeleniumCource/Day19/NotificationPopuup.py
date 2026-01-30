import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("useAutomationExtension", False)

options.add_argument("--disable notification")


driver = webdriver.Chrome()
driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='My Location Now']").click()


