import os
from datetime import date
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()

PORT = int(os.environ.get('PORT', 5000))
TOKEN = os.environ.get("TOKEN")
PROBLEMS = {
    "2021-10-02": "https://leetcode.com/problems/palindrome-linked-list/",
    "2021-10-06": "https://leetcode.com/problems/remove-linked-list-elements/",
    "2021-10-08": "https://leetcode.com/problems/delete-node-in-a-linked-list/",
    "2021-10-10": "https://leetcode.com/problems/intersection-of-two-linked-lists/",
    "2021-10-12": "https://leetcode.com/problems/remove-duplicates-from-sorted-list/",
    "2021-10-14": "https://leetcode.com/problems/swapping-nodes-in-a-linked-list/",
    "2021-10-16": "https://leetcode.com/problems/next-greater-node-in-linked-list/",
    "2021-10-18": "https://leetcode.com/problems/next-greater-node-in-linked-list/",
    "2021-10-20": "https://leetcode.com/problems/odd-even-linked-list/",
    "2021-10-22": "https://leetcode.com/problems/add-two-numbers-ii/",
    "2021-10-24": "https://leetcode.com/problems/sort-list/",
    "M2021-10-26": "https://leetcode.com/problems/insertion-sort-list/",
    "2021-10-28": "https://leetcode.com/problems/reverse-linked-list-ii/",
    "2021-10-30": "https://leetcode.com/problems/merge-in-between-linked-lists/"
}


def get_task(update, context):
    today = str(date.today())
    if isinstance(today, str):
        update.message.reply_text(f"Today's task \n\n - {PROBLEMS.get(today)}")
    else:
        update.message.reply_text("There's some error")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("get_task", get_task))

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://enigmatic-sands-07553.herokuapp.com/' + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
