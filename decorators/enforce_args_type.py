from functools import wraps

def enforce(*types):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            #convert args into simething mutable
            newargs = []
            for(a, t) in zip(args, types): 
                newargs.append(t(a))
            return fn(*newargs,**kwargs)
        return wrapper
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("hello", 3)