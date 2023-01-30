import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters
)

TOKEN = os.environ['TOKEN']


def start(update: Update, context: CallbackContext):
    update.message.reply_html(text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()