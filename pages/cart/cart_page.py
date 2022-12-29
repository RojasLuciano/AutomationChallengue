
from pages.base_page import BasePage
from pages.checkout.checkout_page import CheckOutPage
from utils.locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, driver):
        self.locator = CartPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        """Check if the page is loaded"""
        return True if self.find_element(*self.locator.YOUR_CART_TITLE) else False

    def tap_checkout(self):
        """Click checkout button"""
        self.find_element(*self.locator.CHECKOUT).click()
        return CheckOutPage(self.driver)

    def tap_remove_backpack(self):
        """Click remove backpack button"""
        self.find_element(*self.locator.REMOVE_BACKPACK).click()

    def tap_remove_bike_light(self):
        """Click remove bike light button"""
        self.find_element(*self.locator.REMOVE_BIKE_LIGHT).click()

    def tap_continue_shopping(self):
        """Click continue shopping button"""
        self.find_element(*self.locator.CONTINUE_SHOPPING).click()

    def get_item_list_quantity(self):
        """Get item list quantity"""
        div = self.find_element(*self.locator.CART_LIST)
        res = list(div.find_elements(*self.locator.CART_ITEM))
        return len(res)

