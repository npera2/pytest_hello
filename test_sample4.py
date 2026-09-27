"""
在一个类中将多个测试分组
"""

"""
测试类：类名以 Test 开头（不能带 __init__ 方法），如 TestDivide
测试文件：文件名以 test_ 开头或 _test 结尾，如 test_sample.py
测试函数：函数名以 test_ 开头，如 test_answer
"""

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")  # 检查对象 x（字符串 "hello"）是否有名为 check 的属性或方法。


"""
2. 什么时候用类而不是函数？
纯函数测试：简单场景，直接写 def test_xxx(): 即可
测试类：当多个用例需要共享状态（比如打开同一个数据库连接）、或想按功能分组时，用类把相关用例组织在一起更整洁
"""

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

"""
$ pytest -k TestClassDemoInstance -q test_sample4.py
注：-k, 指定所要测试的类;
    -q, 指定所要测试的文件
"""