from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

'''This class is the parents for all screen'''
'''is contains all the generic methods and utilities for all screen'''


class BaseScreen:
    """инициализация драйвера"""
    def __init__(self, driver):
        self.driver = driver

    '''нажать (тапнуть)'''
    def tap(self, by_locators, timeout=200):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find tap element by locator {by_locators}")
        e.click()

    '''окно выбора прод/препрод'''
    def change_prod_preprod(self, by_locators, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                  message=f"Can't find tap and hold element by locator {by_locators}")
        a = self.driver.find_element_by_id('online.paycash.app:id/tv_version')
        TouchAction(self.driver).long_press(a, 5).perform()

    '''ввести в поле текст'''
    def send_keys(self, by_locators, data, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find tap element by locator {by_locators}")
        e.send_keys(data)

    '''очистить текстовое поле'''
    def clear(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find tap element by locator {by_locators}")
        e.clear()

    '''элемент виден'''
    def is_visible(self, by_locators, timeout=200):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                         message=f"Can't find visible element by locator {by_locators}")

    '''элемент не виден'''
    def is_invisible(self, by_locators, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by_locators),
                                                         message=f"Can't find invisible element by locator {by_locators}")

    '''элемент доступен для нажатия (кликабелен)'''
    def is_enable_to_tap(self, by_locators, timeout=200):
        e = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locators),
                                                      message=f"Can't find enable tap element by locator {by_locators}")
        return e

    '''элемент не доступен для нажатия (не кликабелен)'''
    def is_disable_to_tap(self, by_locators, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators) and
                                                      EC.element_to_be_clickable(by_locators),
                                                      message=f"Can't find disable tap element by locator {by_locators}")
        except:
            return True

    '''наличие элемента (мб не виден, но доступен)'''
    def is_presence(self, by_locators, timeout=300):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locators),
                                                         message=f"Can't find visible element by locator {by_locators}")

    '''наличие элемента (мб виден, но недоступен)'''
    def is_inpresence(self, by_locators, timeout=300):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locators),
                                                         message=f"Can't find visible element by locator {by_locators}")

    '''получить и сравнить текст'''
    def get_text(self, by_locators, text, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(by_locators, text),
                                                      message=f"Can't find text on element by locator {by_locators}")
        return e

    '''получить текст'''
    def get_text2(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locators),
                                                      message=f"Can't find text on element by locator {by_locators}")
        return e.text

    '''свайп справа налево'''
    def swipe_element_right_to_left(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find invisible element by locator {by_locators}")
        elementSize = e.size

        elementWidth = elementSize['width']
        elementHeight = elementSize['height']
        startx = elementWidth * 8 / 9
        endx = elementWidth / 9
        starty = elementHeight / 2
        endy = elementHeight / 2

        TouchAction(self.driver).press(e, startx, starty).wait(1000).move_to(e, endx, endy).release().perform()

    '''свайп слева направо'''
    def swipe_element_left_to_right(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find invisible element by locator {by_locators}")
        elementSize = e.size

        elementWidth = elementSize['width']
        elementHeight = elementSize['height']
        startx = elementWidth / 9
        endx = elementWidth * 8 / 9
        starty = elementHeight / 2
        endy = elementHeight / 2

        TouchAction(self.driver).press(e, startx, starty).wait(1000).move_to(e, endx, endy).release().perform()

    '''свайп вниз'''
    def swipe_element_down(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find invisible element by locator {by_locators}")
        elementSize = e.size

        elementWidth = elementSize['width']
        elementHeight = elementSize['height']
        startx = elementWidth / 2
        endx = elementWidth / 2
        starty = elementHeight * 2 / 9
        endy = elementHeight * 8 / 9

        TouchAction(self.driver).press(e, startx, starty).wait(1000).move_to(e, endx, endy).release().perform()

    '''свайп верх'''
    def swipe_element_up(self, by_locators, timeout=10):
        e = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locators),
                                                      message=f"Can't find invisible element by locator {by_locators}")
        elementSize = e.size

        elementWidth = elementSize['width']
        elementHeight = elementSize['height']
        startx = elementWidth / 2
        endx = elementWidth / 2
        starty = elementHeight * 8 / 9
        endy = elementHeight / 9

        TouchAction(self.driver).press(e, startx, starty).wait(1000).move_to(e, endx, endy).release().perform()


