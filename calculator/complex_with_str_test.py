from complex_with_str import Complex_i_logic as com_i
import pytest
@pytest.mark.parametrize(
"input_signs,signs_expected",
    [('4^*2', False),
    ('4^+2', False),
    ('4^:2',False),
    ('4^-2',True),
    ('4^2',True)])
def test_Powers_InputValidity(input_powers,pow_expected):
    """Проверка записи степеней в `InputValidity` функции"""
    assert InputValidity(input_powers)== pow_expected

