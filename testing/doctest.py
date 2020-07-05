# we can write test for function inside of the doctstring
# to run we pass the -m docters -v option to the interpreter

def divide(a,b):
    """
    >>> divide(1,2)
    0.5
    >>> divide(100,10)
    10
    """
    return a / b


def double(values):
    """ double the values in a list

    >>> double([1,2,3,4])
    [2, 4, 6, 8]
    
    >>> double([])
    []
    
    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    
    return [2 * i for i in values]

