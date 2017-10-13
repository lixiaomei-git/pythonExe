from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        print('sig:signature(func):',sig)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        print('bound_types:sig.bind_partial:',bound_types)
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            print('bound_values:sig.bind:',bound_values)
            print('bound_values.arguments:',bound_values.arguments)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x,y,z)

if __name__=='__main__':
    spam(1,2,3)
    spam(1,'hello',5)
    spam(1,'hello','word')        
