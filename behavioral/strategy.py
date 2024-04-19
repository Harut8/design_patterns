"""
One day you decided to create a navigation app for casual travelers.
The app was centered around a beautiful map which helped users quickly orient themselves in any city.

One of the most requested features for the app was automatic route planning.
A user should be able to enter an address and see the fastest route to that destination displayed on the map.

The first version of the app could only build the routes over roads.
People who traveled by car were bursting with joy. But apparently, not everybody likes to drive on their vacation.
So with the next update, you added an option to build walking routes.
Right after that, you added another option to let people use public transport in their routes.

However, that was only the beginning. Later you planned to add route building for cyclists.
And even later, another option for building routes through all of a city’s tourist attractions.
"""

from abc import ABC, abstractmethod


class SellCrypto(ABC):
    @abstractmethod
    def sell_crypto(self):
        pass


class SellBitcoin(SellCrypto):
    def sell_crypto(self):
        print("Selling Bitcoin")


class SellEthereum(SellCrypto):
    def sell_crypto(self):
        print("Selling Etherium")


class SellRipple(SellCrypto):
    def sell_crypto(self):
        print("Selling Ripple")


class TradingBot:
    def __init__(self, sell_crypto: SellCrypto):
        self.sell_crypto = sell_crypto

    def trade(self):
        self.sell_crypto.sell_crypto()


def test():
    trading_bot = TradingBot(SellBitcoin())
    trading_bot.trade()

    trading_bot = TradingBot(SellEthereum())
    trading_bot.trade()

    trading_bot = TradingBot(SellRipple())
    trading_bot.trade()
