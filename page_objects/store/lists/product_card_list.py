import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.product_card_page import ProductCardPage


class ProductCardListLocators:
    PRODUCT_CARD_LIST = Locator(By.CSS_SELECTOR, ".product-thumb")
    NAMED_LINK_TO_PRODUCT_PAGE = Locator(By.CSS_SELECTOR, ".product-thumb .caption h4 a")
    PRODUCT_CARD_PRICE_ = Locator(By.CSS_SELECTOR, ".product-thumb p.price")


class ProductCardList(BasePageObject):

    def __init__(self, driver, parent_object):
        super().__init__(driver=driver, parent_object=parent_object)

    @allure.step
    def open_product_card_page_by_index(self, index: int) -> ProductCardPage:
        self.visible_elements(ProductCardListLocators.PRODUCT_CARD_LIST)[index] \
            .find_element(*ProductCardListLocators.NAMED_LINK_TO_PRODUCT_PAGE) \
            .click()
        return ProductCardPage(self.driver)

    @allure.step
    def get_product_name_by_index(self, index: int) -> str:
        return self.visible_elements(ProductCardListLocators.PRODUCT_CARD_LIST)[index] \
            .find_element(*ProductCardListLocators.NAMED_LINK_TO_PRODUCT_PAGE) \
            .get_attribute("text")

    @allure.step
    def get_product_price_by_index(self, index: int) -> str:
        return self.visible_elements(ProductCardListLocators.PRODUCT_CARD_LIST)[index] \
            .find_element(*ProductCardListLocators.PRODUCT_CARD_PRICE_).text
