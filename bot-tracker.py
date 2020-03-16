
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Comparteix la teva localització en directa i mou-te!")


def where(update, context):
    '''aquesta funció es crida cada cop que arriba una nova localització d'un usuari'''
    # obté la localització
    message = None
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
    location = message.location.latitude, message.location.longitude

    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=str(location))


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.location, where))

updater.start_polling()
