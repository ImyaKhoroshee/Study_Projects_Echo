def format_in_fract_list(string_arg):       #функция конвертация строки в сипсок
    from fractions import Fraction          #из чисел в формате Fraction и знаков в формате строки
    list_arg = []                           
    result = ''
    string_arg += ' '
    set = {'+', '-', '*', ':', ' '}
    for i in string_arg:
        if i not in set:
            result += i
        else:
            list_arg.append(Fraction(result))
            list_arg.append(i)
            result = ''
    list_arg.pop()
    return list_arg
    
def calc_mod(string_arg):
    import format_in_fract_list from comput_modul
    list_arg = format_in_fract_list(string_arg)
    prom_result_list = []
    i = 0
    while i < len(list_arg)-1:
        if list_arg[i+1] == ':':
            prom_result_list.append(list_arg[i]/list_arg[i+2])
            i +=3
        elif list_arg[i+1] == '*':
            prom_result_list.append(list_arg[i]*list_arg[i+2])
            i +=3
        else:
            prom_result_list.append(list_arg[i])
            i +=1
    result = prom_result_list[0]
    for i in range(1, len(prom_result_list)-1):
        if prom_result_list[i] == '+':
            result += prom_result_list[i+1]
        elif prom_result_list[i] == '-':
            result -= prom_result_list[i+1]
    return result

