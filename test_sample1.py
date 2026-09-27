def func(x):
    return x + 1

# pytest 会自动收集所有以 test_ 开头的函数作为测试用例（这就是这里命名为 test_answer 的原因）
def test_answer():
    assert func(3) == 4