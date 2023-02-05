import allure
import pytest

from utils.types import Currency
from utils.page_switcher import PageSwitcher
from page_objects.store.dropdowns.currency_dropdown import CurrencyLocators


@pytest.mark.regression
@allure.title("Currency change test")
@pytest.mark.parametrize("currency_locators, expected_currency", list(zip(list(CurrencyLocators), list(Currency))))
def test_switch_currency(driver, currency_locators, expected_currency):
    main_page = PageSwitcher(driver).open_store_main_page() \
        .open_currency_dropdown() \
        .select_currency(currency_locators)
    assert main_page.is_present_currency(expected_currency.value)
    assert main_page.get_visible_current_currency() == expected_currency.value
    assert main_page.product_card_list.get_product_price_by_index(0).find(expected_currency.value) >= 0
