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