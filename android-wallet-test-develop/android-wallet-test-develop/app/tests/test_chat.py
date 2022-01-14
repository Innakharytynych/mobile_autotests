from app.pages.chat_page import ChatScreen, Locators
from app.config.config import TestData
import pytest

@pytest.mark.usefixtures('init_driver')
class TestChat:
    '''Проверить элементы раздела со всеми чатами'''
    def test_chat_screen(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()

        assert chat_screen.is_visible(Locators.FIELD_SEARCH)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CREATE_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.DIALOG)
        assert chat_screen.is_visible(Locators.DIALOG_DATE)
        assert chat_screen.is_visible(Locators.DIALOG_AVATAR)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Проверить элементы существующего чата'''
    def test_chat_screen_chat(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)

        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_enable_to_tap(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_visible(Locators.YOUR_MESSAGE)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Создать чат с новым аккаунтом'''
    def test_chat_screen_create_chat(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_SEARCH_ACCOUNT)
        chat_screen.send_keys(Locators.POP_UP_NEW_ACCOUNT, TestData.RECEIVER2)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)

        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.TEXT_WARNING_CHAT)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)
        assert chat_screen.is_invisible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_invisible(Locators.YOUR_MESSAGE)

    '''Ввести в поле поиска имя аккаунта, с которым чат уже есть'''
    def test_chat_screen_create_old_chat(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_SEARCH_ACCOUNT)
        chat_screen.send_keys(Locators.POP_UP_NEW_ACCOUNT, TestData.RECEIVER)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)

        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Попробовать создать чат с несуществующим аккаунтом'''
    def test_chat_screen_create_chat_incorrect_account(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_SEARCH_ACCOUNT)
        chat_screen.send_keys(Locators.POP_UP_NEW_ACCOUNT, TestData.NAME_INCORRECT)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)

        assert chat_screen.is_visible(Locators.TEXT_INCORRECT_ACCOUNT)
        assert chat_screen.is_enable_to_tap(Locators.POP_UP_CREATE_CHAT)
        assert chat_screen.is_visible(Locators.TEXT_NEW_CHAT)
        assert chat_screen.is_visible(Locators.TEXT_DESCRIPTION)

    '''Попробовать создать чат с несуществующим аккаунтом, потом с существующим'''
    def test_chat_screen_create_chat_incorrect_correct_account(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_SEARCH_ACCOUNT)
        chat_screen.send_keys(Locators.POP_UP_NEW_ACCOUNT, TestData.NAME_INCORRECT)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)
        chat_screen.clear(Locators.POP_UP_NEW_ACCOUNT)
        chat_screen.send_keys(Locators.POP_UP_NEW_ACCOUNT, TestData.RECEIVER)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)

        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_visible(Locators.YOUR_MESSAGE)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Не ввести имя собеседника, попробовать создать чат'''
    def test_chat_screen_create_chat_without_name(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_SEARCH_ACCOUNT)
        chat_screen.tap(Locators.POP_UP_CREATE_CHAT)

        assert chat_screen.is_disable_to_tap(Locators.POP_UP_CREATE_CHAT)

    '''Выбрать из галереи корректный QR код'''
    def test_chat_screen_create_chat_from_gallery(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_FROM_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_QR)

        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        '''assert chat_screen.is_visible(Locators.YOUR_MESSAGE)'''
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Выбрать из галереи не корректный QR код. Нужно выбрать поискать код и как то загрузить в эмулятор'''
    def test_chat_screen_create_chat_from_gallery_incorrect(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.BTN_CREATE_CHAT)
        chat_screen.tap(Locators.POP_UP_FROM_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_DOWNLOAD)
        chat_screen.tap(Locators.BTN_CHOOSE_QR_DOWNLOAD)

        '''assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_visible(Locators.YOUR_MESSAGE)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)'''

    '''Поиск в списке чатов корректного имени собеседника, с которым есть чат'''
    def test_chat_search_correct_name(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.RECEIVER)

        assert chat_screen.is_visible(Locators.SEARCH_NAME)
        assert chat_screen.is_enable_to_tap(Locators.DIALOG)
        assert chat_screen.is_visible(Locators.DIALOG_DATE)
        assert chat_screen.is_visible(Locators.DIALOG_AVATAR)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Ввести в поиск сообщение, которое есть где-то в чатах'''
    def test_chat_search_correct_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.MESSAGE)

        assert chat_screen.is_visible(Locators.MESSAGE_TEXT)
        assert chat_screen.is_enable_to_tap(Locators.DIALOG)
        assert chat_screen.is_visible(Locators.DIALOG_DATE)
        assert chat_screen.is_visible(Locators.DIALOG_AVATAR)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Ввести в поиск сообщение, которого нет в чатах'''
    def test_chat_search_incorrect_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.MEMO)

        assert chat_screen.is_visible(Locators.IMAGE_NOTHING)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING_FOUND)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Поиск в списке чатов корректного имени собеседника, с которым нет чата'''
    def test_chat_search_correct_name_without_chat(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.NAME_CHAT)

        assert chat_screen.is_visible(Locators.IMAGE_NOTHING)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING_FOUND)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Ввести в поиск свое имя'''
    def test_chat_search_correct_yourself_name(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.RECIPIENT)

        assert chat_screen.is_visible(Locators.IMAGE_NOTHING)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING_FOUND)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Поиск в списке чатов некорректного имени собеседника'''
    def test_chat_search_incorrect_name(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.FIELD_SEARCH)
        chat_screen.send_keys(Locators.FIELD_SEARCH, TestData.NAME_INCORRECT)

        assert chat_screen.is_visible(Locators.IMAGE_NOTHING)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING_FOUND)
        assert chat_screen.is_visible(Locators.TEXT_NOTHING)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Отправить сообщение в чат'''
    def test_chat_send_correct_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.FIELD_MESSAGE)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)

        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Нажать кнопку отправки без текста в поле сообщения'''
    def test_chat_send_without_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)

        assert chat_screen.is_enable_to_tap(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Отправить несколько сообщений в чат'''
    def test_chat_send_correct_3message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.FIELD_MESSAGE)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)

        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Отправить сообщение в чат, сменить аккаунт, посмотреть что сообщение пришло'''
    def test_chat_send_receive_correct_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.FIELD_MESSAGE)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)
        chat_screen.tap(Locators.BTN_LEFT_BACK)
        chat_screen.tap(Locators.TEXT_AKK_NAME)
        chat_screen.tap(Locators.BTN_CHANGE_AKK1)
        chat_screen.swipe_element_down(Locators.BTN_CHAT)

        assert chat_screen.is_visible(Locators.UNREAD_MESSAGE)
        assert chat_screen.is_visible(Locators.NEW_MESSAGE_FUTER)
        assert chat_screen.get_text(Locators.TEXT_AKK_NAME, '521115.pcash')
        assert chat_screen.is_visible(Locators.FIELD_SEARCH)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CREATE_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.DIALOG)
        assert chat_screen.is_visible(Locators.DIALOG_DATE)
        assert chat_screen.is_visible(Locators.DIALOG_AVATAR)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Попробовать отправить длинное сообщение в чат'''
    def test_chat_send_long_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.FIELD_MESSAGE)
        chat_screen.send_keys(Locators.FIELD_MESSAGE, TestData.LONG_MESSAGE)
        chat_screen.tap(Locators.BTN_MESSAGE_SEND)

        assert chat_screen.get_text2(Locators.FIELD_MESSAGE) == 'Message'
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Удалить сообщение в чате'''
    def test_chat_delete_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.swipe_element_right_to_left(Locators.MESSAGE_TEXT)

        assert chat_screen.is_visible(Locators.MY_MESSAGE_TEST)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Удалить чат'''
    def test_chat_delete_chat(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.swipe_element_right_to_left(Locators.DIALOG2)

        assert chat_screen.is_visible(Locators.FIELD_SEARCH)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CREATE_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.DIALOG)
        assert chat_screen.is_visible(Locators.DIALOG_DATE)
        assert chat_screen.is_visible(Locators.DIALOG_AVATAR)
        assert chat_screen.is_enable_to_tap(Locators.BTN_WALLET)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_SELL)
        assert chat_screen.is_enable_to_tap(Locators.BTN_BUY)
        assert chat_screen.is_enable_to_tap(Locators.BTN_OTHER)
        assert chat_screen.is_enable_to_tap(Locators.BTN_RES_AND_TRANS)

    '''Выбрать корректный QR из галереи и отправить. Проверить ассерт'''
    def test_chat_send_qr_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_QR_CHAT)
        chat_screen.tap(Locators.BTN_QR_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_QR)

        '''assert chat_screen.is_enable_to_tap(Locators.BTN_QR_IMAGE_SAVE)'''
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Выбрать корректный QR из галереи и отправить. Сохранить отправленный код'''
    def test_chat_save_qr_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_QR_CHAT)
        chat_screen.tap(Locators.BTN_QR_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_GALLERY)
        chat_screen.tap(Locators.BTN_CHOOSE_QR)
        chat_screen.tap(Locators.BTN_QR_IMAGE_SAVE)

        assert chat_screen.is_visible(Locators.TEXT_QR_IMAGE_SAVE)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Сохранить полученный qr код'''
    def test_chat_download_qr_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_QR_IMAGE_DOWNLOAD)

        assert chat_screen.is_visible(Locators.TEXT_QR_IMAGE_SAVE)
        assert chat_screen.is_enable_to_tap(Locators.BTN_QR_CHAT)
        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER_CHAT)
        assert chat_screen.is_visible(Locators.FIELD_MESSAGE)
        assert chat_screen.is_visible(Locators.BTN_MESSAGE_SEND)
        assert chat_screen.is_visible(Locators.RECIPIENT_NAME_NEW)
        assert chat_screen.is_visible(Locators.BTN_RES_AND_TRANS)

    '''Кликнуть на полученный qr-код'''
    def test_chat_tap_download_qr_message(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_QR_IMAGE)

        assert chat_screen.is_enable_to_tap(Locators.BTN_TRANSFER)
        assert chat_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert chat_screen.is_visible(Locators.FIELD_RECEIVER)
        assert chat_screen.is_visible(Locators.FIELD_SUMM)
        assert chat_screen.is_visible(Locators.FIELD_MEMO)

    '''ТРАНСФЕР С ЧАТА'''
    '''Проверить элементы раздела. Должно быть заполнено только имя получателя'''
    def test_chat_transfer_screen(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        '''name = chat_screen.get_text2(Locators.RECIPIENT_NAME_NEW)'''
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)

        assert chat_screen.get_text2(Locators.FIELD_RECEIVER) == '521115.pcash'
        assert chat_screen.is_visible(Locators.CHOOSE_TOKEN)
        assert chat_screen.is_visible(Locators.FIELD_RECEIVER)
        assert chat_screen.is_visible(Locators.FIELD_SUMM)
        assert chat_screen.is_visible(Locators.FIELD_MEMO)
        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Трансфер корректной суммы'''
    def test_chat_transfer_screen_correct(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)


    '''Трансфер корректной суммы. Смена токена'''
    def test_chat_transfer_screen_correct_change_token(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_RUBCASH)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Пропустить выбор токена'''
    def test_chat_transfer_screen_no_token(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)
        assert chat_screen.is_visible(Locators.FIELD_RECEIVER)
        assert chat_screen.is_visible(Locators.FIELD_SUMM)
        assert chat_screen.is_visible(Locators.FIELD_MEMO)

    '''Трансфер большей суммы, чем есть на счету'''
    def test_chat_transfer_screen_big_summ(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_visible(Locators.TEXT_INPUT_ERROR)
        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)
        assert chat_screen.is_visible(Locators.FIELD_RECEIVER)
        assert chat_screen.is_visible(Locators.FIELD_SUMM)
        assert chat_screen.is_visible(Locators.FIELD_MEMO)

    '''Трансфер корректной суммы. Пропустить ввод мемо'''
    def test_chat_transfer_screen_correct_without_memo(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Изменить имя получателя'''
    def test_chat_transfer_screen_correct_change_name_reciver(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.clear(Locators.FIELD_RECEIVER)
        chat_screen.send_keys(chat_screen.FIELD_RECEIVER, TestData.RECEIVER2)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Удаление имени, которое было, ввод не корректного имени, удаление, ввод корректного имени'''
    def test_chat_transfer_screen_incorrect_correct_change_name_reciver(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.clear(Locators.FIELD_RECEIVER)
        chat_screen.send_keys(chat_screen.FIELD_RECEIVER, TestData.NAME_INCORRECT)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.clear(Locators.FIELD_RECEIVER)
        chat_screen.send_keys(chat_screen.FIELD_RECEIVER, TestData.RECEIVER2)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Попытка перевести меньше 0,00001 CASH'''
    def test_chat_transfer_min_amount_CASH(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_CASH)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевести меньше 0.00001 EOS'''
    def test_chat_transfer_min_amount_EOS(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_EOS)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_EOS)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода меньшей суммы LQ чем 1.0000 из чата'''
    def test_chat_transfer_min_amount_LQ(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_LQ)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_MIN_LQ)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Попытка перевода 0.0000 из чата'''
    def test_chat_transfer_zero(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_ZERO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Изменить аккаунт из трансфера чата'''
    def test_chat_transfer_change_account(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.TEXT_AKK_NAME)

        assert chat_screen.is_disable_to_tap(Locators.TEXT_AKK_NAME)

    '''Ввести первую сумму, удалить, ввод корректной суммы'''
    def test_chat_transfer_screen_incorrect_correct_summ(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.send_keys(chat_screen.FIELD_RECEIVER, TestData.RECEIVER)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_BIG)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.clear(Locators.FIELD_SUMM)
        chat_screen.send_keys(Locators.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert chat_screen.conver_in_num(Locators.TEXT_POPUP_VALUE) == chat_screen.conver_in_num(TestData.SUM_TRANSFER)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

    '''Удалить общую сумму, попробовать сделать трансфер'''
    def test_chat_transfer_without_all_summ(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.clear(Locators.FIELD_SUMM_TOTAL)
        chat_screen.tap(Locators.FIELD_MEMO)
        chat_screen.send_keys(chat_screen.FIELD_MEMO, TestData.MEMO)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)

        assert chat_screen.is_disable_to_tap(Locators.BTN_TRANSFER)

    '''Трансфер с ограничением максимальной комиссии в 250 токенов'''
    def test_chat_transfer_commission_250(self):
        chat_screen = ChatScreen(self.driver)
        chat_screen.open_chat()
        chat_screen.tap(Locators.DIALOG)
        chat_screen.tap(Locators.BTN_TRANSFER_CHAT)
        chat_screen.tap(Locators.CHOOSE_TOKEN)
        chat_screen.tap(Locators.TOKEN_NAME_UAHCASH)
        chat_screen.tap(Locators.FIELD_SUMM)
        chat_screen.send_keys(chat_screen.FIELD_SUMM, TestData.SUM_TRANSFER_250_COMMISSION)
        chat_screen.tap(Locators.TEXT_YOU_SEND)
        chat_screen.tap(Locators.BTN_TRANSFER)
        commission = chat_screen.conver_in_num(Locators.TEXT_POPUP_COMMISSION)
        chat_screen.tap(Locators.BTN_TRANSFER_CONFIRM)

        assert commission == chat_screen.conver_in_num(TestData.MAX_COMMISSION)
        assert chat_screen.get_text2(Locators.TEXT_POPUP_TOKEN) == 'UAHCASH'
        assert chat_screen.is_visible(Locators.TEXT_ID_TRANSACTION)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_VALUE)
        assert chat_screen.is_visible(Locators.TEXT_POPUP_TOKEN)
        assert chat_screen.is_enable_to_tap(Locators.BTN_CHECK_BLOCKSIO)

