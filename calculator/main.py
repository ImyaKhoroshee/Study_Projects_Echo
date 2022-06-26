


def RC_calculator():
    import colorama
    from pretty_input import pretty_input as Intro_block
    from validcheck import userTerminal
    from conversion_modul import conversion_of_mixed_fractions as MixFractionIn
    from comput_modul import calc_mod
    from return_conversion import conversion_to_mixed_fraction as MixFractionOut
    from complex_with_str import Complex_i_logic as remove_i
    from separator_module import separator
    from calc_logging import read_data_file as write_log
    Intro_block()
    while True:
        equation = userTerminal()
        if equation == False :break
        # print(f'after validcheck  \n{equation}')
        start_eq = equation

        equation = MixFractionIn(equation)
        # print(f'after MixFractionIn \n{equation}')

        equation = separator(equation)
        # print(f'after separator \n{equation}')

        image_parts = remove_i(equation[1])
        # print(f'after complex_logic \n{image_parts}')

        result_parts = []
        result_parts.append(equation[0]+image_parts[0])
        result_parts.append(image_parts[1])
        # print(f'after result_parts append\n {result_parts}')
        result_parts = list(map(calc_mod,result_parts))
        # print(f'after calc_mod\n{result_parts}')

        result_parts = list(map(MixFractionOut,result_parts))
        # print(f'after MixFractionOut\n{result_parts}')
        
        answer = join_results(result_parts)
        write_log(start_eq,answer)
        print(colorama.Fore.MAGENTA,f'Ответ:\n {answer}')
        print(colorama.Style.RESET_ALL)

def join_results(results):
    if results[1] != '':
            if results[1][0] == '-':
                results[1] =results[1]+'i'
            else:
                results[1] ='+'+results[1]+'i'
    return results[0]+results[1]

RC_calculator()



