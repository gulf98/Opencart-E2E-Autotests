import allure
import pytest

from page_objects.store.pages.main_page import MainPage


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the main page")
def test_main_page_elements_visibility(driver):
    MainPage(driver) \
        .open_page() \
        .check_for_visible_elements() \
        .check_for_present_elements()


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the product card page")
def test_product_card_page_elements_visibility(driver):
    MainPage(driver) \
        .open_page() \
        .product_card_list.open_product_card_page_by_index(0) \
        .check_for_visible_elements()
