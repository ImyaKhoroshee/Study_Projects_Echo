from prettytable import PrettyTable  # pip install PrettyTable        
import colorama as cs # pip install colorama

def userTerminal():
    
    while True:
        print(cs.Fore.GREEN)
        user_req = input('Введите ОДНОЙ СТРОКОЙ выражение, значение которого нужно найти, и нажмите клавишу "ввод":\n')
        user_req = user_req.replace(' ','')
        if InputValidity(user_req) == True: break
    user_req = user_req.replace('--','+')
    user_req = user_req.replace('++','+')
    print(cs.Fore.GREEN, "Принято, вычисляю...")
    print(cs.Fore.RESET  ,end='')

    return user_req


def InputValidity(user_req :str):
    validset = {'0','1','2','3','4','5','6','7','8','9','*',':','+','-','i','/','_'}
    if user_req[0] not in validset:
        print(cs.Fore.RED,f"Первый символ невалидный - ' {user_req[0]} ' , исправьте ввод")
        return False
    for i in range(1,len(user_req)):
        if user_req[i]  not in validset:
            print(cs.Fore.RED,f"Вы ввели невалидный символ ' {user_req[i]} ' на {i+1}-м месте, исправьте ввод")
            return False
        if user_req[i] == user_req[i-1] and user_req[i] in {'*', ':' ,'/'}:
            print(cs.Fore.RED,f"У вас двойной символ матоперации -  на {i+1}-м месте  , уточните ввод")
            return False
        if user_req[i] == 'i' and  user_req[i-1].isdigit():
            user_req[i-1:i].replace('i','*i')
    return True


# print(userTerminal())


