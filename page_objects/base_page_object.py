import logging
import os
from typing import List

import allure
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
        self.logger = self.__logger_init()

    def __logger_init(self):
        logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        file = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file)
        logger.setLevel(self.driver.log_level)
        return logger

    def present_element(self, locator: tuple) -> WebElement:
        self.logger.info(f"Waiting for an element {locator} to appear")
        try:
            return self.web_driver_wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Did not wait for the element to appear in the DOM {locator}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Did not wait for the element to appear in the DOM {locator}")

    def visible_element(self, locator: tuple) -> WebElement:
        self.logger.info(f"Waiting for visible element {locator}")
        try:
            return self.web_driver_wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Didn't wait for element to be visible {locator}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Didn't wait for element to be visible {locator}")

    def visible_elements(self, locator: tuple) -> List[WebElement]:
        self.logger.info(f"Waiting for visible elements {locator}")
        try:
            return self.web_driver_wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Didn't wait for elements to be visible {locator}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Didn't wait for elements to be visible {locator}")

    def click(self, locator: tuple) -> None:
        element = self.visible_element(locator)
        self.logger.info(f"Clicking on element {locator}")
        ActionChains(self.driver).move_to_element(element) \
            .pause(self._ACTION_CHAINS_PAUSE) \
            .click() \
            .perform()

    def input(self, locator: tuple, value: str) -> None:
        element = self.visible_element(locator)
        self.logger.info(f"Input {value} in the {locator} field")
        self.click(locator)
        element.clear()
        element.send_keys(value)

    def is_present_element_with_text(self, locator: tuple, text: str) -> bool:
        self.logger.info(f"Waiting for the {locator} element with the text {text} to appear in the DOM")
        try:
            return self.web_driver_wait.until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.logger.error(f"Did not wait for the element to appear in the DOM {locator}")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Did not wait for the element to appear in the DOM {locator}")

    def present_alert(self) -> Alert:
        self.logger.info(f"Waiting for an alert")
        try:
            return self.web_driver_wait.until(EC.alert_is_present())
        except TimeoutException:
            self.logger.error(f"Didn't wait for the alert")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise TimeoutException(f"Didn't wait for the alert")
