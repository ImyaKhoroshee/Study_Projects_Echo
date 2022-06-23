
# На вход получаем от Модуля преобразования полных дробей
import re

# здесь просто на понимание разные многочлены. Членом является часть выражения, отделенная от других членов операцией сложения или вычитания.
# a+b+c -> ['a+b+c','']
# a+bi*d-c -> ['a-c','bi*d']
# a-bi*d+c*ei -> ['a','-bi*d+c*ei']
# a/bi+c/d-f*g -> [ 'c/d-f*g', 'a/bi']
#  Проверочные примеры
# string_input1 = '-1i+2i*3i:4i^5i+23/6i-23/7*i-1+2*3:4^5+23/6'# ['-1+2*3:4^5+23/6','-1i+2i*3i:4i^5i+23/6i-23/7*i' ]
# string_input2 = '-42/34i:3i+5*3-56/32i+56/23*7^2-5^3i+32*3' # [ '5*3+56/23*7^2+32*3','-42/34i:3i-56/32i-5^3i',]
# string_input3 = '4i*56+56-31i*4-56' # ['56-56','4i*56-31i*4']
# string_input4 = '4i*4:5+4:4*5+4*4i:5+642-3i:56+4+i'# ['4:4*5+642+4','4i*4:5+4*4i-3i:56+i']
# string_input5 = '4/5*3*2i+45+3*4/5i*2-2-3*4/5:2i'# ['45-2','4/5*3*2i+3*4/5i*2-3*4/5:2i']

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

    clean_equation.append(listRes2) #сводим результат в финальный список
    clean_equation.append(listRes)
    return clean_equation   


# print(separator(string_input1))


# init_string = '5+4i+4*-4:4i-34'
# temp = ''
# result=[]
# set_before_minus = {':','*','^'}
# for i,symb in enumerate(init_string[:-1]):
    
#     if symb == "+" or (symb == "-" and init_string[i-1] not in set_before_minus) :
#         result.append(temp)
#         #if #in temp есть i  или нет. Через метод find() index()
#         temp =''
#     temp += symb
# temp += init_string[-1]
# result.append(temp)
# print(result)