import pytest
from DZ.func_translate import get_det_language, func_trans, func_det_tran

def test_det_lag1():
    assert get_det_language("en") == "en"

def test_tran_lag2():
    assert func_trans("Hello") == "Здравствуйте"

def test_tran_lag3():
    assert func_det_tran("light") == ('en', 'свет')