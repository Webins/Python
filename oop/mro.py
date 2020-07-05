class A:
    def do_something(self):
        print("Method defined in: A")
    pass

class B(A):
    def do_something(self):
        print("Method defined in: B")
        super().do_something()
    pass

class C(A):
    def do_something(self):
        print("Method defined in: C")
        super().do_something()
    pass

class D(B,C):
    def do_something(self):
        print("Method defined in: D")
        super().do_something()
    pass


# Hierarchy
#   A
#  / \
# B   C
#  \ /
#   D

#print(D.__mro__)
#print(D.mro())
#help(D)

d = D()
d.do_something()
