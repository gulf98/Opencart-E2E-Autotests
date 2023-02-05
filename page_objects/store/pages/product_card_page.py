import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.types import Locator
from page_objects.store.pages.base_page import BasePage


class ProductCardPageLocators:
    THUMBNAIL = Locator(By.CSS_SELECTOR, "a[class='thumbnail']")
    TABS_LOCATOR = Locator(By.CSS_SELECTOR, ".nav-tabs li")
    ADD_TO_WISH_LIST = Locator(By.CSS_SELECTOR, "button[data-original-title*='Add to Wish List']")
    ADD_TO_COMPARE = Locator(By.CSS_SELECTOR, "button[data-original-title*='Compare this Product']")
    PRODUCT_QUANTITY = Locator(By.CSS_SELECTOR, "#input-quantity")
    ADD_TO_CART = Locator(By.CSS_SELECTOR, "button[id='button-cart']")


class ProductCardPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(ProductCardPageLocators.THUMBNAIL)
        self.visible_elements(ProductCardPageLocators.TABS_LOCATOR)
        self.visible_element(ProductCardPageLocators.ADD_TO_WISH_LIST)
        self.visible_element(ProductCardPageLocators.ADD_TO_COMPARE)
        self.visible_element(ProductCardPageLocators.PRODUCT_QUANTITY)
        self.visible_element(ProductCardPageLocators.ADD_TO_CART)
        return self
