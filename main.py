from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8392536324:AAHr6dlM0hk9Qv5WP-rTOUsLMdvPBw6PtQw"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Бот запущен 🚀")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
