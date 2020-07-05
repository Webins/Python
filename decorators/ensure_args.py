from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError(f"No kwargs allowed in {fn.__name__} function")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"Hello my name is {name}")

greet("Tony")
greet(name ="Juan")