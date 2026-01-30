import time

from driver import implicitly_wait
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

righclick = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
time.sleep(2)
actions = ActionChains(driver)
actions.context_click(righclick).perform()
time.sleep(2)






