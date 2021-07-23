import unittest
from add_on_class import AOC, covering_around

class A:
    def __init__(self):
        pass

class B(A):
    pass
    
class C:
    def __init__(self):
        pass

@covering_around([A])
class D(AOC):
    def __pre_init__(self):
        self.new_attr = 3
        
@covering_around([A,B,C])
class E(AOC):
    def __pre_init__(self):
        self.new_attr = 3
        

class Test(unittest.TestCase):
    def test_true_core(self):
        a = D(A)()
        self.assertAlmostEqual(a.new_attr, 3)

    def test_child_of_true_core(self):
        a = D(B)()
        self.assertAlmostEqual(a.new_attr, 3)

    def test_false_core(self):
        could = True
        try:
            a = D(C)()
        except:
            could = False
        self.assertAlmostEqual(could, False)

    def test_multi_true_cores(self):
        a = E(B)()
        b = E(C)()
        self.assertAlmostEqual(a.new_attr, 3)
        self.assertAlmostEqual(b.new_attr, 3)