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
        
    def function(self):
        return "function"


a = D(A)()
print(a.new_attr)
print(a.function())

b = D(B)()
print(b.new_attr)
print(b.function())

c = D(C)()