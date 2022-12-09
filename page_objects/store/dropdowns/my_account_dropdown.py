import allure
from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.login_page import LoginPage
from page_objects.store.pages.register_page import RegisterPage


class MyAccountDropdown(BasePageObject):
    _LOCATOR_REGISTER = (By.LINK_TEXT, "Register")
    _LOCATOR_LOGIN = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def open_register_page(self) -> RegisterPage:
        self.click(self._LOCATOR_REGISTER)
        return RegisterPage(self.driver)

    @allure.step
    def open_login_page(self) -> LoginPage:
        self.click(self._LOCATOR_LOGIN)
        return LoginPage(self.driver)
