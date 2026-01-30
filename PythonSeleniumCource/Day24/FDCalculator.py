import time

import excelutils

import ExcelUtils
from selenium import webdriver
from selenium. webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
driver.maximize_window()

file = 'C:/Users/LENOVO/OneDrive/Documents/PythonSelenium/PythonDDT/FixedDepositCal.xlsx'
rows = ExcelUtils.getRowCount(file,"Sheet1")

#Reading data from excel...
for row in range(2, rows+1):
    principle = ExcelUtils.readData(file,"Sheet1", row, 1)
    int_rate = ExcelUtils.readData(file, "Sheet1", row, 2)
    period1 = ExcelUtils.readData(file, "Sheet1", row, 3)
    period2 = ExcelUtils.readData(file, "Sheet1", row, 4)
    frequency = ExcelUtils.readData(file, "Sheet1", row, 5)
    exp_maturity = ExcelUtils.readData(file, "Sheet1", row, 6)

# Passing data to the appplicaion...........
driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(int_rate)
driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)

perioddrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
perioddrp.select_by_visible_text(period2)

frequencydrp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
frequencydrp.select_by_visible_text(frequency)

driver.find_element(By.XPATH, "//img[contains(@src, 'btn_calcutate.gif')]").click()

act_maturity = driver.find_element((By.XPATH,"//span[@id='resp_matval']/strong")).text

#3. Validation...
if float(act_maturity) == float(exp_maturity):
    print("Test pass")
    excelutils.writeData(file, "Sheet1", rows+1, act_maturity,"Pass")


















