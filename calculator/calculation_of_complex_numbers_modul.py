'''
Нужно убрать мнимые единици учитывая степени
'''

# f = "-3+i+5-2i^3"
# f = "3*i+1:i+10*i*2:3*i+21/2*i*2*i"
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
f = "1:2"
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
        return arg[:-1], "i"

def math_num_i(arg: int):
    if arg > 1:
        pass

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
        ord_fract2 = list(arg2, 1)
    numerator = ord_fract1[0] * ord_fract2[1]
    denominator = ord_fract1[1] * ord_fract2[0]
    result = str(numerator) + "/" + str(denominator)
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

def math_calc(arg):
    """
    Функция перебирает список из мат. формул и отправляет их
    в разные функции соответствующие нужной мат. операции
    """
    for c in arg:
        if "*" in c or ":" in c:
            stack_num, stack_char = decomposition_formula(c)
            print(stack_num, stack_char)
            for i in range(len(stack_char)):
                if stack_char[i] == ":":
                    temp_result = math_div(stack_num[i], stack_num[i+1])
                    stack_num[i+1] = temp_result
            print(stack_num)
    # return real_number, imaginary_number

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
    print(new_arg_f)
    return new_arg_f

def formula_split(arg_f):
    '''
    Делаем из строки список разделяя его по знеку "+"
    '''
    new_arg_f = arg_f.split("+")
    print(new_arg_f)
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

f1 = preparation_formula_separation(f)
f2 = formula_split(f1)
# f3 = sorting_math_operations(f2)
math_calc(f2)
