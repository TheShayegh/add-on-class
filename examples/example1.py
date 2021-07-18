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