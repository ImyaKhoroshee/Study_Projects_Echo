'''
Модуль принимает строку с формулой и строку с результатом
решения формулы и возвращает запись в текстовый файл с
указанием времени в момент записи
'''

import datetime

def read_data_file(arg_formula, arg_solved_formula):
    dt_now = str(datetime.datetime.now())
    data = open("use_logs.txt", "a")
    data.seek(0)
    data.write("user formula:\n"
               "{0}\n"
               "solution result:\n"
               "{1}\n"
               "date:\n"
               "{2}\n-------------------------\n"
               .format(arg_formula, arg_solved_formula, dt_now))
    data.close()

formula_user = "a+b=c"
solved_formula = "1"
read_data_file(formula_user, solved_formula)
