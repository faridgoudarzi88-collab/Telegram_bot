import telebot

TOKEN = 8451759208:AAE_c7qEKC6BwaDE9at4yxDKVBAE70zHRq0
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات هیولای سودده فعال شد 🚀")

bot.polling()
