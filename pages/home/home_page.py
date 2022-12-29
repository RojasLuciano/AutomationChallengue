from pages.base_page import BasePage
from pages.cart.cart_page import CartPage
from utils.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        """Check if the page is loaded"""
        return True if self.find_element(*self.locator.LOGO) else False

    def add_to_cart(self):
        """Add to cart"""
        if self.element_is_present(*self.locator.REMOVE_FROM_CART_BACKPACK):
            self.find_element(*self.locator.REMOVE_FROM_CART_BACKPACK).click()
        self.add_to_cart_backpack()

        if self.element_is_present(*self.locator.REMOVE_FROM_CART_BIKE_LIGHT):
            self.find_element(*self.locator.REMOVE_FROM_CART_BIKE_LIGHT).click()
        self.add_to_cart_bike_light()

    def add_to_cart_backpack(self):
        """Add to cart backpack"""
        if self.element_is_present(*self.locator.REMOVE_FROM_CART_BACKPACK):
            self.find_element(*self.locator.REMOVE_FROM_CART_BACKPACK).click()
        self.find_element(*self.locator.ADD_TO_CART_BACKPACK).click()

    def add_to_cart_bike_light(self):
        """Add to cart bike light"""
        self.find_element(*self.locator.ADD_TO_CART_BIKE_LIGHT).click()

    def tap_cart(self):
        """Click cart button"""
        self.find_element(*self.locator.CART).click()
        return CartPage(self.driver)
