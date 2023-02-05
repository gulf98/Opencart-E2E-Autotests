import random
from uuid import uuid4

import allure
import pytest

from utils.config import ADMIN_PANEL_CREDENTIALS
from utils.page_switcher import PageSwitcher


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the admin panel login page")
def test_admin_panel_login_page_elements_visibility(driver):
    PageSwitcher(driver).open_admin_panel_login_page() \
        .check_for_visible_elements()


@pytest.mark.smoke
@allure.title("Adding new product in admin panel")
def test_adding_new_product_in_admin_panel(driver):
    actual_success_message = PageSwitcher(driver).open_admin_panel_login_page() \
        .login(*ADMIN_PANEL_CREDENTIALS) \
        .click_to_menu_catalog() \
        .click_to_menu_catalog_products() \
        .click_to_add_product() \
        .fill_in_name(str(uuid4())) \
        .fill_in_meta_tag_title(str(uuid4())) \
        .click_to_data_tab() \
        .fill_in_model(str(uuid4())) \
        .fill_in_price(random.randint(1, 100)) \
        .click_to_save() \
        .get_success_message()
    assert "Success: You have modified products!" in actual_success_message


@pytest.mark.smoke
@allure.title("Removing product from list in admin panel")
def test_removing_product_from_list_in_admin_panel(driver):
    actual_success_message = PageSwitcher(driver).open_admin_panel_login_page() \
        .login(*ADMIN_PANEL_CREDENTIALS) \
        .click_to_menu_catalog() \
        .click_to_menu_catalog_products() \
        .product_card_list.select_by_index(0) \
        .click_to_delete_product() \
        .accept_delete() \
        .get_success_message()
    assert "Success: You have modified products!" in actual_success_message
