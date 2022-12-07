from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject


class BasePage(BasePageObject):
    _LOCATOR_CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group")
    _LOCATOR_CURRENT_CURRENCY = (By.CSS_SELECTOR, "strong")
    _LOCATOR_MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "#top .dropdown")
    _LOCATOR_COMPONENTS_DROPDOWN = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3)")

    def __init__(self, driver):
        super().__init__(driver)

    def open_currency_dropdown(self):
        self.click(self._LOCATOR_CURRENCY_DROPDOWN)
        from page_objects.store.dropdowns.currency_dropdown import CurrencyDropdown
        return CurrencyDropdown(self.driver)

    def is_present_currency(self, text: str) -> bool:
        return self.is_present_element_with_text(self._LOCATOR_CURRENT_CURRENCY, text)

    def get_visible_current_currency(self) -> str:
        return self.visible_element(self._LOCATOR_CURRENT_CURRENCY).text

    def open_my_account_dropdown(self):
        self.click(self._LOCATOR_MY_ACCOUNT_DROPDOWN)
        from page_objects.store.dropdowns.my_account_dropdown import MyAccountDropdown
        return MyAccountDropdown(self.driver)

    def open_components_dropdown(self):
        self.click(self._LOCATOR_COMPONENTS_DROPDOWN)
        from page_objects.store.dropdowns.components_dropdown import ComponentsDropdown
        return ComponentsDropdown(self.driver)