import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/devtools/package-summary.html")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//a[normalize-space()='org.openqa.selenium']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Index']").click()
time.sleep(5)

