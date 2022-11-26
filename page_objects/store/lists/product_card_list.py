from selenium.webdriver.common.by import By

from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.product_card_page import ProductCardPage


class ProductCardList(BasePageObject):
    _LOCATOR_PRODUCT_CARD_LIST = (By.CSS_SELECTOR, ".product-thumb")
    _LOCATOR_NAMED_LINK_TO_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-thumb .caption h4 a")
    _LOCATOR_PRODUCT_CARD_PRICE_ = (By.CSS_SELECTOR, ".product-thumb p.price")

    def __init__(self, driver):
        super().__init__(driver)

    def open_product_card_page_by_index(self, index: int) -> ProductCardPage:
        self.visible_elements(self._LOCATOR_PRODUCT_CARD_LIST)[index] \
            .find_element(*self._LOCATOR_NAMED_LINK_TO_PRODUCT_PAGE) \
            .click()
        return ProductCardPage(self.driver)

    def get_product_name_by_index(self, index: int) -> str:
        return self.visible_elements(self._LOCATOR_PRODUCT_CARD_LIST)[index] \
            .find_element(*self._LOCATOR_NAMED_LINK_TO_PRODUCT_PAGE) \
            .get_attribute("text")

    def get_product_price_by_index(self, index: int) -> str:
        return self.visible_elements(self._LOCATOR_PRODUCT_CARD_LIST)[index] \
            .find_element(*self._LOCATOR_PRODUCT_CARD_PRICE_) \
            .text
