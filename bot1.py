# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler


def start(update, context):
    '''funció que saluda i que s'executarà quan el bot rebi la comanda /start'''
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Soc un bot bàsic.")


# declara una constant amb el access-token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))

# engega el bot
updater.start_polling()
