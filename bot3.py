import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler



def fib(n):
    '''calcula nombre de fibonacci'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Soc un bot amb comandes /suma i /fibo.")


def suma(bot, update, args):
    try:
        x = float(args[0])
        y = float(args[1])
        s = x + y
        bot.send_message(chat_id=update.message.chat_id, text=str(s))
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def fibo(bot, update, args):
    try:
        n = int(args[0])
        f = fib(n)
        bot.send_message(chat_id=update.message.chat_id, text=str(f))
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('suma', suma, pass_args=True))
dispatcher.add_handler(CommandHandler('fibo', fibo, pass_args=True))
updater.start_polling()
