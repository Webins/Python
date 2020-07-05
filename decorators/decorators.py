#decorators wraps other function and enhance their behavior
#are examples of high order funcion and have their own syntax

#decorators as function

def be_polite(fn,name=""):
    def wrapper():
        print("What a pleasure to meet you!")
        fn(name)
        print("Have a great day")

    return wrapper

def greet(name="Paulo"):
    print("My name is " + name)

(be_polite(greet,"Kira"))()

#With syntax sugar
def be_polite2(fn):
    def wrapper(name):
        print("What a pleasure to meet you!")
        fn(name)
        print("Have a great day")

    return wrapper

@be_polite2
def greet2(name):
    print("My name is " + name)

greet2("Lalo")


#decorator with different signature
def be_polite3(fn):
    def wrapper(*args,**kwargs):
        print("What a pleasure to meet you!")
        fn(*args,**kwargs)
        print("Have a great day")

    return wrapper

@be_polite3
def greet3(name, city):
    print("My name is " + name + " I'm living in " + city)


greet3("Larry","New York")
