import os
from telegram.ext import Updater, CommandHandler
from StartCommandClass import StartCommand
from HelpCommandClass import HelpCommand

BOT_API_KEY = os.environ['TelegramAPIKey']

class Bot():
    def __init__(self, token):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler('start', StartCommand.execute))
        self.dispatcher.add_handler(CommandHandler('help', HelpCommand.execute))

    def start(self):
        """Запуск бота"""
        self.updater.start_polling()
        self.updater.idle()

if __name__ == '__main__':
    # Replace the value with your bot token
    bot = Bot(token=BOT_API_KEY)
    bot.start()