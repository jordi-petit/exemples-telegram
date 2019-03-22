import random
import os

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_intraday

import matplotlib
import matplotlib.pyplot as plt


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Comandes: /preus i /grafica")


def preus(bot, update, args):
    try:
        for simbol in args:
            quote = Stock(simbol)
            preu = quote.get_price()
            nom = quote.get_company()['companyName']
            missatge = "%s %s %s\n" % (simbol, nom, preu)
            bot.send_photo(chat_id=update.message.chat_id, photo=quote.get_logo()['url'])
            bot.send_message(chat_id=update.message.chat_id, text=missatge)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def grafica(bot, update, args):
    try:
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        dataframe = get_historical_intraday(args[0], output_format='pandas')
        dataframe = dataframe.filter(items=['close'])
        dataframe.plot()
        plt.savefig(fitxer, bbox_inches='tight')
        bot.send_photo(chat_id=update.message.chat_id, photo=open(fitxer, 'rb'))
        os.remove(fitxer)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

# hack pel Mac
matplotlib.use('Agg')

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('preus', preus, pass_args=True))
dispatcher.add_handler(CommandHandler('grafica', grafica, pass_args=True))

updater.start_polling()

