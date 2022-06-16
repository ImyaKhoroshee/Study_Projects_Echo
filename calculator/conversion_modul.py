# Fixed (16.06.2022)
# Модуль преобразования целой части дроби. 

def conversion_of_mixed_fractions(string_exp):
    result = ''
    intermediatelist = []

    set = {'+', '-', '*', ':', 'i', '_', '/'}

    for i in range (0, len(string_exp)):
        if string_exp[i] not in set:
            result += string_exp[i]
        else:
            intermediatelist.append(result)
            intermediatelist.append(string_exp[i])
            result = ''

    intermediatelist.append(result)

    conversed_fract_list = []
    i = 0

    while i < len(intermediatelist)-1:

        if intermediatelist[i].isdigit() and intermediatelist[i+1] == '_':
            conversed_fract_list.append(int(intermediatelist[i])*int(intermediatelist[i+4])+int(intermediatelist[i+2]))
            i+=3
        else:
            conversed_fract_list.append(intermediatelist[i])
            i+=1

    conversed_fract_list.append(intermediatelist[-1])

    string_conversed_franctions = "".join(map(str,conversed_fract_list))
    return string_conversed_franctions

# numeric_expression = '5_1/46+3i+1/i-63-3/70:5/6+4_1/23+10i*2/3i+10_1/2i*2i+5_1/4+5_1/67'
# numeric_expression = '5_1/4+5_1/67'
# print(f'Оригинал: {numeric_expression}')
# print(f'Результат: {conversion_of_mixed_fractions(numeric_expression)}')