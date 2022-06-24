# ставим модуль python-telegram-bot
# python -m pip install -U python-telegram-bot
# Ссылка на чат с нашим ботом t.me/Our_Calculator_Bot. 

from encodings import utf_8
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
f = open('.telegram\config.txt', 'r', encoding='utf_8')   # Путь для Тани
# f = open('config.txt', 'r', encoding='utf_8')   # Путь для Антона
token_calc = f.read()
f.close()
TOKEN = token_calc
updater = Updater(token=TOKEN)
dp = updater.dispatcher


def start(update, context):     # Приветствие
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я Бот-калькулятор. Я умею вычислять выражения с рациональными и комплексными числами. Чтобы попробовать, жми /keys")

def start_test(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Да, хочу", callback_data='Круто'),
            InlineKeyboardButton("Нет, я сам посчитаю", callback_data='Молодец'),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Хочешь посчитать?', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    query.edit_message_text(text=query.data)

updater.dispatcher.add_handler(CallbackQueryHandler(button))

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
    from validcheck import InputValidityTelebot as tele_check
    user_text = update.message.text[7:]
    checked_input = tele_check(user_text)
    if checked_input == 0:
        context.bot.send_message(chat_id=user_text.effective_chat.id, 
                             text="Вы хотите посчитать это выражение?")
        # yes = KeyboardButton('Да,хочу', )
        # yes =
    else:
        context.bot.send_message(chat_id=user_text.effective_chat.id, 
                             text=f"{checked_input[1]}, код ошибки {checked_input[0]}")


# def commands_list(update,context):  # Список всех доступных команд  дорабатывает Сергей. 
#     context.bot.send_message(chat_id=update.effective_chat.id,
#     text = ("/{0} - команда перевода смешанной дроби в неправильную \n "
#     " "
#     " "
#     "/{1} - blabla ".format('frommix','tomix')))

start_handler = CommandHandler('start', start) # если увидишь команду `/start`, то вызови функцию `start()`
dispatcher.add_handler(start_handler)  

start_handler = CommandHandler('frommix', mix_frac_conv)
dispatcher.add_handler(start_handler) 

# start_handler = CommandHandler('help', commands_list)
# dispatcher.add_handler(start_handler)

start_handler = CommandHandler('calc', run_main)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('checkme', input_tele_check)
dispatcher.add_handler(start_handler)   

start_handler = CommandHandler('tomix', conv_to_mix_frac)
dispatcher.add_handler(start_handler) 

start_handler = CommandHandler('keys', start_test)
dispatcher.add_handler(start_handler)   

print('server is working')
updater.start_polling() # запуск прослушивания сообщений
updater.idle()          # обработчик нажатия Ctrl+C