import requests
url = 'https://hyperion.listock.io/v2/history/get_transaction?id=e8a78a86c112b57a14af3a88972ff2fe91456eb63f685f07af6d70a1e6574b28'
r = requests.get(url)
data = r.json()
print(data['actions'][3]['act']['data']['quantity'])


'''обмен'''
'''сумма списания ID - 'локатор айдишника как текст
парсит сумму при обмене с гипериона'''
def parser_quantity_from_you(self, ID):
    url = f'https://hyperion.listock.io/v2/history/get_transaction?id={ID}'
    r = requests.get(url)
    data = r.json()
    quantity = data['actions'][1]['act']['data']['quantity']
    return quantity

"""парсит сумму получения после обмена с гипериона"""
def parser_quantity_to_you(self, ID):
    global quantity
    url = f'https://hyperion.listock.io/v2/history/get_transaction?id={ID}'
    r = requests.get(url)
    data = r.json()
    symbol = data['actions'][1]['act']['data']['symbol']
    if 'CASH' in symbol:
        quantity = data['actions'][8]['act']['data']['quantity']
    elif 'LI' in symbol:
        quantity = data['actions'][4]['act']['data']['quantity']
    elif 'EOS' in symbol:
        quantity = data['actions'][5]['act']['data']['quantity']
    return quantity



"""парсит сумму получения после обмена с гипериона"""

'''pars_1 = swap_screen.parser_quantity_from_you(swap_screen.get_text(Locators.POP_UP_TRANSACTION_ID))

а потом сравнить pars_1 c cуммой отправки с попапа

assert pop_up_1 == pars_1'''

