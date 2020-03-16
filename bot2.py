import datetime

from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Usa /help per veure les comandes disponibles.")


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Soc un bot amb comandes /start, /help i /hora.")


def hora(update, context):
    missatge = str(datetime.datetime.now())
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=missatge)


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('hora', hora))

updater.start_polling()
