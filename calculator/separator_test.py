import pytest
from separator_module import separator
#вручную вызываем в консоли по python -m pytest separator_test.py
def test_smoke_separator():
    assert separator('2^i+3') == ['3','2^i']
@pytest.mark.parametrize(
"input_str,output_strs",
    [('-1i+2i*2i:4i^5i+24/6i-23/7*i-1+2*3:4^5+23/6', ['-1+2*3:4^5+23/6','-1i+2i*2i:4i^5i+24/6i-23/7*i']),
    ('-42/34i:3i+5*3-56/32i+56/23*7^2-5^3i+32*3', ['5*3+56/23*7^2+32*3','-42/34i:3i-56/32i-5^3i']),
    ('4i*56+56-31i*4-56',['56-56','4i*56-31i*4']),
    ('4i*4:5+4:4*5+4*4i:5+642-3i:56+4+i',['4:4*5+642+4','4i*4:5+4*4i-3i:56+i']),
    ('4/5*3*2i+45+3*4/5i*2-2-3*4/5:2i',['45-2','4/5*3*2i+3*4/5i*2-3*4/5:2i'])])
def test_separator(input_str,output_strs):
    """Проверка разделения членов с мнимой частью в `separator` функции"""
    assert separator(input_str)== output_strs