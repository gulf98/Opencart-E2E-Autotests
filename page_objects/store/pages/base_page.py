import allure
from selenium.webdriver.common.by import By

from utils.types import Locator
from page_objects.base_page_object import BasePageObject


class BasePageLocators:
    CURRENCY_DROPDOWN = Locator(By.CSS_SELECTOR, "#top .btn-group")
    CURRENT_CURRENCY = Locator(By.CSS_SELECTOR, "strong")
    MY_ACCOUNT_DROPDOWN = Locator(By.CSS_SELECTOR, "#top .dropdown")
    COMPONENTS_DROPDOWN = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3)")


class BasePage(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def open_currency_dropdown(self):
        self.click(BasePageLocators.CURRENCY_DROPDOWN)
        from page_objects.store.dropdowns.currency_dropdown import CurrencyDropdown
        return CurrencyDropdown(driver=self.driver, parent_object=self)

    @allure.step
    def is_present_currency(self, text: str) -> bool:
        return self.is_present_element_with_text(BasePageLocators.CURRENT_CURRENCY, text)

    @allure.step
    def get_visible_current_currency(self) -> str:
        return self.visible_element(BasePageLocators.CURRENT_CURRENCY).text

    @allure.step
    def open_my_account_dropdown(self):
        self.click(BasePageLocators.MY_ACCOUNT_DROPDOWN)
        from page_objects.store.dropdowns.my_account_dropdown import MyAccountDropdown
        return MyAccountDropdown(self.driver)

    @allure.step
    def open_components_dropdown(self):
        self.click(BasePageLocators.COMPONENTS_DROPDOWN)
        from page_objects.store.dropdowns.components_dropdown import ComponentsDropdown
        return ComponentsDropdown(self.driver)
