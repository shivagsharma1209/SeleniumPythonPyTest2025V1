import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
webdriverwait = WebDriverWait(driver, 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                                    ElementNotVisibleException,
                                                                    ElementNotSelectableException])

# driver.get("https://www.google.com")
driver.get("https://www.google.com/search?q=python+selenium+tutorial&safe=active")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()

# time.sleep(5)

searchlink = webdriverwait.until(EC.presence_of_element_located((By.XPATH,"//h3[@id='_Hps3acDZFtic4-EPraPX2Qo_122']")))
searchlink.click()

# driver.find_element(By.XPATH,"//a[normalize-space()='Downloads']").click()
driver.quit()










