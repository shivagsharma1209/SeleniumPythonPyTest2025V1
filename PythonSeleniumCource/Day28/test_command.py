from selenium import webdriver


class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("admin@yourstore.com","admin"),
                              ("admin1@yourstore.com","admin1"),
                              ("admin2@yourstore.com","admin2")
                              ]
                             )
    def test_login(self,user,pwd):
        self.driver =webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.find_element_by_name("txtUsername").send_keys(user)
        driver.find_element_by_id("txtPassword").send_keys(pwd)
        driver.find_element_by_id("btnLogin").click()

        try:
            self.status=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True

        except:
            self.driver.close()
            assert self.status==False
