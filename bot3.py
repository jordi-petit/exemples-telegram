from telegram.ext import Updater, CommandHandler


def fib(n):
    '''calcula l'n-èsim nombre de fibonacci'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soc un bot amb comandes /suma x y i /fibo n on x,y i n són nombres.")


def suma(update, context):
    try:
        x = float(context.args[0])
        y = float(context.args[1])
        s = x + y
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(s))
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')


def fibo(update, context):
    try:
        n = int(context.args[0])
        f = fib(n)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(f))
    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣')


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('suma', suma))
dispatcher.add_handler(CommandHandler('fibo', fibo))
updater.start_polling()
