from appium.webdriver.common.mobileby import MobileBy
from app.pages.base_page import BaseScreen
from app.config.config import TestData
from selenium.webdriver.common.by import By


class Locators:
    BTN_SKIP = (MobileBy.ID, 'online.paycash.app:id/btnSkip')
    BTN_NULL_PIN = (MobileBy.ID, 'online.paycash.app:id/cv_0')
    BTN_ENTER_PK = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")')
    FIELD_PRIVAT_KEY = (MobileBy.ID, 'online.paycash.app:id/et_input')
    TEXT_WARNING = (MobileBy.ID, 'online.paycash.app:id/ivWarning')
    BTN_ADD_ACC = (MobileBy.ID, 'online.paycash.app:id/addButton')
    BTN_WITHDRAW = (MobileBy.ID, 'online.paycash.app:id/fl_p2p_sell')
    BTN_NO_CARD = (MobileBy.ID, 'online.paycash.app:id/iv_bank_card')
    BTN_ADD_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_action')
    FIELD_CARD_NUMBER = (MobileBy.ID, 'online.paycash.app:id/et_card_number')
    FIELD_COUNTRY = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')
    FIELD_BANK = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText')
    CHEKBOX_DEFAULT_CARD = (MobileBy.ID, 'online.paycash.app:id/sw_make_default')
    BTN_SAVE_CARD = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Save")')
    TEXT_MY_CARD = (MobileBy.ANDROID_UIAUTOMATOR, 'text("My card")')
    CARD_DETAILS = (MobileBy.ID, 'online.paycash.app:id/toolbar_title')
    BLOCK_CARD = (MobileBy.ID, 'online.paycash.app:id/balanceCard')
    BLOCK_CARD_NUMBER= (MobileBy.ID, 'online.paycash.app:id/tv_card_number')
    BLOCK_CARD_BANK = (MobileBy.ID, 'online.paycash.app:id/tv_bank')
    BLOCK_CARD_COUNTRY = (MobileBy.ID, 'online.paycash.app:id/tv_country')
    TEXT_INCORRECT_CARD = (MobileBy.ID, 'online.paycash.app:id/textinput_error')
    BTN_ADD_MORE_CARDS = (MobileBy.ID, 'online.paycash.app:id/btn_add_bank_card')
    BTN_LEFT_BUTTON = (MobileBy.ID, 'online.paycash.app:id/toolbar_left_button')
    BTN_TREE_DOTS = (MobileBy.ID, 'online.paycash.app:id/iv_right')
    BTN_TREE_DOTS2 = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView[2]')
    BTN_MAKE_DEFAULT_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_make_default_card')
    BTN_DELETE_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_remove_card')
    BTN_CONFIRM_DELETE_CARD = (MobileBy.ID, 'online.paycash.app:id/btn_got_it')
    BTN_CANCEL_DELETE_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_negative_action')
    EDIT_CARD = (MobileBy.ID, 'online.paycash.app:id/tv_edit_card')
    TEXT_MAIN_CARD = (MobileBy.ANDROID_UIAUTOMATOR, 'text("Main")')
    BTN_SETTINGS = (MobileBy.ID, 'online.paycash.app:id/iv_configure')
    TEXT_AKK_NAME = (MobileBy.ID, 'online.paycash.app:id/text_username')
    BTN_VERSION = (MobileBy.ID, 'online.paycash.app:id/tv_version')
    BTN_PROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_prod')
    BTN_PREPROD = (MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod')

class CardScreen(BaseScreen, Locators):

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