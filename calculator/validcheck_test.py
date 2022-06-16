
#вручную вызываем в консоли по python -m pytest validcheck_test.py
from validcheck import InputValidity
def test1_InputValidity():
    """Проверка разрешенных символов `InputValidity` функции"""
    output = InputValidity('0123456789*-+:i/_')
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