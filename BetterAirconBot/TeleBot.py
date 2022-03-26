import telebot
Api_Key = "5186000556:AAEzgPoLXOq6yjckIgv3vjP3WSyoBXP5yJc"
bot = telebot.TeleBot(Api_Key)
@bot.message_handler(commands=['Start'])
def Start(message):
    bot.reply_to(message,"Hey! How is it going ?")
bot.polling()
