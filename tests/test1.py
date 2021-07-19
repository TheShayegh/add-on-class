import unittest
from add_on_class import AOC

class A:
    def __init__(self):
        self.a = 2
        self.z = 1

    def __getattr__(self, attr):
        return f"->{attr}"

    def func(self):
        return 25

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 4
        self.z = 3

    def main(self):
        return self.func()*2

class C(B):
    def __init__(self):
        super().__init__()
        self.c = 12
        self.x = 63

    def func(self):
        return super().func()-10

class Decorator1(AOC):
    def __post_init__(self):
        self.d = 72
        self.x = 96

    def func(self):
        return self.__core.func(self)*3

    def new_func(self):
        return "new function"

class Decorator2(AOC):
    def second_func(self):
        return 100

    def main(self):
        return self.second_func()+self.__core.main(self)

dec = Decorator1(C)()

class Test(unittest.TestCase):
    def test_decorator1_d(self):
        self.assertAlmostEqual(dec.d, 72)

    def test_decorator1_x(self):
        self.assertAlmostEqual(dec.x, 96)

    def test_decorator1_new_func(self):
        self.assertAlmostEqual(dec.new_func(), "new function")

    def test_decorator1_func(self):
        self.assertAlmostEqual(dec.func(), 45)

    def test_decorator1_c(self):
        self.assertAlmostEqual(dec.c, 12)

    def test_decorator1_b(self):
        self.assertAlmostEqual(dec.b, 4)

    def test_decorator1_z(self):
        self.assertAlmostEqual(dec.z, 3)

    def test_decorator1_a(self):
        self.assertAlmostEqual(dec.a, 2)

    def test_decorator1_unk(self):
        self.assertAlmostEqual(dec.unk, "->unk")

    def test_decorator1_main(self):
        self.assertAlmostEqual(dec.main(), 90)

    def test_multi_decorators(self):
        dec1_1 = Decorator1(C)()
        dec2_1 = Decorator2(C)()
        dec1_2 = Decorator1(C)()
        self.assertAlmostEqual(dec1_2.main(), 90)