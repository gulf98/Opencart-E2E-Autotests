from enum import Enum

import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.base_page_object import BasePageObject


class CurrencyLocators(Enum):
    USD = Locator(By.CSS_SELECTOR, "button[name='USD']")
    EUR = Locator(By.CSS_SELECTOR, "button[name='EUR']")
    GBP = Locator(By.CSS_SELECTOR, "button[name='GBP']")


class CurrencyDropdown(BasePageObject):

    def __init__(self, driver, parent_object):
        super().__init__(driver=driver, parent_object=parent_object)

    @allure.step
    def select_currency(self, currency_locators: CurrencyLocators):
        self.click(currency_locators.value)
        return self.parent_object
