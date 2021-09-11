import telebot


bot = telebot.TeleBot("1839295884:AAH65ue1E9gh7-GoC30zDATmiazk85GIHNo", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Howdy, how are you doing?")


bot.polling()