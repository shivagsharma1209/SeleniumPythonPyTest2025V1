import pytest
from selenium.webdriver.chrome import webdriver


class TestLogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         


    def test_login_edge(self):
        pass

    def test_login_firefox(self):
        pass

