
example1 ='3i+1:i+10i*2:3*i-10_1/2i*2i'
example2 = '2i*65/34*3^2:45'

def counting_ipowerdigits(pow_string:str,found_index:int): #подфункция для Complex_i_logic для определения числа степени
    pow_negative = False
    i_pow_num = ''
    for let in pow_string[found_index+1:]: #собираем цифры справа от ^
        if pow_string[found_index+1] == '-': #Не забываем, что степень может быть отрицательная
            pow_negative = True 
            continue
        if let.isdigit():
            i_pow_num +=let
        else: break
    # print(i_pow_num)
    if pow_negative ==True: return -1*int(i_pow_num)
    else: return int(i_pow_num)

def clean_up_i(init_part:str): #меняем i на 1,если с цифрой - то просто убираем
    result_part =''
    for letter in init_part:
        if letter == 'i':
            if result_part[-1].isdigit() : 
                result_part+=''
            else: 
                result_part+='1'
        else: result_part+=letter
    # print(result_part)
    return result_part

# def join_Eq_back(parts_list): #fail попытка сделать только с join, без join-replace, 
#     parts_list = ['+'+item for item in parts_list if item[0] != '-' ]
#     res_string = ''.join(parts_list)
#     return res_string

def Complex_i_logic(inp_str:str):
    inp_str = inp_str.replace("-","+-")
    all_parts = filter(None,inp_str.split('+'))
    real_parts = []
    img_parts = []
    i_pow = 0
    div_check = False
    part_isneg =False

    for part in all_parts:
        for j in range(len(part)-1): #проходимся по элементу списка(члену выражения),запоминая последние знаки деления/умножения
            if part[j] =='i':
                if div_check == True and part[j+1] == '^':
                    i_pow -= counting_ipowerdigits(part,j+1)
                elif div_check == True:
                    i_pow -=1
                elif part[j+1] == '^':
                    i_pow += counting_ipowerdigits(part,j+1)
                else: 
                    i_pow +=1
            if part[j] == ':' and div_check == True: div_check = False
            elif part[j] ==':': div_check = True
                
        if part[-1] =='i': #последний символ вне цикла из-за индексов
            if div_check == True :i_pow -=1
            else : i_pow +=1
        
        print(f"i_pow is {i_pow}")
        if part[0] == '-': part_isneg = True #проверяем знак члена
        if i_pow < 0 and part_isneg == True: #если оба минус, сокращаем сразу.
            part = part[1:]
            part_isneg = False
            i_pow = abs(i_pow)
        part = clean_up_i(part)
        match abs(i_pow) %4 : #не забываем добавить минус отрицательной степени, если он не сокращается
            case 0: # =1 при i>=0
                if i_pow < 0 and part_isneg == False: real_parts.append('-'+part)
                else:real_parts.append(part)
            case 1:# =i при i>=0
                if i_pow < 0 and part_isneg== False: img_parts.append('-'+part)
                else:img_parts.append(part)
            case 2:# =-1 при i>=0
                if i_pow < 0 and part_isneg == False: real_parts.append(part)
                elif part_isneg == True: real_parts.append(part[1:])
                else : real_parts.append('-'+part)
            case 3:# =-i при i>=0
                if i_pow < 0 and part_isneg == False: img_parts.append(part)
                elif part_isneg == True: img_parts.append(part[1:])
                else : img_parts.append('-'+part)
        part_isneg = False
        div_check = False
        i_pow = 0
    # print(real_parts,img_parts)
    real_parts_str ='+'.join(real_parts)
    real_parts_str = real_parts_str.replace('+-','-')
    img_parts_str = '+'.join(img_parts)
    img_parts_str = img_parts_str.replace('+-','-')
    return real_parts_str,img_parts_str

part1 = '-10i*2:3:2*i^2'
part2 = '-10i*i:3i-12/3i*i/3+2:2i*i^4'
print(part1)
print(Complex_i_logic(part1))











