import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.store.pages.base_page import BasePage


class RegisterSuccessPageLocators:
    PAGE_LOAD = Locator(By.CSS_SELECTOR, "#common-success")
    SUCCESS_HEADER = Locator(By.CSS_SELECTOR, "h1")


class RegisterSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def wait_for_page_load(self):
        self.present_element(RegisterSuccessPageLocators.PAGE_LOAD)
        return self

    @allure.step
    def get_success_header_text(self) -> str:
        return self.visible_element(RegisterSuccessPageLocators.SUCCESS_HEADER).text
