import allure
import pytest

from page_objects.store.pages.main_page import MainPage
from test_data.personal_data import (
    correct_random_person,
    person_with_empty_firstname,
    person_with_empty_lastname,
    person_with_empty_email,
    person_with_empty_telephone,
    person_with_empty_password,
    person_with_empty_password_confirm,
    person_with_different_passwords
)


@pytest.mark.smoke
@allure.title("Checking the visibility of elements on the register page")
def test_register_page_elements_visibility(driver):
    MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .check_for_visible_elements()


@pytest.mark.smoke
@allure.title("Registering a new user")
def test_registering_new_user(driver):
    person = correct_random_person()
    register_success_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .register_person(person) \
        .wait_for_page_load()
    assert register_success_page.get_success_header_text() == "Your Account Has Been Created!"


@pytest.mark.regression
@allure.title("Attempt to register an existing user")
def test_registering_existing_user(driver):
    person = correct_random_person()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .register_person(person) \
        .wait_for_page_load() \
        .open_my_account_dropdown() \
        .logout() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_alert_danger_text() == "Warning: E-Mail Address is already registered!"


@pytest.mark.regression
@allure.title("Registration attempt with a non-accepted privacy policy")
def test_registering_non_accepted_privacy_policy(driver):
    person = correct_random_person()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .fill_all_personal_fields(person) \
        .try_to_continue()
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_alert_danger_text() == "Warning: You must agree to the Privacy Policy!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty firstname")
def test_registering_empty_firstname(driver):
    person = person_with_empty_firstname()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_firstname_danger_text() == "First Name must be between 1 and 32 characters!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty lastname")
def test_registering_empty_lastname(driver):
    person = person_with_empty_lastname()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_lastname_danger_text() == "Last Name must be between 1 and 32 characters!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty email")
def test_registering_empty_email(driver):
    person = person_with_empty_email()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_email_danger_text() == "E-Mail Address does not appear to be valid!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty telephone")
def test_registering_empty_telephone(driver):
    person = person_with_empty_telephone()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_telephone_danger_text() == "Telephone must be between 3 and 32 characters!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty password")
def test_registering_empty_password(driver):
    person = person_with_empty_password()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_password_danger_text() == "Password must be between 4 and 20 characters!"


@pytest.mark.regression
@allure.title("Attempt to register with an empty confirm")
def test_registering_empty_password_confirm(driver):
    person = person_with_empty_password_confirm()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_password_confirm_danger_text() == "Password confirmation does not match password!"


@pytest.mark.regression
@allure.title("Attempt to register with different passwords")
def test_registering_different_passwords(driver):
    person = person_with_different_passwords()
    register_page = MainPage(driver) \
        .open_page() \
        .open_my_account_dropdown() \
        .open_register_page() \
        .try_to_register_person(person)
    assert register_page.get_header_text() == "Register Account"
    assert register_page.get_password_confirm_danger_text() == "Password confirmation does not match password!"
