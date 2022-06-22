# ставим модуль python-telegram-bot
# python -m pip install -U python-telegram-bot
# Ссылка на чат с нашим ботом t.me/Our_Calculator_Bot. 

from encodings import utf_8
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler # обработчик CommandHandler (фильтрует сообщения с командами)

f = open('.telegram\config.txt', 'r', encoding='utf_8')   # Путь для Тани :)
token_calc = f.read()
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
start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
dispatcher.add_handler(start_handler)    

def mixed_fractions_conversion(update, context): # привязала бота к модулю преобразования целой части дроби. 
    from conversion_modul import conversion_of_mixed_fractions
    # print(type(update.message.text))              4_5/6+2i-6_2/7  => 29/6+2i-44/7
    # print(update.message.text)
    blabla = update.message.text[11:]
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_of_mixed_fractions(blabla))

start_handler = CommandHandler('frommixed', mixed_fractions_conversion) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)    

def conversion_to_mixed_fractions(update, context): # привязала бота к модулю обратного преобразования дроби
    from return_conversion import conversion_to_mixed_fraction
    from fractions import Fraction
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
                             text="Вы хотите посчитать это выражение(да/нет)?")
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


def commands_list(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text = ("/{0} - команда перевода смешанной дроби в неправильную \n "
    " "
    " "
    "/{1} - blabla ".format('frommixed','tomixed')))


start_handler = CommandHandler('help', commands_list) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('calc', run_main) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('checkme', input_tele_check) # если увидишь команду `/frommixed`, то вызови функцию `mixed_fractions_conversion()`
dispatcher.add_handler(start_handler)   

start_handler = CommandHandler('tomixed', conversion_to_mixed_fractions) # если увидишь команду `/tomixed`, то вызови функцию `conversion_to_mixed_fractions()`
dispatcher.add_handler(start_handler)    

print('server is working')

# запуск прослушивания сообщений
updater.start_polling() # наверное это для постоянной работы (none_stop=True)
# обработчик нажатия Ctrl+C
updater.idle()