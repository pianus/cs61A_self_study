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

def map_link(f,s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f,s.rest))

def filter_link(f,s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered
def join_link(s, separator):
    if s is Link.empty:
        return s
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)

def partitions(n,m):
    """Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m,s), using_m)
        without_m = partitions(n, m-1)
        return with_m + without_m

def print_partition(n,m):
    lists = partitions(n,m)
    strings = map_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))

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
def fib_tree(n):
    if n == 1 or n == 0:
        return Tree(n)
    else:
        left = Tree(fib_tree(n-2))
        right = Tree(fib_tree(n-1))
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def sum_labels(t):
    return t.label + sum([sum_labels(b) for b in t.branches])

def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        return sum([leaves(b) for b in t.branches], [])

def prune_repeats(t, seen):
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prune_repeats(b, seen)

#build a data abstraction for set, using linked list
#this impliment set as ordered sequences
# a set is represented by a linked list with unique elements that is ordered form least to greatest

def empty(s):
    return s is Link.empty

def contains(s, v):

    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)

def adjoin(s, v):
    if empty(s) or v < s.first:
        return Link(v, s)
    elif v == s.first:
        return s
    else:
        return Link(s.first, adjoin(s.rest, v))

def intersect(set1, set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect(set1.rest, set2)
        elif e2 < e1:
            return intersect(set2.rest, set1)

def union(set1,set2):
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union(set1.rest, set2))
        elif e1 > e2:
            return Link(e2, union(set2.rest, set1))

def add(s,v):
    assert not empty(s), "Cannot add to am empty set."
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v, s.rest)
    elif s.first < v:
        add(s.rest, v)
    return s

#Binary Tree class
#good for binary search (a theta(log) operation)
class BTree(Tree):
    empty = Tree(None)

    def __init__(self,label, left = empty, right = empty):
        Tree.__init__(self, label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2
'''
    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            return 'BTree({0}, {1})'.format(self.label, self.left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)
'''
def contents(t):
    if t is BTree.empty:
        return []
    else:
        return contents(t.left) + [t.lavel] + contents(t.right)

#balanced binary search tree means for every branches in a BST tree
# there are same amount of branches within them
def balanced_bst(s):
    """construct a binary search tree from a sorted list"""
    if not s:
        return BTree.empty
    else:
        mid = len(s) // 2
        left = balanced_bst(s[:mid])
        right = balanced_bst(s[mid+1:])
    return BTree(s[mid], left, right)

def largest(t):
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)

def second_largest(t):
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.label
    else:
        return second.largest(t.right)

def contains(s,v):
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    elif s.label > v:
        return contains(s.left, v)

def adjoin(s, v):
    if s is BTree.empty:
        return BTree(v)
    elif s.label == v:
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin(s.right, v))
    elif s.label > v:
        return BTree(s.label, adjoin(s.left, v), s.right)
