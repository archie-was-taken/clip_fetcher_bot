from telegram.ext import (ApplicationBuilder,
                      CommandHandler,
                      MessageHandler,
                      filters)

from bot_commands import *

if __name__ == '__main__':
    with open('../assets/api_key.txt') as api_key:
        api_key = api_key.read()

def setup(api_key: str):
    application = ApplicationBuilder().token(api_key).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('url', url))
    application.add_handler(CommandHandler('download', download))
    application.add_handler(CommandHandler('dl', download))
    application.add_handler(CommandHandler('audio', audio))
    application.add_handler(CommandHandler('help', help_command))

    # handler for unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # handler for people who make the unholy mistake of thinking
    # this bot is sentient
    application.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), normal_chat)
    )
    application.run_polling()