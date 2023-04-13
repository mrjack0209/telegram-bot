from telegram import Update
from telegram.ext import CallbackContext


class StartCommand:
    @staticmethod
    def execute(update: Update, context: CallbackContext):
        """Обработчик комманды /start """
        update.message.reply_text('Привет! Я ERP KMPZ BOT')