import allure
from selenium.webdriver.common.by import By

from utils.types import Locator
from page_objects.base_page_object import BasePageObject


class AddProductPageLocators:
    NAME = Locator(By.CSS_SELECTOR, "#form-product > * #input-name1")
    META_TAG_TITLE = Locator(By.CSS_SELECTOR, "#form-product > * #input-meta-title1")
    MODEL = Locator(By.CSS_SELECTOR, "#form-product > * #input-model")
    PRICE = Locator(By.CSS_SELECTOR, "#form-product > * #input-price")
    SAVE_BUTTON = Locator(By.CSS_SELECTOR, "button[data-original-title='Save']")
    DATA_TAB = Locator(By.LINK_TEXT, 'Data')


class AddProductPage(BasePageObject):

    @allure.step
    def fill_in_name(self, value):
        self.input(AddProductPageLocators.NAME, value)
        return self

    @allure.step
    def fill_in_meta_tag_title(self, value):
        self.input(AddProductPageLocators.META_TAG_TITLE, value)
        return self

    @allure.step
    def fill_in_model(self, value):
        self.input(AddProductPageLocators.MODEL, value)
        return self

    @allure.step
    def fill_in_price(self, value):
        self.input(AddProductPageLocators.PRICE, value)
        return self

    @allure.step
    def click_to_data_tab(self):
        self.click(AddProductPageLocators.DATA_TAB)
        return self

    @allure.step
    def click_to_save(self):
        self.click(AddProductPageLocators.SAVE_BUTTON)
        from page_objects.admin_panel.products_page import ProductsPage
        return ProductsPage(self.driver)
