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

    def test_user_registration_missing_data(self, get_url_value):
        """Test to verify the mandatory fields functionality"""
        self.logger.info("------- test_user_registration_missing_data ----------- ")
        self.pageobj(self.driver)
        self.logger.info(f"THE VALUE OF THE URL IS : {get_url_value}")
        self.setupObj.navigate_to_url(get_url_value)
        self.regObj.handle_cookies()
        self.click_web_element(self.regObj.button_further)


        if self.regObj.verify_mandatory_fields_warning() and self.verifyPageURL(self.regObj.reg_start_url) == True:

            self.logger.info("############### Mandatory Fields error warning was found! ################### ")
        else:
            pytest.fail("No warning was found, test failed!")

    def test_user_registration_all_valid_data(self, get_url_value):
        """Test to verify the mandatory fields functionality"""
        self.logger.info("------- test_user_registration_missing_data ----------- ")
        self.pageobj(self.driver)
        self.logger.info(f"THE VALUE OF THE URL IS : {get_url_value}")
        self.setupObj.navigate_to_url(get_url_value)
        self.regObj.handle_cookies()
        self.click_web_element(self.regObj.button_further)


        if self.regObj.verify_mandatory_fields_warning() and self.verifyPageURL(self.regObj.reg_start_url) == True:

            self.logger.info("############### Mandatory Fields error warning was found! ################### ")
        else:
            pytest.fail("No warning was found, test failed!")


    @pytest.mark.parametrize("description",["Test when Security Question Answers are same"])
    def test_user_registration_with_security_answers_same(self, get_url_value, description):
        self.logger.info("------- test_user_registration_with_security_answers_same ----------- ")
        valid_data=self.get_test_data_for_description(description)
        if valid_data:
            self.pageobj(self.driver)
            self.logger.info(f"THE VALUE OF THE URL IS : {get_url_value}")
            self.setupObj.navigate_to_url(get_url_value)
            self.regObj.handle_cookies()
            self.logger.info(valid_data.items())
            self.logger.info(f"First name: {valid_data['firstname']}")
            print(f"Executing test for row: {valid_data}")
            self.regObj.fill_registration_form(valid_data)

            if self.regObj.verify_same_security_answers_warning()==True:
                self.logger.info("Security Warning was found!")
            else:
                pytest.fail("No security warning was found, test failed!")

        else:
            pytest.skip(f"No test data found for description: {description}")















    def pageobj(self, getdriver):
        self.setupObj = SetUp(getdriver)
        self.regObj = Registration(getdriver)
