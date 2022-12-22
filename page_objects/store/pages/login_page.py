import allure
from selenium.webdriver.common.by import By

from page_objects.store.pages.account_page import AccountPage
from page_objects.store.pages.base_page import BasePage


class LoginPage(BasePage):
    _LOCATOR_EMAIL = (By.CSS_SELECTOR, "#input-email")
    _LOCATOR_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    _LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def fill_in_email(self, value: str):
        self.input(self._LOCATOR_EMAIL, value)
        return self

    @allure.step
    def fill_in_password(self, value: str):
        self.input(self._LOCATOR_PASSWORD, value)
        return self

    @allure.step
    def click_to_login(self):
        self.click(self._LOCATOR_LOGIN_BUTTON)
        return self

    @allure.step
    def login(self, email: str, password: str) -> AccountPage:
        self.fill_in_email(email)
        self.fill_in_password(password)
        self.click_to_login()
        return AccountPage(self.driver)
