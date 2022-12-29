from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.CLASS_NAME, 'app_logo')
    PRODUCTS = (By.XPATH, "//*[contains(text(), 'Products')]")
    MENU_BURGER = (By.ID, 'react-burger-menu-btn')
    MENU_BURGER_ALL_ITEMS = (By.ID, 'inventory_sidebar_link')
    MENU_BURGER_LOGOUT = (By.ID, 'about_sidebar_link')
    MENU_BURGER_RESET_APP_STATE = (By.ID, 'reset_sidebar_link')
    MENU_BURGER_CLOSE = (By.ID, 'react-burger-cross-btn')
    CART = (By.ID, 'shopping_cart_container')
    ADD_TO_CART_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    REMOVE_FROM_CART_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')

    ADD_TO_CART_BIKE_LIGHT = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    REMOVE_FROM_CART_BIKE_LIGHT = (By.ID, 'remove-sauce-labs-bike-light')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//*[@data-test="error"]')


class CartPageLocators(object):
    YOUR_CART_TITLE = (By.XPATH, "//*[contains(text(), 'Your Cart')]")
    DESCRIPTION = (By.XPATH, "//*[contains(text(), 'DESCRIPTION')]")
    CART = (By.ID, 'shopping_cart_container')
    REMOVE = (By.ID, 'remove-sauce-labs-backpack')
    CHECKOUT = (By.ID, 'checkout')
    CONTINUE_SHOPPING = (By.ID, 'continue-shopping')
    REMOVE_BACKPACK = (By.ID, 'remove-sauce-labs-backpack')
    REMOVE_BIKE_LIGHT = (By.ID, 'remove-sauce-labs-bike-light')
    CART_LIST = (By.CLASS_NAME, 'cart_list')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')


class CheckoutPageLocators(object):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')
    CANCEL = (By.ID, 'cancel')
    CHECKOUT_INFO = (By.XPATH, "//*[contains(text(), 'Checkout: Your Information')]")
    CHECKOUT_OVERVIEW = (By.XPATH, "//*[contains(text(), 'Checkout: Overview')]")
    FINISH = (By.ID, 'finish')
    COMPLETE_HEADER = (By.XPATH, "//*[contains(text(), 'THANK YOU FOR YOUR ORDER')]")
    BACK_HOME = (By.ID, 'back-to-products')
