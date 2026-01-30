import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#Find the year..
driver.find_element(By.XPATH, "//input[@id='dob']").click()

month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Jun")

year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("1979")


date = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
time.sleep(2)

for date in date:
    if date.text == "12":
        date.click()
        break
time.sleep(2)

driver.close()


