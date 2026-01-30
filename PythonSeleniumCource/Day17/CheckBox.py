import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1...To find and select a single check box
# driver.find_element(By.XPATH, "//input[@id='sunday']").click()

#2. To select multiple checkboxes on a webpage

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains (@id,'day')]")
print(len(checkboxes))

#Selection of all check boxes...
# for checkbox in range (len(checkboxes)):
#     checkboxes[checkbox].click()
#     time.sleep(5)

# for checkbox in checkboxes:
#     checkbox.click()

#3. Select multiple checboxes by choice..............
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "sunday" or weekname == "saturday":
#         checkbox.click()
#         time.sleep(5)

#4. Select last two checkboxes....number elements - 2 = starting index
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
#     time.sleep(5)

#5. To select first two checkboxes....

# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()
#         time.sleep(5)
#6. To clearing all check boxes at once...

for checkbox in checkboxes:
    checkbox.click()
    time.sleep(5)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()







