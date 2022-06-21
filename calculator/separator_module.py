
# На вход получаем от Модуля преобразования полных дробей
import re
# string_input = '-1i+2i*3i:4i^5i+23/6i-23/7*i-1+2*3:4^5+23/6'# ['-1i+2i*3i:4i^5i+23/6i-23/7*i', '-1+2*3:4&5+23/6']
# string_input = '-42/34i:3i+5*3-56/32i+56/23*7^2-5^3i+32*3' # ['-42/34i:3i-56/32i-5^3i', '5*3+56/23*7&2+32*3']
# string_input = '4i*56+56-31i*4-56' # ['4i-31i', '56+56*4-56']
# string_input = '4i*4:5+4:4*5+4*4i:5+642-3i:56+4+i' ['4i*4i-3i+i', '4:5+4:4*5+4:5+642:56+4']
# string_input = '4/5*3*2i+45+3*4/5i*2-2-3*4/5:2i' ['2i*4/5i:2i', '4/5*3+45+3*2-2-3*4/5']
# string_input = '2^i+3' ['2^i', '3']
def separator (string_conversion):    
    listRes = []
    listRes2 = []
    clean_equation = []
    temp_conversion = []
    token_start = [ '+', '^', '*','/',':','&']
    token_end = ['-', '+', '^', '*','/',':','&']
    temp_conversion = string_conversion.replace('^','&')
    sort = re.findall(r'\D\d+[/]\d+i|\D\d+[/]\d+\Di|\D\d+[&]\d+i|\D\d+[&]i|\D\d+[/]i|\d+[/]\d+i|\d+[/]\d+\Di|\d+[&]\d+i|\d+[&]i|\d+[/]i|\D\d+i|\d+i|\Di|\d+|\D', temp_conversion)

    for i in sort:
        if "i" in i:
            listRes.append(i)
        else:
            listRes2.append(i)


    listRes = ''.join(listRes)


    listRes = re.findall(r'\d+[/]\d+i|\d+[&]\d+i|\d+[&]i|\d+[/]\d+\Di|\d+[/]i|\d+i|\d+i|i|\D', listRes) 


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

    listRes = listRes.replace('++','+') \
                     .replace('--','-') \
                     .replace('+-','-') \
                     .replace('-+','-') \
                     .replace('&','^')

    listRes2 = listRes2.replace('++','+') \
                     .replace('--','-') \
                     .replace('+-','-') \
                     .replace('-+','-') \
                     .replace('**','^')

    clean_equation.append(listRes) #сводим результат в финальный список
    clean_equation.append(listRes2)
    return clean_equation   


