import allure
from selenium.webdriver.common.by import By

from infrastructure.types import Locator
from page_objects.store.pages.base_page import BasePage
from page_objects.store.lists.product_card_list import ProductCardList


class MainPageLocators:
    SLIDESHOW = Locator(By.CSS_SELECTOR, "div#slideshow0")
    SLIDESHOW_BUTTON_PREV = Locator(By.CSS_SELECTOR, ".slideshow div.swiper-button-prev")
    SLIDESHOW_BUTTON_NEXT = Locator(By.CSS_SELECTOR, ".slideshow div.swiper-button-next")
    SLIDESHOW_PAGINATION_BULLETS = Locator(By.CSS_SELECTOR, "div[class*='swiper-pagination slideshow0'] span")
    CAROUSEL = Locator(By.CSS_SELECTOR, "div[id = carousel0]")
    CAROUSEL_BUTTON_PREV = Locator(By.CSS_SELECTOR, ".carousel div.swiper-button-prev")
    CAROUSEL_BUTTON_NEXT = Locator(By.CSS_SELECTOR, ".carousel div.swiper-button-next")
    CAROUSEL_PAGINATION_BULLETS = Locator(By.CSS_SELECTOR, "div[class*='swiper-pagination carousel0'] span")


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.product_card_list = ProductCardList(driver=driver, parent_object=self)

    def open_page(self):
        self.driver.get(self.driver.base_url)
        return self

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(MainPageLocators.SLIDESHOW)
        self.visible_elements(MainPageLocators.SLIDESHOW_PAGINATION_BULLETS)
        self.visible_element(MainPageLocators.CAROUSEL)
        self.present_element(MainPageLocators.CAROUSEL_BUTTON_PREV)
        self.visible_elements(MainPageLocators.CAROUSEL_PAGINATION_BULLETS)
        return self

    @allure.step
    def check_for_present_elements(self):
        self.present_element(MainPageLocators.SLIDESHOW_BUTTON_PREV)
        self.present_element(MainPageLocators.SLIDESHOW_BUTTON_NEXT)
        self.present_element(MainPageLocators.CAROUSEL_BUTTON_NEXT)
        return self
