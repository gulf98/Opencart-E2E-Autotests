from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePageObject:
    _WEB_DRIVER_WAIT_TIMEOUT = 5
    _ACTION_CHAINS_PAUSE = 0.1

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.web_driver_wait = WebDriverWait(driver=driver, timeout=self._WEB_DRIVER_WAIT_TIMEOUT)

    def present_element(self, locator: tuple) -> WebElement:
        try:
            return self.web_driver_wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался появления в DOM элемента {locator}")

    def visible_element(self, locator: tuple) -> WebElement:
        try:
            return self.web_driver_wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def visible_elements(self, locator: tuple) -> List[WebElement]:
        try:
            return self.web_driver_wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    def click(self, locator: tuple) -> None:
        ActionChains(self.driver).move_to_element(self.visible_element(locator)) \
            .pause(self._ACTION_CHAINS_PAUSE) \
            .click() \
            .perform()

    def input(self, locator: tuple, value: str) -> None:
        element = self.visible_element(locator)
        self.click(locator)
        element.clear()
        element.send_keys(value)

    def is_present_element_with_text(self, locator: tuple, text: str) -> bool:
        try:
            return self.web_driver_wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError(f"Не дождался появления в DOM элемента {locator}")

    def present_alert(self) -> Alert:
        try:
            return self.web_driver_wait.until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError(f"Не дождался появления алерта")
