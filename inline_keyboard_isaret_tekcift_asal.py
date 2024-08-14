#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import math 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

gelen_sayi = 0

def AsalKontrol(s):
    Asal = True
    for i in range(2, round(math.sqrt(s))):
        if(s % i == 0):
            Asal = False
            break
    if(Asal):
        return "Sayı Asal."
    else:
        return "Sayı Asal Değil."

def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("İşaret", callback_data='1'),
            InlineKeyboardButton("Tek/Çift", callback_data='2'),
        ],
        [InlineKeyboardButton("Asal", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    
def sayi(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    global gelen_sayi
    gelen_sayi = update.message.text.split(" ")[-1]
    keyboard = [
        [
            InlineKeyboardButton("İşaret", callback_data='1'),
            InlineKeyboardButton("Tek/Çift", callback_data='2'),
        ],
        [InlineKeyboardButton("Asal", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    if(query.data == "1"):
        d = "Pozitif" if int(gelen_sayi) > 0 else "Negatif" if int(gelen_sayi) < 0 else "İşaretsiz"
        query.edit_message_text(text=f"Sayı: {d}")
    elif(query.data == "2"):
        d = "Çift" if int(gelen_sayi) % 2 == 0 else "Tek"
        query.edit_message_text(text=f"Sayı: {d}")
    elif(query.data == "3"):
        query.edit_message_text(text="Sayı: " + AsalKontrol(int(gelen_sayi)))
    # query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7144099326:AAHa2zHgkaFmwLORg5aqs4K31uNawTYt-Sg")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler("sayi", sayi))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()