import allure
import pytest

from page_objects.store.pages.main_page import MainPage


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the catalog page")
def test_catalog_page_elements_visibility(driver):
    MainPage(driver) \
        .open_page() \
        .open_components_dropdown() \
        .open_monitors() \
        .check_for_visible_elements()
