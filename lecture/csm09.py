def foo():
    a = 0
    while a < 10:
        print("hello")
        yield a
        a += 1
        print("World")

def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen:
    ...     print(i)
    16
    8
    4
    2
    1
    """
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n//2
            yield n
        else:
            n = n*3+1
            yield n

class Tree():
    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k = 0):
        indented = []
        for b in self.branches:
            for line in b.indented(k+1):
                indented.append('  ' + line)
        return [str(self.label)] + indented

    def is_leaf(self):
        return not self.branches

def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield t.label
    for i in t.branches:
        yield from tree_sequence(i)

def all_paths(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5), Tree(6)]), Tree(3, [Tree(4), Tree(7)])])
    >>> print(list(all_paths(t)))
    [[1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 7]]
    """
    if t.is_leaf():
        yield [t.label]
    for b in t.branches:
        for i in all_paths(b):
            yield [t.label] + i
