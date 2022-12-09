import random
from uuid import uuid4

import allure
from mimesis import Person

from page_objects.admin_panel.login_page import LoginPage as AdminPanelLoginPage
from page_objects.store.pages.main_page import MainPage

ADMIN_USER = "user"
ADMIN_PASSWORD = "bitnami"


@allure.title("Checking the visibility of elements on the main page")
def test_main_page_elements_visibility(driver):
    MainPage(driver).check_for_visible_elements() \
        .check_for_present_elements()


@allure.title("Checking the visibility of elements on the catalog page")
def test_catalog_page_elements_visibility(driver):
    MainPage(driver).open_components_dropdown() \
        .open_monitors() \
        .check_for_visible_elements()


@allure.title("Checking the visibility of elements on the product card page")
def test_product_card_page_elements_visibility(driver):
    MainPage(driver).product_card_list.open_product_card_page_by_index(0) \
        .check_for_visible_elements()


@allure.title("Checking the visibility of elements on the admin panel login page")
def test_admin_panel_login_page_elements_visibility(driver):
    AdminPanelLoginPage(driver).check_for_visible_elements()


@allure.title("Checking the visibility of elements on the register page")
def test_register_page_elements_visibility(driver):
    MainPage(driver).open_my_account_dropdown() \
        .open_register_page() \
        .check_for_visible_elements()


@allure.title("Currency change test")
def test_switch_currency(driver):
    main_page = MainPage(driver)
    main_page.open_currency_dropdown().select_pound_sterling()
    main_page.is_present_currency("£")
    assert main_page.get_visible_current_currency() == "£"
    assert main_page.product_card_list.get_product_price_by_index(0).find("£") >= 0


@allure.title("Registering a new user in store")
def test_registering_new_user_in_store(driver):
    register_success_page = MainPage(driver) \
        .open_my_account_dropdown() \
        .open_register_page() \
        .register_random_person(Person()) \
        .wait_for_page_load()
    assert register_success_page.get_success_title_text() == "Your Account Has Been Created!"


@allure.title("Adding new product in admin panel")
def test_adding_new_product_in_admin_panel(driver):
    actual_success_message = AdminPanelLoginPage(driver).login(ADMIN_USER, ADMIN_PASSWORD) \
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


@allure.title("Removing product from list in admin panel")
def test_removing_product_from_list_in_admin_panel(driver):
    actual_success_message = AdminPanelLoginPage(driver).login(ADMIN_USER, ADMIN_PASSWORD) \
        .click_to_menu_catalog() \
        .click_to_menu_catalog_products() \
        .product_card_list.select_by_index(0) \
        .click_to_delete_product() \
        .accept_delete() \
        .get_success_message()
    assert "Success: You have modified products!" in actual_success_message
