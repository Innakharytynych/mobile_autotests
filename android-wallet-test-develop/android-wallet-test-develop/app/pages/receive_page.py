from appium.webdriver.common.mobileby import MobileBy
from app.pages.base_page import BaseScreen
from app.config.config import TestData

class Locators:
    BTN_SKIP = (MobileBy.ID, 'online.paycash.app:id/btnSkip')
    BTN_NULL_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_0')
    BTN_ENTER_PK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")')
    FIELD_PRIVAT_KEY = (MobileBy.ID, 'online.paycash.app:id/et_input')
    TEXT_WARNING = (MobileBy.ID, 'online.paycash.app:id/ivWarning')
    BTN_ADD_ACC = (MobileBy.ID, 'online.paycash.app:id/addButton')
    BTN_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/fl_replenish')
    TEXT_SCAN_QR = (MobileBy.ID, 'online.paycash.app:id/tv_scan_qr_title')
    QR_IMAGE = (MobileBy.ID, 'online.paycash.app:id/qr_code_image_view')
    RECIPIENT_NAME = (MobileBy.ID, 'online.paycash.app:id/tv_nickname')
    REVEIVE_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tv_replenish_amount')
    REVEIVE_MEMO = (MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("some text").instance(0));')
    REVEIVE_MEMO2 = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("fdgfgfgfgngn").instance(0));')
    BTN_REMOVE_SUM = (MobileBy.ID, 'online.paycash.app:id/btnRemove')
    BTN_SEND_IN_CHAT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Send in chat")')
    BTN_REMOVE_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/ivClearText')
    BTN_REMOVE_DATA  = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Clear the date")')
    BTN_SHARE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Share")')
    BTN_SETTINGS_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/tv_set_memo')
    TEXT_DEPOSIT_TOKEN = (MobileBy.ID, 'online.paycash.app:id/text_send')
    RECEIVE_TOKEN = (MobileBy.ID, 'online.paycash.app:id/ivSelectedTokenIcon')
    BTN_TOKEN_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    BTN_TOKEN_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("UAHCASH").instance(0));')
    FIELD_AMOUNT_RECEIVE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Top-up amount")')
    FIELD_MEMO_RECEIVE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("MEMO")')
    BTN_SAVE_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/btnSave')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    RECIPIENT_NAME_FLETCERCAT1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("fletchercat1").instance(0));')
    BTN_SEND = (MobileBy.ID, 'online.paycash.app:id/btnSend')
    BTN_QR_CHAT = (MobileBy.ID, 'online.paycash.app:id/btnScanQr')
    BTN_TRANSFER_CHAT = (MobileBy.ID, 'online.paycash.app:id/btnSend')
    BTN_QR_IMAGE = (MobileBy.ID, 'online.paycash.app:id/iv_qr_code')
    FIELD_MESSAGE = (MobileBy.ID, 'online.paycash.app:id/et_chat_message')
    BTN_MESSAGE_SEND = (MobileBy.ID, 'online.paycash.app:id/btnSendMessage')
    BTN_QR_IMAGE_SAVE = (MobileBy.ID, 'online.paycash.app:id/btn_download_self')
    BTN_RES_AND_TRANS = (MobileBy.ID, 'online.paycash.app:id/sw_free_trx')

    BTN_ADD_MORE_ACC = (MobileBy.ID, 'online.paycash.app:id/tvAdd')
    BTN_ENTER_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnImportPrivateKey')
    DETAIL_TOKEN_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/fl_replenish')
    TOKEN_RECEIVE_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,'text("RUBCASH")' )
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/iv_configure')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')


class ReceiveScreen(BaseScreen, Locators):

    def __init__(self, driver):
        super().__init__(driver)

    '''Screen Actions'''
    def login_by_privat_key(self):
        self.tap(Locators.BTN_SKIP)
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY_M4)
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

    '''Войти в приложение и переключится на препрод без онбординга'''
    def login_and_preprod_2(self):
        self.login_without_onboard()
        self.change_preprod()
        self.tap_null_4_times()

    '''Войти в приложение и переключится на прод без онбординга'''
    def login_and_prod2(self):
        self.login_without_onboard()
        self.change_prod()
        self.tap_null_4_times()

    '''парсит текст с поля и преобразует в число'''
    def conver_in_num(self, by_locator):
        try:
            text = self.get_text2(by_locator)
        except:
            text = by_locator
        num = ''.join(i for i in text if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return float(num)