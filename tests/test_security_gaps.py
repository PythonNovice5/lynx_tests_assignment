import pytest
from pages.basepage import BasePage
from pages.loggedinpage import LoggedinPage
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.setup import SetUp


class TestSecurityGaps(BasePage):

    @pytest.mark.sql_injection
    @pytest.mark.parametrize("credentialstype", ["sql_injection_creds"])
    def test_sql_injection_login_admin(self, credentialstype, get_url_value):
        self.logger.info("------- test_sql_injection_login_admin ----------- ")
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
            self.logger.info(f"Test passed {test_desc}")
        else:
            pytest.fail(f"Test Failed {test_desc}!")

    @pytest.mark.ftp_access
    def test_ftp_unauthorized_access(self, get_url_value):
        self.logger.info("------- test_ftp_unauthorized_access ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        self.homepageObj.handle_welcome_page_popup()
        self.homepageObj.handle_cookies()
        ftp_url = self.homepageObj.get_ftp_url()

        response = self.homepageObj.get_response(ftp_url)
        print(type(response))
        status_code = response.status_code
        if status_code != 200:
            self.logger.info(
                f"Test passed - test_ftp_unauthorized_access {status_code}"
            )
        else:
            pytest.fail(f"Test failed - test_ftp_unauthorized_access {status_code}")

    @pytest.mark.usage_data_access
    def test_usage_data_access(self, get_url_value):
        self.logger.info("------- test_usage_data_access ----------- ")
        self.pageobj(self.driver)
        self.setupObj.navigate_to_url(get_url_value)
        url = self.driver.current_url
        url = url + "metrics"
        response = self.homepageObj.get_response(url)
        status_code = response.status_code
        if status_code != 200:
            self.logger.info(f"Test passed - test_usage_data_access {status_code}")
        else:
            pytest.fail(f"Test failed - test_usage_data_access {status_code}")

    def pageobj(self, getdriver):
        self.setupObj = SetUp(getdriver)
        self.homepageObj = HomePage(getdriver)
        self.loginObj = LoginPage(getdriver)
        self.loggedinObj = LoggedinPage(getdriver)
