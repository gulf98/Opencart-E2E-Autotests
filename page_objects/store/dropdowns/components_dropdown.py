import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.catalog_page import CatalogPage


class ComponentsDropdownLocators:
    MICE = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(1)")
    MONITORS = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(2)")
    PRINTERS = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(3)")
    SCANNERS = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(4)")
    WEB = Locator(By.CSS_SELECTOR, "#menu > div> ul > li:nth-child(3) > div > div > ul > li:nth-child(5)")


class ComponentsDropdown(BasePageObject):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def open_mice(self) -> CatalogPage:
        self.click(ComponentsDropdownLocators.MICE)
        return CatalogPage(self.driver)

    @allure.step
    def open_monitors(self) -> CatalogPage:
        self.click(ComponentsDropdownLocators.MONITORS)
        return CatalogPage(self.driver)

    @allure.step
    def open_printers(self) -> CatalogPage:
        self.click(ComponentsDropdownLocators.PRINTERS)
        return CatalogPage(self.driver)

    @allure.step
    def open_scanners(self) -> CatalogPage:
        self.click(ComponentsDropdownLocators.SCANNERS)
        return CatalogPage(self.driver)

    @allure.step
    def open_web_cameras(self) -> CatalogPage:
        self.click(ComponentsDropdownLocators.WEB)
        return CatalogPage(self.driver)
