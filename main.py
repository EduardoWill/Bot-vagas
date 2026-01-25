#roda o bot
import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = TeleBot(token)

@bot.message_handler(commands=['start','help']) 
def commands(msg):
    if msg.text == '/start':
        bot.send_message(msg.chat.id,"Opa fala!")
    elif msg.text =='/help':
        bot.send_message(msg.chat.id,"Lista de comandos")


bot.infinity_polling()