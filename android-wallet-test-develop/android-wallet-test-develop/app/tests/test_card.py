from app.pages.card_page import CardScreen, Locators
from app.config.config import TestData
import pytest


@pytest.mark.usefixtures('init_driver')
class TestCard:

    '''проверить экран добавления карты'''
    def test_card_screen(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)

        assert card_screen.is_visible(Locators.FIELD_CARD_NUMBER)
        assert card_screen.is_visible(Locators.CHEKBOX_DEFAULT_CARD)
        assert card_screen.is_visible(Locators.FIELD_COUNTRY)
        assert card_screen.is_visible(Locators.FIELD_BANK)
        assert card_screen.is_disable_to_tap(Locators.BTN_SAVE_CARD)

    '''Добавить первую корректную карту'''
    def test_add_card(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить вторую корректную карту'''
    def test_add_more_card(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        card_screen.tap(Locators.BTN_ADD_MORE_CARDS)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4141414141414')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить вторую корректную карту. Сделать ее основной'''
    def test_add_more_card2(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        card_screen.tap(Locators.BTN_ADD_MORE_CARDS)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4141414141414')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)
        card_screen.tap(Locators.BTN_TREE_DOTS2)
        card_screen.tap(Locators.BTN_MAKE_DEFAULT_CARD)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.TEXT_MAIN_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить первую корректную карту. Отредактировать номер'''
    def test_edit_card(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.FIELD_CARD_NUMBER)
        card_screen.clear(Locators.FIELD_CARD_NUMBER)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4141414141414')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.TEXT_MAIN_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить первую корректную карту. Отредактировать страну'''
    def test_edit_card_country(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.FIELD_COUNTRY)
        card_screen.clear(Locators.FIELD_COUNTRY)
        card_screen.send_keys(Locators.FIELD_COUNTRY, 'test')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить первую корректную карту. Отредактировать страну'''
    def test_edit_card_bank(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.FIELD_BANK)
        card_screen.clear(Locators.FIELD_BANK)
        card_screen.send_keys(Locators.FIELD_BANK, 'test')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.BTN_SAVE_CARD)

        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)

    '''Добавить некорректную карту'''
    def test_add_incorrect_card(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4211111111111111')
        card_screen.send_keys(Locators.FIELD_COUNTRY, 'test')
        card_screen.send_keys(Locators.FIELD_BANK, 'test')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.BTN_SAVE_CARD)

        assert card_screen.is_disable_to_tap(Locators.BTN_SAVE_CARD)
        assert card_screen.is_visible(Locators.TEXT_INCORRECT_CARD)

    '''Добавить корректную карту, удалить страну'''
    def test_add_correct_card_del_country(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.clear(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.CARD_DETAILS)

        assert card_screen.is_disable_to_tap(Locators.BTN_SAVE_CARD)

    '''Добавить корректную карту, удалить страну'''
    def test_add_correct_card_del_bank(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.clear(Locators.FIELD_BANK)
        card_screen.tap(Locators.CARD_DETAILS)

        assert card_screen.is_disable_to_tap(Locators.BTN_SAVE_CARD)

    '''Добавить вторую корректную карту. Удалить первую'''
    def test_add_more_card_del(self):
        card_screen = CardScreen(self.driver)
        card_screen.login_without_onboard()
        card_screen.tap(Locators.BTN_WITHDRAW)
        card_screen.tap(Locators.BTN_NO_CARD)
        card_screen.tap(Locators.BTN_ADD_CARD)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4111111111111111')
        card_screen.tap(Locators.CARD_DETAILS)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        card_screen.tap(Locators.BTN_ADD_MORE_CARDS)
        card_screen.send_keys(Locators.FIELD_CARD_NUMBER, '4141414141414')
        card_screen.tap(Locators.CARD_DETAILS)
        COUNTRY = card_screen.get_text2(Locators.FIELD_COUNTRY)
        card_screen.tap(Locators.BTN_SAVE_CARD)
        COUNTRY2 = card_screen.get_text2(Locators.BLOCK_CARD_COUNTRY)
        card_screen.tap(Locators.BTN_TREE_DOTS)
        card_screen.tap(Locators.BTN_DELETE_CARD)
        card_screen.tap(Locators.BTN_CONFIRM_DELETE_CARD)

        assert COUNTRY == COUNTRY2
        assert card_screen.is_visible(Locators.BLOCK_CARD)
        assert card_screen.is_visible(Locators.TEXT_MAIN_CARD)
        assert card_screen.is_visible(Locators.BLOCK_CARD_NUMBER)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_visible(Locators.BTN_SETTINGS)
        assert card_screen.is_visible(Locators.BLOCK_CARD_COUNTRY)
        assert card_screen.is_enable_to_tap(Locators.BTN_TREE_DOTS)
        assert card_screen.is_enable_to_tap(Locators.BTN_ADD_MORE_CARDS)
        assert card_screen.is_enable_to_tap(Locators.BTN_LEFT_BUTTON)
