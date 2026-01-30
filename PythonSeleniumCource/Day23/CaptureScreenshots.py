import os

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\LENOVO\\PycharmProjects\\PythonProject\\PythonSeleniumCource\\Day23\\screenshot.png")
# driver.save_screenshot(os.getcwd()+"homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"homepage.png")
driver.quit()

# driver.get_screenshot_as_png()
driver.get_screenshot_as_base64()
driver.execute_script("window.scrollTo(20,20)")

