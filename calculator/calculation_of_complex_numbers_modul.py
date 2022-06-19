'''
Нужно убрать мнимые единици учитывая степени
'''

import fractions

# f = "-3+i+5-2i"
f = "3*i+1:i+10*i*2:3*i+21/2*i*2*i"
# f = "1:1i:1i"
# f = "8:2i:1i"
# f = "2:3i"
# f = "2i:3i"
# f = "2i:3"
# f = "3/8:2/3i"
# f = "3/4i:7/8"
# f = "1/2i:5/6i"
# f = "1/2:2/3"
# f = "4:2"
# f = "1:2"
# f = "2*8"
# f = "3*4*9"
# f = "3i*4i*9i"
# f = "3i*4*9i"
# f = "3*4i*9i"
# f = "3*4*9i"
# f = "3*4i*9"
# f = "3i*4*9"
# return "23", ""

def clear_num_i(arg):
    """
    Функция разделяет и возвращает по отдельности число и мнимую i
    """
    if arg[0] == "i":
        return "1", "i"
    elif arg[0] == "-" and arg[1] == "i":
        return "-1", "i"
    else:
        return arg[:arg.find("i")], "i"

def reduction_fractions(arg):
    """
    Функция сокращает дроби
    """
    num_list = list(map(int, arg.split("/")))
    if num_list[0] == num_list[1]: return 1
    elif num_list[1] == 1: return num_list[0]
    num1 = max(num_list)
    num2 = min(num_list)
    while num1 != 0 and num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    num_list[0] = num_list[0] // num1
    num_list[1] = num_list[1] // num1
    if num_list[1] == 1: return str(num_list[0])
    else:
        return "/".join(map(str, num_list))

