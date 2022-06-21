import fractions
from comput_modul import calc_mod
#вручную вызываем в консоли по python -m pytest comput_modul_test.py
def test1_calc_mod():
    """Проверка сложения `calc_mod` функции"""
    output = calc_mod('5+5')
    assert output == fractions.Fraction(10,1)
def test2_calc_mod():
    """Проверка вычитания `calc_mod` функции"""
    output = calc_mod('5-5')
    assert output == fractions.Fraction(0,1)
def test3_calc_mod():
    """Проверка умножения `calc_mod` функции"""
    output = calc_mod('5*5')
    assert output == fractions.Fraction(25,1)
def test4_calc_mod():
    """Проверка умножения `calc_mod` функции"""
    output = calc_mod('5:5')
    assert output == fractions.Fraction(1,1)
def test5_calc_mod():
    """Проверка сложения и вычитания дробей `calc_mod` функции"""
    output = calc_mod('2/5+4/5-3/10')
    assert output == fractions.Fraction(9,10)
def test5_calc_mod():
    """Проверка умножения и деления дробей `calc_mod` функции"""
    output = calc_mod('2/5*4/5:32*1/10')
    assert output == fractions.Fraction(1,1000)