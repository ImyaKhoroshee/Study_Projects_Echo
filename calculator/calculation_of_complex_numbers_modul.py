'''
Нужно убрать мнимые единици учитывая степени
'''

# f = "-3+i+5-2i"
f = "3*i+1:i+10*i*2:3*i+21/2*i*2*i"

def math_calc(arg1, char, arg2):
    '''
    Если число содержит "i", то оно делится на число
    перед "i" само "i" и степень и после этого
    производится вычисление
    '''
    list_arg1 = ["", "", ""]
    list_arg2 = ["", "", ""]
    # if "i" in arg1: arg1, arg2 = arg2, arg1
    for j in range(3):
        if "i" in arg1[0].isdigit():
            if arg1[0].isdigit():
                list_arg1[0] = int(arg1[:arg1.count("i")])
            else:
                list_arg1[0] = 1
        else:
            list_arg1[0] = arg1
        if arg2[0].isdigit():
            list_arg2[0] = int(arg2[:arg2.count("i")])
        else:
            list_arg2[0] = 1
        if "i" in arg1:
            list_arg1[1] = "i"
            if "^" in arg1:
                list_arg1[2] = arg1[arg1.count("^")+1:]
        if "i" in arg2:
            list_arg2[1] = "i"
            if "^" in arg2:
                list_arg2[2] = arg2[arg2.count("^")+1:]
    if char == ":" and arg2 == "i":
        result = "-" + arg1 + arg2
        return result
    if char == "*":
        num = 1
        if "i" in arg1:
            for c in (arg1, arg2):
                if c[0].isdigit():
                    num *= int(c[:c.count("i")])
                else:
                    num *= 1
        result = str(num) + "i"
        return result

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

def sorting_math_operations(arg_f):
    '''
    Каждый элемент списка arg_f при необходимости делится на мелкие
    мат. уравнения и находится результат решения
    '''
    num = ""
    result = []
    temp_result = []
    for c in arg_f:
        if "*" in c or ":" in c:
            for i in range(len(c)):
                if c[i] in "*:":
                    temp_result.append(num)
                    if len(temp_result) == 3:
                        print(temp_result)
                        temp_result[0] = (math_calc(
                                              temp_result[0], 
                                              temp_result[1], 
                                              temp_result[2]))
                        temp_result = temp_result[0]
                    temp_result.append(c[i])
                    num = ""
                else:
                    num += c[i]
            temp_result.append(num)
            num = ""
            print(temp_result)
            result.append(math_calc(temp_result[0], 
                                    temp_result[1], 
                                    temp_result[2]))
        else:
            result.append(c)
    print(result)

f1 = preparation_formula_separation(f)
f2 = formula_split(f1)
f3 = sorting_math_operations(f2)
# math_calc(f2)
