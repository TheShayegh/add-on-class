from construction_requirements_integrator import CRI
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
        super().__init__(x=x, y=y, z=z)

    def __construct__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.volume = x*y*z

    def get_volume(self):
        if self.is_constructed:
            return self.volume
        else:
            raise Exception("The object is not constructed yet!")

example1 = Example(z=2)
XProvider().provide_for(example1)
YProvider().provide_for(example1)
print(example1.get_volume())
# >>> 24
print(example1.x, example1.y, example1.z)
# >>> 6 2 2

example2 = Example(z=2)
print(example2.get_volume())
# >>> Exception: The object is not constructed yet!