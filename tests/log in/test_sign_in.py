import pytest

from pages.login.login_page import LoginPage


@pytest.mark.login
@pytest.mark.all
@pytest.mark.usefixtures("setup")
class TestSignInPage:

    def test_sign_in_standard_user(self):
        """This test case is to verify that standard user can login successfully"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("standard_user")
        assert home.check_page_loaded()

    def test_sign_in_locked_out_user(self):
        """This test case is to verify that locked out user can not login"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("locked_out_user")
        assert home.check_page_loaded()

    def test_sign_in_invalid_user(self):
        """This test case is to verify that invalid user can not login"""
        login = LoginPage(self.driver)
        assert login.login_with_invalid_user("locked_out_user")

    def test_sign_in_problem_user(self):
        """This test case is to verify that problem user can login"""
        login = LoginPage(self.driver)
        home = login.login_with_valid_user("problem_user")
        assert home.check_page_loaded()
