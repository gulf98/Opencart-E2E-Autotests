import allure
from selenium.webdriver.common.by import By

from page_objects.store.lists.product_card_list import ProductCardList
from page_objects.store.pages.base_page import BasePage


class CatalogPage(BasePage):
    _LOCATOR_CATALOG_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .list-group-item")
    _LOCATOR_LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#list-view")
    _LOCATOR_GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    _LOCATOR_SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    _LOCATOR_PRODUCT_SHOW_LIMIT = (By.CSS_SELECTOR, "#input-limit")

    def __init__(self, driver):
        super().__init__(driver)
        self.product_card_list = ProductCardList(driver=driver, parent_object=self)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_elements(self._LOCATOR_CATALOG_MENU_ITEMS)
        self.visible_element(self._LOCATOR_LIST_VIEW_BUTTON)
        self.visible_element(self._LOCATOR_GRID_VIEW_BUTTON)
        self.visible_element(self._LOCATOR_SORT_DROPDOWN)
        self.visible_element(self._LOCATOR_PRODUCT_SHOW_LIMIT)
