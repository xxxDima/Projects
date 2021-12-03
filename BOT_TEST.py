import telebot
from telebot import types
from seting_telegram import token
from datetime import date
from random import randint
import nbrb


client = telebot.TeleBot(token)


@client.message_handler(commands=['start'])
def start(message):
    chat_id = []
    client.send_message(message.chat.id, 'Меня создал красавчик Дмитрий ;)\n /help, чтобы узнать что я умею')
    for i in [message.chat.id]:
        chat_id.append(i)
    print(chat_id)


@client.message_handler(commands=['help'])
def start(message):
    today = date.today()
    markup = types.InlineKeyboardMarkup()
    button_random = types.InlineKeyboardButton('Рандомное число от 0 до 100', callback_data='rand')
    buttonB = types.InlineKeyboardButton('Послать товарища', callback_data='b')
    button_nbrb = types.InlineKeyboardButton('График курсов валюют', callback_data='nbrb')

    markup.row(button_random)
    markup.row(buttonB)
    markup.row(button_nbrb)

    client.send_message(message.chat.id,
                        f'Выберите из списка, того что я умею по состоянию на {today}',
                        reply_markup=markup)


@client.message_handler(content_types=['text'])
def send_message(message):
    text = message.text.lower()
    if text == "@my_puppetbot курс валют":
        # seave_grafic = open('C:\\Users\\USER\\PycharmProjects\\pythonProject1\\График.png', "rb")
        nbrb.curse_per_week()
        photo = open('C:\\Users\\USER\\PycharmProjects\\pythonProject1\\График.png', "rb")
        client.send_photo(message.chat.id, photo)
    elif text == '/help':
        start()
    # elif text == "/stop":
    #     client.send_message(message.chat.id, "Я подчиняюсь только своему господину, Дмитрию")



@client.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'rand':
        rand = randint(0, 100)
        client.send_message(call.message.chat.id, f'число {rand}!')
    elif call.data == 'b':
        client.send_message(call.message.chat.id, 'ИДИ НАХУЙ!')
    elif call.data == 'nbrb':
        nbrb.curse_per_week()
        photo = open('C:\\Users\\USER\\PycharmProjects\\pythonProject1\\График.png', 'rb')
        client.send_photo(call.message.chat.id, photo)


client.polling(none_stop=True, interval=0)
