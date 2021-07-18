from abstract_additive_class import AAD

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

class FirstAdditive(AAD):
    def __post_init__(self):
        self.first_added_property = 3
    
    def first_added_functionality(self):
        return 30

    def child_functionality(self):
        return self.__core.child_functionality(self)*2

class SecondAdditive(AAD):
    def __pre_init__(self, pre):
        self.pre = pre

    def __post_init__(self, post):
        self.post = post
        self.child_property = 12

    def child_functionality(self):
        return self.__core.child_functionality(self)*3


added = SecondAdditive(FirstAdditive(Child))(pre=4, post=8)
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