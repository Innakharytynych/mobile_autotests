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
    BTN_CHAT = (MobileBy.ID, 'online.paycash.app:id/navigation_chat')
    FIELD_SEARCH = (MobileBy.ID, 'online.paycash.app:id/et_search_bar')
    SEARCH_NAME = (MobileBy.ANDROID_UIAUTOMATOR, 'text("fletchercat1")')
    BTN_CREATE_CHAT = (MobileBy.ID, 'online.paycash.app:id/btnCreateChat')
    DIALOG = (MobileBy.ID, 'online.paycash.app:id/tv_dialog_with')
    DIALOG2 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]')
    DIALOG_DATE = (MobileBy.ID, 'online.paycash.app:id/tv_time')
    DIALOG_AVATAR = (MobileBy.ID, 'online.paycash.app:id/tvAvatarText')
    IMAGE_NOTHING = (MobileBy.ID, 'online.paycash.app:id/iv_image')
    TEXT_NOTHING_FOUND = (MobileBy.ID, 'online.paycash.app:id/tv_description')
    TEXT_NOTHING = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Nothing is found")')
    MESSAGE_TEXT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Test")')
    BTN_WALLET = (MobileBy.ID, 'online.paycash.app:id/navigation_wallet')
    BTN_SELL = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_sell')
    BTN_BUY = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_buy')
    BTN_OTHER = (MobileBy.ID, 'online.paycash.app:id/navigation_other')
    BTN_RES_AND_TRANS = (MobileBy.ID, 'online.paycash.app:id/sw_free_trx')
    BTN_QR_CHAT = (MobileBy.ID, 'online.paycash.app:id/btnScanQr')
    BTN_TRANSFER_CHAT = (MobileBy.ID, 'online.paycash.app:id/btnSend')
    BTN_QR_IMAGE = (MobileBy.ID, 'online.paycash.app:id/iv_qr_code')
    FIELD_MESSAGE = (MobileBy.ID, 'online.paycash.app:id/et_chat_message')
    BTN_MESSAGE_SEND = (MobileBy.ID, 'online.paycash.app:id/btnSendMessage')
    BTN_QR_IMAGE_SAVE = (MobileBy.ID, 'online.paycash.app:id/btn_download_self')
    BTN_QR_IMAGE_DOWNLOAD = (MobileBy.ID, 'online.paycash.app:id/btn_download')
    RECIPIENT_NAME_NEW = (MobileBy.ID, 'online.paycash.app:id/viewAvatar')
    TEXT_WARNING_CHAT = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Warning! This chat is available on this device only")')
    MY_MESSAGE_TEST = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Test")')
    YOUR_MESSAGE = (MobileBy.ID, 'online.paycash.app:id/ll_message')
    POP_UP_SEARCH_ACCOUNT = (MobileBy.ID, 'online.paycash.app:id/btnSearch')
    POP_UP_SKAN_CAMERA = (MobileBy.ID, 'online.paycash.app:id/btnScanCamera')
    POP_UP_FROM_GALLERY = (MobileBy.ID, 'online.paycash.app:id/btnQrFromGallery')
    BTN_CHOOSE_GALLERY = (MobileBy.ID, 'com.google.android.apps.photos:id/image')
    BTN_CHOOSE_DOWNLOAD = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Download")')
    BTN_CHOOSE_QR = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 10, 2021 10:35:09 AM"]')
    BTN_CHOOSE_QR_INCORRECT = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 7, 2021 4:28:53 AM"]')
    BTN_CHOOSE_QR_DOWNLOAD = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 8, 2021 6:43:58 AM"]')
    POP_UP_NEW_ACCOUNT = (MobileBy.ID, 'online.paycash.app:id/et_recipient')
    POP_UP_CREATE_CHAT = (MobileBy.ID, 'online.paycash.app:id/btn_create_chat')
    BTN_SKAN_QR = (MobileBy.ID, 'online.paycash.app:id/menu_scan_qr')
    TEXT_NEW_CHAT = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    TEXT_DESCRIPTION = (MobileBy.ID, 'online.paycash.app:id/textTextView')
    TEXT_INCORRECT_ACCOUNT = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/tvSettingsTitle')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_ADD_MORE_ACC = (MobileBy.ID, 'online.paycash.app:id/tvAdd')
    BTN_ENTER_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnImportPrivateKey')
    BTN_CHANGE_AKK1 = (MobileBy.ANDROID_UIAUTOMATOR, 'text("521115.pcash")')
    BTN_LEFT_BACK = (MobileBy.ID, 'online.paycash.app:id/btnBack')
    UNREAD_MESSAGE = (MobileBy.ID, 'online.paycash.app:id/tv_unread_count')
    NEW_MESSAGE_FUTER = (MobileBy.ACCESSIBILITY_ID, 'Chat, 1 new notifications')
    BTN_QR_GALLERY = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Select from gallery")')
    TEXT_QR_IMAGE_SAVE = (MobileBy.ID, 'online.paycash.app:id/tvTitle')
    BTN_TRANSFER = (MobileBy.ID, 'online.paycash.app:id/btnSend2')
    BTN_TRANSFER_CONFIRM = (MobileBy.ID, 'online.paycash.app:id/btn_send')
    CHOOSE_TOKEN = (MobileBy.ID, 'online.paycash.app:id/ivSelectedTokenIcon')
    FIELD_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/et_recipient')
    FIELD_SUMM = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the amount of transfer")')
    FIELD_MEMO = (MobileBy.ANDROID_UIAUTOMATOR, 'text("MEMO")')
    FIELD_SUMM_TOTAL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Total amount to be charged")')
    TEXT_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/text_commission')
    TOKEN_NAME_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("UAHCASH").instance(0));')
    TOKEN_NAME_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NAME_EOS = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EOS").instance(0));')
    TOKEN_NAME_LQ = (MobileBy.ANDROID_UIAUTOMATOR,
                      'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQC").instance(0));')

    TEXT_YOU_SEND = (MobileBy.ID, 'online.paycash.app:id/text_send')
    TEXT_POPUP_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tvAmount')
    TEXT_POPUP_AMOUNT_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/tvSendAmount')
    TEXT_POPUP_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/tvCommission')
    TEXT_POPUP_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/tvReceiver')
    TEXT_ID_TRANSACTION = (MobileBy.ID, 'online.paycash.app:id/tvTransactionId')
    POPUP_DETAIL_TRANSACTION = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    TEXT_POPUP_VALUE = (MobileBy.ID, 'online.paycash.app:id/tvSendAmountValue')
    TEXT_POPUP_TOKEN = (MobileBy.ID, 'online.paycash.app:id/tvSendAmountToken')
    BTN_CHECK_BLOCKSIO = (MobileBy.ID, 'online.paycash.app:id/btnCheck')
    TEXT_INPUT_ERROR = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Insufficient balance")')

