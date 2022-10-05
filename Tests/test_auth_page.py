from Config.config import TestData
from Pages.auth_page import AuthPage
from Tests.test_base import BaseTest
import pytest


class TestAuth(BaseTest):

    @pytest.fixture(scope="function")
    def setup(self, web_browser):
        self.auth_page = AuthPage(web_browser)

    @pytest.mark.usefixtures("setup")
    def test_registration(self):
        """Регистрация пользователя"""
        self.auth_page.sign_up.click()
        self.auth_page.registry_new_account(TestData.NAME, TestData.TEL,
                                            TestData.EMAIL, TestData.PASSWORD)
        self.auth_page.wait_page_loaded()
        assert self.auth_page.visible_button_add_store()

    @pytest.mark.usefixtures("setup")
    def test_login_positive(self):
        """Вход в аккаунт с валидными данными"""
        self.auth_page.log_in(TestData.EMAIL, TestData.PASSWORD)
        assert self.auth_page.visible_button_add_store()

    @pytest.mark.usefixtures("setup")
    def test_logout(self):
        """Выход из аккаунта"""
        self.auth_page.log_in(TestData.EMAIL, TestData.PASSWORD)
        self.auth_page.close_window_with_add_store()
        self.auth_page.logout_personal_area()
        self.auth_page.wait_page_loaded()
        assert self.auth_page.visible_fields_mail_and_psw()

    @pytest.mark.usefixtures("setup")
    def test_login_negative(self):
        """Вход в аккаунт с невалидными данными"""
        self.auth_page.log_in(TestData.EMAIL, "12345678Qw")
        assert self.auth_page.visible_button_error_login()





