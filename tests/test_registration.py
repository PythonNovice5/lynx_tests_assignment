import pytest

from pages.basePage import BasePage
from pages.registerationPage import Registration
from pages.setup import SetUp
from utilities.utils import read_data_from_csv


class TestRegistration(BasePage):

    def get_test_data_for_description(self,description):
        csv_data = read_data_from_csv('valid_data.csv')
        for row in csv_data:
            if row.get('description') == description:
                return row
        return None

    def xtest_user_registration_with_missing_data(self, get_url_value):
        """Test to verify the mandatory fields functionality"""
        self.logger.info("------- xtest_user_registration_with_missing_data ----------- ")
        self.pageobj(self.driver)
        self.logger.info(f"THE VALUE OF THE URL IS : {get_url_value}")
        self.setupObj.navigate_to_url(get_url_value)
        self.regObj.handle_cookies()
        self.click_web_element(self.regObj.button_further)

        if self.regObj.verify_mandatory_fields_warning() and self.verifyPageURL(self.regObj.reg_start_url) is True:
            self.logger.info("############### Mandatory Fields error warning was found! ################### ")
        else:
            pytest.fail("No warning was found, test failed!")

    @pytest.mark.parametrize("description", ["Valid test With valid values for registration"])
    def xtest_user_registration_all_valid_data(self, get_url_value,description):
        """Test to verify the functionality of the form when valid is data is provided for mandatory fields"""
        self.logger.info("------- test_user_registration_all_valid_data ----------- ")
        valid_data = self.get_test_data_for_description(description)
        if valid_data:
            self.logger.info("RUNNING TEST WITH DESCRIPTION: " + valid_data['description'])
            self.pageobj(self.driver)
            self.setupObj.navigate_to_url(get_url_value)
            self.regObj.handle_cookies()
            self.regObj.fill_registration_form(valid_data)
            self.regObj.click_web_element(self.regObj.button_further)
            # self.regObj.select_own_account_YesOrNo(valid_data['ownaccount'])

            if self.verifyPageURL(self.regObj.reg_regulatory_url) == True:
                self.logger.info("User is able to proceed further to next page after giving all valid inputs!")
            else:
                pytest.fail("User could not proceed to the next page, test failed!")

        else:
            pytest.skip(f"No test data found for description: {description}")

    @pytest.mark.parametrize("description", ["Valid test With valid values for registration"])
    def test_user_registration_all_valid_data(self, get_url_value, description):
        """Test to verify the functionality of the form when valid is data is provided for mandatory fields"""
        self.logger.info("------- test_user_registration_all_valid_data ----------- ")
        valid_data = self.get_test_data_for_description(description)
        if valid_data:
            self.logger.info("RUNNING TEST WITH DESCRIPTION: " + valid_data['description'])
            self.pageobj(self.driver)
            self.setupObj.navigate_to_url(get_url_value)
            self.regObj.handle_cookies()
            self.regObj.fill_registration_form(valid_data)
            self.regObj.click_web_element(self.regObj.button_further)


            if self.verifyPageURL(self.regObj.reg_regulatory_url) is True:
                self.logger.info("User is able to proceed further to next page after giving all valid inputs!")
            else:
                pytest.fail("User could not proceed to the next page, test failed!")

            self.regObj.select_own_account_YesOrNo(valid_data['ownaccount'])
            self.regObj.enter_initial_amount(valid_data)
            self.regObj.enter_tax_information(valid_data)
            self.regObj.tax_residence_details(valid_data)
            self.regObj.enter_job_related_information(valid_data)
            self.regObj.previous_financial_services(valid_data)
            self.regObj.click_web_element(self.regObj.button_further)

            if self.verifyPageURL(self.regObj.tradeinfo_url) == True:
                self.logger.info("User is able to proceed further to next page after giving all valid inputs!")
            else:
                pytest.fail("User could not proceed to the next page, test failed!")
        else:
            pytest.skip(f"No test data found for description: {description}")

    @pytest.mark.parametrize("description",["Test when Security Question Answers are same"])
    def xtest_user_registration_with_security_answers_same(self, get_url_value, description):
        self.logger.info("------- test_user_registration_with_security_answers_same ----------- ")
        valid_data=self.get_test_data_for_description(description)
        if valid_data:
            self.pageobj(self.driver)
            self.logger.info(f"THE VALUE OF THE URL IS : {get_url_value}")
            self.setupObj.navigate_to_url(get_url_value)
            self.regObj.handle_cookies()
            self.logger.info(valid_data.items())

            print(f"Executing test for row: {valid_data}")
            self.regObj.fill_registration_form(valid_data)

            if self.regObj.verify_same_security_answers_warning() is True:
                self.logger.info("Verified: Security Warning was found!")
            else:
                pytest.fail("No security warning was found, test failed!")

        else:
            pytest.skip(f"No test data found for description: {description}")

    @pytest.mark.parametrize("description", ["Verify if LYNX portfolio can only be opened with self account"])
    def xtest_open_portfolio_with_own_acc(self, get_url_value, description):
        """Test to verify if LYNX portfolio can only be opened with self account"""
        self.logger.info("------- test_open_portfolio_with_own_acc ----------- ")
        valid_data = self.get_test_data_for_description(description)
        if valid_data:
            self.logger.info("RUNNING TEST WITH DESCRIPTION: " + valid_data['description'])
            self.pageobj(self.driver)
            self.setupObj.navigate_to_url(get_url_value)
            self.regObj.handle_cookies()
            self.regObj.fill_registration_form(valid_data)
            self.regObj.click_web_element(self.regObj.button_further)
            self.verifyPageURL(self.regObj.reg_regulatory_url)
            self.regObj.select_own_account_YesOrNo(valid_data['ownaccount'])

            if self.regObj.account_declaration_warning() is True:
                self.logger.info("Verified:User is not allowed to open portfolio on behalf of others, Only self trading account is permitted!")
            else:
                pytest.fail("No blocker warning found, test failed!")

        else:
            pytest.skip(f"No test data found for description: {description}")






    def pageobj(self, getdriver):
        self.setupObj = SetUp(getdriver)
        self.regObj = Registration(getdriver)
