import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    """ Login page elements """
    email_box = (By.ID, "email")
    password_box = (By.ID, "password")
    login_button = (By.ID, "loginButton")
    login_error_msg = (By.CSS_SELECTOR, ".error")

    def login_to_the_app(self, email, password):
        self.enter_value_into_element(self.email_box, email, "email")
        self.enter_value_into_element(self.password_box, password, "password")
        self.click_web_element(self.login_button)
        self.logger.info("Clicked on Login button")

    def verify_login_errormsg(self):
        self.wait_and_find_element(self.login_error_msg)
        self.logger.info(
            "warning message:" + self.get_text_of_element(self.login_error_msg)
        )
        text = self.get_text_of_element(self.login_error_msg)
        assert (
            self.get_text_of_element(self.login_error_msg)
            == "Invalid email or password."
        )
        self.logger.info("Verified the login error message successfully..")
        return True

    def verify_login(self, credtype):
        if credtype == "invalid_creds":
            self.verify_login_errormsg()
            return True
        if credtype == "sql_injection_creds":
            self.verify_login_errormsg()
            return True
        elif credtype == "valid_creds":
            time.sleep(2)
            self.verifyPageURL("search")
            self.logger.info(
                "user is able to login into the application successfully with valid credentials"
            )
            return True
        return False
