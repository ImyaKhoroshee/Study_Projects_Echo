
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
        if bool(equation) == False: break
        print(equation)
        # equation = MixFractionIn(equation)
        # print(equation)
        equation = calc_mod(equation)
        print(equation) 
        equation = MixFractionOut(equation)
        print(colorama.Fore.MAGENTA,f'Ответ:\n {equation}')
        print(colorama.Style.RESET_ALL)






RC_calculator()