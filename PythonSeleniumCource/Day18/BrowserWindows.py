import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

windowid = driver.current_window_handle
print(windowid)     #50CC4D6CCBF11CC2FABDDA17F14A3069..each time it will change dynamically...

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(2)

windowsID = driver.window_handles
# print(windowsID)
#
# parentWindowID=windowsID[0]
# # print("Parent window Id is ...", parentWindowID)
# childwindowID = windowsID[1]
# # print("Child window Id is ...", childwindowID)
#
# driver.switch_to.window(childwindowID)
# print("Title of the child window is...", driver.title)    #Human Resources Management Software | HRMS | OrangeHRM
# time.sleep(5)
#
# driver.switch_to.window(parentWindowID)
# print("Title of the parent window is...", driver.title)

#Handling multilpe browser windows....
# for window in windowsID:
#     driver.switch_to.window(window)
#     print("Title of the window is...", driver.title)

#Select and close specific brwer window....
time.sleep(2)
for window in windowsID:
    driver.switch_to.window(window)
    if driver.title == "Human Resources Management Software | HRMS | OrangeHRM":
        driver.close()




