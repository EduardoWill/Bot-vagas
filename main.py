#roda o bot
import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = TeleBot(token)

vagas_temp = {}
@bot.message_handler(commands=['start','help','Pesquisar']) 
def commands(msg):
    if msg.text == '/start':
        bot.send_message(msg.chat.id,"Opa fala!")
    elif msg.text =='/help':
        bot.send_message(msg.chat.id,"Lista de comandos")
    elif msg.text =='/Pesquisar':
        bot.send_message(msg.chat.id, "Digite o nome da vaga:")
        bot.register_next_step_handler(msg, pegar_nivel) # passa para o próximo quando esse campo for preenchido

def pegar_nivel(msg):
    chat_id = msg.chat.id
    nomeVaga = msg.text #coleta o nome da vaga
    vagas_temp[chat_id] = {'nome': nomeVaga}
    bot.send_message(msg.chat.id, "Digite o nível de experiência:")
    bot.register_next_step_handler(msg,pegar_regiao,nomeVaga )

def pegar_regiao(msg,nomeVaga):
    chat_id = msg.chat.id
    nivel = msg.text #coleta o nivel
    vagas_temp[chat_id]['nivel'] = nivel
    bot.send_message(msg.chat.id, "Digite sua região: ")
    bot.register_next_step_handler(msg, salvar_vaga, nomeVaga, nivel)

def salvar_vaga(msg,nomeVaga, nivel):
    chat_id = msg.chat.id
    regiao = msg.text # coleta a região
    vagas_temp[chat_id]['regiao'] = regiao
    usuario = msg.from_user.username #Salva o nome do usuário
    vagas_temp[chat_id]['usuario'] = usuario

    bot.send_message(
        chat_id,
        f"Vaga registrada temporariamente:\n"
        f"Nome: {nomeVaga}\n"
        f"Nível: {nivel}\n"
        f"Região: {regiao}\n"
        f"Usuário: {usuario}"
    )

    # opcional: imprime no console para verificação
    print(vagas_temp[chat_id])

bot.infinity_polling()