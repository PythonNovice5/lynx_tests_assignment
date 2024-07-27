import pytest
from pages.basepage import BasePage
from pages.loggedinpage import LoggedinPage
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.setup import SetUp


class TestOwasp(BasePage):

    @pytest.mark.smoke
    @pytest.mark.pagination
    def test_pagination(self, get_url_value):
        """Test to verify the pagination"""
        self.logger.info("------- test_pagination_ ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        self.homepageObj.handle_welcome_page_popup()
        self.homepageObj.handle_cookies()
        items_text_page_1 = self.homepageObj.get_list_of_items()
        self.logger.info("Got the list of items on Page 1")
        self.homepageObj.go_to_next_page()
        items_text_page_2 = self.homepageObj.get_list_of_items()
        self.logger.info("Got the list of items on Page 2")
        # Compare the items
        different_items = set(items_text_page_2) - set(items_text_page_1)
        if different_items:
            self.logger.info(
                "Pagination works correctly. Different items are displayed on the second page."
            )
            self.logger.info(
                "######################## TEST PASSED ######################### "
            )
        else:
            pytest.fail(
                "Pagination does not work correctly. Same items are displayed on both pages!"
            )

    @pytest.mark.smoke
    @pytest.mark.items_per_page
    @pytest.mark.parametrize("items_per_page", ["number_of_items"])
    def test_number_of_items_per_page(self, get_url_value, items_per_page):
        """Test to verify the number of items per page functionality"""
        self.logger.info("------- test_number_of_items_per_page ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        self.homepageObj.handle_welcome_page_popup()
        self.homepageObj.handle_cookies()
        data = self.homepageObj.get_test_data("test_data")[items_per_page]
        for items_per_page in data:
            expected_items = items_per_page
            self.homepageObj.select_items_per_page(items_per_page)
            actual_items_on_page = len(self.homepageObj.get_list_of_items())
            if actual_items_on_page == expected_items:
                self.logger.info(
                    f"Items per page were verified sucessfully, items per page in dropdown - {expected_items} Actual Items on Page: {actual_items_on_page}"
                )
                self.logger.info(
                    "######################## TEST PASSED ######################### "
                )
            else:
                pytest.fail(
                    f"Number of items per page could not be verified Expected: {expected_items} Actual: {actual_items_on_page}"
                )

    @pytest.mark.smoke
    @pytest.mark.language_switch
    @pytest.mark.parametrize("language", ["Deutsch", "English"])
    def test_languagues_used(self, get_url_value, language):
        """Test to verify the different languages"""
        self.logger.info("------- test_valid_login ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        self.homepageObj.handle_welcome_page_popup()
        self.homepageObj.handle_cookies()
        data = self.homepageObj.get_test_data("test_data")["languages"][language]
        test_desc = data["description"]
        self.homepageObj.select_language_webpage(language)
        if self.homepageObj.verify_languages(data) == True:
            self.logger.info(f"Test passed, {test_desc}")
            self.logger.info(
                "######################## TEST PASSED ######################### "
            )
        else:
            pytest.fail(f"Test failed - {test_desc}")

    @pytest.mark.smoke
    @pytest.mark.login_check
    @pytest.mark.parametrize(
        "credentialstype",
        [
            "invalid_creds",
            "valid_creds",
        ],
    )
    def test_login(self, get_url_value, credentialstype):
        """Test to verify the login with valid and invalid creds"""
        self.logger.info("------- test_valid_login ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        self.homepageObj.handle_welcome_page_popup()
        self.homepageObj.handle_cookies()
        self.homepageObj.navigate_to_login_page()
        self.verifyPageURL("login")
        data = self.homepageObj.get_test_data("login_creds")[credentialstype]
        email = data["user"]
        password = data["password"]
        test_desc = data["description"]
        self.loginObj.login_to_the_app(email, password)

        if self.loginObj.verify_login(credentialstype) == True:
            self.logger.info(f"Test passed - {test_desc}")
            self.logger.info(
                "######################## TEST PASSED ######################### "
            )
        else:
            pytest.fail(f"Test failed - {test_desc}")

    def pageobj(self, getdriver):
        self.setupObj = SetUp(getdriver)
        self.homepageObj = HomePage(getdriver)
        self.loginObj = LoginPage(getdriver)
        self.loggedinObj = LoggedinPage(getdriver)
