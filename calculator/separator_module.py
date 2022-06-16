# На вход получаем от Модуля преобразования полных дробей
# вида '21/4*6+3*i+1:i-63-3/70:5/6+93/23+10*i*2:3*i+21/2*i*2*i'
#      '21/4*6+(3*i+1:i)-63-3/70:5/6+93/23+(10*i*2:3*i+21/2*i*2*i)'
#      '21/4*6-63-3/70:5/6+93/23', '3*i+1:i+10*i*2:3*i+21/2*i*2*i' 

from distutils.command.clean import clean
import re
string_import = "21/4*6+3*i+1:i-63-3/70:5/6+93/23+10*i*2:3*i+21/2*i*2*i"
result = ''
listres = []
listres2 = []
clean_equation = ''

result = re.findall(r'\d+[/]+\d+\Di|\d+\Di|\d+\D', string_import)
for i in result:
    if 'i' in i :
        listres.append(i)
    else:
        listres2.append(i)
    
print("+".join(listres))
print('+'.join(listres2))
# listres = listres.replace("++","+")
# listres2 = listres2.replace("++","+")
