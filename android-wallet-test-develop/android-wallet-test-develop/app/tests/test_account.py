'необходимо обновить, вход без онбординга сейчас'
from app.pages.wallet_page import WalletScreen, Locators
from app.config.config import TestData
import pytest
import requests

@pytest.mark.usefixtures('init_driver')
class TestAccount:

    '''логин fletchercat1, проверка элементов главного экрана'''
    def test_check_account_screen(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_without_onboard()

        assert account_screen.get_text(Locators.TEXT_AKK_NAME, 'fletchercat1')
        assert account_screen.is_visible(Locators.SCREEN_MY_WALLET)
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert account_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert account_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert account_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert account_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert account_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert account_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert account_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert account_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Добавить аккаунт'''
    def test_add_akk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_ADD_MORE_ACC)
        account_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        account_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        account_screen.tap(Locators.BTN_ADD_ACC)

        assert account_screen.get_text(Locators.TEXT_AKK_NAME, '333334.pcash')
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert account_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert account_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert account_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert account_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert account_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert account_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert account_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert account_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert account_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Показать приватный ключ'''
    def test_show_pk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_SHOW_PK)
        account_screen.tap_null_4_times()

        assert account_screen.is_visible(Locators.POKAZ_PK_POPUP)
        assert account_screen.is_enable_to_tap(Locators.COPY_PK_POPUP)

    '''Сменить аккаунт'''
    def test_change_akk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.open_app()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_ADD_MORE_ACC)
        account_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        account_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        account_screen.tap(Locators.TEXT_WARNING)
        account_screen.tap(Locators.BTN_ADD_ACC)
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_CHANGE_AKK1)

        assert account_screen.get_text(Locators.TEXT_AKK_NAME, '521115.pcash')
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert account_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert account_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert account_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert account_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert account_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert account_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert account_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert account_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert account_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Сменить аккаунт с первого на второй и повторно со второго на первый'''
    def test_change2_akk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_ADD_MORE_ACC)
        account_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        account_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        account_screen.tap(Locators.BTN_ADD_ACC)
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_CHANGE_AKK1)
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_CHANGE_AKK2)

        assert account_screen.get_text(Locators.TEXT_AKK_NAME, '333334.pcash')
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert account_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert account_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert account_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert account_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert account_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert account_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert account_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert account_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert account_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Удалить единственный аккаунт'''
    def test_dell_one_akk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_DELETE)
        account_screen.tap(Locators.BTN_REMOVE)
        account_screen.tap_null_4_times()

        assert account_screen.is_visible(Locators.SCREEN_WELCOME)
        assert account_screen.is_enable_to_tap(Locators.BTN_ENTER_PK)
        assert account_screen.is_enable_to_tap(Locators.BTN_CREATE_WALLET)

    '''Удалить аккаунт, если есть не один аккаунт'''
    def test_dell_more_akk(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_ADD_MORE_ACC)
        account_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        account_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        account_screen.tap(Locators.BTN_ADD_ACC)
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_DELETE)
        account_screen.tap(Locators.BTN_REMOVE)
        account_screen.tap_null_4_times()

        assert account_screen.get_text(Locators.TEXT_AKK_NAME, 'avpw.pcash')
        assert account_screen.is_visible(Locators.SCREEN_MY_WALLET)
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert account_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert account_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert account_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert account_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert account_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert account_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert account_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert account_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert account_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert account_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert account_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Попробовать удалить аккаунт, если пин-код не корректный 5 раз'''
    def test_dell_akk_incorrect_pin(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_DELETE)
        account_screen.tap(Locators.BTN_REMOVE)

        for i in range(6):
            account_screen.tap_one_4_times()

        assert account_screen.is_enable_to_tap(Locators.BTN_UNDESTAND)
        assert account_screen.is_visible(Locators.PICTURE_WRONG_PIN)

    '''Отменить удаление аккаунта'''
    def test_dell_akk_cancel_remove_acc(self):
        account_screen = WalletScreen(self.driver)
        account_screen.login_by_privat_key()
        account_screen.tap(Locators.BTN_AKK_NAME)
        account_screen.tap(Locators.BTN_DELETE)
        account_screen.tap(Locators.BTN_REMOVE_CANCEL)

        assert account_screen.is_enable_to_tap(Locators.BTN_SHOW_PK)
        assert account_screen.is_enable_to_tap(Locators.BTN_DELETE)
        assert account_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_ACC)
