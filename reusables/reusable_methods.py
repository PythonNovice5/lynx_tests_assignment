from selenium.webdriver.support.ui import Select
from pages.basePage import BasePage

class Reusables(BasePage):
    def select_option(self,dropdown_element, selector_type, value):
        elem=self.wait_for_element_to_be_visible(dropdown_element)
        self.scrollToElement(elem)
        self.logger.info(("Scrolled into element"))
        dropdown = Select(elem)

        if selector_type == "text":
            dropdown.select_by_visible_text(value)
        elif selector_type == "value":
            dropdown.select_by_value(value)
        elif selector_type == "index":
            dropdown.select_by_index(int(value))
        else:
            raise ValueError("Invalid selector type. Use 'text', 'value', or 'index'.")