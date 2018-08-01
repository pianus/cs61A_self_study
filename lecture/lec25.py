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

class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess

def improve(update, done, guess=1, max_updates = 1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return last_guess
    except ValueError:
        raise IterImproveError(guess)

def find_zero(f, guess = 1):
    def done(x):
        return f(x) == 0
    try:
        return improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last_guess
