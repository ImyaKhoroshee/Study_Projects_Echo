import pytest
from conversion_modul import conversion_of_mixed_fractions as Conv_in
#вручную вызываем в консоли по python -m pytest conversion_modul_test.py
def test1_Conv_in():
    """Проверка одной дроби `Conv_in` функции"""
    output = Conv_in('5_1/3')
    assert output == '16/3'
def test2_Conv_in():
    """Проверка эталонного примера `Conv_in` функции"""
    output = Conv_in('5_1/4*6-3*i+1:i-63-3/70:5/6+4_1/23+10*i*2:3*i+10_1/2*i*2*i')
    assert output == '21/4*6-3*i+1:i-63-3/70:5/6+93/23+10*i*2:3*i+21/2*i*2*i'
def test3_Conv_in():
    """Проверка двух дробей, у одной знак минус `Conv_in` функции"""
    output = Conv_in('5_1/3-3_4/5')
    assert output == '16/3-19/5'
def test4_Conv_in():
    """Проверка одной дроби `Conv_in` функции"""
    output = Conv_in('5_1/3*3_4/5*42/3')
    assert output == '16/3*19/5*42/3'