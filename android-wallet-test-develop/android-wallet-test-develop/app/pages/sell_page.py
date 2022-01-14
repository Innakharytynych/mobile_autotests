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
    BTN_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/ll_username')
    BTN_SELL = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_sell')
    BLOCK_TOKEN = (MobileBy.ID, 'online.paycash.app:id/iv_token_image')
    TOKEN_NAME_USD = (MobileBy.ANDROID_UIAUTOMATOR, 'text("USDCASH")')
    TOKEN_NAME_UA_POPUP = (MobileBy.ANDROID_UIAUTOMATOR, 'text("UAHCASH")')
    TOKEN_NAME_UA = (MobileBy.ANDROID_UIAUTOMATOR,'text("UAHCASH")')
    BTN_IN_ORDERS = (MobileBy.ID, 'online.paycash.app:id/tv_in_deals_balance')
    BTN_SHOW_HISTORY = (MobileBy.ID, 'online.paycash.app:id/iv_show_history')
    BTN_BANK_CARD = (MobileBy.ID, 'online.paycash.app:id/iv_bank_card')
    BTN_CREATE_ORDER = (MobileBy.ID, 'online.paycash.app:id/tv_create_order')
    TEXT_NO_ACTIVE_ORDERS = (MobileBy.ANDROID_UIAUTOMATOR, 'text("No active orders")')
    IMAGE_NO_ACTIVE_ORDERS =(MobileBy.ID, 'online.paycash.app:id/iv_image')
    MY_ODRERS = (MobileBy.ID, 'online.paycash.app:id/sb_my_orders')
    ALL_ORDERS = (MobileBy.ID, 'online.paycash.app:id/sb_other_orders')
    DEAL_NUMBER = (MobileBy.ID, 'online.paycash.app:id/tv_id')
    DEAL_SUMM = (MobileBy.ID, 'online.paycash.app:id/tv_volume')
    DEAL_DATE = (MobileBy.ID, 'online.paycash.app:id/tv_date')
    DEAL_BYER = (MobileBy.ID, 'online.paycash.app:id/tv_seller_buyer_title')
    DEAL_BYER_NAME = (MobileBy.ID, 'online.paycash.app:id/tv_seller_buyer')
    DEAL_STATUS = (MobileBy.ID, 'online.paycash.app:id/tv_status')
    DEAL_COPY = (MobileBy.ID, 'online.paycash.app:id/iv_copy')
    DEAL_CHAT = (MobileBy.ID, 'online.paycash.app:id/iv_chat')
    DEAL_WATCH = (MobileBy.ID, 'online.paycash.app:id/rrv_alarm')
    DEAL_TIMER = (MobileBy.ID, 'online.paycash.app:id/tv_timer')
    DEAL_CANCELED_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Transaction cancelled by the buyer")')
    DEAL_COMPLETED_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Transaction completed successfully")')

    BTN_CARD = (MobileBy.ID, 'online.paycash.app:id/iv_bank_card')
    BTN_WITHDRAW = (MobileBy.ID, 'online.paycash.app:id/rb_withdrawal_card')
    BTN_PAY_INVOICE = (MobileBy.ID, 'online.paycash.app:id/rb_pay_link')
    TOKEN_USD = (MobileBy.ID, 'online.paycash.app:id/tv_token_symbol')
    BTN_WITHDRAW_MAX = (MobileBy.ID, 'online.paycash.app:id/tv_max')
    FIELD_AMOUNT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the withdrawal amount")')
    FIELD_MIN_AMOUNT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Minimum transaction limit")')
    FIELD_MAX_AMOUNT = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Maximum transaction limit").instance(0));')

    BTN_NEW_SELL_ORDER = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("New order").instance(0));')
    BTN_NEW_SELL_ORDER2 = (MobileBy.ID, 'online.paycash.app:id/btn_create_deal')
    BTN_ADD_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_action')
    FIELD_CARD_NUMBER = (MobileBy.ID, 'online.paycash.app:id/et_card_number')
    FIELD_COUNTRY = (MobileBy.XPATH,
                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')
    FIELD_BANK = (MobileBy.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')
    CHEKBOX_DEFAULT_CARD = (MobileBy.ID, 'online.paycash.app:id/sw_make_default')
    BTN_SAVE_CARD = (MobileBy.ID, 'online.paycash.app:id/btn_save')
    CARD_DETAILS = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    BTN_LEFT_BUTTON = (MobileBy.ID, 'online.paycash.app:id/toolbar_left_button')
    TEXT_BALANCE = (MobileBy.ID, 'online.paycash.app:id/tv_balance')
    TEXT_INSUFFICIENT_BALANCE = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    TEXT_LIMIT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Limit is above order amount")')
    TEXT_LIMIT_MIN = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Minimal limit exceeds maximum limit")')
    BTN_CONFIRM_SELL_ORDER = (MobileBy.ID, 'online.paycash.app:id/btn_pick_password')
    FIELD_LINK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Insert link to invoice")')
    BTN_QR = (MobileBy.ID, 'online.paycash.app:id/tv_action_text')
    FIELD_AMOUNT_LINK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the invoice amount")')
    FIELD_COUNTRY_LINK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Specify the country")')
    TEXT_RATE = (MobileBy.ID, 'online.paycash.app:id/tv_rate')
    MY_SELL_ODRER_TRANS = (MobileBy.ID, 'online.paycash.app:id/tv_rating')
    MY_SELL_ODRER_TYPE = (MobileBy.ID, 'online.paycash.app:id/tv_status')
    MY_SELL_ODRER_ID = (MobileBy.ID, 'online.paycash.app:id/tv_id')
    MY_SELL_ODRER_MY = (MobileBy.ID, 'online.paycash.app:id/tv_my_order')
    MY_SELL_ODRER_AVALIABLE = (MobileBy.ID, 'online.paycash.app:id/tv_available')
    MY_SELL_ODRER_RATE = (MobileBy.ID, 'online.paycash.app:id/tv_rate')
    MY_SELL_ODRER_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_credential')
    MY_SELL_ODRER_COPY_CARD = (MobileBy.ID, 'online.paycash.app:id/iv_credential_copy')
    MY_SELL_ODRER_BANK = (MobileBy.ID, 'online.paycash.app:id/tv_bank')
    MY_SELL_ODRER_CANCEL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Cancel order")')
    MY_SELL_ODRER_PAUSE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Pause order")')

    BTN_RES_AND_TRANS = (MobileBy.ID, 'online.paycash.app:id/sw_free_trx')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/iv_configure')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')


class SellScreen(BaseScreen, Locators):

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
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY)
        self.tap(Locators.TEXT_WARNING)
        self.tap(self.BTN_ADD_ACC)

    '''ввести пин-код 0000'''
    def tap_null_4_times(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)


    '''Сменить с прода на препрод'''
    def change_preprod(self):
        self.tap(Locators.BTN_SETTINGS)
        self.change_prod_preprod(Locators.BTN_VERSION)
        self.tap(Locators.BTN_PREPROD)

    '''Сменить с препрода на прод'''
    def change_prod(self):
        self.tap(Locators.BTN_SETTINGS)
        self.change_prod_preprod(Locators.BTN_VERSION)
        self.tap(Locators.BTN_PROD)

    '''Войти в приложение и переключится на препрод'''
    def login_and_preprod(self):
        self.login_by_privat_key()
        self.change_preprod()
        self.tap_null_4_times()

    '''Войти в приложение и переключится на прод'''
    def login_and_prod(self):
        self.login_by_privat_key()
        self.change_prod()
        self.tap_null_4_times()

    '''парсит сумму списания при обмене с гипериона'''

    def parser_quantity_from_you(self, ID):
        url = f'https://hyperion.listock.io/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        quantity = data['actions'][1]['act']['data']['quantity']
        return quantity

    '''парсит сумму получения после обмена с гипериона'''

    def parser_quantity_to_you(self, ID):
        global quantity
        url = f'https://hyperion.listock.io/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        symbol = data['actions'][1]['act']['data']['symbol']
        if 'CASH' in symbol:
            quantity = data['actions'][10]['act']['data']['quantity']
        elif 'LI' in symbol:
            quantity = data['actions'][6]['act']['data']['quantity']
        elif 'EOS' in symbol:
            quantity = data['actions'][5]['act']['data']['quantity']
        return quantity

    '''парсит memo после обмена с гипериона'''

    def parser_memo(self, ID):
        url = f'https://hyperion.listock.io/v2/history/get_transaction?id={ID}'
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