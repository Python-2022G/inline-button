import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)

TOKEN = os.environ['TOKEN']

like = 0
dislike = 0



def start(update: Update, context: CallbackContext):
    inline_keyboard = [ 
        [
            InlineKeyboardButton(text='👍', callback_data='like'), 
            InlineKeyboardButton(text='👎', callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text='x', callback_data='close')
        ]
    ]
    update.message.reply_html(
            text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", 
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        )

def callback_btn(update: Update, context: CallbackContext):
    data = update.callback_query.data 
    global like, dislike
    if data == 'like':
        like += 1
    elif data == 'dislike':
        dislike += 1
    elif data == 'close':
        update.callback_query.delete_message()
        like = 0
        dislike = 0
        return 

    inline_keyboard = [ 
        [
            InlineKeyboardButton(text=f'👍: {like}', callback_data='like'), 
            InlineKeyboardButton(text=f'👎: {dislike}', callback_data='dislike')
        ],
        [
            InlineKeyboardButton(text='x', callback_data='close')
        ]
    ]
    update.callback_query.edit_message_reply_markup(
                            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
                        )


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))

    dp.add_handler(handler=CallbackQueryHandler(callback=callback_btn))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()