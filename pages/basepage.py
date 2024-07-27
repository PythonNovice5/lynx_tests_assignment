import pytest
from utilities.object_sync import ObjectSync
from utilities.utils import *


@pytest.mark.usefixtures("setup")
class BasePage(ObjectSync):
    # def __init__(self, driver):
    #     self.driver = driver
    # logger = configure_logger()

    def verifyPageURL(self, url):
        self.logger.info(
            f"Verifying url: {url} in current page  {self.driver.current_url}"
        )
        assert url in self.driver.current_url
        self.logger.info(
            f"Verified the URL successfully, the user is on the expected page: {self.driver.current_url}"
        )
        return True

    def get_test_data(self, test_data_file):
        test_data = read_data_from_json(test_data_file + ".json")
        return test_data

    # def verify_languages(self,language_data):
