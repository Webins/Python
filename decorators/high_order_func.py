#passed func as arg
def sum(n, func):
    total = 0
    for num in range (1, n+1):
        total += func(n)
    
    return total

def square(n):
    return n**2

def cube(n):
    return n**3

print(sum(3,square))
print(sum(3,cube))

#nested func
def say_hello(name):
    def greet():
        from random import choice 
        return choice(('Good morning','Good afternoon','Good night'))

    return f"{greet()} {name}"

print(say_hello("Peter"))


#returned func
def make_laugh_func():
  
    def get_laugh():
        from random import choice 
        return choice(("Jajaja", "Jejeje", "hahaha", "hehehe"))

    return get_laugh()

print(say_hello("Peter ") + (make_laugh_func)() )

