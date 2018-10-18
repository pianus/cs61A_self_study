class FlatMapper:
    """
    A FlatMapper takes a function fn that returns an iterable
    value.  The  flat_map method takes an iterable s and
    returns a generator over all values in the iterables
    returned by calling fn on each element of s.
    >>> stutter = lambda x: [x, x]
    >>> m = FlatMapper(stutter)
    >>> g = m.flat_map((2, 3, 4, 5))
    >>> type(g)
    <class 'generator'>
    >>> list(g)
    [2, 2, 3, 3, 4, 4, 5, 5]
    """
    def __init__(self, fn):
        self.fn = fn

    def flat_map(self,s):
        for i in s:
            yield from self.fn(i)

class Adele:
    times = '1000'
    def __init__(self, you):
        self.call = you
    def __str__(self):
        return self.times

class Hello(Adele):
    def __next__(self):
            return next(self.call)

never = iter('scheme2Bhome')

def any(more):
    next(never)
    print(outside)
    yield next(never)
    print(next(never))
    yield more(more)


def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that
        are all true values.
    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    while x:
        yield x
        x = f(x)
