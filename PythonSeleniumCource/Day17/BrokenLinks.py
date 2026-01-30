import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# brokenlinks = driver.find_elements(By.TAG_NAME, "a")
brokenlinks = driver.find_elements(By.XPATH, "//a[@href]")
count = 0
for link in brokenlinks:
    url=link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        pass
    res = requests.head(url)
    if res.status_code >= 400:
        print(url, "   Link is broken")
    count += 1
else:
    print("Total number of broken links..", "   Link is valid")









