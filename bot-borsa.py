import random
import os

from telegram.ext import Updater, CommandHandler

from iexfinance.stocks import Stock, get_historical_intraday

import matplotlib
import matplotlib.pyplot as plt


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Usa les comandes /preus i /grafica")


def preus(update, context):
    try:
        for simbol in context.args:
            quote = Stock(simbol)
            preu = quote.get_price()
            nom = quote.get_company()['companyName']
            missatge = "%s %s %s\n" % (simbol, nom, preu)
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=quote.get_logo()['url'])
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=missatge)
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')


def grafica(update, context):
    try:
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        dataframe = get_historical_intraday(
            context.args[0],
            output_format='pandas')
        dataframe = dataframe.filter(items=['close'])
        dataframe.plot()
        plt.savefig(fitxer, bbox_inches='tight')
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(fitxer, 'rb'))
        os.remove(fitxer)
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')


# hack pel Mac
matplotlib.use('Agg')

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('preus', preus))
dispatcher.add_handler(CommandHandler('grafica', grafica))

updater.start_polling()
