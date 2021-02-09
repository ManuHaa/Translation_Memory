class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class NullObject:

    def _ _init_ _(self, *args, **kwargs): pass
    def _ _call_ _(self, *args, **kwargs): return self
    def _ _repr_ _(self): return "Null(  )"
    def _ _nonzero_ _(self): return 0

    def _ _getattr_ _(self, name): return self
    def _ _setattr_ _(self, name, value): return self
    def _ _delattr_ _(self, name): return self