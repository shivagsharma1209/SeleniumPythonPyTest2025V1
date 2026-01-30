import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#1. JS Alert take action by clicling k with action using the method = accept()..............
# driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Click for JS Alert')]").click()
# time.sleep(5)
# alertpopup1 = driver.switch_to.alert
# alertpopup1.accept()
# time.sleep(5)

#2. Alert type = Take action either click ok or click cancel to proceed further.......accept(0/dismiss().......
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']").click()
# time.sleep(5)
alertpopup2 = driver.switch_to.alert
# alertpopup2.accept()
# time.sleep(5)
alertpopup2.dismiss()
# time.sleep(5)

#3. This statement will open the popuup wndow on the webpage.........
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(5)
#
# alertpopup = driver.switch_to.alert
# # print(alertpopup.text)
# # #Passing test to the alert popu up window.............
# # alertpopup.send_keys("Accepting the alert.....")
# # time.sleep(5)
# # #Accepting the alert using the accept()....................
# # alertpopup.accept()
# # time.sleep(5)
#
# #Cancelling the alert usig the dismiss()..............
# print(alertpopup.text)
# alertpopup.send_keys("Cancelling the alert.....")
# alertpopup.dismiss()
# time.sleep(5)




