
#вручную вызываем в консоли по python -m pytest validcheck_test.py
# from validcheck import InputValidity
from validcheck import InputValidityTelebot as in_val_t
import pytest
# def test1_InputValidity():
#     """Проверка разрешенных символов `InputValidity` функции"""
#     output = InputValidity('01_2/3+4*5-6:7i+8^9')
#     assert output == True
# def test2_InputValidity():
#     """Проверка запрещенных символов `InputValidity` функции"""
#     output = InputValidity('a')
#     assert output == False
# def test3_InputValidity():
#     """Проверка запрещенных символов `InputValidity` функции"""
#     output = InputValidity('(3)')
#     assert output == False
# def test4_InputValidity():
#     """Проверка запрещенных символов `InputValidity` функции"""
#     output = InputValidity('(√3)')
#     assert output == False
# def test5_InputValidity():
#     """Проверка эталонного выражения в ' `InputValidity` функции"""
#     output = InputValidity('5_1/4*6-3*i+1:i-63-3/70:5/6+4_1/23+10*i*2:3*i+10_1/2*i*2*i')
#     assert output == True
# def test6_InputValidity():
#     """Проверка неправильной записи числителя полной дроби  `InputValidity` функции"""
#     output = InputValidity('5_1/4+4_/3+1_2/3')
#     assert output == False
# def test7_InputValidity():
#     """Проверка неправильной записи полной дроби без знаменателя  `InputValidity` функции"""
#     output = InputValidity('5_1*6-3*i+1:i-63')
#     assert output == False
# def test8_InputValidity():
#     """Проверка неправильной записи полной дроби без дробной части  `InputValidity` функции"""
#     output = InputValidity('3/70:5/6+4_1/23+10_')
#     assert output == False
# def test9_InputValidity():
#     """Проверка отрицательной степени  `InputValidity` функции"""
#     output = InputValidity('4^-2')
#     assert output == True

# @pytest.mark.parametrize(
# "input_powers,pow_expected",
#     [('4^*2', False),
#     ('4^+2', False),
#     ('4^:2',False),
#     ('4^-2',True),
#     ('4^2',True)])
# def test_Powers_InputValidity(input_powers,pow_expected):
#     """Проверка записи степеней в `InputValidity` функции"""
#     assert InputValidity(input_powers)== pow_expected

def test1_InputValidityTelebot():
    """Проверка разрешенных символов `InputValidity` функции"""
    output = in_val_t('01_2/3+4*5-6:7i+8^9')
    assert output == 0
def test2_InputValidityTelebot():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = in_val_t('3*a4+5')
    assert output == (1,"Вы ввели невалидный символ ' a ' на 3-м месте, исправьте ввод")
def test3_InputValidityTelebot():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = in_val_t('3*(4+5)')
    assert output == (1,"Вы ввели невалидный символ ' ( ' на 3-м месте, исправьте ввод")
def test4_InputValidityTelebot():
    """Проверка запрещенных символов `InputValidity` функции"""
    output = in_val_t('√3')
    assert output == (1,"Первый символ невалидный - ' √ ' , исправьте ввод")
def test5_InputValidityTelebot():
    """Проверка эталонного выражения в ' `InputValidity` функции"""
    output = in_val_t('5_1/4*6-3*i+1:i-63-3/70:5/6+4_1/23+10*i*2:3*i+10_1/2*i*2*i')
    assert output == 0
def test6_InputValidityTelebot():
    """Проверка неправильной записи числителя полной дроби  `InputValidity` функции"""
    output = in_val_t('5_1/4+4_/3+1_2/3')
    assert output == (3,'Не указан числитель полной дроби на 8-м месте  , уточните ввод')
def test7_InputValidityTelebot():
    """Проверка неправильной записи полной дроби без знаменателя  `InputValidity` функции"""
    output = in_val_t('5_1*6-3*i+1:i-63')
    assert output == (3,'Не указаны части дроби на 2-м месте  , уточните ввод')
def test8_InputValidityTelebot():
    """Проверка неправильной записи полной дроби без дробной части  `InputValidity` функции"""
    output = in_val_t('3/70:5/6+4_+10')
    assert output == (3,'Не указан числитель полной дроби на 11-м месте  , уточните ввод')
def test9_InputValidityTelebot():
    """Проверка отрицательной степени  `InputValidity` функции"""
    output = in_val_t('4^-2')
    assert output == 0

@pytest.mark.parametrize(
"input_powers,pow_expected",
    [('4^*2', (2,'У вас двойной символ матоперации -  на 3-м месте  , уточните ввод')),
    ('4^+2', (2,'У вас двойной символ матоперации -  на 3-м месте  , уточните ввод')),
    ('4^:2',(2,'У вас двойной символ матоперации -  на 3-м месте  , уточните ввод')),
    ('4^-2',0),
    ('4^2',0)])
def test_Powers_InputValidityTelebot(input_powers,pow_expected):
    """Проверка записи степеней в `InputValidity` функции"""
    assert in_val_t(input_powers)== pow_expected

