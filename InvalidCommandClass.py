from telegram import Update
from telegram.ext import CallbackContext


class InvalidCommand:
    @staticmethod
    def execute(update: Update, context: CallbackContext):
        """Выполняется при получении недопустимой команды"""
        update.message.reply_text('Неверная команда. Используйте /help для просмотра доступных команд.')