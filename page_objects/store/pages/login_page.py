from selenium.webdriver.common.by import By

from page_objects.store.pages.base_page import BasePage


class LoginPage(BasePage):
    _LOCATOR_EMAIL = (By.CSS_SELECTOR, "#input-email")
    _LOCATOR_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    _LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_email(self, value: str):
        self.input(self._LOCATOR_EMAIL, value)
        return self

    def fill_in_password(self, value: str):
        self.input(self._LOCATOR_PASSWORD, value)
        return self

    def click_to_login(self):
        self.click(self._LOCATOR_LOGIN_BUTTON)
        return self

    def login(self, email: str, password: str):
        self.fill_in_email(email)
        self.fill_in_password(password)
        self.click_to_login()
