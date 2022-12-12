import allure
from selenium.webdriver.common.by import By

from page_objects.store.pages.base_page import BasePage
from page_objects.store.lists.product_card_list import ProductCardList


class MainPage(BasePage):
    _LOCATOR_SLIDESHOW = (By.CSS_SELECTOR, "div#slideshow0")
    _LOCATOR_SLIDESHOW_BUTTON_PREV = (By.CSS_SELECTOR, ".slideshow div.swiper-button-prev")
    _LOCATOR_SLIDESHOW_BUTTON_NEXT = (By.CSS_SELECTOR, ".slideshow div.swiper-button-next")
    _LOCATOR_SLIDESHOW_PAGINATION_BULLETS = (By.CSS_SELECTOR, "div[class*='swiper-pagination slideshow0'] span")
    _LOCATOR_CAROUSEL = (By.CSS_SELECTOR, "div[id = carousel0]")
    _LOCATOR_CAROUSEL_BUTTON_PREV = (By.CSS_SELECTOR, ".carousel div.swiper-button-prev")
    _LOCATOR_CAROUSEL_BUTTON_NEXT = (By.CSS_SELECTOR, ".carousel div.swiper-button-next")
    _LOCATOR_CAROUSEL_PAGINATION_BULLETS = (By.CSS_SELECTOR, "div[class*='swiper-pagination carousel0'] span")

    def __init__(self, driver):
        super().__init__(driver)
        self.product_card_list = ProductCardList(driver)
        driver.get(driver.base_url)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(self._LOCATOR_SLIDESHOW)
        self.visible_elements(self._LOCATOR_SLIDESHOW_PAGINATION_BULLETS)
        self.visible_element(self._LOCATOR_CAROUSEL)
        self.present_element(self._LOCATOR_CAROUSEL_BUTTON_PREV)
        self.visible_elements(self._LOCATOR_CAROUSEL_PAGINATION_BULLETS)
        return self

    @allure.step
    def check_for_present_elements(self):
        self.present_element(self._LOCATOR_SLIDESHOW_BUTTON_PREV)
        self.present_element(self._LOCATOR_SLIDESHOW_BUTTON_NEXT)
        self.present_element(self._LOCATOR_CAROUSEL_BUTTON_NEXT)
        return self
