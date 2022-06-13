# Модуль преобразования целой части дроби. 
# Данный код не походит для последней дроби в нашем примере.

def conversion_of_mixed_fractions(string_exp):
    result = ''
    list = []

    set = {'+', '-', '*', ':', 'i', '_', '/'}

    for i in range (0, len(string_exp)):
        if string_exp[i] not in set:
            result += string_exp[i]
        else:
            list.append(result)
            list.append(string_exp[i])
            result = ''

    list2 = []
    i = 0

    while i < len(list):

        if list[i].isdigit() and list[i+1] == '_':
            list2.append(int(list[i])*int(list[i+4])+int(list[i+2]))
            i+=3
        else:
            list2.append(list[i])
            i+=1

    string_conversed_franctions = "".join(map(str,list2))
    return string_conversed_franctions


numeric_expression = '5_1/46+3i+1/i-63-3/70:5/6+4_1/23+10i2/3i+10_1/2i*2i'
print(f'Оригинал: {numeric_expression}')
print(f'Результат: {conversion_of_mixed_fractions(numeric_expression)}')