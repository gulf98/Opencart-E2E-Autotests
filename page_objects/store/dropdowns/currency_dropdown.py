import allure
from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject


class CurrencyDropdown(BasePageObject):
    _LOCATOR_EURO = (By.CSS_SELECTOR, "button[name='EUR']")
    _LOCATOR_POUND_STERLING = (By.CSS_SELECTOR, "button[name='GBP']")
    _LOCATOR_DOLLAR = (By.CSS_SELECTOR, "button[name='USD']")
    _CURRENCIES = {
        "$": _LOCATOR_DOLLAR,
        "€": _LOCATOR_EURO,
        "£": _LOCATOR_POUND_STERLING
    }

    def __init__(self, driver, parent_object):
        super().__init__(driver=driver, parent_object=parent_object)

    @allure.step
    def select_currency_by_symbol(self, currency: str):
        self.click(self._CURRENCIES[currency])
        return self.parent_object
