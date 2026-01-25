#roda o bot
from telebot import TeleBot

bot = TeleBot('8282196893:AAHW33iMoX6a5QVP9HvUTmsoTErswILo9AI')

@bot.message_handler(commands=['start','help']) 
def commands(msg):
    if msg.text == '/start':
        bot.send_message(msg.chat.id,"Opa!")
    elif msg.text =='/help':
        bot.send_message(msg.chat.id,"Lista de comandos")


bot.infinity.polling()