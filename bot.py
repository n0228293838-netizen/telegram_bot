import telebot
from telebot import types

bot = telebot.TeleBot("ТВОЙ_ТОКЕН")

@bot.message_handler(commands=["start"])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("О боте", "Контакты")
    bot.send_message(m.chat.id, "Привет! Выбери кнопку 👇", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "О боте")
def about(m):
    bot.send_message(m.chat.id, "Это мой первый бот. Я делаю его для портфолио.")

@bot.message_handler(func=lambda m: m.text == "Контакты")
def contacts(m):
    bot.send_message(m.chat.id, "Telegram: @твой_ник")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.send_message(m.chat.id, "Нажми /start, чтобы увидеть меню")

bot.polling()
