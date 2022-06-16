
#вручную вызываем в консоли по python -m pytest validcheck_test.py
from validcheck import InputValidity
def test1_InputValidity():
    """Проверка разрешенных символов `InputValidity` функции"""
    output = InputValidity('01_2/3+4*5-6:7i+8^9')
    assert output == True
def test2_InputValidity():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = InputValidity('a')
    assert output == False
def test3_InputValidity():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = InputValidity('(3)')
    assert output == False
def test4_InputValidity():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = InputValidity('(√3)')
    assert output == False
def test5_InputValidity():
    """Проверка эталонного выражения в ' `InputValidity` функции"""
    output = InputValidity('5_1/4*6-3*i+1:i-63-3/70:5/6+4_1/23+10*i*2:3*i+10_1/2*i*2*i')
    assert output == True
def test6_InputValidity():
    """Проверка неправильной записи числителя полной дроби  `InputValidity` функции"""
    output = InputValidity('5_1/4+4_/3+1_2/3')
    assert output == False
def test7_InputValidity():
    """Проверка неправильной записи полной дроби без знаменателя  `InputValidity` функции"""
    output = InputValidity('5_1*6-3*i+1:i-63')
    assert output == False
def test8_InputValidity():
    """Проверка неправильной записи полной дроби без дробной части  `InputValidity` функции"""
    output = InputValidity('3/70:5/6+4_1/23+10_')
    assert output == False
def test9_InputValidity():
    """Проверка отрицательной степени  `InputValidity` функции"""
    output = InputValidity('4^-2')
    assert output == True
