from page_objects.base_page_object import BasePageObject


class AccountPage(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
