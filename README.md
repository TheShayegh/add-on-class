# Abstract Object Decorator Package

With the help of this module, you can implement decorators careless about things you don't want to change.
You can see an example of this application below.

```python
from abstract_object_decorator import AOD

class Parent:
    def __init__(self):
        self.parrent_property = 1

    def parent_functionality(self):
        return 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_property = 2
        self.parrent_property = 67

    def child_functionality(self):
        return 20

class FirstDecorator(AOD):
    def __post_init__(self):
        self.first_decorator_property = 3
    
    def first_decorator_functionality(self):
        return 30

    def child_functionality(self):
        return self.__core.child_functionality(self)*2

class SecondDecorator(AOD):
    def __pre_init__(self, pre):
        self.pre = pre

    def __post_init__(self, post):
        self.post = post
        self.child_property = 12

    def child_functionality(self):
        return self.__core.child_functionality(self)*3


decorated = SecondDecorator(FirstDecorator(Child))(pre=4, post=8)
print(decorated.parrent_property)
# >>> 67
print(decorated.child_property)
# >>> 12
print(decorated.first_decorator_property)
# >>> 3
print(decorated.parent_functionality())
# >>> 10
print(decorated.child_functionality())
# >>> 120
print(decorated.first_decorator_functionality())
# >>> 30
print(issubclass(type(decorated), Parent))
# >>> True
print(decorated.pre)
# >>> 4
print(decorated.post)
# >>> 8
```

NOTE: 

* ALWAYS put `AOD` as the first base class.
* ALWAYS call `AOD.__init__` as the first line of class initializer.
* NEVER call any other base class initializer.
* Use `self.obj` to access the core object of the decorator.
* EVERY getter or setter will be redirected to the object.

Another example is here:

```python
from abstract_object_decorator import AOD

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
    
class D(AOD):
    def __post_init__(self):
        self.new_attr = 2
        
    def function(self):
        return "(D.function->"+self.__core.function(self)+"->D.function.end)"

class E(AOD):
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
# >>> BDecoratedByDDecoratedByE
```

## Installation
```pip install abstract-object-decorator```