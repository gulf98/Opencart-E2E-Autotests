import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.store.lists.product_card_list import ProductCardList
from page_objects.store.pages.base_page import BasePage


class CatalogPageLocators:
    CATALOG_MENU_ITEMS = Locator(By.CSS_SELECTOR, "#column-left .list-group-item")
    LIST_VIEW_BUTTON = Locator(By.CSS_SELECTOR, "#list-view")
    GRID_VIEW_BUTTON = Locator(By.CSS_SELECTOR, "#grid-view")
    SORT_DROPDOWN = Locator(By.CSS_SELECTOR, "#input-sort")
    PRODUCT_SHOW_LIMIT = Locator(By.CSS_SELECTOR, "#input-limit")


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_card_list = ProductCardList(driver=driver, parent_object=self)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_elements(CatalogPageLocators.CATALOG_MENU_ITEMS)
        self.visible_element(CatalogPageLocators.LIST_VIEW_BUTTON)
        self.visible_element(CatalogPageLocators.GRID_VIEW_BUTTON)
        self.visible_element(CatalogPageLocators.SORT_DROPDOWN)
        self.visible_element(CatalogPageLocators.PRODUCT_SHOW_LIMIT)
