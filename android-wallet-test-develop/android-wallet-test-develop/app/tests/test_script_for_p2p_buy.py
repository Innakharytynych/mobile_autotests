from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'Pixel 3 API 28'
desired_caps['automationName'] = 'UiAutomator1'
desired_caps['newCommandTimeout'] = '600'
desired_caps['app'] = (r'D:\work\android-wallet-test\app\paycash.apk')
desired_caps['appPackage'] = 'online.paycash.app'
desired_caps['appActivity'] = 'online.paycash.app.ui.splash.OnboardingActivity'
desired_caps['clearSystemFiles'] = True
desired_caps['ignoreHiddenApiPolicyError'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(600)

key='5JX53ed9KHapu6UHBLyw4J6x1t1ss7WtvbZXKZS3Ex9HDzzq4jx'

def test_buy():
        for i in range(8):
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/cv_0').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter private key")').click()
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/et_input').send_keys(key)
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/ivWarning').click()
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/addButton').click()
        '''driver.find_element(MobileBy.ID, 'online.paycash.app:id/iv_configure').click()

        a = driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_version')
        TouchAction(driver).long_press(a, None, None, 6000).release().perform()

        driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_mainnet_preprod').click()
        for i in range(4):
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/cv_0').click()'''
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/navigation_pay_cash_buy').click()
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_create_order').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the purchase amount")').send_keys('0.1')
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Specify the country")').send_keys('Test')
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Specify a bank")').send_keys('Test')
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("New order").instance(0));').click()
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/btn_pick_password').click()
        for i in range(10):
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_create_order').click()
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Enter the purchase amount")').send_keys('0.1')
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Specify the country")').send_keys('Test')
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("Specify a bank")').send_keys('Test')
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_rate').click()
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/tv_create_order').click()
            driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("New order").instance(0));').click()
            driver.find_element(MobileBy.ID, 'online.paycash.app:id/btn_pick_password').click()