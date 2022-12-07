from mimesis import Person
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

    def __init__(self, driver):
        super().__init__(driver)

    def check_for_visible_elements(self):
        self.visible_element(self._LOCATOR_FIRSTNAME)
        self.visible_element(self._LOCATOR_LASTNAME)
        self.visible_element(self._LOCATOR_EMAIL)
        self.visible_element(self._LOCATOR_TELEPHONE)
        self.visible_element(self._LOCATOR_PASSWORD)
        self.visible_element(self._LOCATOR_PASSWORD_CONFIRM)
        self.visible_element(self._LOCATOR_AGREE_PRIVACY_POLICY)
        self.visible_element(self._LOCATOR_CONTINUE_BUTTON)

    def fill_in_firstname(self, value: str):
        self.input(self._LOCATOR_FIRSTNAME, value)
        return self

    def fill_in_lastname(self, value: str):
        self.input(self._LOCATOR_LASTNAME, value)
        return self

    def fill_in_email(self, value: str):
        self.input(self._LOCATOR_EMAIL, value)
        return self

    def fill_in_telephone(self, value: str):
        self.input(self._LOCATOR_TELEPHONE, value)
        return self

    def fill_in_password(self, value: str):
        self.input(self._LOCATOR_PASSWORD, value)
        return self

    def fill_in_password_confirm(self, value: str):
        self.input(self._LOCATOR_PASSWORD_CONFIRM, value)
        return self

    def agree_to_privacy_policy(self):
        self.click(self._LOCATOR_AGREE_PRIVACY_POLICY)
        return self

    def register_random_person(self, person: Person) -> RegisterSuccessPage:
        self.fill_in_firstname(person.first_name())
        self.fill_in_lastname(person.last_name())
        self.fill_in_email(person.email())
        self.fill_in_telephone(person.telephone())
        password = person.password()
        self.fill_in_password(password)
        self.fill_in_password_confirm(password)
        self.click(self._LOCATOR_AGREE_PRIVACY_POLICY)
        self.click_to_continue()
        return RegisterSuccessPage(self.driver)

    def click_to_continue(self) -> RegisterSuccessPage:
        self.click(self._LOCATOR_CONTINUE_BUTTON)
        return RegisterSuccessPage(self.driver)
