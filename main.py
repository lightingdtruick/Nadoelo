
import telebot

bot = telebot.TeleBot("1312031611:AAHbF5xMuwFExLmO5tHxhLzOOj63Lsxm0p0")


keyba = telebot.types.ReplyKeyboardMarkup()
keyba.row('мандарин','яблоко', 'банан')

@bot.message_handler(commands=['privet'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, а ты ничего такой,вот, можешь выбрать  ', reply_markup=keyba)

@bot.message_handler(commands=['commands'])
def satart_message(message):
    bot.send_message(message.chat.id, 'Не, я все так же ничего не умею толком, но вот - возьми банан.')


@bot.message_handler(content_types=["text"])
def handle_message(message):
    bot.send_message(message.from_user.id,'Зачем такие плохие слова мне пишешь....')




bot.polling(none_stop=True, interval=0)