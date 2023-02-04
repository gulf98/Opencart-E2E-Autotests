import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.admin_panel.products_page import ProductsPage
from page_objects.base_page_object import BasePageObject

class MainPageLocators:
    MENU_CATALOG = Locator(By.CSS_SELECTOR, "#menu-catalog")
    MENU_CATALOG_PRODUCTS = Locator(By.LINK_TEXT, "Products")

class MainPage(BasePageObject):


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def click_to_menu_catalog(self):
        self.click(MainPageLocators.MENU_CATALOG)
        return self

    @allure.step
    def click_to_menu_catalog_products(self) -> ProductsPage:
        self.click(MainPageLocators.MENU_CATALOG_PRODUCTS)
        return ProductsPage(self.driver)
