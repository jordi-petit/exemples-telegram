import datetime

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola!")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Soc un bot amb comandes /start, /help i /hora.")

def hora(bot, update):
    missatge = str(datetime.datetime.now())
    bot.send_message(chat_id=update.message.chat_id, text=missatge)


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('hora', hora))

updater.start_polling()
