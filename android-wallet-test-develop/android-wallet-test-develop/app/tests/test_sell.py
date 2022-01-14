from app.pages.sell_page import SellScreen, Locators
from app.config.config import TestData
import pytest


@pytest.mark.usefixtures('init_driver')
class TestSell:

    '''ВЫВОД НА КАРТУ
    проверить экран'''
    def test_sell_screen(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)

        assert sell_screen.is_visible(Locators.BLOCK_TOKEN)
        assert sell_screen.is_visible(Locators.TOKEN_NAME_USD)
        assert sell_screen.is_visible(Locators.BTN_IN_ORDERS)
        assert sell_screen.is_enable_to_tap(Locators.BTN_SHOW_HISTORY)
        assert sell_screen.is_enable_to_tap(Locators.BTN_BANK_CARD)
        '''assert sell_screen.is_visible(Locators.DEAL_NUMBER)
        assert sell_screen.is_visible(Locators.DEAL_SUMM)
        assert sell_screen.is_visible(Locators.DEAL_DATE)
        assert sell_screen.is_visible(Locators.DEAL_BYER)
        assert sell_screen.is_visible(Locators.DEAL_BYER_NAME)
        assert sell_screen.is_visible(Locators.DEAL_STATUS)
        assert sell_screen.is_enable_to_tap(Locators.DEAL_COPY)
        assert sell_screen.is_enable_to_tap(Locators.DEAL_CHAT)
        assert sell_screen.is_visible(Locators.DEAL_WATCH)
        assert sell_screen.is_visible(Locators.DEAL_TIMER)'''
        assert sell_screen.is_visible(Locators.MY_ODRERS)
        assert sell_screen.is_visible(Locators.ALL_ORDERS)
        assert sell_screen.is_enable_to_tap(Locators.BTN_CREATE_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_NO_ACTIVE_ORDERS)
        assert sell_screen.is_visible(Locators.IMAGE_NO_ACTIVE_ORDERS)

    '''Создать заявку на продажу на карту'''
    def test_new_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators. BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)
        sell_screen.tap (Locators.BTN_CONFIRM_SELL_ORDER)

        '''assert TestData.SELL_AMOUNT == sell_screen.get_text2(Locators.MY_SELL_ODRER_AVALIABLE)'''
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_TRANS)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_TYPE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_ID)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_MY)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_AVALIABLE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_RATE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_CARD)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_BANK)
        assert sell_screen.is_enable_to_tap(Locators.MY_SELL_ODRER_CANCEL)
        assert sell_screen.is_enable_to_tap(Locators.MY_SELL_ODRER_PAUSE)

    '''Создать заявку на продажу на карту большей суммы, чем есть на балансе'''
    def test_new_big_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.MAX_SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_INSUFFICIENT_BALANCE)

    '''Создать заявку на продажу на карту меньше минимальной допустимой суммы 0.01'''
    def test_new_small_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.MIN_SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на продажу на карту,ввести сумму, изменить токен'''
    def test_change_token_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BLOCK_TOKEN)
        sell_screen.tap(Locators.TOKEN_NAME_UA_POPUP)

        assert sell_screen.is_visible(Locators.BLOCK_TOKEN)
        assert sell_screen.is_visible(Locators.TOKEN_NAME_UA)
        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)
        '''assert sell_screen.clear(Locators.FIELD_AMOUNT)'''

    '''Создать заявку на продажу на карту,ввести сумму, попробовать изменить аккаунт'''
    def test_change_name_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_AKK_NAME)

        assert sell_screen.is_disable_to_tap(Locators.BTN_AKK_NAME)

    '''Создать заявку на продажу, удалить минимальную сумму, попробовать создать заявку'''
    def test_del_min_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MIN_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на продажу, удалить максимальную сумму, попробовать создать заявку'''
    def test_del_max_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MAX_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на продажу, не заполнять поля, попробовать создать заявку'''
    def test_clear_field_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на продажу, удалить минимальную сумму, ввести большее значение, попробовать создать заявку'''
    def test_del_min_max_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MIN_AMOUNT)
        sell_screen.send_keys(Locators.FIELD_MIN_AMOUNT, TestData.MAX_SELL_LIMIT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_LIMIT)

    '''Создать заявку на продажу, удалить минимальную сумму, ввести меньшее значение, попробовать создать заявку'''
    def test_del_min_min_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MIN_AMOUNT)
        sell_screen.send_keys(Locators.FIELD_MIN_AMOUNT, TestData.MIN_SELL_LIMIT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)
        sell_screen.tap(Locators.BTN_CONFIRM_SELL_ORDER)

        '''assert TestData.SELL_AMOUNT == sell_screen.get_text2(Locators.MY_SELL_ODRER_AVALIABLE)'''
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_TRANS)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_TYPE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_ID)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_MY)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_AVALIABLE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_RATE)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_CARD)
        assert sell_screen.is_visible(Locators.MY_SELL_ODRER_BANK)
        assert sell_screen.is_enable_to_tap(Locators.MY_SELL_ODRER_CANCEL)
        assert sell_screen.is_enable_to_tap(Locators.MY_SELL_ODRER_PAUSE)

    '''Создать заявку на продажу, удалить максимальную сумму, ввести большее значение, попробовать создать заявку'''
    def test_del_max_max_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MAX_AMOUNT)
        sell_screen.send_keys(Locators.FIELD_MAX_AMOUNT, TestData.MAX_SELL_LIMIT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_LIMIT)

    '''Создать заявку на продажу, удалить максимальную сумму, ввести меньшее значение, чем введенная сумма, попробовать создать заявку'''
    def test_del_max_min_sell_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_CARD)
        sell_screen.tap(Locators.BTN_ADD_CARD)
        sell_screen.send_keys(Locators.FIELD_CARD_NUMBER, TestData.CARD_NUMBER1)
        sell_screen.tap(Locators.CARD_DETAILS)
        sell_screen.tap(Locators.BTN_SAVE_CARD)
        sell_screen.tap(Locators.BTN_LEFT_BUTTON)
        sell_screen.send_keys(Locators.FIELD_AMOUNT, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.clear(Locators.FIELD_MAX_AMOUNT)
        sell_screen.send_keys(Locators.FIELD_MAX_AMOUNT, TestData.MIN_SELL_LIMIT)
        sell_screen.tap(Locators.TEXT_BALANCE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_LIMIT_MIN)

    '''ОПЛАТА СЧЕТА'''
    '''Проверить экран'''
    def test_pay_invoice_screen(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_PAY_INVOICE)

        assert sell_screen.is_visible(Locators.FIELD_LINK)
        assert sell_screen.is_enable_to_tap(Locators.BTN_QR)
        assert sell_screen.is_visible(Locators.FIELD_AMOUNT_LINK)
        assert sell_screen.is_visible(Locators.FIELD_COUNTRY_LINK)
        assert sell_screen.is_visible(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на оплату счета'''
    def test_pay_invoice_order(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_PAY_INVOICE)
        sell_screen.send_keys(Locators.FIELD_LINK, TestData.LINK)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.send_keys(Locators.FIELD_AMOUNT_LINK, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.send_keys(Locators.FIELD_COUNTRY_LINK, TestData.COUNTRY)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)
        sell_screen.tap(Locators.BTN_CONFIRM_SELL_ORDER)

        assert sell_screen.is_visible(Locators.BLOCK_TOKEN)
        assert sell_screen.is_visible(Locators.TOKEN_NAME_USD)
        assert sell_screen.is_visible(Locators.BTN_IN_ORDERS)
        assert sell_screen.is_enable_to_tap(Locators.BTN_SHOW_HISTORY)
        assert sell_screen.is_enable_to_tap(Locators.BTN_BANK_CARD)
        '''assert sell_screen.is_visible(Locators.DEAL_NUMBER)
        assert sell_screen.is_visible(Locators.DEAL_SUMM)
        assert sell_screen.is_visible(Locators.DEAL_DATE)
        assert sell_screen.is_visible(Locators.DEAL_BYER)
        assert sell_screen.is_visible(Locators.DEAL_BYER_NAME)
        assert sell_screen.is_visible(Locators.DEAL_STATUS)
        assert sell_screen.is_enable_to_tap(Locators.DEAL_COPY)
        assert sell_screen.is_enable_to_tap(Locators.DEAL_CHAT)
        assert sell_screen.is_visible(Locators.DEAL_WATCH)
        assert sell_screen.is_visible(Locators.DEAL_TIMER)'''
        assert sell_screen.is_visible(Locators.MY_ODRERS)
        assert sell_screen.is_visible(Locators.ALL_ORDERS)
        assert sell_screen.is_enable_to_tap(Locators.BTN_CREATE_ORDER)
        assert sell_screen.is_visible(Locators.TEXT_NO_ACTIVE_ORDERS)
        assert sell_screen.is_visible(Locators.IMAGE_NO_ACTIVE_ORDERS)

    '''Создать заявку на оплату счета, не указав страну'''
    def test_pay_invoice_order_without_country(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_PAY_INVOICE)
        sell_screen.send_keys(Locators.FIELD_LINK, TestData.LINK)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.send_keys(Locators.FIELD_AMOUNT_LINK, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на оплату счета, не указав cумму'''
    def test_pay_invoice_order_without_amount(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_PAY_INVOICE)
        sell_screen.send_keys(Locators.FIELD_LINK, TestData.LINK)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.send_keys(Locators.FIELD_AMOUNT_LINK, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)

    '''Создать заявку на оплату счета, не указав ссылку'''
    def test_pay_invoice_order_without_link(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        sell_screen.tap(Locators.BTN_CREATE_ORDER)
        sell_screen.tap(Locators.BTN_PAY_INVOICE)
        sell_screen.send_keys(Locators.FIELD_AMOUNT_LINK, TestData.SELL_AMOUNT)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.send_keys(Locators.FIELD_COUNTRY_LINK, TestData.COUNTRY)
        sell_screen.tap(Locators.TEXT_RATE)
        sell_screen.tap(Locators.BTN_NEW_SELL_ORDER)

        assert sell_screen.is_disable_to_tap(Locators.BTN_NEW_SELL_ORDER)


    '''Отобразить историю сделок
    def test_show_deals(self):
        sell_screen = SellScreen(self.driver)
        sell_screen.login_without_onboard()
        sell_screen.tap(Locators.BTN_SELL)
        if sell_screen.is_visible(Locators.BTN_SHOW_HISTORY):
            sell_screen.tap(Locators.BTN_SHOW_HISTORY)'''