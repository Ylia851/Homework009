from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
from game import win


def hello(update: Update, context: ContextTypes) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


update = Updater('m_token.txt')

update.dispatcher.add_handler(CommandHandler("hello", hello))
update.dispatcher.add_handler(CommandHandler("game", win))

update.start_polling()
update.idle()
