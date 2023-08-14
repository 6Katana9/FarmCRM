from telebot import telebot
from decouple import config


TOKEN = config('TOKEN')

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Здравствуйте, я бот, который будет отправлять вам файл с запросами на лекарство')


def send_excel(file_path, user):
    f = open(file_path,"rb")

    bot.send_document(config('USER_ID'), f, caption=f'Филиал: {user.username}\nАдресс аптеки: {user.address}\nОтправитель: {user.first_name} {user.last_name}\nНомер телефона {user.telephone_name}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
