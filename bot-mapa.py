import random
import os

from staticmap import StaticMap, CircleMarker

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Envia'm la teva localització!")


def where(update, context):
    try:
        lat, lon = update.message.location.latitude, update.message.location.longitude
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        mapa = StaticMap(500, 500)
        mapa.add_marker(CircleMarker((lon, lat), 'blue', 10))
        imatge = mapa.render()
        imatge.save(fitxer)
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(fitxer, 'rb'))
        os.remove(fitxer)
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.location, where))

updater.start_polling()
