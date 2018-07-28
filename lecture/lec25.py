from operator import add, mul, truediv

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

def reduce(f, s, initial):
    """Combine elements of s using f starting at initial """
    """
    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    """Combine elements of s using f starting at initial """
    """
    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))
