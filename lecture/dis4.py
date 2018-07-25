def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def mutate(fun):
        nonlocal n
        n = fun(n)
        print(n)
        return memory(n)
    return mutate

def add_this_many(x, el, lst):
    """
    Adds el to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    lst.extend(len([i for i in lst if i == x]) * [el])

def reverse(lst):
    """
    Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    for i in range(len(lst)):
        lst.insert(i,lst.pop())

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    lst = [[fn(i),i] for i in s]
    lst = sorted(lst)
    dic = {}
    for key, value in lst:
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]
    return dic

def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key, value in d.items():
        if type(value) == dict:
            replace_all_deep(value,x,y)
        elif value == x:
            d[key] = y
