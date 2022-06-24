import re

def separator(input_string):
    temp = ''
    result=[]
    set_before_minus = {':','*','^',''}
    clean = []
    clean2 = []
    clean_equation = []
    for i,symb in enumerate(input_string[:-1]):
        
        if symb == "+" or (symb == "-" and input_string[i-1] not in set_before_minus) :
            result.append(temp)
            temp =''
        temp += symb
    temp += input_string[-1]
    result.append(temp)
    for x in result:
        if any("i" in filt for filt in x) == True:
            clean.append(x)
        else:
            clean2.append(x)
  
    clean = ''.join(clean)
    clean2 = ''.join(clean2)
    clean_equation.append(clean2) 
    clean_equation.append(clean)
    return clean_equation
