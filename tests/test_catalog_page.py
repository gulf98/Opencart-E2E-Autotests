import allure
import pytest

from utils.page_switcher import PageSwitcher


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the catalog page")
def test_catalog_page_elements_visibility(driver):
    PageSwitcher(driver).open_store_main_page() \
        .open_components_dropdown() \
        .open_monitors() \
        .check_for_visible_elements()
