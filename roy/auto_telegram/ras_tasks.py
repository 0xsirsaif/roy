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
    task = PROBLEMS.get(today)
    if task:
        update.message.reply_text(f"Today's task \n\n - {task}")
    else:
        update.message.reply_text("No task for day")


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("get_task", get_task))

    updater.start_polling()


if __name__ == '__main__':
    main()
