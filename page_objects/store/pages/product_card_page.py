import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.store.pages.base_page import BasePage


class ProductCardPage(BasePage):
    _LOCATOR_THUMBNAIL = (By.CSS_SELECTOR, "a[class='thumbnail']")
    _LOCATOR_TABS_LOCATOR = (By.CSS_SELECTOR, ".nav-tabs li")
    _LOCATOR_ADD_TO_WISH_LIST = (By.CSS_SELECTOR, "button[data-original-title*='Add to Wish List']")
    _LOCATOR_ADD_TO_COMPARE = (By.CSS_SELECTOR, "button[data-original-title*='Compare this Product']")
    _LOCATOR_PRODUCT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
    _LOCATOR_ADD_TO_CART = (By.CSS_SELECTOR, "button[id='button-cart']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(self._LOCATOR_THUMBNAIL)
        self.visible_elements(self._LOCATOR_TABS_LOCATOR)
        self.visible_element(self._LOCATOR_ADD_TO_WISH_LIST)
        self.visible_element(self._LOCATOR_ADD_TO_COMPARE)
        self.visible_element(self._LOCATOR_PRODUCT_QUANTITY)
        self.visible_element(self._LOCATOR_ADD_TO_CART)
        return self
