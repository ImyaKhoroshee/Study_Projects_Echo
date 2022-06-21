from complex_with_str import Complex_i_logic as com_i
import pytest
#вручную вызываем в консоли по python -m pytest complex_with_str_test.py
@pytest.mark.parametrize(
"input_signs,signs_expected",
    [('-10i*2:3:2*i',( '10*2:3:2*1','')), # n%4 = 2 ->-1
    ('-10i*2:3:2',( '','-10*2:3:2')), # n%4 = 1 ->i
    ('-10i*2:3*2i',( '-10*2:3*2','')), # n%4 = 0 ->1
    ('-10i*2i:3:2i',( '','10*2:3:2')),# n%4 = 3 ->-i
    ('10i*2i*3i*i',( '10*2*3*1',''))]) # n%4 = 0 ->1
def test1_Complex_i_logic(input_signs,signs_expected):
    """Проверка сокращения  i в `Complex_i_logic` функции"""
    assert com_i(input_signs)== signs_expected

@pytest.mark.parametrize(
    "input_pows,pows_expected",
    [('-i^2*3^2:2i^2',( '-1^2*3^2:2^2','')),# n%4 = 0
    ('-i^3*3^2:2i^2',( '','-1^3*3^2:2^2')),# n%4 = 1
    ('-i^2*3i^2:2i^2',( '1^2*3^2:2^2','')), # n%4 = 2
    ('-i^2*3i^2:2i^1',( '','1^2*3^2:2^1'))]) # n%4 = 3
def test2_Complex_i_logic(input_pows,pows_expected):
    """Проверка сложения степеней  i в `Complex_i_logic` функции"""
    assert com_i(input_pows)== pows_expected

def test3_Complex_i_logic():#1,-1,0,2
    """Проверка сортировки членов  в `Complex_i_logic` функции"""
    assert com_i('3i+1:i+10i*2:3*i-10_1/2i*2i') == ('10*2:3*1+10_1/2*2','3-1:1')
def test4_Complex_i_logic():#3,-3,-2,-4
    """Проверка сортировки членов  в `Complex_i_logic` функции"""
    assert com_i('3i^3+1:i^3+10*2:3i*i-1/2i*2i^-5') == ('10*2:3*1-1/2*2^-5','-3^3+1:1^3')