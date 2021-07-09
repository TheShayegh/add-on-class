from abc import ABC

class AOD(ABC):
    def __init__(self, obj):
        self.obj = obj
        pass

    def __getattr__(self, item):
        return getattr(self.obj, item)