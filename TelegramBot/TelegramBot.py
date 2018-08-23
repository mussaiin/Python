import telebot

token = "275592646:AAH31RmN4OFI5jQ8TyMe3m1JjtHK_CTzsbs"
bot = telebot.TeleBot(token)

#bot.send_message()
upd = bot.get_updates()
#print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Привет, я бот-попугай. Я буду повторять за тобой.")

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Просто печатай, я буду повторять.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, (message.text).upper())

bot.polling(none_stop=True, interval=0)
