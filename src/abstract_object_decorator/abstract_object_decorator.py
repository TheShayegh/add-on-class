class AOD:
    def __init__(self, obj):
        self.obj = obj

    def __getattribute__(self, attribute):
        if attribute in ['__dict__','__class__','obj'] :
            return object.__getattribute__(self, attribute)
        if attribute in self.__class__.__dict__:
            return object.__getattribute__(self, attribute)
        if attribute in self.__dict__:
            return object.__getattribute__(self, attribute)
        return self.obj.__getattribute__(attribute)

    def __setattr__(self, attribute, value):
        if attribute in ['obj'] :
            return object.__setattr__(self, attribute, value)
        return self.obj.__setattr__(attribute, value)