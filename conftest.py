import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--base_url", action="store", default="http://192.168.0.105:8081")
    parser.addoption("--drivers_path", action="store", default=os.path.expanduser("~/selenium_drivers"))
    parser.addoption("--headless_mode", action="store_true")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    drivers_path = request.config.getoption("--drivers_path")
    headless_mode = request.config.getoption("--headless_mode")

    if browser == "chrome":
        service = ChromeService(executable_path=drivers_path + "/chromedriver")
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.headless = True
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = FirefoxService(executable_path=drivers_path + "/geckodriver")
        options = webdriver.FirefoxOptions()
        if headless_mode:
            options.headless = True
        _driver = webdriver.Firefox(service=service, options=options)
    elif browser == "opera":
        service = ChromeService(executable_path=drivers_path + "/chromedriver")
        options = webdriver.ChromeOptions()
        if headless_mode:
            options.headless = True
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser == "safari":
        _driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    request.addfinalizer(_driver.close)

    _driver.maximize_window()
    _driver.base_url = base_url

    return _driver
