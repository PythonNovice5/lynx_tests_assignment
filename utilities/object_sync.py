# wait_conditions.py


from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging

LOGGER = logging.getLogger(__name__)


class ObjectSync:
    # def __init__(self, driver, default_timeout=10):
    #     self.driver = driver
    # logger = configure_logger()
    default_timeout = 10
    logger = LOGGER

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException as e:
            self.logger.exception(
                f"Timed out waiting for element to be clickable: {locator}"
            )
            raise e

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except WebDriverException as e:
            self.logger.exception(
                f"Timed out waiting for element to be visible: {locator}"
            )
            raise e

    def wait_for_element_to_be_invisible(self, locator, timeout=None):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except WebDriverException as e:
            self.logger.exception(
                f"Timed out waiting for element to be invisible: {locator}"
            )
            raise e

    def click_web_element(self, locator, timeout=10):
        try:
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            # self.scrollToElement(locator)
            element.click()
        except (
            TimeoutException,
            ElementClickInterceptedException,
            NoSuchElementException,
        ) as e:
            self.logger.exception(f"Error clicking element: {locator}")
            raise e

    def enter_value_into_element(self, locator, keys, attr=None, timeout=10):
        try:
            element = self.wait_for_element_to_be_visible(locator, timeout)
            element.clear()
            element.send_keys(keys)
            self.logger.info(f"Entered {attr} as: {keys}")
        except WebDriverException as e:
            self.logger.exception(f"Error sending keys to element: {locator}")
            raise e

    def get_text_of_element(self, locator, timeout=5) -> str:
        try:
            element = self.wait_for_element_to_be_visible(locator, timeout)
            return element.text
        except WebDriverException as e:
            self.logger.exception(f"Error getting text of element: {locator}")
            raise e

    def wait_and_find_element(self, locator, timeout=10) -> WebElement:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except WebDriverException as e:
            self.logger.exception(f"Timed out waiting for element presence: {locator}")
            raise e

    def wait_and_find_elements(self, locator, timeout=10) -> WebElement:
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except WebDriverException as e:
            self.logger.exception(f"Timed out waiting for element presence: {locator}")
            raise e

    def scrollToElement(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 5, 5).perform()
