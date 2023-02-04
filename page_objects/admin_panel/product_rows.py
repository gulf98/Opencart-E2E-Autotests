import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.admin_panel.products_page import ProductsPage
from page_objects.base_page_object import BasePageObject


class ProductRowsLocators:
    PRODUCT_ROWS = Locator(By.CSS_SELECTOR, "#form-product >* table > tbody > tr")
    PRODUCT_ROW_CHECKBOX = Locator(By.CSS_SELECTOR, "#form-product >* table >tbody> tr > td > input[type='checkbox']")


class ProductRows(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def select_by_index(self, index: int) -> ProductsPage:
        self.visible_elements(ProductRowsLocators.PRODUCT_ROWS)[index] \
            .find_element(*ProductRowsLocators.PRODUCT_ROW_CHECKBOX) \
            .click()
        return ProductsPage(self.driver)
