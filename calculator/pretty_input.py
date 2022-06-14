from prettytable import PrettyTable  # pip install PrettyTable
import colorama         # pip install colorama
from colorama import Fore, Back, Style

def pretty_input():
    colorama.init()
    print()
    print(Fore.BLACK + '                    КАЛЬКУЛЯТОР')
    print(Fore.BLACK + '  для работы с рациональными и комплексными числами \n')
    print(Style.BRIGHT, end='')
    print(Fore.RED + '              Инструкция пользователя\n')
    print(Fore.BLUE + ' Арифметические действия и простые дроби обозначаются:')
    print(Style.BRIGHT, end='')

    name = ['Сложение','Вычитание','Умножение','Деление','Дробь']
    data = ['+','-','*',':','/']

    columns = len(name)  
    table = PrettyTable(name)  
    data_data = data[:]     

    while data_data:    
        table.add_row(data_data[:columns])
        data_data = data_data[columns:]
    print(Fore.BLUE, end='')
    print(table)
    print()

    name1 = ['Пример записи дроби с целой частью','Пример записи мнимой части']
    data1 = ['4_1/47','2i2i или 10i2:3i']

    columns1 = len(name1)  
    table1 = PrettyTable(name1)  
    data1_data1 = data1[:]     

    while data1_data1:    
        table1.add_row(data1_data1[:columns1])
        data1_data1 = data1_data1[columns1:]
    print(Fore.BLUE, end='')
    print(table1)
    print(Fore.GREEN)

    string = input('Введите ОДНОЙ СТРОКОЙ выражение, значение которого нужно найти, и нажмите клавишу "ввод":\n')

pretty_input()

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# colorama.init() # обязательно для Windows 10.
# print(Fore.BLACK + 'Черный текст яркий')
# print(Style.BRIGHT)
# print(Fore.RED + 'Красный текст')
# print(Fore.GREEN + 'Зеленый цвет')
# print(Fore.BLUE + 'Синий цвет')
# print(Fore.MAGENTA + 'Пурпурный цвет')
# print(Fore.CYAN + 'Цвет морской волны')
# print(Fore.RESET)
# print(Style.RESET_ALL) # это сброс цветов консоли к начальным значениям.