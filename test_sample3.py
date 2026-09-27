import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("不能除以0")  # 被测代码用raise
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):  # 测试代码断言会抛出异常
        divide(1, 0)