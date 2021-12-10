from plug.base64 import encoder, decoder
from config import bot
from plug.web import webcheck, findip, scan
from plug.start import start, help, send_text
from plug.animals import cats, dogs
from plug.chat import get_id, id_chat
#from plug.rate import rate_dollar, rate_rub, rate_btc, rate_euro
#from plug.ratecbr import rate_cbr

@bot.message_handler(commands=['start'])
def any_start(m):
    start(m)

@bot.message_handler(commands=['help'])
def any_help(m):
    help(m)

#@bot.message_handler(commands=['ratteBTC'])
#def any_ratecbr(m):
#    rate_cbr(m)

@bot.message_handler(commands=['id'])
def any_id(m):
    get_id(m)

@bot.message_handler(commands=['chatid'])
def any_chatid(m):
    id_chat(m)

@bot.message_handler(commands=['encode'])
def any_encode(m):
    encoder(m)

@bot.message_handler(commands=['decode'])
def any_decode(m):
    decoder(m)

@bot.message_handler(commands=['webcheck'])
def any_webcheck(m):
    webcheck(m)

@bot.message_handler(commands=['ipweb'])
def any_ipweb(m):
    findip(m)

@bot.message_handler(commands=['webscanner'])
def any_webscanner(m):
    scan(m)

#@bot.message_handler(commands=['dollar'])
#def any_dollar(m):
#    rate_dollar(m)
    
#@bot.message_handler(commands=['btcrub'])
#def any_btcrub(m):
#     rate_rub(m)

#@bot.message_handler(commands=['euro'])
#def any_euro(m):
#    rate_euro(m)

#@bot.message_handler(commands=['btcdoll'])
#def any_btc(m):
#    rate_btc(m)

@bot.message_handler(commands=['cats'])
def any_cats(m):
    cats(m)

@bot.message_handler(commands=['dogs'])
def any_dogs(m):
    dogs(m)

@bot.message_handler(content_types=['text'])
def any_text(m):
    send_text(m)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)