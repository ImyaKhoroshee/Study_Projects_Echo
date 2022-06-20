# По лекции не получилось создать бота, использовала этот сайт https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/

# создаем виртуальное окружение, если нет
# $ python -m venv .telegram --prompt TelegramBot
# активируем виртуальное окружение 
# $ source .telegram/bin/activate
# ставим модуль python-telegram-bot
# (TelegramBot):~$ python -m pip install -U python-telegram-bot

# Ссылка на чат с нашим ботом t.me/Our_Calculator_Bot. 

from encodings import utf_8
import telegram
from telegram.ext import Updater, CommandHandler # обработчик CommandHandler (фильтрует сообщения с командами)
from telegram.ext import MessageHandler, Filters # чтобы отвечать на все команды, которые не были распознаны предыдущими обработчиками.
# from CallbackContext import telegram
from conversion_modul import conversion_of_mixed_fractions
# import conversion_modul
f = open("calculator\config.txt", 'r', encoding='utf_8')
all_config = f.read()
sep_configs =  all_config.split('\n', 1)
f.close()
# print(sep_configs[1])
TOKEN = sep_configs[1]
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# def start(update, context):
#     # print(type(update.message.text))
#     # print(update.message.text)
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text="Привет, посчитать тебе пример?")

# start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
# dispatcher.add_handler(start_handler)    

def preobraz(update, context):
    # print(type(update.message.text))
    # print(update.message.text)
    blabla = update.message.text[5:]
    print(blabla)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_of_mixed_fractions(blabla))

start_handler = CommandHandler('sum', preobraz) # если увидишь команду `/start`, то вызови функцию `start()`
dispatcher.add_handler(start_handler)    
print('start server')

# import logging      # Журнал
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

# # функция обработки команды '/start'
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text="Привет, посчитать тебе пример?")


# функция обработки текстовых сообщений (функция обратного вызова) ЭХО
# def echo(update, context):
#     text = 'Ты написал: ' + update.message.text 
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text=text)    

# # функция обработки команды '/caps'
# # Команда /caps будет принимать какой-то текст в качестве аргумента и отвечать на него тем же текстом, 
# # только в верхнем регистре. Аргументы команды (например /caps any args) будут поступать в функцию обратного вызова в 
# # виде списка ['any', 'args'], разделенного по пробелам:
# def caps(update, context):
#     print(type(context))
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                                 text=conversion_of_mixed_fractions(str(context.args)))
#     # # if context.args:
#     #     text_caps = conversion_of_mixed_fractions(context.args) # хотела попробовать ввод пользователя в свою функцию пропихнуть. Не вышло
#     #     # text_caps = ' '.join(context.args).upper()
#     #     context.bot.send_message(chat_id=update.effective_chat.id, 
#     #                             text=text_caps)
#     # else: # если в команде не указан аргумент
#     #     context.bot.send_message(chat_id=update.effective_chat.id, 
#     #                             text='Ты не ввел свой пример')
#     #     context.bot.send_message(chat_id=update.effective_chat.id, 
#     #                             text='Напиши: /caps и свой пример')


# # функция обработки не распознных команд
# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, 
#                              text="Я не знаю такую команду.")

# # обработчик команды '/start'
# start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
# dispatcher.add_handler(start_handler)    

# # обработчик текстовых сообщений
# # говорим обработчику `MessageHandler`, если увидишь текстовое 
# # сообщение (фильтр `Filters.text`)  и это будет не команда 
# # (фильтр ~Filters.command), то вызови функцию `echo()`
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

# # обработчик команды '/caps'
# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)

# # обработчик не распознных команд
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)

# # запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()