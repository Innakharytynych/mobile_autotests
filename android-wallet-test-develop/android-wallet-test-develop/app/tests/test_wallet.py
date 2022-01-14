from app.pages.wallet_page import WalletScreen, Locators
from app.config.config import TestData
import pytest
import requests

@pytest.mark.usefixtures('init_driver')
class TestWallet:

    '''Проверка элементов главного экрана'''
    def test_check_wallet_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()

        assert wallet_screen.is_visible(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SKAN_QR)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Закрыть пригласить друга'''
    def test_close_invite_friend(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_INVITE_FRIEND_CLOSE)

        assert wallet_screen.is_invisible(Locators.BTN_INVITE_FRIEND)
        assert wallet_screen.is_invisible(Locators.BTN_INVITE_FRIEND_QR)

    '''Открыть пригласить друга'''
    def test_open_invite_friend(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_INVITE_FRIEND)

        assert wallet_screen.is_visible(Locators.QR_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.LINK_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.SHARE_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.COPY_INVITE_FRIEND)

    '''Добавить токен'''
    def test_add_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_ADD_TOKEN)
        if wallet_screen.is_visible(Locators.SCREEN_ADD_TOKEN):
            wallet_screen.tap(Locators.BTN_TOKEN)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TOKEN_ADDED)

    '''Проверка, что добавленный токен отобразился в списке активных'''
    def test_add_token_is_visible(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_ADD_TOKEN)
        if wallet_screen.is_visible(Locators.SCREEN_ADD_TOKEN):
            wallet_screen.tap(Locators.BTN_TOKEN_EURCASH)
        wallet_screen.tap(Locators.BTN_LEFT_BUTTON)

        assert wallet_screen.is_visible(Locators.TOKEN_NAME_MAIN_PAGE_EURCASH)

    '''Добавить уже добавленный токен'''
    def test_add_added_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_ADD_TOKEN)
        if wallet_screen.is_visible(Locators.SCREEN_ADD_TOKEN):
            wallet_screen.tap(Locators.BTN_TOKEN)
        wallet_screen.tap(Locators.BTN_TOKEN_ADDED)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TOKEN_ADDED)

    '''Отмена добавления токена. Возврат на главный экран'''
    def test_cancel_add_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_ADD_TOKEN)
        wallet_screen.tap(Locators.BTN_LEFT_BUTTON)

        assert wallet_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SKAN_QR)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''скрыть токен с ненулевым балансом из списка кошелька'''
    def test_delete_token_with_notnull_balance(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.swipe_element_right_to_left(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)

        assert wallet_screen.is_invisible(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)
        assert wallet_screen.is_disable_to_tap(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)

    '''скрыть токен с нулевым балансом из списка кошелька'''
    def test_delete_token_with_null_balance(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.swipe_element_right_to_left(Locators.TEXT_NULL_BALANCE)

        assert wallet_screen.is_invisible(Locators.TEXT_NULL_BALANCE)

    '''скрыть токен и повторно добавить его с ненулевым балансом'''
    def test_delete_add_token_with_notnull_balance(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.swipe_element_right_to_left(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)
        wallet_screen.tap(Locators.BTN_ADD_TOKEN)
        wallet_screen.tap(Locators.BLOCK_RUBCASH)
        wallet_screen.tap(Locators.BTN_LEFT_BUTTON)

        assert wallet_screen.is_visible(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)

'''Сменить прод на препрод
    def test_change_prod_preprod(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.login_and_preprod_2()

        assert wallet_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SKAN_QR)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BUY)'''

'''Сменить препрод на прод
    def test_change_preprod_prod(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.login_and_prod()

        assert wallet_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SKAN_QR)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BUY)'''