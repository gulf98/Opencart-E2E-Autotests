import allure
from selenium.webdriver.common.by import By

from page_objects.store.pages.base_page import BasePage
from page_objects.store.pages.register_success_page import RegisterSuccessPage


class RegisterPage(BasePage):
    _LOCATOR_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    _LOCATOR_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    _LOCATOR_EMAIL = (By.CSS_SELECTOR, "#input-email")
    _LOCATOR_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    _LOCATOR_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    _LOCATOR_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    _LOCATOR_AGREE_PRIVACY_POLICY = (By.CSS_SELECTOR, "input[name='agree']")
    _LOCATOR_CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    _LOCATOR_HEADER = (By.CSS_SELECTOR, "h1")
    _LOCATOR_FIRST_NAME_TEXT_DANGER = (By.CSS_SELECTOR, "#account div:nth-child(3) [class='text-danger']")
    _LOCATOR_LAST_NAME_TEXT_DANGER = (By.CSS_SELECTOR, "#account div:nth-child(4) [class='text-danger']")
    _LOCATOR_EMAIL_TEXT_DANGER = (By.CSS_SELECTOR, "#account div:nth-child(5) [class='text-danger']")
    _LOCATOR_TELEPHONE_TEXT_DANGER = (By.CSS_SELECTOR, "#account div:nth-child(6) [class='text-danger']")
    _LOCATOR_PASSWORD_TEXT_DANGER = (By.CSS_SELECTOR, "fieldset:nth-child(2) > div:nth-child(2) [class='text-danger']")
    _LOCATOR_PASSWORD_CONFIRM_TEXT_DANGER = \
        (By.CSS_SELECTOR, "fieldset:nth-child(2) > div:nth-child(3) [class='text-danger']")
    _LOCATOR_ALERT_DANGER = (By.CSS_SELECTOR, "div[class*='alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(self._LOCATOR_FIRSTNAME)
        self.visible_element(self._LOCATOR_LASTNAME)
        self.visible_element(self._LOCATOR_EMAIL)
        self.visible_element(self._LOCATOR_TELEPHONE)
        self.visible_element(self._LOCATOR_PASSWORD)
        self.visible_element(self._LOCATOR_PASSWORD_CONFIRM)
        self.visible_element(self._LOCATOR_AGREE_PRIVACY_POLICY)
        self.visible_element(self._LOCATOR_CONTINUE_BUTTON)

    @allure.step
    def fill_in_firstname(self, value: str):
        self.input(self._LOCATOR_FIRSTNAME, value)
        return self

    @allure.step
    def fill_in_lastname(self, value: str):
        self.input(self._LOCATOR_LASTNAME, value)
        return self

    @allure.step
    def fill_in_email(self, value: str):
        self.input(self._LOCATOR_EMAIL, value)
        return self

    @allure.step
    def fill_in_telephone(self, value: str):
        self.input(self._LOCATOR_TELEPHONE, value)
        return self

    @allure.step
    def fill_in_password(self, value: str):
        self.input(self._LOCATOR_PASSWORD, value)
        return self

    @allure.step
    def fill_in_password_confirm(self, value: str):
        self.input(self._LOCATOR_PASSWORD_CONFIRM, value)
        return self

    @allure.step
    def agree_to_privacy_policy(self):
        self.click(self._LOCATOR_AGREE_PRIVACY_POLICY)
        return self

    @allure.step
    def click_to_continue(self) -> RegisterSuccessPage:
        self.click(self._LOCATOR_CONTINUE_BUTTON)
        return RegisterSuccessPage(self.driver)

    @allure.step
    def fill_all_personal_fields(self, person: dict):
        self.fill_in_firstname(person["firstname"])
        self.fill_in_lastname(person["lastname"])
        self.fill_in_email(person["email"])
        self.fill_in_telephone(person["telephone"])
        self.fill_in_password(person["password"])
        self.fill_in_password_confirm(person["password_confirm"])
        return self

    @allure.step
    def register_person(self, person: dict) -> RegisterSuccessPage:
        self.fill_all_personal_fields(person)
        self.agree_to_privacy_policy()
        self.click_to_continue()
        return RegisterSuccessPage(self.driver)

    @allure.step
    def try_to_continue(self):
        self.click(self._LOCATOR_CONTINUE_BUTTON)
        return self

    @allure.step
    def try_to_register_person(self, person: dict):
        self.fill_all_personal_fields(person)
        self.agree_to_privacy_policy()
        self.try_to_continue()
        return self

    @allure.step
    def get_header_text(self) -> str:
        return self.visible_element(self._LOCATOR_HEADER).text

    @allure.step
    def get_firstname_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_FIRST_NAME_TEXT_DANGER).text

    @allure.step
    def get_lastname_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_LAST_NAME_TEXT_DANGER).text

    @allure.step
    def get_email_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_EMAIL_TEXT_DANGER).text

    @allure.step
    def get_telephone_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_TELEPHONE_TEXT_DANGER).text

    @allure.step
    def get_password_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_PASSWORD_TEXT_DANGER).text

    @allure.step
    def get_password_confirm_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_PASSWORD_CONFIRM_TEXT_DANGER).text

    @allure.step
    def get_alert_danger_text(self) -> str:
        return self.visible_element(self._LOCATOR_ALERT_DANGER).text
