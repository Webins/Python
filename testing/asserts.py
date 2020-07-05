# asserts accept an expression
# returs none if the expression is truthy
# return AssertionError if the expression is falsy
# Accepts an optional error message as a second argument

# If a python file is run with -O flag (optimization mode)
# assertions will not be evaluated

def add(x, y):
    assert x > 0 and y > 0, "Both number must be positive"
    return x+y


pass

print(add(50, 10))
#print(add(-5,10))