class ChatScreen(BaseScreen, Locators):

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

    '''Вход в приложение без регистрации'''
    def open_app(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''ввести пин-код 0000'''
    def tap_null_4_times(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''Сменить с прода на препрод'''
    def change_preprod(self):
        self.tap(Locators.BTN_OTHER)
        self.tap(Locators.BTN_SETTINGS)
        self.change_prod_preprod(Locators.BTN_VERSION)
        self.tap(Locators.BTN_PREPROD)

    '''Сменить с препрода на прод'''
    def change_prod(self):
        self.tap(Locators.BTN_OTHER)
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

    def open_chat(self):
        self.open_app()
        self.tap(Locators.BTN_CHAT)

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

    '''парсинг суммы с комиссией'''
    def parser_quantity_from_you2(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        quantity = data['actions'][0]['act']['data']['quantity']
        return quantity

    '''парсинг суммы без комиссии'''
    def parser_quantity_from_you_without_com(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        quantity = data['actions'][0]['act']['data']['amount']
        return quantity

    '''парсинг имени получателя'''
    def parser_name_from_you_com(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        name = data['actions'][0]['act']['data']['to']
        return name

    '''парсинг имени получателя без комиссии'''
    def parser_name_from_you(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        name = data['actions'][0]['act']['data']['to']
        return name

