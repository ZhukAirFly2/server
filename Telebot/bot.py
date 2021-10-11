import telebot
import time
from telebot import types

bot = telebot.TeleBot("1792415744:AAEzLHonCGTHTjQ460bamBH_Y0-6t849tSM")

a = 1

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup = types.ReplyKeyboardMarkup(True)
    buttonA = types.KeyboardButton('Совет')
    buttonB = types.KeyboardButton('Услуги')
    buttonC = types.KeyboardButton('Модели')

    markup.row(buttonA, buttonB, buttonC)

    bot.send_message(message.chat.id, 'Спасибо, что выбрали нашу авиакомпанию', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Совет':
        markup1 = telebot.types.InlineKeyboardMarkup()
        markup1.add(telebot.types.InlineKeyboardButton(text='10', callback_data=10))
        markup1.add(telebot.types.InlineKeyboardButton(text='30', callback_data=30))
        markup1.add(telebot.types.InlineKeyboardButton(text='100', callback_data=100))
        bot.send_message(message.chat.id, text="Сколько советов вам дать?", reply_markup=markup1)
    if message.text == 'Услуги':
        bot.send_message(message.chat.id, "Эконом класс: 1 000$\nСтандарт класс: 5 000$\nБизнесс класс: 10 000$\n")
        time.sleep(0.5)
        markup2 = telebot.types.InlineKeyboardMarkup()
        markup2.add(telebot.types.InlineKeyboardButton(text='ДА', callback_data='yes'))
        markup2.add(telebot.types.InlineKeyboardButton(text='ДА!', callback_data='yes!'))
        bot.send_message(message.chat.id, text="Вам нравятся наши предложения?", reply_markup=markup2)
    if message.text == 'Модели':
        bot.send_message(message.chat.id, "В нашей компании есть:\n1)Пассажирский самолёт\n2)Истребитель\n3)Грузовой самолёт\n")
        time.sleep(0.3)
        bot.send_message(message.chat.id,"Чтобы унать подробнее о самолёте, напишите его название")
        if message.text == 'Грузовой самолёт' or message.text == 'Грузовой':
            bot.send_message(message.chat.id, "Для пассажиров более 100кг")
        if message.text == 'Истребитель':
            bot.send_message(message.chat.id, "Ваша жизнь в ваших руках")
        if message.text == 'Пассажирский самолёт' or message.text == 'Пассажирский':
            bot.send_message(message.chat.id, "Со своей едой в самолёт НЕЛЬЗЯ, еда и напитки в полёт НЕ включены!")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    answer = 'КУПИ БИЛЕТ НА САМОЛЁТ!!!'
    answer1 = ''
    if call.data == '10':
        for i in range(10):
            bot.send_message(call.message.chat.id, answer)
            time.sleep(0.3)
    elif call.data == '30':
        for i in range(30):
            bot.send_message(call.message.chat.id, answer)
            time.sleep(0.3)
    elif call.data == '100':
        for i in range(100):
            bot.send_message(call.message.chat.id, answer)
            time.sleep(0.3)
    elif call.data == 'yes':
        answer1 = 'Мы были уверены, что вам понравится 😉'
    elif call.data == 'yes!':
        answer1 = 'Мы были уверены, что вам понравится! 😉'
    time.sleep(0.7)
    bot.send_message(call.message.chat.id, answer1)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling(none_stop=True)