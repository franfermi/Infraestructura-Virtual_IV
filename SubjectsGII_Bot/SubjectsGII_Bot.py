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

@bot.message_handler(commands=['num_asignaturas'])
def comando_numAsig(message):
    """Función que muestra el número de asignaturas almacenadas. """
    chat_id = message.chat.id
    res = funcionesDB.numeroAsigDisponibles()
    bot.send_message(chat_id, res)

@bot.message_handler(commands=['ayuda'])
def comando_ayuda(message):
    chat_id = message.chat.id
	bot.send_message(chat_id, "Lista de comandos implementados: \n\n/hola - Comando de inicio\n\n/adios - Comando de despedida\n\n/num_asignaturas - Número de asignaturas almacenadas\n\n")

bot.polling(none_stop=True)
