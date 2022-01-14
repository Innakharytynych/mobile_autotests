from appium.webdriver.common.mobileby import MobileBy
from app.pages.base_page import BaseScreen
from app.config.config import TestData
import requests

class Locators:
    BTN_SKIP = (MobileBy.ID, 'online.paycash.app:id/btnSkip')
    BTN_NULL_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_0')
    BTN_ONE_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_1')
    TEXT_WARNING = (MobileBy.ID, 'online.paycash.app:id/ivWarning')
    PICTURE_WRONG_PIN = (MobileBy.ID, 'online.paycash.app:id/iv_wrong_pin_code')
    BTN_UNDESTAND = (MobileBy.ID, 'online.paycash.app:id/btn_got_it')
    SCREEN_WELCOME = (MobileBy.ID,'online.paycash.app:id/cl_root')
    BTN_CREATE_WALLET = (MobileBy.ID, 'online.paycash.app:id/tvCreateWallet')
    BTN_ENTER_PK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")')
    FIELD_PRIVAT_KEY = (MobileBy.ID, 'online.paycash.app:id/et_input')
    BTN_DEL_PK = (MobileBy.ID, 'online.paycash.app:id/text_input_end_icon')
    BTN_ADD_ACC = (MobileBy.ID, 'online.paycash.app:id/addButton')
    BTN_SEND = (MobileBy.ID, 'online.paycash.app:id/fl_send')
    BTN_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/fl_replenish')
    BTN_SWAP = (MobileBy.ID, 'online.paycash.app:id/fl_swap')
    BTN_WITHDRAW = (MobileBy.ID, 'online.paycash.app:id/fl_p2p_sell')
    BTN_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/ll_username')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_ADD_MORE_ACC = (MobileBy.ID, 'online.paycash.app:id/tvAdd')
    BTN_SHOW_PK = (MobileBy.ID, 'online.paycash.app:id/btnShowPrivateKey')
    POKAZ_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/tvPrivateKey')
    COPY_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnCopy')
    BTN_DELETE = (MobileBy.ID, 'online.paycash.app:id/btnRemove')
    BTN_REMOVE = (MobileBy.ID, 'online.paycash.app:id/btn_got_it')
    BTN_REMOVE_CANCEL = (MobileBy.ID, 'online.paycash.app:id/tv_negative_action')
    BTN_CHANGE_AKK1 = (MobileBy.ANDROID_UIAUTOMATOR, 'text("avpw.pcash")')
    BTN_CHANGE_AKK2 = (MobileBy.ANDROID_UIAUTOMATOR, 'text("333334.pcash")')
    BTN_ADD_NEWACC = (MobileBy.ID, 'online.paycash.app:id/btnAdd')
    BTN_ENTER_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnImportPrivateKey')
    BTN_CREATE_WALLET_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnCreateNewWallet')
    SCREEN_ADD_TOKEN = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    BTN_ADD_TOKEN = (MobileBy.ID, 'online.paycash.app:id/iv_add_token')
    BTN_TOKEN = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add").instance(0));')
    BTN_TOKEN_ADDED = (MobileBy.ANDROID_UIAUTOMATOR,  'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Added").instance(0));')
    BLOCK_RUBCASH = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]')
    BTN_TOKEN_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,  'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NULL_BALANCE = (MobileBy.ANDROID_UIAUTOMATOR, 'text("JPYCASH")')
    TEXT_NULL_BALANCE = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("JPYCASH").instance(0));')
    TOKEN_NAME_MAIN_PAGE_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NAME_MAIN_PAGE_EURCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                                    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EURCASH").instance(0));')

    TEXT_TOKEN_NAME_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR, 'text("UAHCASH")')
    TEXT_TOKEN_NAME_LQC = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LQC").instance(0));')
    TEXT_TOKEN_NAME_EOS = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EOS").instance(0));')

    BTN_TOKEN_EURCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                           'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EURCASH").instance(0));')
    TEXT_TOKEN_NAME_JPYCASH = (MobileBy.ANDROID_UIAUTOMATOR, 'text("JPYCASH")')
    BTN_SKAN_QR = (MobileBy.ID, 'online.paycash.app:id/menu_scan_qr')
    BTN_RES_AND_TRANS = (MobileBy.ID, 'online.paycash.app:id/sw_free_trx')
    BTN_WALLET = (MobileBy.ID, 'online.paycash.app:id/navigation_wallet')
    BTN_CHAT = (MobileBy.ID, 'online.paycash.app:id/navigation_chat')
    BTN_SELL = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_sell')
    BTN_BUY = (MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_buy')
    BTN_OTHER = (MobileBy.ID, 'online.paycash.app:id/navigation_other')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_LEFT_BUTTON = (MobileBy.ID, 'online.paycash.app:id/toolbar_left_button')
    BTN_INVITE_FRIEND = (MobileBy.ID, 'online.paycash.app:id/tv_invite_friend')
    BLOCED = (MobileBy.ID, 'online.paycash.app:id/tv_blocked_p2p')
    BTN_INVITE_FRIEND_QR = (MobileBy.ID, 'online.paycash.app:id/rrv_message')
    BTN_INVITE_FRIEND_CLOSE = (MobileBy.ID, 'online.paycash.app:id/iv_close')
    LINK_INVITE_FRIEND = (MobileBy.ID, 'online.paycash.app:id/tv_invite_link')
    SHARE_INVITE_FRIEND = (MobileBy.ID, 'online.paycash.app:id/ll_share')
    COPY_INVITE_FRIEND = (MobileBy.ID, 'online.paycash.app:id/ll_copy')
    QR_INVITE_FRIEND = (MobileBy.ID, 'online.paycash.app:id/qr_code_image_view')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')
    ALL_TOKENS_MAIN_PAGE = (MobileBy.ID, 'online.paycash.app:id/recycler_tokens')
    HISTORY_TOKEN = (MobileBy.ID, 'online.paycash.app:id/recycler_content')
    DETAIL_TOKEN_NAME_TITLE = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    DETAIL_TOKEN_SEND = (MobileBy.ID, 'online.paycash.app:id/fl_send')
    DETAIL_TOKEN_RECEIVE = (MobileBy.ID, 'online.paycash.app:id/fl_replenish')
    DETAIL_TOKEN_WITHDRAW = (MobileBy.ID, 'online.paycash.app:id/fl_smart_button')
    DETAIL_TOKEN_BALLANCE = (MobileBy.ID, 'online.paycash.app:id/tv_balance')
    DATE_TRANSACTIONS = (MobileBy.ID, 'online.paycash.app:id/tv_date')
    COUNT_TRANSACTION = (MobileBy.ID, 'online.paycash.app:id/action_count')
    TEXT_ACTION_NAME = (MobileBy.ID, 'online.paycash.app:id/action_name')
    TEXT_ACTION_TIME = (MobileBy.ID, 'online.paycash.app:id/action_time')
    TEXT_TRANSFER_COMMISSION = (MobileBy.ANDROID_UIAUTOMATOR, 'text("transfer commission")')
    DETAIL_TRANSACTION_POPUP = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    DETAIL_TRANSACTION_POPUP_ID = (MobileBy.ID, 'online.paycash.app:id/tvTransactionId')
    DETAIL_TRANSACTION_POPUP_SUM = (MobileBy.ID, 'online.paycash.app:id/tvAmount')
    DETAIL_TRANSACTION_POPUP_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/tvReceiver')
    DETAIL_TRANSACTION_POPUP_MEMO = (MobileBy.ID, 'online.paycash.app:id/tvMemo')
    BTN_TRANSACTION_REPEAT = (MobileBy.ID, 'online.paycash.app:id/btnRepeat')
    BTN_COPY_ID = (MobileBy.ID, 'online.paycash.app:id/btnTransactionCopy')
    BTN_COPY_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/btnReceiverCopy')
    BTN_COPY_MEMO = (MobileBy.ID, 'online.paycash.app:id/btnMemoCopy')
    BTN_BLOCKSIO_TRANSFER = (MobileBy.ID, 'online.paycash.app:id/text_checks_on_blocks_io')
    TEXT_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/text_commission')
    BTN_REPEAT_SEND = (MobileBy.ID, 'online.paycash.app:id/btn_send')
    TEXT_POPUP_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/tvReceiver')
    TEXT_POPUP_AMOUNT = (MobileBy.ID, 'online.paycash.app:id/tvAmount')
    TEXT_POPUP_AMOUNT_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/tvSendAmount')
    TEXT_POPUP_COMMISSION = (MobileBy.ID, 'online.paycash.app:id/tvCommission')
    BTN_LEFT_BACK = (MobileBy.ID, 'online.paycash.app:id/iv_back')
    TEXT_ID_TRANSACTION = (MobileBy.ID, 'online.paycash.app:id/tvTransactionId')
    POPUP_DETAIL_TRANSACTION = (MobileBy.ID, 'online.paycash.app:id/text_confirm_title')
    TEXT_POPUP_VALUE = (MobileBy.ID, 'online.paycash.app:id/tvSendAmountValue')
    TEXT_POPUP_TOKEN = (MobileBy.ID, 'online.paycash.app:id/tvSendAmountToken')
    BTN_CHECK_BLOCKSIO = (MobileBy.ID, 'online.paycash.app:id/btnCheck')
    FIELD_SUMM = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the amount of transfer")')
    FIELD_SUMM_TOTAL = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Total amount to be charged")')
    FIELD_RECEIVER = (MobileBy.ID, 'online.paycash.app:id/et_recipient')
    BTN_QR = (MobileBy.ID, 'online.paycash.app:id/btnScanQr')
    BTN_QR_SKAN_CAMERA = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Scan with a camera")')
    BTN_QR_GALLERY = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Select from gallery")')
    BTN_ALLOW = (MobileBy.ID, 'com.android.packageinstaller:id/permission_message')
    BTN_CHOOSE_GALLERY = (MobileBy.ID, 'com.google.android.apps.photos:id/image')
    BTN_CHOOSE_QR = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 10, 2021 10:35:09 AM"]')
    BTN_CHOOSE_QR_INCORRECT = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 7, 2021 4:28:53 AM"]')
    BTN_CHOOSE_QR_BIG = (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Photo taken on Sep 10, 2021 1:24:22 PM"]')
    BTN_BACK_APP = (MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')

    TEXT_ERROR = (MobileBy.ID, 'online.paycash.app:id/vw_account')
    TEXT_YOU_SEND = (MobileBy.ID, 'online.paycash.app:id/text_send')
    FIELD_MEMO = (MobileBy.ANDROID_UIAUTOMATOR, 'text("MEMO")')
    BTN_TRANSFER = (MobileBy.ID, 'online.paycash.app:id/btnSend2')
    BTN_TRANSFER_CONFIRM = (MobileBy.ID, 'online.paycash.app:id/btn_send')
    CHOOSE_TOKEN = (MobileBy.ID, 'online.paycash.app:id/ivSelectedTokenIcon')
    TOKEN_CHANGE = (MobileBy.ID, 'online.paycash.app:id/tvTokenBalance')
    TOKEN_NAME_UAHCASH = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("UAHCASH").instance(0));')
    TOKEN_NAME_RUBCASH = (MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("RUBCASH").instance(0));')
    TOKEN_NAME_EOS = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("EOS").instance(0));')
    TEXT_INPUT_ERROR = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Insufficient balance")')
    TEXT_INPUT_ERROR_NAME = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Account does not exist")')
    BTN_DELETE_ICON = (MobileBy.ID, 'online.paycash.app:id/ivClearText')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/tvSettingsTitle')


class WalletScreen(BaseScreen, Locators):

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

    '''Вход в приложение без регистрации'''
    def open_app(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''подтвердить пин-код 1111, а не 0000'''
    def tap_one_4_times(self):
        for i in range(4):
            self.tap(self.BTN_ONE_PIN)

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
        self.tap_null_4_times()

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

    '''def parser_quantity_to_you(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        quantity = data['actions'][2]['act']['data']['amount']
        return quantity'''

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
        quantity = data['actions'][1]['act']['data']['quantity']
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
        name = data['actions'][1]['act']['data']['to']
        return name

    '''парсинг имени получателя без комиссии'''
    def parser_name_from_you(self, ID):
        url = f'https://hyperion.paycash.online/v2/history/get_transaction?id={ID}'
        r = requests.get(url)
        data = r.json()
        name = data['actions'][0]['act']['data']['to']
        return name

    '''парсит текст с поля и преобразует в число'''
    def conver_in_num(self, by_locator):
        try:
            text = self.get_text2(by_locator)
        except:
            text = by_locator
        num = ''.join(i for i in text if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return float(num)