def math_div_int(arg1, arg2):
    """
    Функция делит два числа полученных из функции math_div()
    и возвращает целое число, если числа делятся без остатка или
    дробь
    """
    if arg1 % arg2 == 0:
        result = str(arg1 // arg2)
    else:
        result = str(arg1) + "/" + str(arg2)
        result = reduction_fractions(result)
    return result

def math_div_ord_fract(arg1, arg2):
    """
    Функция делит обыкновенные дроби
    """
    if "/" in arg1:
        ord_fract1 = list(map(int, arg1.split("/")))
    else:
        ord_fract1 = list(int(arg1), 1)
    if "/" in arg2:
        ord_fract2 = list(map(int, arg2.split("/")))
    else:
        ord_fract2 = list(int(arg2), 1)
    numerator = ord_fract1[0] * ord_fract2[1]
    denominator = ord_fract1[1] * ord_fract2[0]
    if denominator == 1:
        result = str(numerator)
    else:
        result = str(numerator) + "/" + str(denominator)
        result = reduction_fractions(result)
    return result

def math_div(arg_num1, arg_num2):
    """
    Функция принимает список из двух чисел в виде строк и отправляет
    их в функцию деления дробных чисел или целых чисел
    """
    if "/" in arg_num1 or "/" in arg_num2:
        if "i" in arg_num1 and "i" in arg_num2:
            num1 = clear_num_i(arg_num1)[0]
            num2 = clear_num_i(arg_num2)[0]
            result = math_div_ord_fract(num1, num2)
        elif "i" in arg_num1 and "i" not in arg_num2:
            num1, num_i = clear_num_i(arg_num1)
            num2 = arg_num2
            result = math_div_ord_fract(num1, num2) + num_i
        elif "i" not in arg_num1 and "i" in arg_num2:
            num1 = arg_num1
            num2, num_i = clear_num_i(arg_num2)
            result = "-" + math_div_ord_fract(num1, num2) + num_i
        else:
            num1 = arg_num1
            num2 = arg_num2
            result = math_div_ord_fract(num1, num2)

    else:
        if "i" in arg_num1 and "i" in arg_num2:
            num1 = int(clear_num_i(arg_num1)[0])
            num2 = int(clear_num_i(arg_num2)[0])
            result = math_div_int(num1, num2)
        elif "i" in arg_num1 and "i" not in arg_num2:
            num1, num_i = clear_num_i(arg_num1)
            num1 = int(num1)
            num2 = int(arg_num2)
            result = math_div_int(num1, num2) + num_i
        elif "i" not in arg_num1 and "i" in arg_num2:
            num1 = int(arg_num1)
            num2, num_i = clear_num_i(arg_num2)
            num2 = int(num2)
            result = "-" + math_div_int(num1, num2) + num_i
        else:
            num1 = int(arg_num1)
            num2 = int(arg_num2)
            result = math_div_int(num1, num2)
    return result

def math_mult_ord_fract(arg1, arg2):
    """
    Функция перемножает обыкновенные дроби
    """
    ord_fract1 = []
    ord_fract2 = []
    if "/" in arg1:
        ord_fract1 = list(map(int, arg1.split("/")))
    else:
        ord_fract1.append(int(arg1))
        ord_fract1.append(1)
    if "/" in arg2:
        ord_fract2 = list(map(int, arg2.split("/")))
    else:
        ord_fract2.append(int(arg2))
        ord_fract2.append(1)
    numerator = ord_fract1[0] * ord_fract2[0]
    denominator = ord_fract1[1] * ord_fract2[1]
    result = str(numerator) + "/" + str(denominator)
    result = reduction_fractions(result)
    return result

def math_mult(arg_num1, arg_num2):
    """
    Функция перемножает натуральные дроби и целые числа
    """
    if "/" in arg_num1 or "/" in arg_num2:
        if "i" in arg_num1 and "i" in arg_num2:
            num1 = clear_num_i(arg_num1)[0]
            num2 = clear_num_i(arg_num2)[0]
            result = math_mult_ord_fract(num1, num2)
        elif "i" in arg_num1 and "i" not in arg_num2:
            num1, num_i = clear_num_i(arg_num1)
            num2 = arg_num2
            result = math_mult_ord_fract(num1, num2) + num_i
        elif "i" not in arg_num1 and "i" in arg_num2:
            num1 = arg_num1
            num2, num_i = clear_num_i(arg_num2)
            result = math_mult_ord_fract(num1, num2) + num_i
        else:
            num1 = arg_num1
            num2 = arg_num2
            result = math_mult_ord_fract(num1, num2)

    else:
        if "i" in arg_num1 and "i" in arg_num2:
            num1 = int(clear_num_i(arg_num1)[0])
            num2 = int(clear_num_i(arg_num2)[0])
            result = str(num1 * num2 * -1)
        elif "i" in arg_num1 and "i" not in arg_num2:
            num1, num_i = clear_num_i(arg_num1)
            num1 = int(num1)
            num2 = int(arg_num2)
            result = str(num1 * num2) + num_i
        elif "i" not in arg_num1 and "i" in arg_num2:
            num1 = int(arg_num1)
            num2, num_i = clear_num_i(arg_num2)
            num2 = int(num2)
            result = str(num1 * num2) + num_i
        else:
            num1 = int(arg_num1)
            num2 = int(arg_num2)
            result = str(num1 * num2)
    return result

def adding_numbers(arg_list):
    """
    Функция складывает элементы списка
    """
    result_num = 0
    result_num_i = 0
    num_list_i = []
    num_list = []
    for i in range(len(arg_list)):
        if "i" in arg_list[i]:
            num_list_i.append(arg_list[i])
        else:
            num_list.append(arg_list[i])
    for c in num_list:
        if "/" not in c:
            f_num = fractions.Fraction(int(c), 1)
        else:
            num1, num2 = list(map(int, c.split("/")))
            f_num = fractions.Fraction(num1, num2)
        result_num += f_num
    if len(num_list_i) > 1:
        for char in num_list_i:
            if char == "i": char = "1i"
            if char == "-i": char = "-1i"
            if "/" not in char:
                f_num = fractions.Fraction(int(char[:char.find("i")]), 1)
            else:
                num1, num2 = list(map(int, char.find("i").split("/")))
                f_num = fractions.Fraction(num1, num2)
            result_num_i += f_num
        if result_num_i == 1 or result_num_i == -1: result_num_i = ""
    return str(result_num), str(result_num_i) + "i"

def math_calc(arg):
    """
    Функция перебирает список из мат. формул и отправляет их
    в разные функции соответствующие нужной мат. операции
    """
    result_list = []
    for c in arg:
        if "*" in c or ":" in c:
            stack_num, stack_char = decomposition_formula(c)
            for i in range(len(stack_char)):
                if stack_char[i] == ":":
                    temp_result = math_div(stack_num[i], stack_num[i+1])
                    stack_num[i+1] = temp_result
                elif stack_char[i] == "*":
                    temp_result = math_mult(stack_num[i], stack_num[i+1])
                    stack_num[i+1] = temp_result
            result_list.append(stack_num[-1])
        else:
            result_list.append(c)
    """
    Складываем все элементы результирующего списка
    """
    if len(result_list) < 2:
        if result_list[0][-1] == "i":
            return None, result_list[0]
        else:
            return result_list[0], None
    else:
        result_num, result_num_i = adding_numbers(result_list)
        return result_num, result_num_i

def preparation_formula_separation(arg_f):
    '''
    Добавляем "+" перед "-", если он не унарный и 
    убираем "*" перед "i"
    '''
    new_arg_f = "" + arg_f[0]
    for i in range(1, len(arg_f)):
        if arg_f[i] == "-":
            new_arg_f += "+"
        if arg_f[i] == "*" and arg_f[i + 1] == "i":
            continue
        new_arg_f += arg_f[i]
    return new_arg_f

def formula_split(arg_f):
    '''
    Делаем из строки список разделяя его по знаку "+"
    '''
    new_arg_f = arg_f.split("+")
    return new_arg_f

def decomposition_formula(arg):
    """
    Функция разбивает каждую формулу на два стека с счислами
    и знаками мат. операций
    """
    stack_char = []
    stack_num = []
    num = ""
    for i in range(len(arg)):
        if arg[i] == "*" or arg[i] == ":":
            stack_num.append(num)
            num = ""
            stack_char.append(arg[i])
        else:
            num += arg[i]
    stack_num.append(num)
    num = ""
    return stack_num, stack_char

def main_calc_i():
    f1 = preparation_formula_separation(f)
    f2 = formula_split(f1)
    # f3 = sorting_math_operations(f2)
    num, num_i = math_calc(f2)
    print(num, num_i)
    return num, num_i

main_calc_i()
