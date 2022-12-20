from page_objects.store.pages.base_page import BasePage


class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
