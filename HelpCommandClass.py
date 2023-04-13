from telegram import Update, ParseMode
from telegram.ext import CallbackContext


class HelpCommand:
    COMMANDS = [
        '/start - Запустить бота',
        '/help - Список доступных команд',
        '/echo <text> - Повторить заданный текст',
        '/register - Регистрация нового пользователя'
    ]

    @staticmethod
    def execute(update: Update, context: CallbackContext):
        """Обработчик комманды /help """
        command_list = '\n'.join(HelpCommand.COMMANDS)
        update.message.reply_text(f'Доступные команды:\n\n{command_list}', parse_mode=ParseMode.MARKDOWN)