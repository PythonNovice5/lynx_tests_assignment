import pytest

from utilities.logger_config import configure_logger
from utilities.object_sync import ObjectSync

@pytest.mark.usefixtures("setup")
class BasePage(ObjectSync):
    # def __init__(self, driver):
    #     self.driver = driver
    # logger = configure_logger()

    def verifyPageURL(self,url):
        assert url in self.driver.current_url
        self.logger.info(f"Verified the URL successfully, the user is on the expected page: {self.driver.current_url}")
        return True
