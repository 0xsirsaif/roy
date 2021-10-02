import os
from datetime import date
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()

TOKEN = os.environ.get("TOKEN")
HEROKUAPP = os.environ.get("HEROKUAPP")

PORT = int(os.environ.get('PORT', 5000))
PROBLEMS = {}


def get_task(update, context):
    today = str(date.today())
    if isinstance(today, str):
        update.message.reply_text(f"Today's task \n\n - {PROBLEMS.get(today)}")
    else:
        update.message.reply_text("There's some error")


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("get_task", get_task))

    updater.start_polling()


if __name__ == '__main__':
    main()
