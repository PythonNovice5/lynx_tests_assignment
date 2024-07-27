from pages.basePage import BasePage
from settings import LYNX_WEB_URL


class SetUp(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, get_url_value):
        self.driver.delete_all_cookies()
        url = LYNX_WEB_URL + get_url_value['registrationURL']
        self.logger.info(f"-------- Going to the URL: {url} -------------")
        self.driver.get(url)
