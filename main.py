import telebot

bot = telebot.TeleBot('6463160630:AAFWs4DP3oJZ3s9OYLdFPPI8DJL1L-ji4B8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Саламбрат', parse_mode='Markdown')

@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'бегибрат', parse_mode='Markdown')

bot.infinity_polling()