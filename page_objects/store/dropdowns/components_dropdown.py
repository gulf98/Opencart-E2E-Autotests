import allure
from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.catalog_page import CatalogPage


class ComponentsDropdown(BasePageObject):
    _LOCATOR_MICE = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(1)")
    _LOCATOR_MONITORS = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(2)")
    _LOCATOR_PRINTERS = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(3)")
    _LOCATOR_SCANNERS = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(4)")
    _LOCATOR_WEB = (By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(5)")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def open_mice(self) -> CatalogPage:
        self.click(self._LOCATOR_MICE)
        return CatalogPage(self.driver)

    @allure.step
    def open_monitors(self) -> CatalogPage:
        self.click(self._LOCATOR_MONITORS)
        return CatalogPage(self.driver)

    @allure.step
    def open_printers(self) -> CatalogPage:
        self.click(self._LOCATOR_PRINTERS)
        return CatalogPage(self.driver)

    @allure.step
    def open_scanners(self) -> CatalogPage:
        self.click(self._LOCATOR_SCANNERS)
        return CatalogPage(self.driver)

    @allure.step
    def open_web_cameras(self) -> CatalogPage:
        self.click(self._LOCATOR_WEB)
        return CatalogPage(self.driver)
