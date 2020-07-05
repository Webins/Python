import time
from inspect import currentframe, getframeinfo

class Animal:
    def __init__(self,kind):
        self._kind = kind

    def show_kind(self):
        print(f"{self.kind}")
    
    @property
    def kind(self):
        return self._kind
        
    pass


class Cat(Animal): 
    def __init__(self, name, age):
        super().__init__(self, "Cat")
        self._name = name
        self._age = age

    def make_sound(self):
        print("Meoww!")
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            fi = getframeinfo(currentframe())
            raise ValueError(f"File \"{fi.filename}\", line {fi.lineno}\nCause: The age can not be negative. Caused at: {time.ctime()}")
        elif value > 30:
            age = 30
        else: age = value
   
    pass

class Dog(Animal):
   
    def __init__(self, name, age):
        super().__init__(self, "Dog")
        self._name = name
        self._age = age

    def make_sound(self):
        print("Woff!")
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            fi = getframeinfo(currentframe())
            raise ValueError(f"File \"{fi.filename}\", line {fi.lineno}\nCause: The age can not be negative. Caused at: {time.ctime()}")
        elif value > 20:
            age = 20
        else: age = value

   
    pass


animal = Animal("Unknown")
cat = Cat("Blue", 8)
dog = Dog("Spike", 5)

print(isinstance(cat, object))
print(isinstance(cat, Animal))
print(isinstance(dog, Animal))
print(isinstance(cat, Dog))
print(isinstance(dog, Cat))

animal.show_kind()
cat.show_kind()
dog.show_kind()
cat.make_sound()
dog.make_sound()

invalid_cat = Cat("Invalid",-8)


#print(dir(animal))
#print(dir(cat))