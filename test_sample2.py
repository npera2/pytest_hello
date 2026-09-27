# -----------pytest 用例--------------
def add(a, b):
    """两数相加"""
    return a + b

def is_even(n):
    """判断是否为偶数"""
    return n % 2 == 0

def max_of_list(numbers):
    """返回列表中的最大值"""
    return max(numbers)

# -----------pytest 用例--------------
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1, 3) == 4

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is True
    assert is_even(0) is True

def test_max_of_list():
    assert max_of_list([1, 5, 3]) == 5
    assert max_of_list([-2, -10, -1]) == -1
    assert max_of_list([42]) == 42