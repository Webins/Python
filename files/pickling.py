import pickle
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

    def __add__(self, rhs):
        if isinstance(rhs, Human):
            return Human(first="Newborn", last=self.last, age=0)
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

humans = (Human("Joy","Rodriguez",32),Human("Lalo","Ortega",16),Human("Alexandra","Martinez",21))

with open('humans.pickle', "wb") as file:
    pickle.dump(humans, file)

with open('humans.pickle', "rb") as file:
    humans = pickle.load(file)
    for human in humans:
        print(human)