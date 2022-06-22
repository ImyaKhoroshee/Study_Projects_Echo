import re
def separator (string_conversion):    
    listRes = []
    listRes2 = []
    clean_equation = []
    temp_conversion = []
    token_start = [ '+', '^', '*','/',':','&']
    token_end = ['-', '+', '^', '*','/',':','&']
    temp_conversion = string_conversion.replace('^','&')
    sort = re.findall(r'[-+]\d+[/]\d+\w[:*^&]\d+[/]\d+\w|[-+]\d+[/]\d+\w[:*^&]\d+[/]\d+|[-+]\d+[/]\d+[:*^&]\d+[/]\d+\w|[-+]\d+[/]\d+\w[:*^&]\d+\w|[-+]\d+\w[:*^&]\d+[/]\d+\w|[-+]\d+[/]\d+[:*^&]\d+\w|[-+]\d+[:*^&]\d+[/]\d+\w|[-+]\d+[/]\d+\w[:*^&]\d+|[-+]\d+\w[:*^&]\d+[/]\d+|[-+]\d+\w[:*^&]\d+\w|[-+]\d+[:*^&]\d+\w|[-+]\d+\w[:*^&]\d+|\d+[/]\d+\w[:*^&]\d+[/]\d+\w|\d+[/]\d+\w[:*^&]\d+[/]\d+|\d+[/]\d+[:*^&]\d+[/]\d+\w|\d+[/]\d+[:*^&]\d+\w|\d+[:*^&]\d+[/]\d+\w|\d+[/]\d+\w[:*^&]\d+|\d+\w[:*^&]\d+[/]\d+|\d+\w[:*^&]\d+\w|\d+[:*^&]\d+\w|\d+\w[:*^&]\d+|[-+]\d+[/]\d+\w|\d+[/]\d+\w|\d+\w|\d+\D\w|\D\d+', temp_conversion)


    for i in sort:
        if "i" in i:
            listRes.append(i)
        else:
            listRes2.append(i)

    listRes = ''.join(listRes)

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
                     .replace('&','^')

    clean_equation.append(listRes2) #сводим результат в финальный список
    clean_equation.append(listRes)
    return clean_equation   
print(separator(string_input))
