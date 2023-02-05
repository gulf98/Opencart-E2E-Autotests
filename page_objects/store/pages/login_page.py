import allure
from selenium.webdriver.common.by import By

from utils.types import Locator
from page_objects.store.pages.account_page import AccountPage
from page_objects.store.pages.base_page import BasePage


class LoginPageLocators:
    EMAIL = Locator(By.CSS_SELECTOR, "#input-email")
    PASSWORD = Locator(By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = Locator(By.CSS_SELECTOR, "input[value='Login']")


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def fill_in_email(self, value: str):
        self.input(LoginPageLocators.EMAIL, value)
        return self

    @allure.step
    def fill_in_password(self, value: str):
        self.input(LoginPageLocators.PASSWORD, value)
        return self

    @allure.step
    def click_to_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)
        return self

    @allure.step
    def login(self, email: str, password: str) -> AccountPage:
        self.fill_in_email(email)
        self.fill_in_password(password)
        self.click_to_login()
        return AccountPage(self.driver)
