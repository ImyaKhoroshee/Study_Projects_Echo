
def RC_calculator():
    import colorama
    from pretty_input import pretty_input as Intro_block
    from validcheck import userTerminal
    from conversion_modul import conversion_of_mixed_fractions as MixFractionIn
    from comput_modul import calc_mod
    from return_conversion import conversion_to_mixed_fraction as MixFractionOut
    Intro_block()
    while True:
        equation = userTerminal()
        print(equation)
        equation = MixFractionIn(equation)
        print(equation)
        equation = calc_mod(equation)
        print(equation) 
        print(MixFractionOut(equation))
        print(equation)
        print(colorama.Fore.MAGENTA,f'Ответ:\n {equation}')
        end_check = bool(input(colorama.Fore.GREEN,"Чтобы продолжить, введите что-нибудь, или по кнопке Enter завершите работу"))
        if end_check == False: break





RC_calculator()