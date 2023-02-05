import allure
from selenium.webdriver.common.by import By

from utils.types import Locator
from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.login_page import LoginPage
from page_objects.store.pages.logout_page import LogoutPage
from page_objects.store.pages.register_page import RegisterPage

class MyAccountDropdownLocators:
    REGISTER = Locator(By.CSS_SELECTOR, "#top a[href$='register']")
    LOGIN = Locator(By.CSS_SELECTOR, "#top a[href$='login']")
    LOGOUT = Locator(By.CSS_SELECTOR, "#top a[href$='logout']")

class MyAccountDropdown(BasePageObject):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def open_register_page(self) -> RegisterPage:
        self.click(MyAccountDropdownLocators.REGISTER)
        return RegisterPage(self.driver)

    @allure.step
    def open_login_page(self) -> LoginPage:
        self.click(MyAccountDropdownLocators.LOGIN)
        return LoginPage(self.driver)

    @allure.step
    def logout(self) -> LogoutPage:
        self.click(MyAccountDropdownLocators.LOGOUT)
        return LogoutPage(self.driver)
