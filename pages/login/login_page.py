from pages.home.home_page import HomePage
from utils.locators import *
from pages.base_page import BasePage
from utils import users


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)
        super().open("https://www.saucedemo.com/")

    def enter_email(self, email):
        """This method is to enter email"""
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_password(self, password):
        """This method is to enter password"""
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        """This method is to click login button"""
        self.find_element(*self.locator.SUBMIT).click()

    def login(self, user):
        """This method is to log in with valid user"""
        user = users.get_user(user)
        self.enter_email(user["name"])
        self.enter_password(user["password"])
        self.click_login_button()

    def login_with_valid_user(self, user):
        """This method is to log in with valid user"""
        self.login(user)
        return HomePage(self.driver)

    def login_with_invalid_user(self, user):
        """This method is to log in with invalid user"""
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text

