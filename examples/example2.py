from add_on_class import AOC

class A:
    def __init__(self):
        pass
    
    def main(self):
        return "(A.main->"+self.function()+"->A.main.end)"
    
    def function(self):
        return "(A.function->A.function.end)"

class B(A):
    def main(self):
        return "(B.main->"+super().main()+"->B.main.end)"
    
    def function(self):
        return "(B.function->B.function.end)"
    
class D(AOC):
    def __post_init__(self):
        self.new_attr = 2
        
    def function(self):
        return "(D.function->"+self.__core.function(self)+"->D.function.end)"

class E(AOC):
    def __pre_init__(self):
        self.new_attr = 3
        
    def function(self):
        return "(E.function->"+self.__core.function(self)+"->E.function.end)"

e = E(D(B))()
print(e.main())
# >>> (B.main->(A.main->(E.function->(D.function->(B.function->B.function.end)->D.function.end)->E.function.end)->A.main.end)->B.main.end)
print(e.new_attr)
# >>> 2
print(issubclass(type(e), B))
# >>> True
print(E(D(B)).__name__)
# >>> BCoveredByDCoveredByE