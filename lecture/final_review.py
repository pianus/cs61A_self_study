from link_tree_class import Link, Tree, BTree


def insert_everywhere(t, val):
    if not t.branches:
        return
    for b in t.branches:
        insert_everywhere(b, val)
    t.branches.append(Tree(val))

def tree_greater_than(t1, t2):
    count = 0
    if t1.label > t2.label:
        count += 1
    if t1.branches:
        for i in range(len(t1.branches)):
            count += tree_greater_than(t1.branches[i], t2.branches[i])
    return count

def flatten(t):
    if t == BTree.empty:
        return Link.empty

    if not t.left == BTree.empty:
        left = flatten(t.left)


def swap_pairs(lst):
    """
    >>> a = Link(2, Link(1, Link(4, Link(3, Link(6, Link(5))))))
    >>> swap_pairs(a)
    >>> a
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    """
    if lst is not Link.empty:
        lst.rest.first, lst.first = lst.first, lst.rest.first
        swap_pairs(lst.rest.rest)

def double_double(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> double_double(a)
    >>> a
    Link(2, Link(2, Link(4, Link(4, Link(6, Link(6))))))
    """
    """
    if lst is not Link.empty:
        lst.first *= 2
        lst.rest = Link(lst.first, lst.rest)
        double_double(lst.rest.rest)
    """
    if lst != Link.empty:
        lst.first = lst.first * 2
        double_double(lst.rest)
        lst.rest = Link(lst.first, lst.rest)
    else:
        return


def pascal_row(s):

    if s is Link.empty:
        return Link(1)

    start = Link(1)
    last = start
    while s.rest is not Link.empty:
        last.rest = Link(s.first + s.rest.first)
        last = last.rest
        s = s.rest
    last.rest = Link(1)
    return start

def behavior(a):
    b = list(mystery(a))
    return [list(i) for i in b]

def mystery(a):
    """
    >>> x = behavior(5)
    >>> x[0]
    [0, 0, 0, 0, 0]
    >>> x[1]
    [1, 0, 1, 0, 1]
    >>> x[2]
    [1, 2, 0, 1, 2]
    >>> y = behavior(2)
    >>> y[0]
    [0, 0]
    >>> y[1]
    [1, 0]
    >>> len(x)
    5
    >>> len(y)
    2
    """
    def mystery2(b):
        for i in range(a) :
            yield (i+1) % b
    for j in  :
        yield
