# Abstract Design Patterns Package

This package, with the aim of accelerating and facilitating the use of some design patterns, offers abstract classes that by inheriting other classes from them, you can more easily achieve the desired design patterns. These classes are implemented to be inherited alongside other classes.



## Construction Requirements Integrator

With the help of this module, classes can be inherited that are built and configured after their needs are met (instead of being launched immediately after creation).
You can see an example of this application below:

```python
from construction_requirements_integrator import CRI, construction_required
from random import random

class XProvider:
    def __init__(self):
        self.x = int((random()*10))

    def provide_for(self, obj):
        obj.meet_requirement('x', self.x)

class YProvider:
    def __init__(self):
        self.y = int((random()*5))

    def provide_for(self, obj):
        obj.meet_requirement('y', self.y)

class Example(CRI):
    def __init__(self, x=None, y=None, z=None):
        CRI.__init__(self, x=x, y=y, z=z)

    def __construct__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.volume = x*y*z

    def get_construction_status(self):
        return self.is_constructed

    @construction_required
    def get_volume(self):
        return self.volume

example1 = Example(z=2)
XProvider().provide_for(example1)
YProvider().provide_for(example1)
print(example1.get_construction_status())
# >>> True
print(example1.get_volume())
# >>> 24
print(example1.x, example1.y, example1.z)
# >>> 6 2 2

example2 = Example(z=2)
print(example2.get_construction_status())
# >>> False
print(example2.get_volume())
# >>> Exception: The object is not constructed yet!
```

* Use `construction_required` annotation to avoid running a function before completion of the construction.

When calling the `__init__` function from the `CRI` class, you can input settings:

* `overwrite_requirement (default: False)`: If true, if one entry is entered multiple times, the previous values will be ignored and the new value replaced.
* `ignore_resetting_error (default: False)`: If `overwrite_requirement` is not true, if one entry is entered multiple times, the object raises an error. This error will not be published if `ignore_resetting_error` is true.
* `auto_construct (default: True)`: If true, the class starts to build, As soon as the class requirements are met. If false, You must call `integrate_requirements` to build the class.
* `purge_after_construction (default: True)`: The class does not need the values collected for the requirements after completing the build process (unless it is stored again during the construction process). Therefore, after completing this process, it will delete them.
You can prevent this by setting `purge_after_construction` to `False`.
* `reconstruct (default: False)`: If true, allows the class to be reconstructed with new values.



## Abstract Object Decorator

With the help of this module, you can implement decorators careless about things you don't want to change.
You can see an example of this application below:

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

class FirstDecorator(Parent, AOD):
    def __init__(self, obj):
        AOD.__init__(self, obj)
        self.first_decorator_property = 3
    
    def first_decorator_functionality(self):
        return 30

    def child_functionality(self):
        return self.obj.child_functionality()*2

class SecondDecorator(Parent, AOD):
    def __init__(self, obj):
        AOD.__init__(self, obj)
        self.child_property = 12

    def child_functionality(self):
        return self.obj.child_functionality()*3


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
```



## Installation
Package is avalable on [PyPI](https://test.pypi.org/project/abstract-design-patterns/).