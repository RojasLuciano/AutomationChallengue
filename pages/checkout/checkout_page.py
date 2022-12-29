from pages.base_page import BasePage
from utils.locators import CheckoutPageLocators
from utils import users


class CheckOutPage(BasePage):
    def __init__(self, driver):
        self.locator = CheckoutPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        """Check if the page is loaded"""
        return True if self.find_element(*self.locator.CHECKOUT_INFO) else False

    def check_overview_page_loaded(self):
        """Check if the page is loaded"""
        return True if self.find_element(*self.locator.CHECKOUT_OVERVIEW) else False

    def complete_user_info(self, user):
        """Complete user info"""
        user = users.get_user(user)
        self.enter_first_name((user["name"]))
        self.enter_last_name((user["last_name"]))
        self.enter_postal_code((user["postal_code"]))

    def enter_first_name(self, first_name):
        """Enter first name"""
        self.find_element(*self.locator.FIRST_NAME).send_keys(first_name)

    def enter_last_name(self, last_name):
        """Enter last name"""
        self.find_element(*self.locator.LAST_NAME).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        """Enter postal code"""
        self.find_element(*self.locator.ZIP_CODE).send_keys(postal_code)

    def click_continue_button(self):
        """Click continue button"""
        self.find_element(*self.locator.CONTINUE).click()

    def click_cancel_button(self):
        """Click cancel button"""
        self.find_element(*self.locator.CANCEL).click()

    def click_finish_button(self):
        """Click finish button"""
        self.find_element(*self.locator.FINISH).click()

    def click_back_button(self):
        """Click back button"""
        self.find_element(*self.locator.BACK_HOME).click()

    def check_order_complete(self):
        """Check if the order is complete"""
        return True if self.find_element(*self.locator.COMPLETE_HEADER) else False
