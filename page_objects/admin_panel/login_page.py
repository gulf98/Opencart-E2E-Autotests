from selenium.webdriver.common.by import By

from page_objects.admin_panel.main_page import MainPage
from page_objects.base_page_object import BasePageObject


class LoginPage(BasePageObject):
    _LOCATOR_USERNAME = (By.CSS_SELECTOR, "#input-username")
    _LOCATOR_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    _LOCATOR_FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "span[class='help-block'] a")
    _LOCATOR_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class$='btn-primary']")
    _LOCATOR_LINK_TO_OPENCART = (By.CSS_SELECTOR, "#footer a")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(driver.base_url + "/admin")

    def check_for_visible_elements(self):
        self.visible_element(self._LOCATOR_USERNAME)
        self.visible_element(self._LOCATOR_PASSWORD)
        self.visible_element(self._LOCATOR_FORGOTTEN_PASSWORD)
        self.visible_element(self._LOCATOR_LOGIN_BUTTON)
        self.visible_element(self._LOCATOR_LINK_TO_OPENCART)
        return self

    def fill_in_username(self, value: str):
        self.input(self._LOCATOR_USERNAME, value)
        return self

    def fill_in_password(self, value: str):
        self.input(self._LOCATOR_PASSWORD, value)
        return self

    def click_to_login(self) -> MainPage:
        self.click(self._LOCATOR_LOGIN_BUTTON)
        return MainPage(self.driver)

    def login(self, username: str, password: str) -> MainPage:
        self.fill_in_username(username)
        self.fill_in_password(password)
        self.click_to_login()
        return MainPage(self.driver)
