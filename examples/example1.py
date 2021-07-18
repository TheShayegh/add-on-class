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

class FirstDecorator(AOD, Parent):
    def __init__(self, obj):
        AOD.__init__(self, obj)
        self.first_decorator_property = 3
    
    def first_decorator_functionality(self):
        return 30

    def child_functionality(self):
        return self.core.child_functionality()*2

class SecondDecorator(AOD, Parent):
    def __init__(self, obj):
        AOD.__init__(self, obj)
        self.child_property = 12

    def child_functionality(self):
        return self.core.child_functionality()*3


decorated = SecondDecorator(FirstDecorator(Child()))
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
