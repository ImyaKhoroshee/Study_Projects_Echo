from prettytable import PrettyTable  

print()
print('     Перед Вами калькулятор для работы с рациональными и комплексными числами.')
print()
print('                     Валидные данные (знаки операций):')
name = ['Сложение','Вычитание','Умножение','Деление','Целая часть дроби','Дробь']
data = ['+','-','*',':','_ (пример: 4_)','/ (пример:1/3)']

columns = len(name)  
table = PrettyTable(name)  
data_data = data[:]     

while data_data:    
    table.add_row(data_data[:columns])
    data_data = data_data[columns:]

print(table)
print()
string = input('Введите то, что нужно вычислить ОДНОЙ СТРОКОЙ и нажмите клавишу "ввод": ')