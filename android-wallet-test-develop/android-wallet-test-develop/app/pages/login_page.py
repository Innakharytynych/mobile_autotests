'''наследует класс Pages поэтому нужно стачала импортировать.
Это главный первый экран после загрузки приложения. В пейкеш это онбординг. там я кликала на кнопку пропустить'''
from appium.webdriver.common.mobileby import MobileBy
from app.pages.base_page import BaseScreen
from app.config.config import TestData

class Locators:
    BTN_SKIP = (MobileBy.ID, 'online.paycash.app:id/btnSkip')
    BTN_NEXT_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/btnForward')
    BTN_BACK_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/btnBack')
    SCREEN1_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/iv_step1')
    SCREEN2_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/iv_step2')
    SCREEN3_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/iv_step3')
    SCREEN4_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/iv_step4')
    INFO_ONBOARD = (MobileBy.ID, 'online.paycash.app:id/rrv_content')
    SCREEN_PIN = (MobileBy.ID, 'online.paycash.app:id/container_enter_pin')
    BTN_NULL_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_0')
    BTN_ONE_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_1')
    BTN_CANCEL = (MobileBy.ID, 'online.paycash.app:id/tv_cancel')
    TEXT_WRONG_PIN = (MobileBy.ID, 'online.paycash.app:id/tv_error')
    SCREEN_WELCOME = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout')
    BTN_CREATE_WALLET = (MobileBy.ID, 'online.paycash.app:id/tvCreateWallet')
    BTN_PICK_NAME = (MobileBy.ID, 'online.paycash.app:id/btnPickUserName')
    BTN_ENTER_NAME = (MobileBy.ID, 'online.paycash.app:id/btnEnterUserName')
    BTN_NAME_CONTAINER = (MobileBy.ID, 'online.paycash.app:id/container')
    BTN_CONTINUE_NAME = (MobileBy.ID, 'online.paycash.app:id/btnContinue')
    CBOX_PCASH_NAME = (MobileBy.ID, 'online.paycash.app:id/rb_use_pcash')
    CBOX_CUSTOM_NAME = (MobileBy.ID, 'online.paycash.app:id/rb_use_custom_name')
    LETTER1 = (MobileBy.ID, 'online.paycash.app:id/et_letter1')
    LETTER2 = (MobileBy.ID, 'online.paycash.app:id/et_letter2')
    LETTER3 = (MobileBy.ID, 'online.paycash.app:id/et_letter3')
    LETTER4 = (MobileBy.ID, 'online.paycash.app:id/et_letter4')
    LETTER5 = (MobileBy.ID, 'online.paycash.app:id/et_letter5')
    LETTER6 = (MobileBy.ID, 'online.paycash.app:id/et_letter6')
    CUSTOM_LETTER1 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter1')
    CUSTOM_LETTER2 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter2')
    CUSTOM_LETTER3 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter3')
    CUSTOM_LETTER4 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter4')
    CUSTOM_LETTER5 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter5')
    CUSTOM_LETTER6 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter6')
    CUSTOM_LETTER7 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter7')
    CUSTOM_LETTER8 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter8')
    CUSTOM_LETTER9 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter9')
    CUSTOM_LETTER10 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter10')
    CUSTOM_LETTER11 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter11')
    CUSTOM_LETTER12 = (MobileBy.ID, 'online.paycash.app:id/et_custom_letter12')
    BTN_ENTER_PK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")')
    BTN_SCAN_QR = (MobileBy.ID, 'online.paycash.app:id/btnScanQr')
    FIELD_PRIVAT_KEY = (MobileBy.ID, 'online.paycash.app:id/et_input')
    TEXT_NOT_PRIVATE_KEY = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    BTN_DEL_PK = (MobileBy.ID, 'online.paycash.app:id/text_input_end_icon')
    TEXT_WARNING = (MobileBy.ID, 'online.paycash.app:id/ivWarning')
    BTN_ADD_ACC = (MobileBy.ID, 'online.paycash.app:id/addButton')
    SCREEN_MY_WALLET = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
    BTN_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/ll_username')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_SHOW_PK = (MobileBy.ID, 'online.paycash.app:id/btnShowPrivateKey')
    BTN_DELETE = (MobileBy.ID, 'online.paycash.app:id/btnRemove')
    BTN_CHANGE_AKK = (MobileBy.ID, 'online.paycash.app:id/tvAccountName')
    BTN_ADD_NEWACC = (MobileBy.ID, 'online.paycash.app:id/btnAdd')
    BTN_ENTER_PK_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnImportPrivateKey')
    BTN_CREATE_WALLET_POPUP = (MobileBy.ID, 'online.paycash.app:id/btnCreateNewWallet')
    BTN_LEFT_BUTTON = (MobileBy.ID, 'online.paycash.app:id/toolbar_left_button')
    BTN_LEFT_BACK = (MobileBy.ID, 'online.paycash.app:id/btnBack')
    BTN_BACK_WELCOME = (MobileBy.ID, 'online.paycash.app:id/btnBack')
    BTN_ADD_MORE_ACC = (MobileBy.ID, 'online.paycash.app:id/tvAdd')
    TEXT_ACC_ALREADY_ADD = (MobileBy.ID, 'online.paycash.app:id/tvTitle')

