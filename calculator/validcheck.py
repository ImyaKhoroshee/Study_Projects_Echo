from prettytable import PrettyTable  # pip install PrettyTable        
import colorama as cs # pip install colorama

def userTerminal():
    while True:
        print(cs.Fore.GREEN)
        user_req = input('Введите ОДНОЙ СТРОКОЙ выражение, значение которого нужно найти, и нажмите клавишу "ввод":\n')
        if bool(user_req) == False: return False
        user_req = user_req.replace(' ','')
        user_req = user_req.replace('--','+')
        user_req = user_req.replace('+-','-')
        user_req = user_req.replace('-+','-')
        user_req = user_req.replace('++','+')
        user_req = user_req.replace('ii','i*i')
        if InputValidity(user_req) == True: break
    if user_req[0] == '+': user_req = user_req[1:]
    print(cs.Fore.GREEN, "Принято, вычисляю...")
    print(cs.Fore.RESET  ,end='')

    return user_req


def InputValidity(user_req :str):
    validset = {'0','1','2','3','4','5','6','7','8','9','*',':','+','-','i','/','_','^'}
    check_str =''

    if user_req[0] not in {'0','1','2','3','4','5','6','7','8','9','+','-','i'}:
        print(cs.Fore.RED,f"Первый символ невалидный - ' {user_req[0]} ' , исправьте ввод")
        return False
    
    for i in range(1,len(user_req)-1):
        if user_req[i]  not in validset:
            print(cs.Fore.RED,f"Вы ввели невалидный символ ' {user_req[i]} ' на {i+1}-м месте, исправьте ввод")
            return False
        if user_req[i-1] in {'*',':','/','^','+'} and user_req[i] in {'*',':','/','^','+'}:
            print(cs.Fore.RED,f"У вас двойной символ матоперации -  на {i+1}-м месте  , уточните ввод")
            return False
        # if user_req[i] == 'i' and (user_req[i-1].isdigit()): #для варианта когда везде *i
            # user_req[i-1:i].replace('i','*i')
        if user_req[i] == '_': #проверка валидности в смешанных дробях
                if not(user_req[i-1].isdigit()): #проверяем слева
                    print(cs.Fore.RED,f"Не указана целая часть полной дроби на {i+1}-м месте  , уточните ввод")
                    return False
                for let in user_req[i+1:]: #проверяем справа
                    if let in {'*',':','+','-','/','_','^'}: 
                        if check_str =='': #если сразу без цифр
                            print(cs.Fore.RED,f"Не указан числитель полной дроби на {i+1}-м месте  , уточните ввод")
                            return False
                        elif let == '/': #цифры нашли, теперь смотрим знак дроби
                            check_str = let
                        elif check_str.count("/") == 0:
                            print(cs.Fore.RED,f"Не указаны части дроби на {i+1}-м месте  , уточните ввод")
                            return False
                        elif len(check_str) < 2:  #знак дроби нашли, а цифры после нет
                            print(cs.Fore.RED,f"Не указан знаменатель полной дроби на {i+1}-м месте  , уточните ввод")
                            return False
                        else:
                            check_str = ''
                            break  #Все нормально, выходим
                    else:
                        check_str +=let
    if user_req[-1] not in validset:
        print(cs.Fore.RED,f"Последний символ невалидный - ' {user_req[-1]} ' , исправьте ввод")
        return False
    if user_req[-1] in {'*',':','+','-','/','_','^'}:
        print(cs.Fore.RED,f"Матоперация ' {user_req[-1]} ' на конце пустая  , уточните ввод")
        return False
                
    return True


# print(userTerminal())


