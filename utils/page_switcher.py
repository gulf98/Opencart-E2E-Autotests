from page_objects.base_page_object import BasePageObject
from page_objects.store.pages.login_page import LoginPage as StoreLoginPage
from page_objects.store.pages.main_page import MainPage
from page_objects.store.pages.register_page import RegisterPage
from page_objects.admin_panel.login_page import LoginPage as AdminPanelLoginPage


class PageSwitcher:
    MAIN_PAGE_URL = ""
    STORE_LOGIN_PAGE_URL = "/index.php?route=account/login"
    STORE_REGISTER_PAGE_URL = "/index.php?route=account/register"
    ADMIN_PANEL_LOGIN_PAGE_URL = "/admin"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url_path):
        self.driver.get(self.driver.base_url + url_path)

    def open_store_main_page(self):
        self.open_page(self.MAIN_PAGE_URL)
        return MainPage(self.driver)

    def open_store_login_page(self):
        self.open_page(self.STORE_LOGIN_PAGE_URL)
        return StoreLoginPage(self.driver)

    def open_store_register_page(self):
        self.open_page(self.STORE_REGISTER_PAGE_URL)
        return RegisterPage(self.driver)

    def open_admin_panel_login_page(self):
        self.open_page(self.ADMIN_PANEL_LOGIN_PAGE_URL)
        return AdminPanelLoginPage(self.driver)
