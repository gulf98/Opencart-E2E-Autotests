import os
import pytest
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver

DEFAULT_BROWSER = "chrome"
DEFAULT_OPENCART_BASE_URL = "http://192.168.0.105:8081"
DEFAULT_SELENIUM_DRIVERS_PATH = "~/selenium_drivers/"
DEFAULT_HEADLESS_MODE = False
DEFAULT_EXECUTOR = "192.168.0.105"
DEFAULT_SELENOID_BROWSER_VERSION = "108.0"
DEFAULT_LOGGING_LEVEL = logging.DEBUG


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default=DEFAULT_BROWSER,
        choices=["chrome", "firefox", "opera"],
        help="possible values: chrome, firefox opera"
    )
    parser.addoption(
        "--url",
        default=DEFAULT_OPENCART_BASE_URL,
        help="opencart application address"
    )
    parser.addoption(
        "--drivers",
        default=os.path.expanduser(DEFAULT_SELENIUM_DRIVERS_PATH),
        help="the path to directory with Selenium drivers"
    )
    parser.addoption(
        "--headless",
        type=bool,
        default=DEFAULT_HEADLESS_MODE,
        help="headless mode, bool type. Default False.")
    parser.addoption(
        "--executor",
        default=DEFAULT_EXECUTOR
    )
    parser.addoption(
        "--browser_version",
        default=DEFAULT_SELENOID_BROWSER_VERSION
    )


@pytest.fixture()
def driver(request) -> WebDriver:
    browser = request.config.getoption("--browser")
    drivers_path = request.config.getoption("--drivers")
    base_url = request.config.getoption("--url")
    headless_mode = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--browser_version")

    if executor == "local":
        if browser == "chrome":
            service = ChromeService(executable_path=drivers_path + "chromedriver")
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.headless = True
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            service = FirefoxService(executable_path=drivers_path + "geckodriver")
            options = webdriver.FirefoxOptions()
            if headless_mode:
                options.headless = True
            driver = webdriver.Firefox(service=service, options=options)
        elif browser == "opera":
            service = ChromeService(executable_path=drivers_path + "operadriver")
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.headless = True
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Browser {browser} is not supported.")
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "browserVersion": browser_version,
            "name": "gulf98",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False,
                "enableLog": True
            },
            "acceptSslCerts": True,
            "acceptInsecureCerts": True,
            "timeZone": "Europe/Moscow"
        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=capabilities
        )

    request.addfinalizer(driver.close)

    driver.log_level = DEFAULT_LOGGING_LEVEL
    driver.test_name = request.node.name

    driver.maximize_window()
    driver.base_url = base_url

    return driver
