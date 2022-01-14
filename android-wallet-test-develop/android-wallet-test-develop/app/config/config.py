class TestData:
    PRIVAT_KEY = '5KZdybonoATbzWj5WcvmRZkM65RffYsThoVA94H14BRMkpzWJw9'
    PRIVAT_KEY_M4 = '5J3adwNbtBLgFxGa9TmBaZFqaBk9Eay3CdQwkhDVm7RkfQhX8tQ'
    RECEIVER = 'fletchercat1'
    RECEIVER2 = 'avpw.pcash'
    RECIPIENT = 'loveisinair1'

    NAME_CHAT = 'innakharytyn'
    MESSAGE = 'Test'
    LONG_MESSAGE = 'Возьмём теперь вопрос о разных мелких группах внутри нашей цивилизации. Чем больше население, тем больше таких групп. И берегитесь обидеть которую-нибудь из них — любителей собак или кошек, врачей, адвокатов, торговцев, начальников, мормонов, баптистов, унитариев, потомков китайских, шведских, итальянских, немецких эмигрантов, техасцев, бруклинцев, ирландцев, жителей штатов Орегон или Мехико. Герои книг, пьес, телевизионных передач не должны напоминать подлинно существующих художников, картографов, механиков. Запомните, Монтэг, чем шире рынок, тем тщательнее надо избегать конфликтов. Все эти группы и группочки, созерцающие собственный пуп, — не дай бог как-нибудь их задеть! Злонамеренные писатели, закройте свои пишущие машинки! Ну что ж, они так и сделали. Журналы превратились в разновидность ванильного сиропа. Книги — в подслащённые помои. Так, по крайней мере, утверждали критики, эти заносчивые снобы. Не удивительно, говорили они, что книг никто не покупает.'

    SUM_TRANSFER = '0.01000'
    SUM_RECEIVE = '0.1'
    SUM_RECEIVE2 = '1.5'
    MEMO = 'some text'
    SUM_TRANSFER_BIG = '100000000000'
    SUM_TRANSFER_MIN_CASH = '0.00000001'
    SUM_TRANSFER_MIN_EOS = '0.00000001'
    SUM_TRANSFER_250_COMMISSION = '125000.00000'
    MAX_COMMISSION = '250'
    SUM_TRANSFER_MIN_LQ = '0.5'
    SUM_EXCHANGE = '1.05000'
    SUM_EXCHANGE_EOS = '0.1'
    SUM_EXCHANGE_LQ = '85000'
    SUM_EXCHANGE_LI = '0.1'
    SUM_MIN_EXCHANGE = '0.001'
    SUM_MAX_EXCHANGE = '10000000000'
    SUM_ZERO = '0'
    SUM_SWAP = '1.25'
    SUM_SWAP_MIN_CASH = '0.000005'
    SUM_SWAP_MIN_LI = '0.00000005'
    SUM_SWAP_MIN_LQ = '0.5'
    SUM_SWAP_ADD_POOL1 = '1'
    SUM_SWAP_ADD_POOL2 = '3'
    SUM_SWAP_WITHDRAW = '50'
    SUM_SWAP_DROB = '50.5'
    SUM_SWAP_MAX = '100000000000000000'

    NAME_INCORRECT = 'fdgfgfgfgngn'
    CARD_NUMBER1 = '4141414141414'
    CARD_NUMBER2 = '4111111111111111'

    SELL_AMOUNT = '0.10000'
    MIN_SELL_AMOUNT = '0.00100'
    MAX_SELL_AMOUNT = '1000000000000'
    MAX_BUY_AMOUNT = '10000000000000'
    MIN_BUY_AMOUNT = '0.00100'
    MIN_SELL_LIMIT = '0.01000'
    MAX_SELL_LIMIT = '1.00000'
    LINK = 'wikipedia.org'
    COUNTRY = 'USA'
    BANK = 'WORLD'

    def short_key(self=None):
        return '5KhuPq1BndMZybu7shtEDomXvpLoZjdqPLqB1HZK4'

    def long_key(self=None):
        return '5khyPq1BndMZybu7shtEDomXvpLoZjdqPLqB1HZK4xgZgRcM4TZ1234'

    def public_key(self=None):
        return 'EOS5crSmt8jDnFcvy3YiAX6GM9GUWD6Zz8eoCYvLnq1r2S8WA2jr3'

    def privat_key_another_blockchain(self=None):
        return '1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm'

    def incorrect_key(self=None):
        return '5KhuPq1BndMZybu7shtEDomXvpLoZjdqPLqB1HZK4xgZgRjkhfr'

    def incorrect_card(self=None):
        return '4242424242424246'

    def short_card(self=None):
        return '424242424'

    def long_card(self=None):
        return '4242424242424246456567566678'