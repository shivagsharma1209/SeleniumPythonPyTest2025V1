from numpy.ma.extras import column_stack
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1. Count number of rows and columns in a webtable..........
# rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
# print("total rowns in a web table =", len(rows))
# coulmns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
# print("total cloumns in a web table =", len(coulmns))

#2. Read specific row and column
# print(driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text)
# print(driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[7]/td[3]").text)

#3. Read all rows and columns from a web table....................
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
for row in range(2,len(rows)+1):
    for coulmn in range(1,len(columns)+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/body/tr[" + str(row) + "]/td[" + str(coulmn) + "]").text
        print(data)

#read based on conditions...
# rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
# columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
#
# for r in range(2, len(rows)+1):
#     author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(rows) + "]/td[2]").text
#     if author == "Mukesh":
#         bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(rows) + "]/td[1]").text
#         print(bookname)








