import inspect

init_string_template = """
def init(
    {0}
) -> None:

    setattr(self, f'_{4}__core', core_cls)

    decore_cls.__pre_init__(
        {1}
    )

    core_cls.__init__(
        {2}
    )

    decore_cls.__post_init__(
        {3}
    )

""".format

def generate_init_string(decore_cls, core_cls):
    all_needs = {}
    post_init_needs = inspect.signature(decore_cls.__post_init__).parameters
    post_init_needs = {name: post_init_needs[name] for name in post_init_needs}
    all_needs.update(post_init_needs)
    pre_init_needs = inspect.signature(decore_cls.__pre_init__).parameters
    pre_init_needs = {name: pre_init_needs[name] for name in pre_init_needs}
    all_needs.update(pre_init_needs)
    init_needs = inspect.signature(core_cls.__init__).parameters
    init_needs = {name: init_needs[name] for name in init_needs}
    all_needs.update(init_needs)

    for need in all_needs:
        if str(all_needs[need].kind) in ['VAR_KEYWORD','VAR_POSITIONAL']:
            raise Exception("AOC can not be added to a function that receives *args or **kwargs as initialization input.")

    def input_args_to_string(args):
        phrases = []
        for arg in args:
            if arg=='self':
                continue
            if all_needs[arg].default is inspect._empty:
                phrases = [arg]+phrases
            else:
                phrases.append(f"{arg}={all_needs[arg].default}")
        phrases = ['self']+phrases
        return ',\n    '.join(phrases)

    def args_to_string(args):
        return ',\n        '.join([arg for arg in args])

    init_string = init_string_template(
        input_args_to_string(all_needs),
        args_to_string(pre_init_needs),
        args_to_string(init_needs),
        args_to_string(post_init_needs),
        decore_cls.__name__,
    )
    return init_string



class AOC:
    def __new__(decore_cls, core_cls):
        name = core_cls.__name__+"CoveredBy"+decore_cls.__name__
        
        fake_scope = {'decore_cls':decore_cls, 'core_cls':core_cls}
        exec(generate_init_string(decore_cls, core_cls), fake_scope)
        init = fake_scope['init']
            
        members = dict(decore_cls.__dict__)
        members['__init__'] = init

        CoveredCls = type(
            name,
            (core_cls,),
            members
        )
        return CoveredCls
    
    
    def __pre_init__(self):
        pass
    def __post_init__(self):
        pass