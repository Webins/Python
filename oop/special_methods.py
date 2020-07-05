from copy import copy

class Human:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last}"
    
    def __len__(self):
        return self.age

    def __add__(lhs, rhs):
        if isinstance(rhs, Human):
            return Human(first="Newborn", last=lhs.last, age=0)
        else:
            raise TypeError(f"{rhs} is not instance of Human")

    def __mul__(self, times):
        if isinstance(times, int):
            return [copy(self) for i in range(times)]
        raise TypeError(f"{times} is not an integer values")
     

    @property
    def first(self):
        return self._first

    @property
    def last(self):
        return self._last
    
    @property
    def age(self):
        return self._age
    

    pass


Elliot = Human("Elliot", "Alderson", 32)

print(Elliot)
print(len(Elliot))

J = Human("Jenny", "Larsen", 30)
K = Human("Kevin", "Jones", 32)

print(J + K)

print(K * 2)


twins = (J + K) * 2

print(twins)