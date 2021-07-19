# Add-On Class Package

This package provides you with a module that allows you to easily define classes that are stacked on top of each other and add features to each other, creating a whole new class.
You can see an example of this application below.

```python
from add_on_class import AOC

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

class FirstAddOn(AOC):
    def __post_init__(self):
        self.first_added_property = 3
    
    def first_added_functionality(self):
        return 30

    def child_functionality(self):
        return self.__core.child_functionality(self)*2

class SecondAddOn(AOC):
    def __pre_init__(self, pre):
        self.pre = pre

    def __post_init__(self, post):
        self.post = post
        self.child_property = 12

    def child_functionality(self):
        return self.__core.child_functionality(self)*3


added = SecondAddOn(FirstAddOn(Child))(pre=4, post=8)
print(added.parrent_property)
# >>> 67
print(added.child_property)
# >>> 12
print(added.first_added_property)
# >>> 3
print(added.parent_functionality())
# >>> 10
print(added.child_functionality())
# >>> 120
print(added.first_added_functionality())
# >>> 30
print(issubclass(type(added), Parent))
# >>> True
print(added.pre)
# >>> 4
print(added.post)
# >>> 8
```

* The output of the AOC constructor is a class itself and you need to get an instance from it again.
* Based on order of calling add-on classes and acording to `__pre_init__` and `__post_init__` functions, overrides occur. Use this logic to customize what you need.
* Use `self.__core` to access the added class directly. It's useful when you need to call a function of core class that is overridden by the add-on one. (See the example above)

Another example is here. Note the type of `E(D(B))`. It is `BCoveredByDCoveredByE` and is a subclass of `B`:

```python
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
```

* NOTE: AOC can not be added to a class that receives *args or **kwargs as initialization input.

## Installation
```pip install add-on-class```