import pytest

from pages.login.login_page import LoginPage


@pytest.mark.shoppingcart
@pytest.mark.all
@pytest.mark.usefixtures("setup")
class TestShoopingCart:

    def test_add_to_shopping_cart(self):
        """This test will add all items to the shopping cart"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart_backpack()
        cart = home.tap_cart()
        assert home.check_page_loaded()
        assert cart.get_item_list_quantity() == 1

    def test_remove_from_shopping_cart(self):
        """This test will remove all items from the shopping cart"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart_backpack()
        cart = home.tap_cart()
        assert cart.check_page_loaded()
        cart.tap_remove_backpack()
        assert cart.get_item_list_quantity() == 0

    def test_add_to_shopping_cart_and_checkout(self):
        """This test will add 2 items to the shopping cart and checkout"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart()
        cart = home.tap_cart()
        assert cart.check_page_loaded()
        checkout = cart.tap_checkout()
        assert checkout.check_page_loaded()

    def test_add_to_shopping_cart_and_continue_shopping(self):
        """This test will add 2 items to the shopping cart and continue shopping"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart()
        cart = home.tap_cart()
        assert cart.check_page_loaded()
        checkout = cart.tap_checkout()
        checkout.complete_user_info("standard_user")
        checkout.click_continue_button()
        assert checkout.check_overview_page_loaded()

    def test_add_to_shopping_cart_and_cancel_checkout(self):
        """This test will add 2 items to the shopping cart and cancel checkout"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart()
        cart = home.tap_cart()
        assert cart.check_page_loaded()
        checkout = cart.tap_checkout()
        checkout.complete_user_info("standard_user")
        checkout.click_cancel_button()
        assert cart.check_page_loaded()

    def test_add_to_shopping_cart_and_finish_shopping(self):
        """This test will add 2 items to the shopping cart and finish shopping"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()
        home.add_to_cart()
        cart = home.tap_cart()
        assert cart.check_page_loaded()
        checkout = cart.tap_checkout()
        checkout.complete_user_info("standard_user")
        checkout.click_continue_button()
        assert checkout.check_overview_page_loaded()
        checkout.click_finish_button()
        assert checkout.check_order_complete()
