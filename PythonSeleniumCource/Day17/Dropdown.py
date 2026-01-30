from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# drp_country=driver.find_elements(By.XPATH, "//select[@id='country']")
dcountry=Select(driver.find_element(By.XPATH, "//select[@id='country']"))

#Select options from dropdown
# dcountry.select_by_value("japan")
# dcountry.select_by_visible_text("japan")

#Capture all options and print
alloptions=dcountry.options
print("Total number of options..",len(alloptions))

for option in alloptions:
    print(option.text)

#Select specific option from dropdown

for option in alloptions:
    if option.text == "Canada":
        option.click()
        break


