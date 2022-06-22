'''
Модуль принимает строку с формулой и строку с результатом
решения формулы и возвращает запись в текстовый файл с
указанием времени в момент записи
'''

import datetime, os

def read_data_file(arg_formula, arg_solved_formula):
    dt_now_temp = datetime.datetime.now()
    dt_now = "{0}:{1}:{2};дата={3}.{4}.{5}".format(
        dt_now_temp.hour,
        dt_now_temp.minute,
        dt_now_temp.second,
        dt_now_temp.day,
        dt_now_temp.month,
        dt_now_temp.year
    )
    data = open(os.path.abspath("use_logs.txt"), "a", encoding="utf-8")
    data.seek(0)
    data.write("формула="
               "{0};"
               "ответ="
               "{1};"
               "время="
               "{2}\n-------------------------\n"
               .format(arg_formula, arg_solved_formula, dt_now)
               )
    data.close()

# formula_user = "a+b"
# solved_formula = "1"
# read_data_file(formula_user, solved_formula)
