from googletrans import Translator

import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Soc un bot traductor.")


def trad(bot, update):
    translator = Translator()
    miss_orig = update.message.text[6:] # esborra el "/trad " del començament del missatge
    miss_trad = translator.translate(miss_orig).text
    bot.send_message(chat_id=update.message.chat_id, text=miss_trad)


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('trad', trad))

updater.start_polling()
