import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basepage import BasePage


class LoggedinPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    """ Loggedin page elements """
    account_link = (By.ID, "navbarAccount")
    logout_link = (By.ID, "navbarLogoutButton")

    def logout(self):
        self.click_web_element(self.account_link)
        self.click_web_element(self.logout_link)
        self.logger.info("Logged out of the application successfully!")
