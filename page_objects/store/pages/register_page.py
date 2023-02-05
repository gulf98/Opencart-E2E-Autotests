import allure
from selenium.webdriver.common.by import By


from utils.types import Locator, Person
from page_objects.store.pages.base_page import BasePage
from page_objects.store.pages.register_success_page import RegisterSuccessPage


class RegisterPageLocators:
    FIRSTNAME = Locator(By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = Locator(By.CSS_SELECTOR, "#input-lastname")
    EMAIL = Locator(By.CSS_SELECTOR, "#input-email")
    TELEPHONE = Locator(By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = Locator(By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = Locator(By.CSS_SELECTOR, "#input-confirm")
    AGREE_PRIVACY_POLICY = Locator(By.CSS_SELECTOR, "input[name='agree']")
    CONTINUE_BUTTON = Locator(By.CSS_SELECTOR, "input[value='Continue']")
    HEADER = Locator(By.CSS_SELECTOR, "h1")
    FIRST_NAME_TEXT_DANGER = Locator(By.CSS_SELECTOR, "#account div:nth-child(3) [class='text-danger']")
    LAST_NAME_TEXT_DANGER = Locator(By.CSS_SELECTOR, "#account div:nth-child(4) [class='text-danger']")
    EMAIL_TEXT_DANGER = Locator(By.CSS_SELECTOR, "#account div:nth-child(5) [class='text-danger']")
    TELEPHONE_TEXT_DANGER = Locator(By.CSS_SELECTOR, "#account div:nth-child(6) [class='text-danger']")
    PASSWORD_TEXT_DANGER = Locator(By.CSS_SELECTOR, "fieldset:nth-child(2) > div:nth-child(2) [class='text-danger']")
    PASSWORD_CONFIRM_TEXT_DANGER = \
        Locator(By.CSS_SELECTOR, "fieldset:nth-child(2) > div:nth-child(3) [class='text-danger']")
    ALERT_DANGER = Locator(By.CSS_SELECTOR, "div[class*='alert-danger']")


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step
    def check_for_visible_elements(self):
        self.visible_element(RegisterPageLocators.FIRSTNAME)
        self.visible_element(RegisterPageLocators.LASTNAME)
        self.visible_element(RegisterPageLocators.EMAIL)
        self.visible_element(RegisterPageLocators.TELEPHONE)
        self.visible_element(RegisterPageLocators.PASSWORD)
        self.visible_element(RegisterPageLocators.PASSWORD_CONFIRM)
        self.visible_element(RegisterPageLocators.AGREE_PRIVACY_POLICY)
        self.visible_element(RegisterPageLocators.CONTINUE_BUTTON)

    @allure.step
    def fill_in_firstname(self, value: str):
        self.input(RegisterPageLocators.FIRSTNAME, value)
        return self

    @allure.step
    def fill_in_lastname(self, value: str):
        self.input(RegisterPageLocators.LASTNAME, value)
        return self

    @allure.step
    def fill_in_email(self, value: str):
        self.input(RegisterPageLocators.EMAIL, value)
        return self

    @allure.step
    def fill_in_telephone(self, value: str):
        self.input(RegisterPageLocators.TELEPHONE, value)
        return self

    @allure.step
    def fill_in_password(self, value: str):
        self.input(RegisterPageLocators.PASSWORD, value)
        return self

    @allure.step
    def fill_in_password_confirm(self, value: str):
        self.input(RegisterPageLocators.PASSWORD_CONFIRM, value)
        return self

    @allure.step
    def agree_to_privacy_policy(self):
        self.click(RegisterPageLocators.AGREE_PRIVACY_POLICY)
        return self

    @allure.step
    def click_to_continue(self) -> RegisterSuccessPage:
        self.click(RegisterPageLocators.CONTINUE_BUTTON)
        return RegisterSuccessPage(self.driver)

    @allure.step
    def fill_all_personal_fields(self, person: Person):
        self.fill_in_firstname(person.firstname)
        self.fill_in_lastname(person.lastname)
        self.fill_in_email(person.email)
        self.fill_in_telephone(person.telephone)
        self.fill_in_password(person.password)
        self.fill_in_password_confirm(person.password_confirm)
        return self

    @allure.step
    def register_person(self, person: Person) -> RegisterSuccessPage:
        self.fill_all_personal_fields(person)
        self.agree_to_privacy_policy()
        self.click_to_continue()
        return RegisterSuccessPage(self.driver)

    @allure.step
    def try_to_continue(self):
        self.click(RegisterPageLocators.CONTINUE_BUTTON)
        return self

    @allure.step
    def try_to_register_person(self, person: Person):
        self.fill_all_personal_fields(person)
        self.agree_to_privacy_policy()
        self.try_to_continue()
        return self

    @allure.step
    def get_header_text(self) -> str:
        return self.visible_element(RegisterPageLocators.HEADER).text

    @allure.step
    def get_firstname_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.FIRST_NAME_TEXT_DANGER).text

    @allure.step
    def get_lastname_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.LAST_NAME_TEXT_DANGER).text

    @allure.step
    def get_email_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.EMAIL_TEXT_DANGER).text

    @allure.step
    def get_telephone_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.TELEPHONE_TEXT_DANGER).text

    @allure.step
    def get_password_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.PASSWORD_TEXT_DANGER).text

    @allure.step
    def get_password_confirm_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.PASSWORD_CONFIRM_TEXT_DANGER).text

    @allure.step
    def get_alert_danger_text(self) -> str:
        return self.visible_element(RegisterPageLocators.ALERT_DANGER).text
