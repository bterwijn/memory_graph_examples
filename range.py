
class My_Iterator:
    def __init__(self, range):
        self.range = range
        self.current = range.start
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.range.step > 0:
            if self.current >= self.range.stop:
                raise StopIteration
        else:
            if self.current <= self.range.stop:
                raise StopIteration
        value = self.current
        self.current += self.range.step
        return value

class My_Range:
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if stop is None:
            self.stop = start
            self.start = 0
            
    def __iter__(self):
        return My_Iterator(self)

print(list(My_Range(5)))
print(list(My_Range(5, 10)))
print(list(My_Range(5, 10, 2)))
print(list(My_Range(0, -5, -2)))
