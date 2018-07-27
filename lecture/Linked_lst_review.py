class Link():
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        """Return a string that would evaluate to s"""
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + Link.__repr__(self.rest)
        return 'Link({0}{1})'.format(self.first, rest)

    def __add__(self,t):
        if self is Link.empty:
            return t
        else:
            return Link(self.first, Link.__add__(self.rest, t))

    @property
    def second(self):
        if self.rest == empty:
            return empty
        else:
            return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    """
    if lst.rest == Link.empty:
        return lst
    elif lst.rest.rest == Link.empty:
        return Link(lst.first, Link.empty)
    return Link(lst.first, skip(lst.rest.rest))

def skip2(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip2(a)
    >>> b
    >>> a
    Link(1, Link(3))
    """
    if lst.rest == Link.empty:
        return None
    elif lst.rest.rest == Link.empty:
        lst.rest = Link.empty
        return None
    lst.rest = lst.rest.rest
    skip2(lst.rest)

def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    reversed = Link.empty
    def inner_reverse(lst):
        nonlocal reversed
        if lst != Link.empty:
            reversed = Link(lst.first, reversed)
            inner_reverse(lst.rest)
    inner_reverse(lst)
    return reversed

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """

    if n == 0:
        return True
    elif t.is_leaf() and (n > 1 and t.label == elem or n > 0 and t.label != elem):
        return False
    elif t.label == elem:
        return any([contains(elem, n-1, b) for b in t.branches] + [n == 1])
    else:
        return any([contains(elem, n, b) for b in t.branches] )

def factor_tree(n):
    for i in range(2,n):
        if n % i == 0:
            return Tree(i, [factor_tree(n//i)])
    return Tree(n)

def stretch(s, repeat = 0):

    if s != Link.empty:
        for i in range(repeat):
            s = Link(s.first, s)
            s = s.rest
        stretch(s.rest, repeat + 1)

a = Link(3, Link(4, Link(5, Link(6))))
