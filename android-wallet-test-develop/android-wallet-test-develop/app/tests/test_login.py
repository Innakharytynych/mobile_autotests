from app.pages.login_page import LoginScreen, Locators
from app.config.config import TestData
import pytest


@pytest.mark.usefixtures('init_driver')
class TestLogin:

    '''онбординг'''
    '''прокликать два экрана, вернуться назад и прокликать до конца'''
    def test_onboard(self):
        login_screen = LoginScreen(self.driver)
        login_screen.tap_next_onboard()

        assert login_screen.is_visible(Locators.SCREEN_PIN)

    '''прокликать все экраны онбординга'''
    def test_all_onboard(self):
        login_screen = LoginScreen(self.driver)

        if login_screen.is_presence(Locators.SCREEN1_ONBOARD) and \
                login_screen.is_visible(Locators.INFO_ONBOARD):
            login_screen.tap(Locators.BTN_NEXT_ONBOARD)
            step1 = True
        if login_screen.is_presence(Locators.SCREEN2_ONBOARD) and \
                login_screen.is_visible(Locators.INFO_ONBOARD):
            login_screen.tap(Locators.BTN_NEXT_ONBOARD)
            step2 = True
        if login_screen.is_presence(Locators.SCREEN3_ONBOARD) and \
                login_screen.is_visible(Locators.INFO_ONBOARD):
            login_screen.tap(Locators.BTN_NEXT_ONBOARD)
            step3 = True
        if login_screen.is_presence(Locators.SCREEN4_ONBOARD) and \
                login_screen.is_visible(Locators.INFO_ONBOARD):
            login_screen.tap(Locators.BTN_NEXT_ONBOARD)
            step4 = True

        assert step1
        assert step2
        assert step3
        assert step4
        assert login_screen.is_visible(Locators.SCREEN_PIN)

    '''пропустить описание'''
    def test_skip_onboard(self):
        login_screen = LoginScreen(self.driver)
        login_screen.tap(Locators.BTN_SKIP)

        assert login_screen.is_visible(Locators.SCREEN_PIN)

    '''тест, что отображается экран с пин-кодом'''
    def test_notify_enable_and_tap(self):
        login_screen = LoginScreen(self.driver)

        assert login_screen.is_visible(Locators.SCREEN_PIN)

    '''добавление и повторение корректного пин-кода'''
    def test_enter_pin_code(self):
        login_screen = LoginScreen(self.driver)
        login_screen.tap_skip()
        login_screen.is_visible(Locators.SCREEN_PIN)
        login_screen.tap_null_8_times()

        assert login_screen.is_visible(Locators.SCREEN_WELCOME)
        assert login_screen.is_enable_to_tap(Locators.BTN_CREATE_WALLET)
        assert login_screen.is_enable_to_tap(Locators.BTN_ENTER_PK)

    '''отмена подтверждения пин-кода'''
    def test_cancel_pin(self):
        login_screen = LoginScreen(self.driver)
        login_screen.tap_skip()
        login_screen.tap_null_4_times()
        login_screen.tap(Locators.BTN_CANCEL)

        assert login_screen.is_visible(Locators.SCREEN_PIN)

    '''проверка, что доступны поля для ввода приватного ключа, кнопки для QR, кнопки Добавить акк'''
    def test_enable_field_and_button(self):
        login_screen = LoginScreen(self.driver)
        login_screen.insert_privat_key()

        assert login_screen.is_enable_to_tap(Locators.FIELD_PRIVAT_KEY)
        assert login_screen.is_enable_to_tap(Locators.BTN_ENTER_PK)
        assert login_screen.is_disable_to_tap(Locators.BTN_SCAN_QR)

    '''Вставить приватный ключ'''
    def test_insert_valid_privat_key(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login_by_privat_key()

        assert login_screen.is_visible(Locators.SCREEN_MY_WALLET)
        assert login_screen.is_visible(Locators.BTN_AKK_NAME)

    '''Вставить приватный ключ, удалить приватный ключ, вставить заново корректный приватный ключ другой'''
    def test_add_another_pk(self):
        login_screen = LoginScreen(self.driver)
        login_screen.enter_private_key_not_click_button(TestData.PRIVAT_KEY)
        login_screen.tap(Locators.FIELD_PRIVAT_KEY)
        login_screen.tap(Locators.BTN_DEL_PK)
        login_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        login_screen.tap(Locators.BTN_ADD_ACC)

        assert login_screen.is_visible(Locators.SCREEN_MY_WALLET)
        assert login_screen.is_visible(Locators.BTN_AKK_NAME)
        assert login_screen.get_text(Locators.TEXT_AKK_NAME, 'fletchercat1')

    '''Вставить приватный ключ аккаунта, который уже добавлен'''
    def test_add_same_pk(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login_by_privat_key()
        login_screen.tap(Locators.BTN_AKK_NAME)
        login_screen.tap(Locators.BTN_ADD_MORE_ACC)
        login_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        login_screen.send_keys(Locators.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY)
        login_screen.tap(Locators.BTN_ADD_ACC)

        assert login_screen.is_visible(Locators.TEXT_ACC_ALREADY_ADD)
        assert login_screen.is_enable_to_tap(Locators.BTN_ADD_ACC)
        assert login_screen.is_enable_to_tap(Locators.BTN_SCAN_QR)

    '''Отмена вставки приватного ключа'''
    def test_cancel_add_pk(self):
        login_screen = LoginScreen(self.driver)
        login_screen.enter_private_key_not_click_button(TestData.PRIVAT_KEY)
        login_screen.tap(Locators.BTN_LEFT_BACK)

        assert login_screen.is_visible(Locators.SCREEN_WELCOME)
        assert login_screen.is_enable_to_tap(Locators.BTN_CREATE_WALLET)
        assert login_screen.is_enable_to_tap(Locators.BTN_ENTER_PK)

    '''Проверить. Вход с корректным пин-кодом
    def test_entry_pin_code(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login_by_privat_key()
        login_screen.close_app()
        login_screen.activate_app('online.paycash.app')
        login_screen.tap_null_4_times()

        assert login_screen.is_visible(Locators.SCREEN_MY_WALLET)
        assert login_screen.is_visible(Locators.BTN_AKK_NAME)'''

    '''отображается экран для выбрать имя из списка'''
    def test_pick_name(self):
        login_screen = LoginScreen(self.driver)
        login_screen.create_wallet()

        assert login_screen.is_visible(Locators.BTN_PICK_NAME)
        assert login_screen.is_enable_to_tap(Locators.BTN_PICK_NAME)

    '''возврат с экрана выбора имени'''
    def test_back_to_welcome(self):
        login_screen = LoginScreen(self.driver)
        login_screen.create_wallet()
        login_screen.tap(Locators.BTN_BACK_WELCOME)

    '''Негативные тесты'''
    '''Пин-код правильный, подтверждение пин-кода не правильное'''
    def test_wrong_pin(self):
        login_screen = LoginScreen(self.driver)
        login_screen.tap_skip()
        login_screen.tap_null_4_times()
        login_screen.tap_one_4_times()

        assert login_screen.is_visible(Locators.TEXT_WRONG_PIN)
        assert login_screen.get_text(Locators.TEXT_WRONG_PIN, Locators.TEXT_WRONG_PIN[1])

    '''Первый аккаунт. Приватный ключ не корректный'''
    @pytest.mark.parametrize('PRIVAT_KEYS', [
        TestData.short_key(),
        TestData.long_key(),
        TestData.public_key(),
        TestData.privat_key_another_blockchain(),
        TestData.incorrect_key()
    ], ids=[
        'short_key (<51)',
        'long_key (>51)',
        'public_key (<51)',
        'privat_key_another_blockchain (<51)',
        'incorrect_key'
    ])
    def test_insert_invalid_privat_key(self, PRIVAT_KEYS):
        login_screen = LoginScreen(self.driver)
        login_screen.enter_private_key_not_add_key()
        login_screen.send_private_key(PRIVAT_KEYS)

        assert login_screen.is_disable_to_tap(Locators.BTN_ADD_ACC) \
               or login_screen.is_visible(Locators.TEXT_NOT_PRIVATE_KEY)


    '''Добавить аккаунт к существующему. Приватный ключ не корректный'''
    @pytest.mark.parametrize('PRIVAT_KEYS', [
        TestData.short_key(),
        TestData.long_key(),
        TestData.public_key(),
        TestData.privat_key_another_blockchain(),
        TestData.incorrect_key()
    ], ids=[
        'short_key (<51)',
        'long_key (>51)',
        'public_key (<51)',
        'privat_key_another_blockchain (<51)',
        'incorrect_key'
    ])
    def test_invalid_private_key_newakk(self, PRIVAT_KEYS):
        login_screen = LoginScreen(self.driver)
        login_screen.login_by_privat_key()
        login_screen.tap(Locators.BTN_AKK_NAME)
        login_screen.tap(Locators.BTN_ADD_NEWACC)
        login_screen.tap(Locators.BTN_ENTER_PK_POPUP)
        login_screen.enter_private_key_not_add_key()
        login_screen.send_private_key(PRIVAT_KEYS)

        assert login_screen.is_disable_to_tap(Locators.BTN_ADD_ACC) \
               or login_screen.is_visible(Locators.TEXT_NOT_PRIVATE_KEY)