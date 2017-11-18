# -*- coding: utf-8 -*-

import os
import telebot
import funcionesDB

TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

commands = { # command description used in the "ayuda" command
    'hola': 'Comando de inicio',
    'adios': 'Comando de despedida',
    'ayuda': 'Da informacion sobre los comandos disponibles',
    'num_asignaturas': 'Número de asignaturas almacenadas',
    'asig_disponibles': 'Asignaturas almacenadas',
    'mostrar_todo': 'Muestra toda la información almacenada'
}

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
    bot.send_message(chat_id, "Bienvenid@ al canal de SubjectsGII, use el comando /ayuda para más información")

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

@bot.message_handler(commands=['asig_disponibles'])
def comando_asigDisponibles(message):
    """Función que muestra las asignaturas almacenadas. """
    chat_id = message.chat.id
    res = funcionesDB.mostrarAsigDisponibles()
    bot.send_message(chat_id, res)

@bot.message_handler(commands=['mostrar_todo'])
def comando_asigDisponibles(message):
    """Función que muestra toda la información almacenada. """
    chat_id = message.chat.id
    res = funcionesDB.mostrarTodo()
    bot.send_message(chat_id, res)

@bot.message_handler(commands=['ayuda'])
def command_help(message):
    chat_id = message.chat.id
    help_text = "Estos son los comandos disponibles: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(chat_id, help_text)

bot.polling(none_stop=True)
