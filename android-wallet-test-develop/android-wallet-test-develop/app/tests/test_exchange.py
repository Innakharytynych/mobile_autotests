from app.pages.exchange_page import ExchangeScreen, Locators
from app.config.config import TestData
import pytest

@pytest.mark.usefixtures('init_driver')
class TestExchange:
    '''ОБМЕН ГЛАВНЫЙ ЭКРАН'''
    '''Обмен cash - cash'''
    '''Проверить экран обмена с выбраными токенами'''
    def test_exchange_cash_screen(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)

        assert exchange_screen.is_visible(Locators.FIELD_EXCHANGE)
        assert exchange_screen.is_visible(Locators.FIELD_RECEIVE)
        assert exchange_screen.is_visible(Locators.TEXT_PATH)
        assert exchange_screen.is_visible(Locators.TEXT_EXCANGE_DIRECT)
        assert exchange_screen.is_visible(Locators.TEXT_EXCHANGE_REVERSE)
        assert exchange_screen.is_visible(Locators.BTN_EXCHANGE)
        assert exchange_screen.get_text2(Locators.TOKEN_NAME_RUBCASH) == 'RUBCASH'
        assert exchange_screen.get_text2(Locators.TOKEN_NAME_UAHCASH) == 'UAHCASH'

    '''Выбрать два токена, ввести сумму обмена больше 0,0403'''
    def test_correct_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''вести Сумма обмена, удалить “минимальная сумма к получению”, произвести обмен'''
    def test_correct2_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести ожидаемую сумму обмена больше 0,0401'''
    def test_correct3_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести сумму обмена меньше 0,04'''
    def test_incorrect_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести сумму обмена 0.00'''
    def test_incorrect2_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена меньше 0,04'''
    def test_incorrect3_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена 0.00'''
    def test_incorrect4_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''вести Сумма обмена, в поле “минимальная сумма к получению” ввести ожидаемую сумму, произвести обмен'''
    def test_correct3_cash_exchange_(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        sum = exchange_screen.get_text2(Locators.FIELD_RECEIVE)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, sum)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, не вводить суммы'''
    def test_incorrect5_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, ввести минимальная сумма к получению больше ожидаемой суммы'''
    def test_incorrect6_cash_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, TestData.SUM_MAX_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators. TEXT_INPUT_ERROR)

    '''Обмен EOS - cash'''
    '''Выбрать два токена, ввести сумму обмена больше 0,08'''
    def test_correct_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE_EOS)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        '''assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)'''
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''вести Сумма обмена, удалить “минимальная сумма к получению”, произвести обмен'''
    def test_correct2_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE_EOS)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        '''assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)'''
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести ожидаемую сумму обмена больше 0,0401'''
    def test_correct3_eos_exchange_(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести сумму обмена меньше 0,08'''
    def test_incorrect_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести сумму обмена 0.00'''
    def test_incorrect2_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена меньше 0,08'''
    def test_incorrect3_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена 0.00'''
    def test_incorrect4_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, не вводить суммы'''
    def test_incorrect5_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, ввести минимальная сумма к получению больше ожидаемой суммы'''
    def test_incorrect6_eos_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE_EOS)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, TestData.SUM_MAX_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Обмен Li*- Li*'''
    '''Выбрать два токена, ввести сумму обмена больше 0,00000800 (обмен не прямой, а через промежуточный токен)'''
    def test_correct_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''вести Сумма обмена, удалить “минимальная сумма к получению”, произвести обмен'''
    def test_correct2_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести сумму обмена меньше 0,0000008'''
    def test_incorrect_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, '0.0000007')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести сумму обмена 0.00'''
    def test_incorrect2_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена меньше 0,0000008'''
    def test_incorrect3_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, '0.0000007')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена 0.00'''
    def test_incorrect4_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, не вводить суммы'''
    def test_incorrect5_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, ввести минимальная сумма к получению больше ожидаемой суммы'''
    def test_incorrect6_li_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, TestData.SUM_MAX_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)


    '''Обмен LQ*- LQ*'''
    '''Выбрать два токена, ввести сумму обмена больше 800'''
    def test_correct_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, '900')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''вести Сумма обмена, удалить “минимальная сумма к получению”, произвести обмен'''
    def test_correct2_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, '900')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести сумму обмена меньше 800'''
    def test_incorrect_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, '700')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести сумму обмена 0.00'''
    def test_incorrect2_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена меньше 800'''
    def test_incorrect3_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, '700')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена 0.00'''
    def test_incorrect4_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, не вводить суммы'''
    def test_incorrect5_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, ввести минимальная сумма к получению больше ожидаемой суммы'''
    def test_incorrect6_lq_exchange(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.BTN_SWAP)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN1)
        exchange_screen.tap(Locators.TOKEN_NAME_LQC)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LQE)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, '800')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, '1000')
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''ОБМЕН ИСТОРИЯ ПО ТОКЕНУ'''
    '''Обмен cash - cash'''
    '''Проверить экран с выбранными токенами'''
    def test_correct_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)

        assert exchange_screen.is_visible(Locators.FIELD_EXCHANGE)
        assert exchange_screen.is_visible(Locators.FIELD_RECEIVE)
        assert exchange_screen.is_visible(Locators.TEXT_PATH)
        assert exchange_screen.is_visible(Locators.TEXT_EXCANGE_DIRECT)
        assert exchange_screen.is_visible(Locators.TEXT_EXCHANGE_REVERSE)
        assert exchange_screen.is_visible(Locators.BTN_EXCHANGE)
        assert exchange_screen.get_text2(Locators.TOKEN_NAME_RUBCASH) == 'RUBCASH'
        assert exchange_screen.get_text2(Locators.TOKEN_NAME_UAHCASH) == 'UAHCASH'

    '''Выбрать второй токен CASH, ввести сумму обмена больше 0,0403'''
    def test_correct_cash_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''вести Сумма обмена, удалить “минимальная сумма к получению”, произвести обмен'''
    def test_correct2_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)
        pop_up_1 = exchange_screen.conver_in_num(Locators.TOKEN1_EXCHANGE)
        pop_up_2 = exchange_screen.conver_in_num(Locators.TOKEN2_RECEIVE)
        pars_1 = exchange_screen.parser_quantity_from_you(exchange_screen.get_text2(Locators.EXCHANGE_ID))
        pars_2 = exchange_screen.parser_quantity_to_you(exchange_screen.get_text2(Locators.EXCHANGE_ID))

        assert pop_up_1 == exchange_screen.conver_in_num(pars_1)
        assert pop_up_2 == exchange_screen.conver_in_num(pars_2)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, ввести сумму обмена меньше 0,04'''
    def test_incorrect_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести сумму обмена 0.00'''
    def test_incorrect2_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена меньше 0,04'''
    def test_incorrect3_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_MIN_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Выбрать два токена, ввести ожидаемую сумму обмена 0.00'''
    def test_incorrect4_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_RECEIVE, TestData.SUM_ZERO)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''вести Сумма обмена, в поле “минимальная сумма к получению” ввести ожидаемую сумму, произвести обмен'''
    def test_correct3_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        sum = exchange_screen.get_text2(Locators.FIELD_RECEIVE)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, sum)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Выбрать два токена, не вводить суммы, кликнуть на "Обмен"'''
    def test_incorrect5_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.BTN_EXCHANGE)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)

    '''Выбрать два токена, ввести минимальная сумма к получению больше ожидаемой суммы'''
    def test_incorrect6_cash_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.clear(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.tap(Locators.FIELD_MIN_RECEIVE)
        exchange_screen.send_keys(Locators.FIELD_MIN_RECEIVE, TestData.SUM_MAX_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)

        assert exchange_screen.is_disable_to_tap(Locators.BTN_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TEXT_INPUT_ERROR)

    '''Первый токен EOS'''
    def test_correct2_eos_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_EOS)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.get_text2(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.get_text2(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.get_text2(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.get_text2(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Первый токен LQ Невозможно проверить ассерт из-за https://pcash.atlassian.net/browse/ALL-350'''
    def test_correct_lq_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_LQB)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE_LQ)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.conver_in_num(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.conver_in_num(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.conver_in_num(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.conver_in_num(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)

    '''Первый токен LI. Ввести корректную суммму больше 0,00000800'''
    def test_correct_li_exchange_history(self):
        exchange_screen = ExchangeScreen(self.driver)
        exchange_screen.open_app()
        exchange_screen.tap(Locators.TOKEN_NAME_LIRUMOW)
        exchange_screen.tap(Locators.BTN_SWAP_HISTORY)
        exchange_screen.tap(Locators.BTN_SELECT_TOKEN2)
        exchange_screen.tap(Locators.TOKEN_NAME_LIUAIEV)
        exchange_screen.tap(Locators.FIELD_EXCHANGE)
        exchange_screen.send_keys(Locators.FIELD_EXCHANGE, TestData.SUM_EXCHANGE_LI)
        exchange_screen.tap(Locators.TEXT_EXCANGE_DIRECT)
        exchange_screen.tap(Locators.BTN_EXCHANGE)
        exchange_amount = exchange_screen.conver_in_num(Locators.POPUP_EXCHANGE_AMOUNT)
        receive_amount = exchange_screen.conver_in_num(Locators.POPUP_RECEIVE_AMOUNT)
        exchange_screen.tap(Locators.BTN_POPUP_CONFIRM)

        assert exchange_amount == exchange_screen.conver_in_num(Locators.TOKEN1_EXCHANGE)
        assert receive_amount == exchange_screen.conver_in_num(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_COMPLETED)
        assert exchange_screen.is_visible(Locators.TOKEN1_EXCHANGE)
        assert exchange_screen.is_visible(Locators.TOKEN2_RECEIVE)
        assert exchange_screen.is_visible(Locators.EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_COPY_EXCHANGE_ID)
        assert exchange_screen.is_enable_to_tap(Locators.BTN_BLOCKSIO_EXCHANGE)
