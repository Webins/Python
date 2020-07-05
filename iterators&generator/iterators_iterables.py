
iterable = "hello"  # an object that can be iterable over a loop
iterator = iter(iterable)

# when next is called on a iterator the iterator return the next item
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break



"""Range User class"""
class Counter:
    @property
    def hi(self):
        return self._hi

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    @hi.setter
    def hi(self, value):
        self._hi = value

    def __init__(self, lo, hi):
        self._current = lo
        self._hi = hi

    # iter() method
    def __iter__(self):
        return self

    # next() method
    def __next__(self):
        if self.current < self.hi:
            rs = self.current
            self.current += 1
            return rs
        else:
            raise StopIteration

    pass


for x in Counter(0, 10):
    print(x)
