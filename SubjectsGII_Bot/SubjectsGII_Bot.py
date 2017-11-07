# -*- coding: utf-8 -*-

import os
import telebot
import funcionesDB

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            chat_id = m.chat.id
            print ("[" + str(chat_id) + "]: " + m.text)
bot.set_update_listener(listener)

@bot.message_handler(commands=['hola'])
def comando_hola(message):
    """Función de bienvenida al bot de Telegram. """
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bienvenid@ al canal de SubjectsGII")

@bot.message_handler(commands=['adios'])
def comando_hola(message):
    """Función de despedida del bot de Telegram. """
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hasta pronto!")

bot.polling(none_stop=True)
