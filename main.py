import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
users = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hi! Welcome to the responser bot! Enter your name.')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)

def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id] = name
    bot.send_message(chat_id, f'Hi, {name}. Enter your surname.')
    bot.register_next_step_handler(message, save_surname)

def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    bot.send_message(chat_id, f'Your data saved successfully...')

@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.idadd
    name = users[chat_id]['name']
    surname = users[chat_id['surname']]
    bot.send_message(chat_id, f'You {name} {surname}')


if __name__ == '__main__':
    print('Bot started...')
    bot.infinity_polling()