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
    BTN_OTHER = (MobileBy.ID, 'online.paycash.app:id/navigation_other')
    BTN_SWAP_LIQ = (MobileBy.ID, 'online.paycash.app:id/btnSwap')
    BTN_SELECT_TOKEN1 = (MobileBy.ID, 'online.paycash.app:id/btnPickToken')
    BTN_SELECT_TOKEN2 = (MobileBy.ID, 'online.paycash.app:id/btnPickReceiveToken')
    TEXT_LIQUIDITY_POOL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Liquidity pool")')
    TOKEN_NAME_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("UAHCASH").instance(0));')
    TOKEN_NAME_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NAME_USDCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("USDCASH").instance(0));')
    TOKEN_NAME_EURCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EURCASH").instance(0));')
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
    TOKEN_NAME_LQA = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQA").instance(0));')
    TOKEN_NAME_LQB = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQB").instance(0));')
    BTN_LEFT_BUTTON = (MobileBy.ID, 'online.paycash.app:id/toolbar_left_button')
    BTN_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/ll_username')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_RES_AND_TRANS = (MobileBy.ID, 'online.paycash.app:id/sw_free_trx')
    BTN_SKAN_QR = (MobileBy.ID, 'online.paycash.app:id/menu_scan_qr')
    SCREEN_SWAP = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    TOKEN_BALANCE1 = (MobileBy.ID, 'online.paycash.app:id/tvTokenBalance')
    TOKEN_SYMBOL1 = (MobileBy.ID, 'online.paycash.app:id/tvTokenSymbol')
    TOKEN_DESC1 = (MobileBy.ID, 'online.paycash.app:id/tvTokenDescription')
    TOKEN_ICON1 = (MobileBy.ID, 'online.paycash.app:id/ivSelectedTokenIcon')
    TOKEN_CONTRACT1 = (MobileBy.ID, 'online.paycash.app:id/tvTokenContract')
    THREE_DOTS1 = (MobileBy.ID, 'online.paycash.app:id/ivArrowForward')
    TOKEN_BALANCE2 = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenBalance')
    TOKEN_SYMBOL2 = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenSymbol')
    TOKEN_SYMBOL22 = (MobileBy.ID, 'online.paycash.app:id/tv_token_symbol')
    TOKEN_DESC2 = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenDescription')
    TOKEN_ICON2 = (MobileBy.ID, 'online.paycash.app:id/ivReceiveSelectedTokenIcon')
    TOKEN_CONTRACT2 = (MobileBy.ID, 'online.paycash.app:id/tvReceiveTokenContract')
    THREE_DOTS2 = (MobileBy.ID, 'online.paycash.app:id/ivReceiveArrowForward')
    TEXT_CURRENT_EXCHANGE_RATE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Current exchange rate")')
    CURRENT_EXCHANGE_RATE = (MobileBy.ID, 'online.paycash.app:id/tvExchangeRateDirect')
    TEXT_CURRENT_POOL_SIZE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Total liquidity tokens issued")')
    CURRENT_POOL_SIZE = (MobileBy.ID, 'online.paycash.app:id/tvPoolVolume')
    TEXT_TOTAL_LIQUIDITY_TOKENS = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Current pool size")')
    TOTAL_LIQUIDITY_TOKENS = (MobileBy.ID, 'online.paycash.app:id/tvLiquidTokens')
    BTN_ADD_LIQ = (MobileBy.ID, 'online.paycash.app:id/btnAddLiquid')
    BNT_WITHDRAW_LIQ = (MobileBy.ID, 'online.paycash.app:id/btnRemoveLiquid')
    FIELD_TOKEN1 = (MobileBy.ID, 'online.paycash.app:id/etAddToken1')
    FIELD_TOKEN2 = (MobileBy.ID, 'online.paycash.app:id/etAddToken2')
    FIELD_TOKEN_NEW1 = (MobileBy.ID, 'online.paycash.app:id/etCreateToken1')
    FIELD_TOKEN_NEW2 = (MobileBy.ID, 'online.paycash.app:id/etCreateToken2')
    FIELD_WITHDRAW_LIQ = (MobileBy.ID, 'online.paycash.app:id/etReceiveLiquid')
    BTN_ADD_LIQUIDITY = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add liquidity to the pool").instance(0));')
    TEXT_NOT_HAVE_POOL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("This pool does not exist. You can create it or choose another pair of tokens")')
    TEXT_ADD_NEW_POOL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Add tokens to the new pool")')
    BTN_CREATE_POOL = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Create pool").instance(0));')
    BTN_WITHDRAW = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Return tokens").instance(0));')
    TEXT_YOU_RECEIVE1 = (MobileBy.ID, 'online.paycash.app:id/tvReceive1')
    TEXT_YOU_RECEIVE2 = (MobileBy.ID, 'online.paycash.app:id/tvReceive2')
    TEXT_MY_LIQ_TOKENS = (MobileBy.ID, 'online.paycash.app:id/tvMyLiquidTokens')
    TEXT_IND_BALANCE = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    MY_LIQ_TOKENS_ICON = (MobileBy.ID, 'online.paycash.app:id/ivLiquidToken')
    MY_LIQ_TOKENS_SYMBOL = (MobileBy.ID, 'online.paycash.app:id/tvLiquidTokenSymbol')
    MY_LIQ_TOKENS_DESC = (MobileBy.ID, 'online.paycash.app:id/tvLiquidTokenDescription')
    MY_LIQ_TOKENS_BAL = (MobileBy.ID, 'online.paycash.app:id/tvLiquidTokenBalance')
    CREATE_EXCHANGE_RATE = (MobileBy.ID, 'online.paycash.app:id/tvCreateExchangeRate')
    POPUP_TEXT = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    POPUP_SUM1_ADD = (MobileBy.ID, 'online.paycash.app:id/tvToken1')
    POPUP_SUM2_ADD = (MobileBy.ID, 'online.paycash.app:id/tvToken2')
    POPUP_BTN_CONFIRM = (MobileBy.ID, 'online.paycash.app:id/btnConfirm')
    POPUP_COMPL_SUM1 = (MobileBy.ID, 'online.paycash.app:id/tvToken1')
    POPUP_COMPL_SUM2 = (MobileBy.ID, 'online.paycash.app:id/tvToken2')
    POPUP_WITHDRAW_RETURN = (MobileBy.ID, 'online.paycash.app:id/tvLiquidToken')
    POPUP_WITHDRAW_GET_TOKEN1 = (MobileBy.ID, 'online.paycash.app:id/tvToken1')
    POPUP_WITHDRAW_GET_TOKEN2 = (MobileBy.ID, 'online.paycash.app:id/tvToken2')
    POPUP_COMPL_WITHDRAW_LIQ = (MobileBy.ID, 'online.paycash.app:id/tvLiquidToken')
    POPUP_COMPL_WITHDRAW_TOKEN1 = (MobileBy.ID, 'online.paycash.app:id/tvToken1')
    POPUP_COMPL_WITHDRAW_TOKEN2 = (MobileBy.ID, 'online.paycash.app:id/tvToken2')
    LIQ_TOKEN = (MobileBy.ID, 'online.paycash.app:id/tvReceive')
    TRANSACTION_ID = (MobileBy.ID, 'online.paycash.app:id/tvTransactionIdValue')
    BTN_TRANSACTION_COPY = (MobileBy.ID, 'online.paycash.app:id/btnTransactionIdCopy')
    TEXT_ERROR_SUMM = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    BTN_VIEW_BLOKSIO = (MobileBy.ID, 'online.paycash.app:id/btnCheck')
    POPUP_ERROR = (MobileBy.ID, 'online.paycash.app:id/image_failure')
    TEXT_ERROR_MIN_SUM = (MobileBy.ANDROID_UIAUTOMATOR, 'text("assertion failure with message: transfer_token : must transfer positive quantity")')
    TEXT_ERROR_DROB_SUM = (MobileBy.ANDROID_UIAUTOMATOR, 'text("assertion failure with message: retire : symbol precision mismatch")')
    BTN_INHERIANCE = (MobileBy.ID, 'online.paycash.app:id/btnInheritance')
    BTN_LIST = (MobileBy.ID, 'online.paycash.app:id/btnCryptoCash')
    BTN_GUARANTIE = (MobileBy.ID, 'online.paycash.app:id/btnOrders')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/btnSettings')
    BTN_WALLET = (MobileBy.ID, 'online.paycash.app:id/navigation_wallet')
    BTN_CHAT = (MobileBy.ID, 'online.paycash.app:id/navigation_chat')
    BTN_SELL = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_sell')
    BTN_BUY = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_buy')

class SwapScreen(BaseScreen, Locators):

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

    '''Вход в раздел'''
    def open_swap(self):
        self.open_app()
        self.tap(Locators.BTN_OTHER)
        self.tap(Locators.BTN_SWAP_LIQ)


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

    '''парсит текст с поля и преобразует в число'''
    def conver_in_num(self, by_locator):
        try:
            text = self.get_text2(by_locator)
        except:
            text = by_locator
        num = ''.join(i for i in text if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return float(num)