class LoginScreen(BaseScreen, Locators):

    def __init__(self, driver):
        super().__init__(driver)

    '''Screen Actions'''
    '''прокликать онбординг все экраны'''
    def tap_next_4_times(self):
        for i in range(4):
            self.tap(self.BTN_NEXT_ONBOARD)

    '''пропустить описание онбординга'''
    def tap_skip(self):
        self.tap(Locators.BTN_SKIP)

    '''прокликать 2 экрана онбординга и кликнуть назад. Прокликнуть онбординг до конца'''
    def tap_next_onboard(self):
        self.tap(Locators.BTN_NEXT_ONBOARD)
        self.tap(Locators.BTN_NEXT_ONBOARD)
        self.tap(Locators.BTN_BACK_ONBOARD)
        self.tap(Locators.BTN_NEXT_ONBOARD)
        self.tap(Locators.BTN_NEXT_ONBOARD)
        self.tap(Locators.BTN_NEXT_ONBOARD)

    '''ввести первый раз пин-код 0000 и подтвердить тоже 0000'''
    def tap_null_8_times(self):
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)

    '''ввести первый раз пин-код 0000'''
    def tap_null_4_times(self):
        for i in range(4):
            self.tap(self.BTN_NULL_PIN)

    '''подтвердить пин-код 1111, а не 0000'''
    def tap_one_4_times(self):
        for i in range(4):
            self.tap(self.BTN_ONE_PIN)

    '''вставить приватный ключ. Использую функцию ввести и подтвердить 0000, которая описана выше
    добавляю локатор чтобы кликнуть на кнопку вставить приватный ключ'''

    def insert_privat_key(self):
        self.tap_null_8_times()
        self.tap(Locators.BTN_ENTER_PK)

    '''ввести Использую функцию кликнуть Пропустить, потом ввести и подтвердить 0000, которая описана выше'''
    def enter_pin_code(self):
        self.tap_skip()
        self.is_visible(Locators.SCREEN_PIN)
        self.tap_null_8_times()

    '''Кликнуть только на кнопку "Вставить приватный ключ'''
    def enter_private_key_not_add_key(self):
        self.tap(Locators.BTN_SKIP)
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)

    '''Вставить ключ'''
    def send_private_key(self, private_key):
        self.send_keys(self.FIELD_PRIVAT_KEY, private_key)
        self.tap(self.BTN_ADD_ACC)

    '''Вставить приватный ключ и не кликать на кнопку добавить'''
    def enter_private_key_not_click_button(self, private_key):
        self.tap(Locators.BTN_SKIP)
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, private_key)
        self.tap(Locators.TEXT_WARNING)

    '''Первичный вход без онбординга'''
    def login_without_onboard(self):
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY)
        self.tap(Locators.TEXT_WARNING)
        self.tap(self.BTN_ADD_ACC)

    '''Вставить приватный ключ полностью'''
    def login_by_privat_key(self):
        self.tap(Locators.BTN_SKIP)
        for i in range(8):
            self.tap(self.BTN_NULL_PIN)
        self.tap(Locators.BTN_ENTER_PK)
        self.send_keys(self.FIELD_PRIVAT_KEY, TestData.PRIVAT_KEY)
        self.tap(Locators.TEXT_WARNING)
        self.tap(self.BTN_ADD_ACC)


    '''кликнуть на купить кошелек'''
    def create_wallet(self):
        self.enter_pin_code()
        self.tap(Locators.BTN_CREATE_WALLET)
