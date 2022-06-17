'''
Нужно убрать мнимые единици учитывая степени
'''

# f = "-3+i+5-2i^3"
f = "3*i+1:i+10*i*2:3*i+21/2*i*2*i"
# return "23", ""

def math_calc(arg):
    for c in arg:
        if "*" in c or ":" in c:
            decomposition_formula(c)
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
            print(num)
    stack_num.append(num)
    num = ""
    print(stack_num, stack_char)
    return stack_num, stack_char

f1 = preparation_formula_separation(f)
f2 = formula_split(f1)
# f3 = sorting_math_operations(f2)
math_calc(f2)
