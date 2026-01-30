import time
import excelutils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
driver.maximize_window()

try:
    cont = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='', database='python')
    cursor = cont.cursor()
    cursor.execute('select * from caldata')
    results = cursor.fetchall()

    # Reading data from excel...

    for row in results:
        principle = row[0]
        int_rate = row[1]
        period1 =  row[2]
        period2 = row[3]
        frequency = row[4]
        exp_maturity = row[5]

    # Passing data to the appplicaion...........
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(int_rate)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)

    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(period2)

    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(frequency)

    driver.find_element(By.XPATH, "//img[contains(@src, 'btn_calcutate.gif')]").click()

    act_maturity = driver.find_element((By.XPATH, "//span[@id='resp_matval']/strong")).text

    # 3. Validation...
    if float(exp_maturity) == float(act_maturity):
        print("Test pass")
    else:
        print("Test fail")
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    time.sleep(5)

except:
    print("Connection unsuccessful")

driver.close()
