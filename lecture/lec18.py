def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

def count_frames(f):
    def counted(*args):
        counted.current_frames += 1
        if counted.max_frames < counted.current_frames:
            counted.max_frames = counted.current_frames
        result = f(*args)
        counted.current_frames -= 1
        return result
    counted.current_frames = 0
    counted.max_frames = 0
    return counted

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

def exp(b,n):
    if n == 0:
        return 1
    else:
        return b * exp(b,n-1)

def square(x):
    return x*x

def fast_exp(b,n):
    if n==0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(b,n//2))
    else:
        return b * fast(exp(b,n-1))
