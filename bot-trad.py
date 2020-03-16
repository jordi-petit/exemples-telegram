from googletrans import Translator

from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soc un bot traductor. Usa /trad text.")


def trad(update, context):
    miss_orig = update.message.text[6:]  # esborra el "/trad " del començament del missatge
    miss_trad = translator.translate(miss_orig).text
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=miss_trad)


translator = Translator()

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('trad', trad))

updater.start_polling()
