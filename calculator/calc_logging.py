'''
Модуль принимает строку с формулой и строку с результатом
решения формулы и возвращает запись в текстовый файл с
указанием времени в момент записи
'''

import datetime

def read_data_file(arg_formula, arg_solved_formula):
    dt_now_temp = datetime.datetime.now()
    dt_now = "{0}:{1}:{2}\nдата:\n{3}.{4}.{5}".format(
        dt_now_temp.hour,
        dt_now_temp.minute,
        dt_now_temp.second,
        dt_now_temp.day,
        dt_now_temp.month,
        dt_now_temp.year
    )
    data = open("use_logs.txt", "a", encoding="utf-8")
    data.seek(0)
    data.write("формула пользователя:\n"
               "{0}\n"
               "результат вычислений:\n"
               "{1}\n"
               "расчёты записаны в:\n"
               "{2}\n-------------------------\n"
               .format(arg_formula, arg_solved_formula, dt_now)
               )
    data.close()

formula_user = "a+b=c"
solved_formula = "1"
read_data_file(formula_user, solved_formula)
