from fractions import Fraction

def conversion_to_mixed_fraction(fraction):
    
    numerator = fraction.numerator
    denominator = fraction.denominator
    
    list = []

    wholepart = numerator//denominator
    list.append(wholepart)
    list.append('_')
    
    temp = denominator*wholepart
    newnumerator = numerator - temp
    list.append(newnumerator)
    list.append('/')
    list.append(denominator)

    result = "".join(map(str,list))
    return result

fraction_of_Gena = Fraction(23, 5)
# fraction_of_Gena = Fraction(231, 46)  # => 5_1/46

print(conversion_to_mixed_fraction(fraction_of_Gena))