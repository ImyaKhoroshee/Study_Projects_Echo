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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update # https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/menju-klaviatury/
# кнопки хочу еще добавить
from telegram.ext import Updater, CommandHandler # обработчик CommandHandler (фильтрует сообщения с командами)
from telegram.ext import MessageHandler, Filters # чтобы отвечать на все команды, которые не были распознаны предыдущими обработчиками.
# from CallbackContext import telegram
from conversion_modul import conversion_of_mixed_fractions
from return_conversion import conversion_to_mixed_fraction

from fractions import Fraction

f = open('config.txt', 'r', encoding='utf_8')   # Путь для Тани :)
token_calc = f.read()
print(token_calc)
# sep_configs =  all_config.split('\n', 1)

# sep_configs[1] = sep_configs[1][:-2]
f.close()
TOKEN = token_calc
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update, context):     # Приветствие
    # print(type(update.message.text))
    # print(update.message.text)
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Да, посчитай}?")
    # btn2 = types.KeyboardButton("Нет, я сам посчитаю?")
    # markup.add(btn1, btn2)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я Бот-калькулятор. Я умею вычислять выражения с рациональными и комплексными числами. Посчитать тебе пример?")
# Введи команду /calc, нажми пробел и введи свой пример.
  

def mixed_fractions_conversion(update, context): # привязала бота к модулю преобразования целой части дроби. 
    # print(type(update.message.text))              4_5/6+2i-6_2/7  => 29/6+2i-44/7
    # print(update.message.text)
    blabla = update.message.text[11:]
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_of_mixed_fractions(blabla))
   

def conversion_to_mixed_fractions(update, context): # привязала бота к модулю обратного преобразования дроби
    # print(type(update.message.text))                  /tomixed 29/6 => 4_5/6
    # print(update.message.text)
    user_input = update.message.text[9:]
    pre_list = user_input.split('/')
    a = int(pre_list[0])
    b = int(pre_list[1])
    ab = Fraction(a, b)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_to_mixed_fraction(ab))

def input_tele_check(update, context):
    from validcheck import InputValidityTelebot as tele_check
    user_text = update.message.text[9:]
    checked_input = tele_check(user_text)
    if checked_input == 0:
        context.bot.send_message(chat_id=user_text.effective_chat.id, 
                             text="Вы хотите посчитать это выражение?")
        # yes = KeyboardButton('Да,хочу', )
        # yes =
    else:
        context.bot.send_message(chat_id=user_text.effective_chat.id, 
                             text=f"{checked_input[1]}, код ошибки {checked_input[0]}")

def run_main(update,context):
    from conversion_modul import conversion_of_mixed_fractions as MixFractionIn
    from comput_modul import calc_mod
    from return_conversion import conversion_to_mixed_fraction as MixFractionOut
    from complex_with_str import Complex_i_logic as remove_i
    from separator_module import separator
    from calc_logging import read_data_file as write_log
    start_eq = update.message.text[6:]
    equation = MixFractionIn(start_eq)
    equation = separator(equation)
    image_parts = remove_i(equation[1])
    result_parts = []
    result_parts.append(equation[0]+image_parts[0])
    result_parts.append(image_parts[1])
    result_parts = list(map(calc_mod,result_parts))
    result_parts = list(map(MixFractionOut,result_parts))
    if result_parts[1] != '':
        result_parts[1] ='+'+result_parts[1]+'i'
    answer = result_parts[0]+result_parts[1]
    write_log(start_eq,answer)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f'Ответ:\n {answer}')

def start_test(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)


def commands_list(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text = ("/{0} - команда перевода смешанной дроби в неправильную \n "
    " "
    " "
    "/{1} - blabla ".format('frommixed','tomixed')))

start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
dispatcher.add_handler(start_handler)  

start_handler = CommandHandler('frommixed', mixed_fractions_conversion) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler) 

start_handler = CommandHandler('help', commands_list) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('calc', run_main) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('checkme', input_tele_check) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)   

start_handler = CommandHandler('tomixed', conversion_to_mixed_fractions) # если увидишь команду `/tomixed`, то вызови функцию `conversion_to_mixed_fractions()`
dispatcher.add_handler(start_handler) 
start_handler = CommandHandler('keys', start_test)
dispatcher.add_handler(start_handler)   

print('server is working')

# import logging      # Журнал
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)


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

# запуск прослушивания сообщений
updater.start_polling() # наверное это для постоянной работы (none_stop=True)
# обработчик нажатия Ctrl+C
updater.idle()