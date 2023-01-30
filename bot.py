import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)

TOKEN = os.environ['TOKEN']


def start(update: Update, context: CallbackContext):
    inline_keyboard = [ 
        [
            InlineKeyboardButton(text='👍', callback_data='like'), 
            InlineKeyboardButton(text='👎', callback_data='dislike')
        ]
    ]
    update.message.reply_html(
            text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", 
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        )

def callback_btn(update: Update, context: CallbackContext):
    print(update.callback_query.data)


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))

    dp.add_handler(handler=CallbackQueryHandler(callback=callback_btn))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()