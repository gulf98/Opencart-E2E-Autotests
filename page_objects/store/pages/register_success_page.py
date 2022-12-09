import allure
from selenium.webdriver.common.by import By

from page_objects.store.pages.base_page import BasePage


class RegisterSuccessPage(BasePage):
    _LOCATOR_PAGE_LOAD = (By.CSS_SELECTOR, "#common-success")
    _LOCATOR_SUCCESS_HEADER = (By.CSS_SELECTOR, "h1")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def wait_for_page_load(self):
        self.present_element(self._LOCATOR_PAGE_LOAD)
        return self

    @allure.step
    def get_success_title_text(self) -> str:
        return self.visible_element(self._LOCATOR_SUCCESS_HEADER).text
