import random
import os

from staticmap import StaticMap, CircleMarker

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Envia'm la teva localització!")


def where(bot, update, user_data):
    try:
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        lat, lon = update.message.location.latitude, update.message.location.longitude
        mapa = StaticMap(500, 500)
        mapa.add_marker(CircleMarker((lon, lat), 'blue', 10))
        imatge = mapa.render()
        imatge.save(fitxer)
        bot.send_photo(chat_id=update.message.chat_id, photo=open(fitxer, 'rb'))
        os.remove(fitxer)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.location, where, pass_user_data=True))

updater.start_polling()

