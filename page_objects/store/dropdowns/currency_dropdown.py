import allure
from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject


class CurrencyDropdown(BasePageObject):
    _LOCATOR_EURO = (By.CSS_SELECTOR, "button[name='EUR']")
    _LOCATOR_POUND_STERLING = (By.CSS_SELECTOR, "button[name='GBP']")
    _LOCATOR_DOLLAR = (By.CSS_SELECTOR, "button[name='USD']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def select_euro(self) -> None:
        self.click(self._LOCATOR_EURO)

    @allure.step
    def select_pound_sterling(self) -> None:
        self.click(self._LOCATOR_POUND_STERLING)

    @allure.step
    def select_dollar(self) -> None:
        self.click(self._LOCATOR_DOLLAR)
