import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("12/01/2025")

year = "2026"
month = "March"
day = "20"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mo = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    ye =  driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mo == month and ye==year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").click()

#Date selection...
dates = driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody/tr/td/a")
for date in dates:
    if date.text == date:
        date.click()
        time.sleep(2)
        break

driver.close()



