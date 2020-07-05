from functools import wraps
#wraps preservers a function's metadata when it is decorated

def log_metadata(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Name: {fn.__name__}")
        print(f"Doc: {fn.__doc__}")
        return fn(*args, **kwargs)
        

    return wrapper


@log_metadata
def add(x,y):
    """Adds two numbers together """
    return x + y

print(add.__doc__)

print(add(5,51))
