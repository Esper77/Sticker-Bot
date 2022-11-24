import telebot
from random import choice


bot = telebot.TeleBot(token="5880785142:AAEU12-MT3jdVPk6M5reRQvEIFG3-QOABtk")


# @bot.message_handler(content_types=["text"])
# def answer(message):
#     text = message.text
#     chat_id = message.chat.id
#
#     bot.send_message(chat_id, text[::-1])


@bot.message_handler(content_types=["sticker"])
def sticker_answer(message):
    with open("hash.txt", "r") as file:
        my_sticker = set(file.readline().split())
    sticker_id = message.sticker.file_id
    chat_id = message.chat.id

    my_sticker.add(sticker_id)

    bot.send_sticker(chat_id, choice(list(my_sticker)))

    with open("hash.txt", "w") as file:
        for x in list(my_sticker):
            file.write(str(x) + " ")


bot.polling()
