# ставим модуль python-telegram-bot
# python -m pip install -U python-telegram-bot
# Ссылка на чат с нашим ботом t.me/Our_Calculator_Bot. 

import os
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler # обработчик CommandHandler (фильтрует сообщения с командами)

# Путь к токену у Тани
# f = open('.telegram\config.txt', 'r', encoding='utf_8')
# # f = open('config.txt', 'r', encoding='utf_8')   
# token_calc = f.read()
# f.close()

# Путь к токену у Антона
f = open(os.path.dirname(__file__)+'\config.txt','r',encoding='utf-8')
all_config = f.read()
f.close()
sep_config = all_config.split('\n')
token_calc = sep_config[1]

TOKEN = token_calc
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Включение встроенных логов бота. Потом посылать строки в лог через logger.info()
# import logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)

def start(update, context):     # Приветствие
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я Бот-калькулятор. Я умею вычислять выражения с рациональными и комплексными числами. Чтобы попробовать, жми /keys")



def run_main(update,context):
    from conversion_modul import conversion_of_mixed_fractions as MixFractionIn
    from comput_modul import calc_mod
    from return_conversion import conversion_to_mixed_fraction as MixFractionOut
    from complex_with_str import Complex_i_logic as remove_i
    from separator_module import separator
    from calc_logging import read_data_file as write_log
    if update.message.text[0]== '/': start_eq = update.message.text[6:]
    else : start_eq = update.message.text
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
    context.bot.send_message(chat_id=update.message.chat_id, 
                             text=f'Ответ:\n {answer}')  

def mix_frac_conv(update, context): # для команды /frommix. Пример: 4_5/6+2i-6_2/7  => 29/6+2i-44/7
    from conversion_modul import conversion_of_mixed_fractions
    # print(type(update.message.text))              
    # print(update.message.text)
    blabla = update.message.text[9:]
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_of_mixed_fractions(blabla))
   
def conv_to_mix_frac(update, context): # для команды /tomix. Пример: 29/6 => 4_5/6
    from return_conversion import conversion_to_mixed_fraction
    from fractions import Fraction
    user_input = update.message.text[7:]
    pre_list = user_input.split('/')
    a = int(pre_list[0])
    b = int(pre_list[1])
    ab = Fraction(a, b)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=conversion_to_mixed_fraction(ab))

def input_tele_check(update, context):
    # print(update)
    from validcheck import InputValidityTelebot as tele_check
    update.message.text = update.message.text[9:]
    # print(update)
    user_text = update.message.text
    # print(user_text)
    checked_input = tele_check(user_text)
    
    choices = [[InlineKeyboardButton("Да", callback_data='c1'+user_text),
              InlineKeyboardButton("Нет", callback_data='c2'+user_text)]]
    choices_markup = InlineKeyboardMarkup(choices)

    if checked_input == 0:
        update.message.reply_text("Вы хотите посчитать это выражение?",reply_markup=choices_markup)
        # context.bot.editMessageText(chat_id=update.message.chat_id, #такая запись просто автоматом считает, без выбора по кнопке
        #                         message_id=update.message.message_id, 
        #                         text=run_main(update,context))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f"{checked_input[1]}, код ошибки {checked_input[0]}")

def buttons_list(update: Update, context: CallbackContext):
    q_update = update.callback_query
    # print(q_update)
    query_txt = q_update.data
    if query_txt[0] == 'c':
        if query_txt[1] == '1':
            q_update.message.text = query_txt[2:]
            # print(q_update)
            run_main(q_update,context)
            context.bot.editMessageText(chat_id=q_update.message.chat_id,
                                message_id=q_update.message.message_id, 
                                text="Без проблем")
        elif query_txt[1] == '2':
            context.bot.editMessageText(chat_id=update.callback_query.message.chat_id,
                                message_id=update.callback_query.message.message_id, 
                                text="Понял, дальше вы сами")
    update.callback_query.answer()

updater.dispatcher.add_handler(CallbackQueryHandler(buttons_list))

def commands_list(update,context):  # Список всех доступных команд  дорабатывает Сергей. 
    context.bot.send_message(chat_id=update.effective_chat.id,
    text = ("Доступные математические символы:\n"
            "------------------------------------------------------------------------\n"
            "'+' сложение                                  '1+2'\n"
            "'-' вычитание                                 '1-2'\n"
            "'*' умножение                                '1*2'\n"
            "':' деление                                      '1:2'\n"
            "'^' возведение в степень           '3^2'\n"
            "'i' обозначение мнимой части '3i*2i:i'\n"
            "------------------------------------------------------------------------\n"
            "Способы записи обыкновенных дробей:\n"
            "------------------------------------------------------------------------\n"
            "правильная дробь            '1/2'\n"
            "неправильная дробь        '5/3'\n"
            "смешанная дробь             '2_3/4\n"
            "дробь применяется для вычисления корня\n"
            "'4^1/2=2' - корень квадратный,\n"
            "'27^1/3=3' - корень кубический\n"
            "------------------------------------------------------------------------\n"
            "Необрабатываемые операции:\n"
            "------------------------------------------------------------------------\n"
            "Не поддерживаются любые буквы кроме 'i'\n"
            "Не поддерживаются скобки '()'\n"
            "Не поддерживаются минусы внутри смешанных дробей '1_-2/3' или '1_2/-3'\n"
            "Не поддерживается знак корня.\n"
            "------------------------------------------------------------------------\n"
            "Команды:\n"
            "------------------------------------------------------------------------\n"
            "/{0} - команда приветствия калькулятора\n"
            "/{1} - команда вызова справки\n"
            "/{2} - команда вычисления выражения\n"
            "'/calc выражение'\n"
            "/{3} - команда перевода смешанной дроби в неправильную\n"
            "/{4} - проверка валидности\n"
            "/{5} - выделение целой части у неправильнай дроби '9/5 = 1_4/5'\n"
            .format('start', 
                    'help', 
                    'calc', 
                    'frommix', 
                    'checkme', 
                    'tomix')))




start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
dispatcher.add_handler(start_handler)  

start_handler = CommandHandler('frommix', mix_frac_conv)
dispatcher.add_handler(start_handler) 

start_handler = CommandHandler('help', commands_list)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('calc', run_main)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('checkme', input_tele_check)
dispatcher.add_handler(start_handler)   

start_handler = CommandHandler('tomix', conv_to_mix_frac)
dispatcher.add_handler(start_handler) 


print('server is working')
updater.start_polling() # запуск прослушивания сообщений
updater.idle()          # обработчик нажатия Ctrl+C