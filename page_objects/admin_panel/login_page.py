import allure
from selenium.webdriver.common.by import By

from utils.types import Locator
from page_objects.admin_panel.main_page import MainPage
from page_objects.base_page_object import BasePageObject


class LoginPageLocators:
    USERNAME = Locator(By.CSS_SELECTOR, "#input-username")
    PASSWORD = Locator(By.CSS_SELECTOR, "#input-password")
    FORGOTTEN_PASSWORD = Locator(By.CSS_SELECTOR, "span[class='help-block'] a")
    LOGIN_BUTTON = Locator(By.CSS_SELECTOR, "button[class$='btn-primary']")
    LINK_TO_OPENCART = Locator(By.CSS_SELECTOR, "#footer a")


class LoginPage(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(LoginPageLocators.USERNAME)
        self.visible_element(LoginPageLocators.PASSWORD)
        self.visible_element(LoginPageLocators.FORGOTTEN_PASSWORD)
        self.visible_element(LoginPageLocators.LOGIN_BUTTON)
        self.visible_element(LoginPageLocators.LINK_TO_OPENCART)

    @allure.step
    def fill_in_username(self, value: str):
        self.input(LoginPageLocators.USERNAME, value)
        return self

    @allure.step
    def fill_in_password(self, value: str):
        self.input(LoginPageLocators.PASSWORD, value)
        return self

    @allure.step
    def click_to_login(self) -> MainPage:
        self.click(LoginPageLocators.LOGIN_BUTTON)
        return MainPage(self.driver)

    @allure.step
    def login(self, username: str, password: str) -> MainPage:
        self.fill_in_username(username)
        self.fill_in_password(password)
        self.click_to_login()
        return MainPage(self.driver)
