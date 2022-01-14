import pytest
from appium import webdriver

@pytest.fixture(scope='function')
def init_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'Pixel 3 API 28'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['newCommandTimeout'] = '600'
    desired_caps['app'] = (r'C:\Users\manet\Documents\android-wallet-test\app\paycash.apk')
    desired_caps['appPackage'] = 'online.paycash.app'
    desired_caps['appActivity'] = 'online.paycash.app.ui.splash.OnboardingActivity'
    '''desired_caps['clearSystemFiles'] = True'''
    desired_caps['noReset'] = True
    desired_caps['ignoreHiddenApiPolicyError'] = True
    desired_caps['autoGrantPermissions'] = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    driver.implicitly_wait(300)
    request.cls.driver = driver

    yield driver
    '''driver.quit()'''