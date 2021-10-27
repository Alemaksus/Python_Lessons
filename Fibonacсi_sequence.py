from itertools import islice

class FibFinit:
    def __init__(self, stop=650): # Stop for number 650
        self.prev = 0
        self.curr = 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr > self.stop:
            raise StopIteration
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


fib = FibFinit()
print(list(islice(fib, 1, 30)))

fib = FibFinit()
print(next(fib))
print(next(fib))
print(next(fib))