import inspect

class AOD:
    def __new__(decore_cls, core_cls):
        name = core_cls.__name__+"DecoratedBy"+decore_cls.__name__
        
        def init(self, *args, **kwargs):
            pre_init_needs = inspect.signature(decore_cls.__pre_init__).parameters
            pre_init_args = [a for a in args if a in pre_init_needs]
            pre_init_kwargs = {k:a for k,a in kwargs.items() if k in pre_init_needs}
            decore_cls.__pre_init__(self, *pre_init_args, **pre_init_kwargs)
            
            init_needs = inspect.signature(core_cls.__init__).parameters
            init_args = [a for a in args if a in pre_init_needs]
            init_kwargs = {k:a for k,a in kwargs.items() if k in pre_init_needs}
            core_cls.__init__(self, *init_args, **init_kwargs)
            
            post_init_needs = inspect.signature(decore_cls.__post_init__).parameters
            post_init_args = [a for a in args if a in post_init_needs]
            post_init_kwargs = {k:a for k,a in kwargs.items() if k in post_init_needs}
            decore_cls.__post_init__(self, *post_init_args, **post_init_kwargs)
            
            setattr(self, f'_{decore_cls.__name__}__core', core_cls)
            
        members = dict(decore_cls.__dict__)
        members['__init__'] = init

        DecoratedCls = type(
            name,
            (core_cls,),
            members
        )
        return DecoratedCls
    
    
    def __pre_init__(self):
        pass
    def __post_init__(self):
        pass