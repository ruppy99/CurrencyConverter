from app import *
from RealTimeCurrencyConverter import *


if __name__ == '__main__':
    currency_url = 'https://api.ratesapi.io/api/latest?base=USD'
    currency_converter = RealTimeCurrencyConverter(currency_url)

    App(currency_converter)
    mainloop()
