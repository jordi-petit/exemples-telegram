# importa l'API de Telegram
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Soc un bot bàsic.")

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))

# engega el bot
updater.start_polling()
