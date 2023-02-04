import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.admin_panel.add_product_page import AddProductPage
from page_objects.base_page_object import BasePageObject


class ProductsPageLocators:
    ADD_PRODUCT_BUTTON = Locator(By.CSS_SELECTOR, "a[data-original-title='Add New']")
    DELETE_PRODUCT_BUTTON = Locator(By.CSS_SELECTOR, "button[data-original-title='Delete']")
    SUCCESS_ALERT = Locator(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")


class ProductsPage(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)
        from page_objects.admin_panel.product_rows import ProductRows
        self.product_card_list = ProductRows(driver)

    @allure.step
    def click_to_add_product(self) -> AddProductPage:
        self.click(ProductsPageLocators.ADD_PRODUCT_BUTTON)
        return AddProductPage(self.driver)

    @allure.step
    def click_to_delete_product(self):
        self.click(ProductsPageLocators.DELETE_PRODUCT_BUTTON)
        return self

    @allure.step
    def accept_delete(self):
        self.present_alert().accept()
        return self

    @allure.step
    def cancel_delete(self):
        self.present_alert().dismiss()
        return self

    @allure.step
    def get_success_message(self) -> str:
        return self.visible_element(ProductsPageLocators.SUCCESS_ALERT).text
