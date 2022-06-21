from fractions import Fraction

def conversion_to_mixed_fraction(fraction):
    
    if fraction == '': 
        return fraction

    fract_list = []
    
    numerator = fraction.numerator
    denominator = fraction.denominator
    
    fract_list.append(numerator)
    fract_list.append(denominator)
    # print(fract_list)

    return_in_list = []
    result = ''

    if fract_list[0] % fract_list[1] == 0:    
        result = str(fract_list[0])
    elif fract_list[0] > fract_list[1] and fract_list[1] != 1: 
        wholepart = (numerator//denominator)            
        return_in_list.append(wholepart)
        return_in_list.append('_')
        temp = denominator*wholepart
        newnumerator = numerator - temp
        return_in_list.append(newnumerator)
        return_in_list.append('/')
        return_in_list.append(denominator)
        result = "".join(map(str,return_in_list))
    elif fract_list[0] < fract_list[1] and abs(fract_list[0])//fract_list[1] != 0:
        wholepart = (abs(numerator)//abs(denominator)) 
        return_in_list.append(wholepart)                
        return_in_list.append('_')
        temp = abs(denominator)*abs(wholepart)
        newnumerator = abs(numerator) - temp
        return_in_list.append(newnumerator)
        return_in_list.append('/')
        return_in_list.append(abs(denominator))
        result = "".join(map(str,return_in_list))
        result = '-' + result
    elif fract_list[0] < fract_list[1] and fract_list[0]//fract_list[1] == 0:
        result = str(abs(numerator)) + '/' + str(abs(denominator))
    elif fract_list[0] < fract_list[1] and abs(fract_list[0])//fract_list[1] == 0 and fract_list[0] < 0:
        result = str(fract_list[0]) + '/' + str(fract_list[1])
    return result

# fraction_of_Gena = Fraction(6)        # 6
# fraction_of_Gena = Fraction(-6)         # -6

# fraction_of_Gena = Fraction(23, 5)      # 4_3/5     Когда числ > знам и знам не равен 1
# fraction_of_Gena = Fraction(10, 4)      # 2_1/2   нужно преоб обычн способом
# fraction_of_Gena = Fraction(231, 46)  # 5_1/46

# fraction_of_Gena = Fraction(-10, 4)     # -2_1/2   Когда числ < знам и деление нацело не равно 0
# fraction_of_Gena = Fraction(10, -4)   # -2_1/2    преобразовываем с abs

# fraction_of_Gena = Fraction(22, 757)     # 22/757 - Когда числ < знам и деление нацело равно 0
# fraction_of_Gena = Fraction(45, 86)     # 45/86    просто сразу в резалт

# fraction_of_Gena = Fraction(-2, 7)    #  -2/7 Когда числ < знам и деление нацело равно 0 и первый эл меньше второго
# fraction_of_Gena = Fraction(2, -7)      # -2/7    просто сразу в резалт c минусом
# fraction_of_Gena = ''
# print(conversion_to_mixed_fraction(fraction_of_Gena))