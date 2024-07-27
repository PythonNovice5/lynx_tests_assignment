from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage
from reusables.reusable_methods import Reusables


class Registration(BasePage):
    def __init__(self, driver):
        self.driver = driver

    cookie_dialog_box = (By.NAME, "CybotCookiebotDialog")
    cookie_adjust = (By.ID, "CybotCookiebotDialogBodyLevelButtonCustomize")
    cookie_decline = (By.ID, "CybotCookiebotDialogBodyButtonDecline")

    """ Contact Details """
    first_name = (By.ID, "firstname")
    last_name = (By.ID, "lastname")
    email = (By.NAME, "email")
    country_code = (By.NAME, "intcode")
    mobile_number = (By.NAME, "mobile")
    # DepotType=""

    """Registration Address Section"""
    street = (By.ID, "street")
    house_number = (By.ID, "streetnumber")
    additional_address = (By.ID, "co")
    postal_code = (By.ID, "zip")
    city = (By.ID, "city")
    country_dropdown = (By.ID, "country")
    state_dropdown = (By.XPATH, "//select[@ng-model='province']")
    postalSameYes = (By.XPATH,"//div[@name='postal_same']//button[@uib-btn-radio='true']")
    postalSameNo = (By.XPATH, "//div[@name='postal_same']//button[@uib-btn-radio='false']")


    """Personal Information Section"""
    birth_day = (By.XPATH, "//select[@ng-model='day']")
    birth_month = (By.XPATH, "//select[@ng-model='month']")
    birth_year = (By.XPATH, "//select[@ng-model='year']")
    country_of_birth_dropdown = (By.ID, "bornin")
    place_of_birth = (By.ID, "place_of_birth")
    nationality_dropdown = (By.ID, "nationality")
    another_nationality_yes = (By.XPATH, "//*[contains(text(),'Another')]//..//..//..//button[contains(text(),'Yes')]")
    another_nationality_no = (By.XPATH, "//*[contains(text(),'Another')]//..//..//..//button[contains(text(),'No')]")
    number_of_dependants = (By.ID, "dependants")

    """Security Questions"""
    grand_mother_first_name_answer = (By.NAME, "first_question")
    additional_second_question_dropdown = (By.XPATH, "//select[@name='second_question']")
    additional_second_question_answer = (By.NAME, "second_question_answer")
    additional_third_question_dropdown = (By.XPATH, "//select[@name='third_question']")
    additional_third_question_answer = (By.NAME, "third_question_answer")

    """Next button"""
    button_further = (By.XPATH, "//button[contains(@class,'move-ahead')]")

    """regulatory info"""
    first_deposit = (By.ID,"deposit")


    """Information in accordance with Section 10 Paragraph 1 No. 2 of the Money Laundering Act"""
    own_account_no = (By.XPATH, "//div[@name='ownaccount']/button[@uib-btn-radio='false']")
    own_account_yes= (By.XPATH, "//div[@name='ownaccount']/button[@uib-btn-radio='true']")

    '''references for assertions'''
    warning_for_same_security_question_answers = (By.NAME,"security_questions_all_same")
    mandatoryFieldsWarningMsg = (By.CSS_SELECTOR,".sticky-error-header")
    reg_start_url = "wizard/start"
    reg_regulatory_url="wizard/personal"
    tradeinfo_url = "wizard/config"
    multiple_nationality_dropdown = (By.ID,"multiplenationality")
    # own_account_warning = (By.XPATH,"//form[contains(@class,'invalid-accepted')]")
    own_account_warning=(By.XPATH,"//div[@ng-show='person.owner.self===false']")
    box_SSN = (By.NAME,"taxid_usperson")

    def handle_cookies(self):
        try:
            if self.wait_for_element_to_be_visible(self.cookie_dialog_box, timeout=10):
                self.click_web_element(self.cookie_adjust)
                self.logger.info("Clicked on Customize cookies")
                self.click_web_element(self.cookie_decline)
                self.logger.info("Clicked on decline unnecessary cookies")
        except:
            pass

    def select_own_account_YesOrNo(self, YesOrNO):
        if YesOrNO=='Yes':
            self.click_web_element(self.own_account_yes)
        elif YesOrNO=='No':
            self.click_web_element(self.own_account_no)
        self.logger.info(f"Own Account Yes/No is selected as: {YesOrNO}")

    def select_button(self,name,yesorno):
        value=""
        if yesorno=="Yes":
            value='true'
        elif yesorno=="No":
            value = 'false'
        loc =(By.XPATH,"//div[@name='{}']/button[@uib-btn-radio='{}']".format(name,value))
        self.click_web_element(loc)



    def tax_residence_details(self,data):
        if 'taxcountry' in data.keys():
            sel = (By.ID,"taxcountry")
            self.select_option(sel,"text",data['taxcountry'])
        if 'taxid_available' in data.keys():
            self.select_button("taxid_available",data['taxid_available'])
        if 'taxid' in data.keys():
            loc=(By.ID,'taxid')
            self.enter_value_into_element(loc,data['taxid'])
        if 'taxid_secondary' in data.keys():
            self.select_button("taxid_secondary",data['taxid_secondary'])

    def verify_presence_of_SSN_box(self):
        if self.wait_and_find_element(self.box_SSN):
            return True
        else:
            return False

    # def enter_job_information(self,data):
    #     self.logger.info("Entering Job related information ----")
    #     fields = data.keys()
    #     if 'activity' in fields:
    #         elem = (By.NAME,'activity')
    #         self.select_option(elem,"index",data['activity'])
    #     if 'occupation' in fields:
    #         loc = (By.XPATH,"//*[@id='occupation' and @required] ")
    #         self.enter_value_into_element(loc,data['occupation'])
    #     if 'industry' in fields:
    #         elem = (By.ID,'industry')
    #         self.select_option(elem,"index",data['industry'])
    #     if 'occupational' in fields:
    #         self.select_button('occupational',data['occupational'])

    def select_this_button(self, button_name, button_text):
        if button_text == "Mister":
            value = "male"
        elif button_text == "Woman":
            value = "female"
        elif button_text == "Individual portfolio":
            value = "account_single"
        elif button_text == "Community depot":
            value = "account_joint"
        else:
            value=button_text.lower()
        loc = (By.XPATH, "//button[@name='%s' and contains(@uib-btn-radio,'%s')]" % (button_name, value))
        self.click_web_element(loc)



    def select_gender(self, maleOrFemale):
        self.select_this_button("gender", maleOrFemale)
        self.logger.info(f"The gender is selected as: {maleOrFemale}")

    def enter_contact_details(self, data):
        self.select_gender(data['salutation'])
        self.enter_value_into_element(self.first_name, data['firstname'])
        self.logger.info(f"Entered first name as {data['firstname']}")
        self.enter_value_into_element(self.last_name, data['lastname'])
        self.logger.info(f"Entered last name as {data['lastname']}")
        self.enter_value_into_element(self.mobile_number, data['mobilenumber'])
        self.logger.info(f"Entered mobile number as {data['mobilenumber']}")
        self.enter_value_into_element(self.country_code, data['countrycode'])
        self.logger.info(f"Entered country code as  {data['countrycode']}")
        self.enter_value_into_element(self.email, data['email'])
        self.logger.info(f"Entered email of person as  {data['email']}")
        self.select_depot_type(data['depottype'])
        self.logger.info(f"Depottype is selected as {data['depottype']}")

    def select_depot_type(self, type):
        self.select_this_button('account_type', type)

    def enter_registration_address(self, data):
        self.enter_value_into_element(self.street, data['street'])
        self.logger.info(f"Entered Street Number as: {data['street']}")
        self.enter_value_into_element(self.house_number, data['housenumber'])
        self.logger.info(f"Entered House Number as: {data['housenumber']}")

        self.enter_value_into_element(self.additional_address, data['additionaladdress'])
        self.logger.info(f"Entered additional address as: {data['additionaladdress']}")

        self.enter_value_into_element(self.postal_code, data['postalcode'])
        self.logger.info(f"Entered postalcode as: {data['postalcode']}")
        self.enter_value_into_element(self.city, data['location'])
        # self.enter_value_into_element(self.additional_address, data['additionaladdress'])
        self.select_option(self.country_dropdown, "text", data['country'])
        self.select_option(self.state_dropdown,"text",data['state'])
        self.postal_address_same_yes_no(data['PostalAddressSameYesNo'])
        self.logger.info(f"Postal address is same Yes/No is selected as {data['PostalAddressSameYesNo']}")



    def postal_address_same_yes_no(self,YesOrNo):
        if YesOrNo=="Yes":
            self.click_web_element(self.postalSameYes)
        elif YesOrNo=="No":
            self.click_web_element(self.postalSameNo)

    def enter_personal_info(self,data):
        self.select_option(self.birth_day,"text",data['birthday'])
        self.logger.info(f"entering birth details")
        self.select_option(self.birth_month,"index",data['birthmonth'])
        self.select_option(self.birth_year,"text",data['birthyear'])
        self.select_option(self.country_of_birth_dropdown,"text",data['countryofbirth'])
        self.enter_value_into_element(self.place_of_birth,data['placeofbirth'])
        self.select_option(self.nationality_dropdown,"text",data['nationality'])
        self.logger.info(f"Entered nationality as: {data['nationality']}")
        self.another_nationality_yes_no(data['anothernationality'])
        self.select_marital_status(data['maritalstatus'])
        self.logger.info(f"Selecting Marital status as: {data['maritalstatus']}")
        self.select_option(self.number_of_dependants,"text",data['numberofdependants'])


    def enter_security_questions_answers(self,data):
        self.logger.info(f"Entering information for Security Questions Section")
        self.enter_value_into_element(self.grand_mother_first_name_answer,data['SA1'])
        self.logger.info(f"Entered the answer for Security question 1 as: {data['SA1']}")
        self.select_option(self.additional_second_question_dropdown,"index",data['SQ2'])
        self.logger.info(f"Selected the second security question from dropdown")
        self.enter_value_into_element(self.additional_second_question_answer, data['SA2'])
        self.select_option(self.additional_third_question_dropdown,"index",data['SQ3'])
        self.enter_value_into_element(self.additional_third_question_answer,data['SA3'])


    def enter_initial_amount(self,data):
        if 'deposit' in data.keys():
            loc = (By.ID,'deposit')
            self.enter_value_into_element(loc,data['deposit'],'deposit')

    def previous_financial_services(self,data):
        if 'previousfinancialservices' in data.keys():
            # loc =( By.XPATH,f"//*[@class='checkbox']/div[contains(@ng-class,'{data['previousfinancialservices']}')]")
            loc = (By.XPATH, f"//input[@type='checkbox' and contains(@ng-model,'{data['previousfinancialservices']}')]//..")
            loc =(By.XPATH,f"//label[@for='{data['previousfinancialservices']}']")
            # loc = (By.XPATH, f"//*[@class='checkbox']/div[contains(@ng-class,'{data['previousfinancialservices']}')]")

            self.click_web_element(loc)
            self.logger.info(f"Selected previous financial services as: {data['previousfinancialservices']}")

    def enter_job_related_information(self,data):#ideally I will put the locators seperatly from the code, could not do because of time constraints
        self.logger.info("Entering Job related information ----")
        fields = data.keys()
        if 'activity' in fields:
            elem = (By.NAME, 'activity')
            self.select_option(elem, "index", data['activity'])
        if 'occupation' in fields:
            loc = (By.XPATH, "//*[@id='occupation' and @required] ")
            self.enter_value_into_element(loc, data['occupation'])
        if 'industry' in fields:
            elem = (By.ID, 'industry')
            self.select_option(elem, "index", data['industry'])
        if 'occupational' in fields:
            self.select_button('occupational', data['occupational'])
        if 'employer_name' in fields:
            loc = (By.XPATH,"//*[@class='slide-in-out']//*[@name='employer_name']")
            self.enter_value_into_element(loc,data['employer_name'],"employer_name")
        if 'employer_street' in fields:
            loc = (By.ID,"employer_street")
            self.enter_value_into_element(loc,data['employer_street'],'employer_street')
        if 'emploer_co' in fields:
            loc = (By.ID,"emploer_co")
            self.enter_value_into_element(loc,data['emploer_co'],'emploer_co')
        if 'employer_zip' in fields:
            loc=(By.ID,"employer_zip")
            self.enter_value_into_element(loc,data["employer_zip"],"employer_zip")
        if 'employer_city' in fields:
            loc =(By.ID,"employer_city")
            self.enter_value_into_element(loc,data["employer_city"],"employer_city")
        if 'employer_state' in fields:
            loc = (By.XPATH,"//div[@class!='ng-hide']/select[@ng-model='province']")
            self.select_option(loc,"index",data['employer_state'])
        if 'employer_years' in fields:
            loc = (By.ID,"employer_years")
            self.select_option(loc,"index",data['employer_years'])
        if 'incomeoptions' in fields:
            loc = (By.ID,"incomeoptions")
            self.select_option(loc,"index",data['incomeoptions'])
        if 'finance' in fields:
            self.select_button("finance",data['finance'])
        if 'publicly_traded_company' in fields:
            self.select_button('publicly_traded_company',data['publicly_traded_company'])
        if 'work_publicly_traded_company' in fields:
            self.select_button('work_publicly_traded_company',data['work_publicly_traded_company'])



    def enter_tax_information(self,data):
        self.logger.info("ENTERING TAX INFORMATION ----")
        fields = data.keys()
        if 'greencard' in fields:
            self.select_button("usperson_1",data['greencard'])
        if 'stay183' in fields:
            self.select_button("usperson_2",data['stay183'])
        if 'mainResidenceUS'  in data.keys():
            self.select_button('usperson_3',data['mainResidenceUS'])
        if 'UScitizenship' in fields:
            self.select_button("usperson_4",data['UScitizenship'])
        if 'jointaccount' in fields:
            self.select_button("usperson_5", data['jointaccount'])
        if 'taxliability' in fields:
            self.select_button("usperson_6",data['taxliability'])






    def verify_same_security_answers_warning(self):
        if self.wait_and_find_element(self.warning_for_same_security_question_answers):
            return True
        else:
            return False

    def verify_mandatory_fields_warning(self):
        return self.wait_and_find_element(self.mandatoryFieldsWarningMsg)

    def fill_registration_form(self, data):
        self.enter_contact_details(data)
        self.enter_registration_address(data)
        self.enter_personal_info(data)
        self.enter_security_questions_answers(data)


    def another_nationality_yes_no(self,YesOrNo):
        if YesOrNo=="Yes":
            value="true"
        elif YesOrNo=="No":
            value="false"

        loc = (By.XPATH,"//div[@name='multiplenationality_exists']//button[@uib-btn-radio='{}']".format(value))
        self.click_web_element(loc)

    def select_marital_status(self,status):
        self.select_this_button("marriage",status)


    def select_option(self,dropdown_element, selector_type, value):
        elem=self.wait_for_element_to_be_visible(dropdown_element)
        self.scrollToElement(elem)
        if selector_type=='index':
            self.logger.info(f"Selecting the dropdown value at index: {value} ")
        else:
            self.logger.info(f"Selecting {value} from the dropdown ")
        dropdown = Select(elem)

        if selector_type == "text":
            dropdown.select_by_visible_text(value)
        elif selector_type == "value":
            dropdown.select_by_value(value)
        elif selector_type == "index":
            dropdown.select_by_index(int(value))
        else:
            raise ValueError("Invalid selector type. Use 'text', 'value', or 'index'.")

    def account_declaration_warning(self):
        if self.wait_and_find_element(self.own_account_warning):
            return True
        else:
            return False


