import telebot

bot = telebot.TeleBot("690490653:AAGaXfro1h81P7R40KkQzAynKZ4vww0CWyY")

ok = dict.fromkeys("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
# bot.send_message(151594111, "test")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши мне слово и я сделаю на его основе феминитив. Например: программист –> "
                          "программистка")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if all(c in ok for c in message.text):
        if message.text.endswith('ст'):
            bot.send_message(message.chat.id, message.text + "ка")
        elif message.text.endswith('ж') | message.text.endswith('ч'):
            bot.send_message(message.chat.id, message.text + "иха")
        elif message.text.endswith('яр') | message.text.endswith('ер') | message.text.endswith('ёр'):
            bot.send_message(message.chat.id, message.text + "ша")
        elif message.text.endswith('ец'):
            bot.send_message(message.chat.id, message.text[:-2] + "чиха")
        elif message.text.endswith('ик'):
            bot.send_message(message.chat.id, message.text[:-1] + "ца")
        elif message.text.endswith('ор') | message.text.endswith('ерт') | message.text.endswith('ист'):
            bot.send_message(message.chat.id, message.text + "ка")
        elif message.text.endswith('ог'):
            bot.send_message(message.chat.id, message.text + "иня")
        elif message.text.endswith('ар'):
            bot.send_message(message.chat.id, message.text + "иха")
        elif message.text.endswith('ий') | message.text.endswith('ый'):
            bot.send_message(message.chat.id, message.text[:-2] + "ая")
        elif message.text.endswith('ель'):
            bot.send_message(message.chat.id, message.text + "ница")
        elif message.text.endswith('т'):
            bot.send_message(message.chat.id, message.text + "эсса")
        elif message.text.endswith('ка') \
                | message.text.endswith('иха') \
                | message.text.endswith('ша') \
                | message.text.endswith('чиха') \
                | message.text.endswith('ца') \
                | message.text.endswith('иня') \
                | message.text.endswith('ница'):
            bot.send_message(message.chat.id, "Кажется тут не нужно ничего менять")
        else:
            bot.send_message(message.chat.id, "Пускай будет " + message.text + "ка")
    else:
        bot.send_message(message.chat.id, "Не похоже на слово")


bot.polling()
