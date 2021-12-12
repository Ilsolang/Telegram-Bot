#from pycbrf import ExchangeRates
#from config import bot
#import decimal

def rate_cbr(m):
    rates = ExchangeRates(locale_en=True)
    print(rates['USD'].rate)
    usd = decimal.Decimal(rates['USD'].rate)
    bot.send_message(m.chat.id, "курс доллара к рублю: " + usd() + "Р")

    