from pages.basepage import BasePage
from settings import WEB_URL


class SetUp(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, get_url_value, default=None):
        self.driver.delete_all_cookies()
        if default == None:
            url = WEB_URL + get_url_value["example_url"]
        else:
            url = WEB_URL + get_url_value[default]
        self.logger.info(f"-------- Going to the URL: {url} -------------")
        self.driver.get(url)
