class CoreOfDecorator:
    def __init__(self, obj):
        self.obj = obj
    
    def __getattribute__(self, attribute):
        if attribute in ['obj','__getattribute__'] :
            return object.__getattribute__(self, attribute)
        return self.obj.__class__.old__getattribute__(self.obj, attribute)
        

class AOD:
    def __init__(self, obj):
        self.obj = obj
        self.obj.__class__.old__getattribute__ = self.obj.__class__.__getattribute__
        self.core = CoreOfDecorator(obj)
        self.obj.decorator_refrence = self
        setattr(obj.__class__, '__getattribute__', AOD.__new_obj_cls__getattribute)

    def __new_obj_cls__getattribute(self, attribute):
        if attribute in ['__dict__','__class__'] :
            return object.__getattribute__(self, attribute)
        if 'decorator_refrence' in self.__dict__:
            return AOD.__getattribute__(object.__getattribute__(self, 'decorator_refrence'), attribute)
        return self.__class__.old__getattribute__(self, attribute)

    def __getattribute__(self, attribute):
        if attribute in ['__dict__','__class__','obj','__getattribute__','core'] :
            return object.__getattribute__(self, attribute)
        if attribute in self.__class__.__dict__:
            return object.__getattribute__(self, attribute)
        if attribute in self.__dict__:
            return object.__getattribute__(self, attribute)
        return getattr(self.core, attribute)

    def __setattr__(self, attribute, value):
        if attribute in ['obj','core'] :
            return object.__setattr__(self, attribute, value)
        return self.obj.__setattr__(attribute, value)
