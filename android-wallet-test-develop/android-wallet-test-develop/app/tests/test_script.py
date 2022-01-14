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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(15)
key='5K2XugGyPq36YccG8LukxeNWLKMLdWiqwu4b1LNYhbeYqtUzi38'

driver.find_element(MobileBy.ID, 'online.paycash.app:id/btnSkip').click()

def test_wallet_main_screen():
    for i in range(4):
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/cv_0').click()
    for i in range(4):
        driver.find_element(MobileBy.ID, 'online.paycash.app:id/cv_0').click()

    driver.find_element(MobileBy.ID, 'online.paycash.app:id/ivPrivateKey').click()
    driver.find_element(MobileBy.ID, 'online.paycash.app:id/addButton').click()
    driver.find_element(MobileBy.ID, 'online.paycash.app:id/et_input').send_keys(key)
    driver.find_element(MobileBy.ID, 'online.paycash.app:id/addButton').click()




