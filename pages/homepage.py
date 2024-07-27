import time

import requests

from utilities.utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    welcome_dialog_box = (By.ID, "mat-dialog-0")
    dismiss_welcome_diaog = (By.XPATH, "//button[contains(@class,'close')]")
    cookie_dialog_box = (By.XPATH, "//div[@aria-label='cookieconsent']")
    cookie_dismiss = (By.CSS_SELECTOR, "a.cc-dismiss")
    cookie_adjust = (By.ID, "CybotCookiebotDialogBodyLevelButtonCustomize")
    cookie_decline = (By.ID, "CybotCookiebotDialogBodyButtonDecline")

    account_link = (By.ID, "navbarAccount")
    login_link = (By.ID, "navbarLoginButton")
    next_button = (By.CSS_SELECTOR, "button.mat-paginator-navigation-next")
    list_of_items = (By.CSS_SELECTOR, "mat-grid-tile .item-name")
    items_per_page_dropdown = (By.ID, "mat-select-0")

    language_selection = (By.XPATH, "//button[@aria-label='Language selection menu']")
    open_side_menu = (By.XPATH, "//button[@aria-label='Open Sidenav']")
    about_us = (By.XPATH, "//a[(contains(@href,'about'))]")
    legal = (By.XPATH, "//a[(contains(@href,'legal'))]")
    customer_feedback = (By.XPATH, "//a[(contains(@href,'contact'))]")
    photo_wall = (By.XPATH, "//a[(contains(@href,'photo-wall'))]")
    help_getting_started = (
        By.XPATH,
        "//a[(contains(@aria-label,'Launch beginners tutorial'))]",
    )
    side_menu_headers = (
        By.XPATH,
        "//*[contains(@class,'mat-divider-horizontal')]/following-sibling::h3",
    )
    side_menu_links = (
        By.XPATH,
        "//i/following-sibling::span[contains(@class,'menu-text')]",
    )

    def navigate_to_login_page(self):
        self.click_web_element(self.account_link)
        self.click_web_element(self.login_link)

    def handle_welcome_page_popup(self):
        # self.wait_for_element_to_be_visible(self.welcome_dialog_box)
        time.sleep(2)
        try:
            if self.wait_for_element_to_be_visible(self.welcome_dialog_box, timeout=1):
                self.click_web_element(self.dismiss_welcome_diaog)
                self.logger.info("Clicked on Dismiss")
                self.wait_for_element_to_be_invisible(self.welcome_dialog_box, 1)
                self.logger.info("Welcome popup handled")
            else:
                self.logger.info("Welcome pop up not present")
        except Exception as e:
            self.logger.exception(
                "Exception occurred while handling welcome popup: %s", str(e)
            )

    def handle_cookies(self):
        try:
            if self.wait_for_element_to_be_visible(self.cookie_dialog_box, timeout=1):
                self.click_web_element(self.cookie_dismiss)
                self.logger.info("Clicked on Dismiss")
                self.wait_for_element_to_be_invisible(self.cookie_dialog_box, 1)
                self.logger.info("Cookie got accepted successfully!!")
            else:
                self.logger.info("Cookie dialog box not present")
        except Exception as e:
            self.logger.exception(
                "Exception occurred while handling Cookie dialog box: %s", str(e)
            )

    def go_to_next_page(self):
        self.scrollToElement(self.wait_and_find_element(self.next_button))
        self.click_web_element(self.next_button)
        self.logger.info("Clicked on Next button to go next page")

    def get_list_of_items(self):
        list_of_items = self.wait_and_find_elements(self.list_of_items, 10)
        items_on_page = [item.text for item in list_of_items]
        return items_on_page

    def select_items_per_page(self, items_per_page):
        self.click_web_element(self.items_per_page_dropdown)
        items_per_page = self.driver.find_element(
            By.XPATH, f"//mat-option/span[text()={items_per_page}]"
        )
        self.click_web_element(items_per_page)

    def select_language_webpage(self, language_input):
        self.click_web_element(self.language_selection)
        elem = self.driver.find_element(
            By.XPATH,
            f"//mat-radio-button/label//input[@aria-label='{language_input}']//..//..//..",
        )

        elem.click()
        self.click_web_element(self.open_side_menu)

    def verify_languages(self, language_data):
        time.sleep(2)
        side_menu_headers = self.wait_and_find_elements(self.side_menu_headers, 10)
        side_menu_headers_text = [h.text for h in side_menu_headers]
        side_menu_links_text = [
            link.text for link in self.wait_and_find_elements(self.side_menu_links, 10)
        ]
        expected_side_menu_headers_text = language_data["Side menu Headers"]
        expected_side_menu_items_text = language_data["Side menu items"]
        self.logger.info(
            f"Expected side menu items: {expected_side_menu_items_text} Actual side menu items: {side_menu_links_text}"
        )
        self.logger.info(
            f"Expected side menu headers: {expected_side_menu_headers_text} Actual side menu headers: {side_menu_headers_text}"
        )
        assert set(side_menu_headers_text) == set(expected_side_menu_headers_text)
        assert set(side_menu_links_text) == set(expected_side_menu_items_text)
        self.driver.refresh()
        return True

    def get_ftp_url(self):
        self.click_web_element(self.open_side_menu)
        self.logger.info("Opened the Side menu on Home page")
        self.click_web_element(self.about_us)
        self.logger.info("Clicked on About us link")
        self.click_web_element(self.legal)
        self.logger.info("On About us page clicked on legal terms link")
        ftp_url = self.driver.current_url.split("legal")[0]
        return ftp_url

    def get_response(self, url, suburl=None):
        if suburl != None:
            url = url + suburl
        else:
            url = url
        response = requests.get(url)
        return response
