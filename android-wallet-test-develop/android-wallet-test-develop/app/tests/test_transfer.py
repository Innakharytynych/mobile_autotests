from app.pages.wallet_page import WalletScreen, Locators
from app.config.config import TestData
import pytest
import requests


@pytest.mark.usefixtures('init_driver')
class TestTransfer:
    '''ИСТОРИЯ ПО ТОКЕНУ. Проверить историю по токену'''
    def test_history_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)

        assert wallet_screen.is_visible(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_visible(Locators.HISTORY_TOKEN)
        assert wallet_screen.is_visible(Locators.DETAIL_TOKEN_NAME_TITLE)
        assert wallet_screen.is_visible(Locators.DETAIL_TOKEN_BALLANCE)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_WITHDRAW)
        assert wallet_screen.is_visible(Locators.DATE_TRANSACTIONS)
        assert wallet_screen.is_enable_to_tap(Locators.COUNT_TRANSACTION)
        assert wallet_screen.is_enable_to_tap(Locators.TEXT_ACTION_NAME)
        assert wallet_screen.is_visible(Locators.TEXT_ACTION_TIME)

    '''Проверить детали транзакции'''
    def test_history_transaction(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.COUNT_TRANSACTION)

        assert wallet_screen.is_visible(Locators.DETAIL_TRANSACTION_POPUP)
        assert wallet_screen.is_visible(Locators.DETAIL_TRANSACTION_POPUP_SUM)
        assert wallet_screen.is_visible(Locators.DETAIL_TRANSACTION_POPUP_RECEIVER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_COPY_ID)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_COPY_RECEIVER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_COPY_MEMO)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_TRANSFER)

    '''Смена аккаунта из истории операций по токену'''
    def test_change_acc_from_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.COUNT_TRANSACTION)
        wallet_screen.tap(Locators.TEXT_AKK_NAME)

        assert wallet_screen.is_disable_to_tap(Locators.TEXT_AKK_NAME)
        assert wallet_screen.is_visible(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_visible(Locators.HISTORY_TOKEN)
        assert wallet_screen.is_visible(Locators.DETAIL_TOKEN_NAME_TITLE)
        assert wallet_screen.is_visible(Locators.DETAIL_TOKEN_BALLANCE)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.DETAIL_TOKEN_WITHDRAW)
        assert wallet_screen.is_visible(Locators.DATE_TRANSACTIONS)
        assert wallet_screen.is_enable_to_tap(Locators.COUNT_TRANSACTION)
        assert wallet_screen.is_enable_to_tap(Locators.TEXT_ACTION_NAME)
        assert wallet_screen.is_visible(Locators.TEXT_ACTION_TIME)

    '''Возврат на главный экран'''
    def test_back_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.COUNT_TRANSACTION)
        wallet_screen.tap(Locators.BTN_LEFT_BACK)

        assert wallet_screen.is_visible(Locators.TEXT_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_ADD_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SETTINGS)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_INVITE_FRIEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SEND)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_RECEIVE)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SWAP)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_WITHDRAW)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_BUY)

    '''Проверка наличия элементов экрана трансфер в истории'''
    def test_transfer_check_screen_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)

        assert wallet_screen.is_visible(Locators.TEXT_TOKEN_NAME_UAHCASH)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM_TOTAL)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''трансфер CASH из истории по токену'''
    def test_transfer_CASH_from_history_wallet_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER,  TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''трансфер EOS из истории по токену'''
    def test_transfer_EOS_from_history_wallet_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO,  TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'EOS'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Повторный трансфер из истории по токену'''
    def test_repeat_transfer(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        if wallet_screen.is_visible(Locators.TEXT_TRANSFER_COMMISSION):
            wallet_screen.tap(Locators.TEXT_TRANSFER_COMMISSION)
        wallet_screen.tap(Locators.BTN_TRANSACTION_REPEAT)
        wallet_screen.tap(Locators.BTN_REPEAT_SEND)

        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Проверка ограничения максимальной коммиссии 250 токенов из истории'''
    def test_transfer_CASH_from_history_250_commission(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER,  TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_250_COMMISSION)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        commission = wallet_screen.conver_in_num(Locators.TEXT_POPUP_COMMISSION)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert commission == wallet_screen.conver_in_num(TestData.MAX_COMMISSION)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Попытка перевода большей суммы из истории, чем есть на счету'''
    def test_transfer_more_token_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO,  TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы из истории CASH чем 0.00001'''
    def test_transfer_CASH_min_from_main_screen_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_CASH)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO,  TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы LQ чем 1.0000 из истории'''
    def test_transfer_LQ_min_min_from_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_LQC)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_LQ)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы EOS чем 0.00001 из истории'''
    def test_transfer_EOS_min_min_from_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_EOS)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода 0'''
    def test_transfer_CASH_zero_from_main_screen_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, '0')
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода большей суммы из истории, чем есть на счету, удаление и корректный ввод суммы'''
    def test_transfer_more_normal_token_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Удаление общей суммы из истории'''
    def test_transfer_delete_total_sum_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.FIELD_SUMM_TOTAL)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Ввод некорректного имени'''
    def test_transfer_incorrect_name_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.NAME_INCORRECT)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR_NAME)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Ввод не корректного имени, удаление, ввод корректного имени'''
    def test_transfer_incorrect_name_correct_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.NAME_INCORRECT)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Ввод первого корректного имени, удаление ввод второго корректного имени'''
    def test_transfer_correct_name_correct_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER2)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Пропустить ввод МЕМО'''
    def test_transfer_CASH_from_history_wallet_screen_without_memo(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER,  TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Пропустить ввод имени'''
    def test_transfer_without_name_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Изменить аккаунт'''
    def test_transfer_without_name_history_change_account(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_AKK_NAME)

        assert wallet_screen.is_disable_to_tap(Locators.TEXT_AKK_NAME)

    '''Изменить токен'''
    def test_transfer_without_name_history_change_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER,  TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TOKEN_CHANGE)
        wallet_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'RUBCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Корректный QR код выбран из галереи. Предварительно в настройках телефона проверить доступ до галереи'''
    def test_transfer_qr_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Не корректный QR код выбран из галереи'''
    def test_transfer_qr_incorrect_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR_INCORRECT)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TEXT_TOKEN_NAME_UAHCASH)
        assert wallet_screen.is_visible(Locators.TEXT_ERROR)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Корректный QR код выбран из галереи на большую сумму, чем есть на счету и изменение токена. В истории был UAHCASH, код для RUBCASH'''
    def test_transfer_qr_big_money_history_change_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR_BIG)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TOKEN_NAME_RUBCASH)
        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Корректный QR код выбран из галереи на большую сумму, чем есть на счету без изменения токена. В истории был RUBCASH, код для RUBCASH'''
    def test_transfer_qr_big_money_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TOKEN_NAME_MAIN_PAGE_RUBCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR_BIG)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TOKEN_NAME_RUBCASH)
        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Отмена выбора кода, возврат'''
    def test_transfer_qr_back_history(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.open_app()
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.DETAIL_TOKEN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_BACK_APP)
        wallet_screen.tap(Locators.BTN_BACK_APP)

        assert wallet_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)


    '''ГЛАВНЫЙ ЭКРАН'''
    '''Проверка наличия элементов экрана трансфер'''
    def test_transfer_check_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)

        assert wallet_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Трансфер CASH из главного экрана'''
    def test_transfer_CASH_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''трансфер EOS из главного экрана'''
    def test_transfer_EOS_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'EOS'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Проверка ограничения максимальной коммиссии 250 токенов из истории'''
    def test_transfer_250_commission(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_250_COMMISSION)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        commission = wallet_screen.conver_in_num(Locators.TEXT_POPUP_COMMISSION)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert commission == wallet_screen.conver_in_num(TestData.MAX_COMMISSION)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)


    '''Смена токена в трансфере'''
    def test_transfer_change_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Попытка перевода большей суммы, чем есть на счету'''
    def test_transfer_more_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)

    '''Попытка перевода меньшей суммы CASH чем 0.00001 из главного экрана'''
    def test_transfer_CASH_min_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_CASH)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы LQ чем 1.0000 из главного экрана'''
    def test_transfer_LQ_min_min_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_LQC)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_LQ)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы EOS чем 0.00001 из главного экрана'''
    def test_transfer_EOS_min_min_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TEXT_TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_EOS)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода 0 из главного экрана'''
    def test_transfer_CASH_zero_from_main_screen(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, '0')
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода большей суммы, чем есть на счету, удаление и корректный ввод суммы'''
    def test_transfer_more_normal_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Удаление общей суммы'''
    def test_transfer_delete_total_sum(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.FIELD_SUMM_TOTAL)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Ввод некорректного имени'''
    def test_transfer_incorrect_name(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, 'hgjhjkhjkjk')
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR_NAME)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''ввод не корректного имени, удадение ввод корректного имени'''
    def test_transfer_incorrect_name_correct(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, 'hjghjhgjghj')
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Ввод первого корректного имени, удадение ввод второго корректного имени'''
    def test_transfer_correct_name_correct(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER2)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.tap(Locators.BTN_DELETE_ICON)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.FIELD_MEMO)
        wallet_screen.send_keys(wallet_screen.FIELD_MEMO, TestData.MEMO)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Пропустить ввод имени'''
    def test_transfer_without_name(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Смена аккаунта с экрана трансфера после ввода данных'''
    def test_transfer_change_name(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_EOS)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.TEXT_AKK_NAME)

        assert wallet_screen.is_disable_to_tap(Locators.TEXT_AKK_NAME)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_TRANSFER)

    '''Смена аккаунта с экрана трансфера до ввода данных'''
    def test_transfer_change_name2(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.TEXT_AKK_NAME)

        assert wallet_screen.is_disable_to_tap(Locators.TEXT_AKK_NAME)

    '''Пропуск ввода мемо'''
    def test_transfer_from_main_screen_without_memo(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.CHOOSE_TOKEN)
        wallet_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == wallet_screen.conver_in_num(
            TestData.SUM_TRANSFER)
        assert wallet_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Пропуск выбора токена'''
    def test_transfer_from_main_screen_without_token(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.FIELD_RECEIVER)
        wallet_screen.send_keys(wallet_screen.FIELD_RECEIVER, TestData.RECEIVER)
        wallet_screen.tap(Locators.FIELD_SUMM)
        wallet_screen.send_keys(wallet_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Корректный QR код выбран из галереи. Предварительно в настройках телефона проверить доступ до галереи'''
    def test_transfer_qr(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)
        wallet_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert wallet_screen.is_visible(Locators.POPUP_DETAIL_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert wallet_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert wallet_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Не корректный QR код выбран из галереи'''
    def test_transfer_qr_incorrect(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR_INCORRECT)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert wallet_screen.is_visible(Locators.TEXT_ERROR)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Корректный QR код выбран из галереи на большую сумму, чем есть на счету'''
    def test_transfer_qr_big_money(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_QR_BIG)
        wallet_screen.tap(Locators.TEXT_YOU_SEND)
        wallet_screen.tap(Locators.BTN_TRANSFER)

        assert wallet_screen.is_visible(Locators.TOKEN_NAME_RUBCASH)
        assert wallet_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Отмена выбора кода, возврат'''
    def test_transfer_qr_back(self):
        wallet_screen = WalletScreen(self.driver)
        wallet_screen.open_app()
        wallet_screen.tap(Locators.BTN_SEND)
        wallet_screen.tap(Locators.BTN_QR)
        wallet_screen.tap(Locators.BTN_QR_GALLERY)
        wallet_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        wallet_screen.tap(Locators.BTN_BACK_APP)
        wallet_screen.tap(Locators.BTN_BACK_APP)

        assert wallet_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert wallet_screen.is_visible(Locators.FIELD_RECEIVER)
        assert wallet_screen.is_visible(Locators.FIELD_SUMM)
        assert wallet_screen.is_visible(Locators.FIELD_MEMO)
        assert wallet_screen.is_disable_to_tap(Locators.BTN_TRANSFER)