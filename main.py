import telebot
from random import choice

TOKEN = ""

bot = telebot.TeleBot(token=TOKEN)


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
