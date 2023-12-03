import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)
users = {}

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_save = telebot.types.InlineKeyboardButton(text='Write to support.')
    keyboard.add(button_save)
    bot.send_message(chat_id, 'Hi! Welcome to the responser bot!', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Data saved.')

@bot.message_handler(func=lambda message: message.text == 'Write to support.')
def write_to_support(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Enter your name.')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)

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
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text='Save', callback_data='save_data')
    button_change = telebot.types.InlineKeyboardButton(text='Change', callback_data='change_data')
    keyboard.add(button_save, button_change)
    bot.send_message(chat_id, f'Save your data?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message.id
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Data saved.')

@bot.callback_query_handler(func=lambda call: call.data == 'change_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Data changed.')
    write_to_support(message)

@bot.message_handler(commands=['remove_keyboard'])
def remove_keyboard(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(chat_id, 'Keyboard remove', reply_markup=keyboard)

@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.id
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f"You are {name} {surname}")


if __name__ == '__main__':
    print('Bot started...')
    bot.infinity_polling()