"""Common Errors When Coding In Python"""


#1 SyntaxError
# None = 1

#2 Nameerror
try:
    print(test)
except NameError:
    print("Name Error Detected")

#3 TypeError
try:
    len(6)
    "string " + []
except TypeError:
    print("Type Error Detected")

#4 IndexError
try:
    list = [1,2,3]
    print(list[4])
except IndexError:
    print("Index Error Detected")

#5 ValueError
try:
    int("foo")
except ValueError:
    print("Value Error Detected")

#6 KeyError
try:
    d = dict()
    d["Foo"]
except KeyError:
    print("Key Error Detected")

#7 AttributeError
try:
    "awesome".foo
except:
    print("Attribute Error Detected")




