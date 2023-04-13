from telegram import Update
from telegram.ext import CallbackContext


class EchoCommand:
    """Represents the /echo command."""

    @staticmethod
    def execute(update: Update, context: CallbackContext):
        """Обработчик комманды /echo """
        text = ' '.join(context.args)
        update.message.reply_text(text)
