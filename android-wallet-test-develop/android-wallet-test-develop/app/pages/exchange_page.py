from appium.webdriver.common.mobileby import MobileBy
from app.pages.base_page import BaseScreen
from app.config.config import TestData
import requests

class Locators:
    BTN_SKIP = (MobileBy.ID, 'online.paycash.app:id/btnSkip')
    BTN_NULL_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_0')
    BTN_ENTER_PK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")')
    FIELD_PRIVAT_KEY = (MobileBy.ID, 'online.paycash.app:id/et_input')
    TEXT_WARNING = (MobileBy.ID, 'online.paycash.app:id/ivWarning')
    BTN_ADD_ACC = (MobileBy.ID, 'online.paycash.app:id/addButton')
    BTN_SWAP = (MobileBy.ID, 'online.paycash.app:id/fl_swap')
    BTN_SWAP_HISTORY = (MobileBy.ID, 'online.paycash.app:id/fl_swap_button')
    BTN_SELECT_TOKEN1 = (MobileBy.ID, 'online.paycash.app:id/btnPickToken')
    BTN_SELECT_TOKEN2 = (MobileBy.ID, 'online.paycash.app:id/btnPickReceiveToken')
    TOKEN_NAME_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("UAHCASH").instance(0));')
    TOKEN_NAME_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NAME_EOS = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EOS").instance(0));')
    TOKEN_NAME_LIUAIEV = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LIUAIEV").instance(0));')
    TOKEN_NAME_LIRUMOW = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LIRUMOW").instance(0));')
    TOKEN_NAME_LQC = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQC").instance(0));')
    TOKEN_NAME_LQE = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQE").instance(0));')
    TOKEN_NAME_LQB = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQB").instance(0));')

    TOKEN1_BALLANCE = (MobileBy.ID, 'online.paycash.app:id/tvTokenBalance')
    TOKEN2_BALLANCE = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenBalance')
    TOKEN1_NAME = (MobileBy.ID, 'online.paycash.app:id/tvTokenDescription')
    TOKEN2_NAME = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenDescription')
    TEXT_EXCANGE_DIRECT = (MobileBy.ID, 'online.paycash.app:id/tvExchangeRateDirect')
    TEXT_EXCHANGE_REVERSE = (MobileBy.ID, 'online.paycash.app:id/tvExchangeRateReverse')
    FIELD_EXCHANGE = (MobileBy.ID, 'online.paycash.app:id/etYouExchange')
    FIELD_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/etYouReceive')
    FIELD_MIN_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/etMinReceive')
    TEXT_PATH = (MobileBy.ID, 'online.paycash.app:id/tvRoute')
    BTN_EXCHANGE = (MobileBy.ID, 'online.paycash.app:id/btnExchange')
    DETAIL_TRANSACTION_POPUP = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    POPUP_EXCHANGE_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tvSendAmount')
    POPUP_RECEIVE_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tvReceiveAmount')
    POPUP_RECEIVE_MIN_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tvMinAmount')
    BTN_POPUP_CONFIRM = (MobileBy.ID, 'online.paycash.app:id/btnConfirm')
    PROGRESS_BAR = (MobileBy.ID, 'online.paycash.app:id/progress_bar')
    EXCHANGE_COMPLETED = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    TOKEN1_EXCHANGE = (MobileBy.ID, 'online.paycash.app:id/tvFrom')
    TOKEN2_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/tvTo')
    EXCHANGE_ID = (MobileBy.ID, 'online.paycash.app:id/tvTransactionIdValue')
    BTN_COPY_EXCHANGE_ID = (MobileBy.ID, 'online.paycash.app:id/btnTransactionIdCopy')
    BTN_BLOCKSIO_EXCHANGE = (MobileBy.ID, 'online.paycash.app:id/btnCheck')
    TEXT_INPUT_ERROR = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    BTN_OTHER = (MobileBy.ID, 'online.paycash.app:id/navigation_other')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/tvSettingsTitle')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')


class ExchangeScreen(BaseScreen, Locators):

    def __init__(self, driver):
        super().__init__(driver)

    '''Screen Actions'''
    def login_by_privat_key(self):
        self.tap(Locators.BTN_SKIP)
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY)
        self.tap(Locators.TEXT_WARNING)
        self.tap(self.BTN_ADD_ACC)

    '''Первичный вход без онбординга'''
    def login_without_onboard(self):
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
        self.tap(Locators.TEXT_WARNING)
        self.tap(self.BTN_ADD_ACC)

    '''ввести пин-код 0000'''
    def tap_null_4_times(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''Вход в приложение без регистрации'''
    def open_app(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''парсит сумму списания при обмене с гипериона'''
    def parser_quantity_from_you(self, ID):
        quantity = ''
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        for i in range(20):
            if data['actions'][i]['action_ordinal'] == 2 and \
                    data['actions'][i]['creator_action_ordinal'] == 0:
                quantity = data['actions'][i]['act']['data']['quantity']
                print(quantity)
                break
            return quantity

    '''парсит сумму получения после обмена с гипериона'''
    def parser_quantity_to_you(self, ID):
        global quantity

        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        symbol = data['actions'][1]['act']['data']['symbol']
        if 'CASH' in symbol:
            for i in range(20):
                if data['actions'][i]['action_ordinal'] == 23 and \
                        data['actions'][i]['creator_action_ordinal'] == 11:
                    quantity = data['actions'][i]['act']['data']['quantity']
                    print(quantity)
                    break
        elif 'LI' in symbol:
            for i in range(20):
                if data['actions'][i]['action_ordinal'] == 15 and \
                        data['actions'][i]['creator_action_ordinal'] == 4:
                    quantity = data['actions'][i]['act']['data']['quantity']
                    print(quantity)
                    break
        elif 'EOS' in symbol:
            for i in range(20):
                if data['actions'][i]['action_ordinal'] == 24 and \
                        data['actions'][i]['creator_action_ordinal'] == 11:
                    quantity = data['actions'][i]['act']['data']['quantity']
                    print(quantity)
                    break
        return quantity

    '''парсит memo после обмена с гипериона'''
    def parser_memo(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        memo = data['actions'][1]['act']['data']['memo']
        return memo

    '''парсит текст с поля и преобразует в число'''
    def conver_in_num(self, by_locator):
        try:
            text = self.get_text2(by_locator)
        except:
            text = by_locator
        num = ''.join(i for i in text if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return float(num)

    '''Сменить с прода на препрод'''
    def change_preprod(self):
        self.tap(Locators.BTN_OTHER)
        self.tap(Locators.BTN_SETTINGS)
        self.change_prod_preprod(Locators.BTN_VERSION)
        self.tap(Locators.BTN_PREPROD)
        self.tap_null_4_times()

    '''Сменить с препрода на прод'''
    def change_prod(self):
        self.tap(Locators.BTN_OTHER)
        self.tap(Locators.BTN_SETTINGS)
        self.change_prod_preprod(Locators.BTN_VERSION)
        self.tap(Locators.BTN_PROD)
        self.tap_null_4_times()