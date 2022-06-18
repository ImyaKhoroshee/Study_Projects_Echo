# На вход получаем от Модуля преобразования полных дробей

import re

string_input = '-+4i+32*3' #переменная для ввода уравнения.

listRes = []
listRes2 = []
clean_equation = []
token_start = [ '+', '^', '*','/',':']
token_end = ['-', '+', '^', '*','/',':']

string_input_clear = string_input.replace('++','+').replace('--','-').replace('+-','-').replace('-+','-')

sort = re.findall(r'\D\d+[/]+\d+\Di|\D\d+\Di|\D\d+i|\d+|\D', string_input_clear)
# расшифровка шаблона регулярных отбора строки, по степени важности.
# \D\d+[/]+\d+\Di - знак, числа, знак деления(/), числа, знак, символ "i" (+21/2*i)
# \D\d+\Di - знак ,числа, знак, символ "i" (+2*i)
# \D\d+i - знак, числа, символ "i" 
# \d+ - числа "32..."
# \D - знак "+"

for i in sort:
    if "i" in i:
        listRes.append(i)
    else:
        listRes2.append(i)


listRes = ''.join(listRes)
listRes = re.findall(r'\d+[/]+\d+\Di|\d+\Di|\d+i|\D', listRes) 

for j in listRes:
    if listRes == []:
        break
    else:
        for i in token_start: # проверка  начала списка и конца, на "мусорные" символы и удаление
            if listRes[0] == i:
                listRes.pop(0)
        for i in token_end:
            if listRes[-1] == i:
                listRes.pop(-1)
listRes = ''.join(listRes) 




listRes2 = ''.join(listRes2)
listRes2 = re.findall(r'\d+[/]+\d+|\d+|\D', listRes2)

for x in listRes2:
    if listRes2 == []:
        break
    else:
        for i in token_start: 
            if listRes2[0] == i:
                listRes2.pop(0)
        for i in token_end:
            if listRes2[-1] == i:
                listRes2.pop(-1)
listRes2 = ''.join(listRes2)

clean_equation.append(listRes) #сводим результат в финальный список
clean_equation.append(listRes2)

print('вывод: мнимая часть [0]:', clean_equation[0], 'вещественная [1]:', clean_equation[1])
