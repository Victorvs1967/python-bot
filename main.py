import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
users = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text='Write to support.')
    button01 = telebot.types.KeyboardButton(text='Button 01')
    button02 = telebot.types.KeyboardButton(text='Button 01')
    button03 = telebot.types.KeyboardButton(text='Button 01')
    keyboard.add(button_support, button01)
    keyboard.add(button02, button03)
    bot.send_message(chat_id, 'Hi! Welcome to the responser bot!', reply_markup=keyboard)

@bot.message_handler(commands=['remove_keyboard'])
def remove_keyboard(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(chat_id, 'Keyboard remove', reply_markup=keyboard)

def save_username(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    bot.send_message(chat_id, f'Hi, {name}. Enter your surname.')
    bot.register_next_step_handler(message, save_surname)

def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    bot.send_message(chat_id, f'Your data saved successfully...')

@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.id
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f"You are {name} {surname}")

@bot.message_handler(func=lambda message: message.text == 'Write to support.')
def write_to_support(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Enter your name.')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


if __name__ == '__main__':
    print('Bot started...')
    bot.infinity_polling()