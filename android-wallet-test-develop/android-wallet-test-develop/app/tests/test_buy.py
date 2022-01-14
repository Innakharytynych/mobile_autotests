from app.pages.buy_page import BuyScreen, Locators
from app.config.config import TestData
import pytest


@pytest.mark.usefixtures('init_driver')
class TestBuy:

    '''Проверить экран'''
    def test_buy_screen(self):
        buy_screen = BuyScreen(self.driver)
        buy_screen.login_without_onboard()
        buy_screen.tap(Locators.BTN_BUY)
        buy_screen.tap(Locators.BTN_SHOW_HISTORY)

        assert buy_screen.is_visible(Locators.BLOCK_TOKEN)
        assert buy_screen.is_visible(Locators.TOKEN_NAME_USD)
        assert buy_screen.is_visible(Locators.BTN_IN_ORDERS)
        assert buy_screen.is_enable_to_tap(Locators.BTN_SHOW_HISTORY)
        assert buy_screen.is_enable_to_tap(Locators.BTN_BANK_CARD)
        '''assert buy_screen.is_visible(Locators.DEAL_NUMBER)
        assert buy_screen.is_visible(Locators.DEAL_SUMM)
        assert buy_screen.is_visible(Locators.DEAL_DATE)
        assert buy_screen.is_visible(Locators.DEAL_SELLER)
        assert buy_screen.is_visible(Locators.DEAL_SELLER_NAME)
        assert buy_screen.is_visible(Locators.DEAL_STATUS)
        assert buy_screen.is_enable_to_tap(Locators.DEAL_COPY)
        assert buy_screen.is_enable_to_tap(Locators.DEAL_CHAT)
        assert buy_screen.is_visible(Locators.DEAL_WATCH)
        assert buy_screen.is_visible(Locators.DEAL_TIMER)'''
        assert buy_screen.is_visible(Locators.MY_ODRERS)
        assert buy_screen.is_visible(Locators.ALL_ORDERS)
        assert buy_screen.is_enable_to_tap(Locators.BTN_CREATE_ORDER)
        assert buy_screen.is_visible(Locators.TEXT_NO_ACTIVE_ORDERS)

    '''Создать заявку на покупку'''
    def test_buy_order(self):
        buy_screen = BuyScreen(self.driver)
        buy_screen.login_without_onboard()
        buy_screen.tap(Locators.BTN_BUY)
        buy_screen.tap(Locators.BTN_CREATE_ORDER)
        buy_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_COUNTRY, TestData.COUNTRY)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_BANK, TestData.BANK)
        buy_screen.tap(Locators.BTN_CREATE_BUY_ORDER)
        buy_screen.tap(Locators.BTN_CONFIRM_ORDER)
        '''pop_up_1 = buy_screen.conver_in_num(Locators.POPUP_BUY_ALL)
        pop_up_2 = buy_screen.conver_in_num(Locators.POPUP_BUY_DEPOSIT)
        pop_up_3 = buy_screen.conver_in_num(Locators.POPUP_BUY_COMISSION)
        pars_1 = buy_screen.parser_quantity_from_you(buy_screen.get_text2(Locators.MY_BUY_ORDER_ID))
        pars_2 = buy_screen.parser_quantity_to_you(buy_screen.get_text2(Locators.MY_BUY_ORDER_ID))

        assert pop_up_1 == buy_screen.conver_in_num(pars_1)
        assert pop_up_2 == buy_screen.conver_in_num(pars_2)'''

        assert buy_screen.is_enable_to_tap(Locators.BTN_IN_ORDERS)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_TRANS)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_ID)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_TYPE)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_AVALIABLE_STATUS)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_AVALIABLE_SUMM)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_RATE)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_COUNTRY)
        assert buy_screen.is_visible(Locators.MY_BUY_ORDER_BANK)
        assert buy_screen.is_enable_to_tap(Locators.MY_BUY_ODRER_CANCEL)
        assert buy_screen.is_enable_to_tap(Locators.MY_BUY_ODRER_PAUSE)

    '''Ввесит большую сумму, чем есть на балансе'''
    def test_buy_order_max(self):
        buy_screen = BuyScreen(self.driver)
        buy_screen.login_without_onboard()
        buy_screen.tap(Locators.BTN_BUY)
        buy_screen.tap(Locators.BTN_CREATE_ORDER)
        buy_screen.send_keys(Locators.FIELD_AMOUNT, TestData.MAX_BUY_AMOUNT)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_COUNTRY, TestData.COUNTRY)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_BANK, TestData.BANK)
        buy_screen.tap(Locators.BTN_CREATE_BUY_ORDER)

        assert buy_screen.is_visible(Locators.TEXT_INSUFFICIENT_BALANCE)
        assert buy_screen.is_disable_to_tap(Locators.BTN_CREATE_BUY_ORDER)

    '''Ввести сумму меньше 0,01'''
    def test_buy_order_min(self):
        buy_screen = BuyScreen(self.driver)
        buy_screen.login_without_onboard()
        buy_screen.tap(Locators.BTN_BUY)
        buy_screen.tap(Locators.BTN_CREATE_ORDER)
        buy_screen.send_keys(Locators.FIELD_AMOUNT, TestData.MIN_BUY_AMOUNT)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_COUNTRY, TestData.COUNTRY)
        buy_screen.tap(Locators.TEXT_RATE)
        buy_screen.send_keys(Locators.FIELD_BANK, TestData.BANK)
        buy_screen.tap(Locators.BTN_CREATE_BUY_ORDER)

        assert buy_screen.is_disable_to_tap(Locators.BTN_CREATE_BUY_ORDER)
