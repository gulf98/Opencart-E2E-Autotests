import allure
import pytest

from page_objects.store.pages.main_page import MainPage


@pytest.mark.regression
@allure.title("Currency change test")
@pytest.mark.parametrize("currency", ["$", "€", "£"])
def test_switch_currency(driver, currency):
    main_page = MainPage(driver) \
        .open_page() \
        .open_currency_dropdown() \
        .select_currency_by_symbol(currency)
    assert main_page.is_present_currency(currency)
    assert main_page.get_visible_current_currency() == currency
    assert main_page.product_card_list.get_product_price_by_index(0).find(currency) >= 0
