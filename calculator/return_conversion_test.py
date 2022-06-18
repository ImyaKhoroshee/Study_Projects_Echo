from fractions import Fraction
import pytest       # pip install pytest
from return_conversion import conversion_to_mixed_fraction as Conv_to
#вручную вызываем в консоли по python -m pytest return_conversion_test.py
def test1_Conv_to():
    """Проверка дроби 6/1 положительной `Conv_to` функции"""
    output = Conv_to(Fraction(6))
    assert output == '6'
def test2_Conv_to():
    """Проверка дроби отрицательной 6/1 `Conv_to` функции"""
    output = Conv_to(Fraction(-6))
    assert output == '-6'   
def test3_Conv_to():
    """Проверка неправильной положительной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(23, 5))
    assert output == '4_3/5'
def test4_Conv_to():
    """Проверка неправильной положительной дроби с двузначным числом в знаменателе `Conv_to` функции"""
    output = Conv_to(Fraction(231, 46))
    assert output == '5_1/46'
def test5_Conv_to():
    """Проверка неправильной отрицательной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(-10, 4))
    assert output == '-2_1/2'
def test6_Conv_to():
    """Проверка неправильной отрицательной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(10, -4))
    assert output == '-2_1/2'
def test7_Conv_to():
    """Проверка правильной положительной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(22, 757))
    assert output == '22/757'
def test7_Conv_to():
    """Проверка правильной отрицальной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(-2, 7))
    assert output == '-2/7'  
def test7_Conv_to():
    """Проверка правильной отрицальной дроби `Conv_to` функции"""
    output = Conv_to(Fraction(2, -7))
    assert output == '-2/7'
def test7_Conv_to():
    """Проверка дроби 6/6 `Conv_to` функции"""
    output = Conv_to(Fraction(6, 6))
    assert output == '1'