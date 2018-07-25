def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) <1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def print_tree(t, indent = 0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)

t = tree(1,
      [tree(3,
          [tree(4),
tree(5),
           tree(6)]),
      tree(2)])

def tree_max(t):
    """ return the max of a tree"""
    assert is_tree(t) == True
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t)] + [tree_max(b) for b in branches(t)])

def height(t):
    """Return the height of a tree"""
    assert is_tree(t) == True
    if is_leaf(t):
        return 1
    else:
        return max([height(b)+1 for b in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t"""
    assert is_tree(t) == True
    if is_leaf(t):
        return label(t)**2
    else:
        return sum([square_tree(b) for b in branches(t)])
t1 = [2, [7, [3], [6, [5], [11]]], [15]]

def find_path(tree, x):
    """
    >>> tt = [2, [7, [3], [6, [5], [11]]], [15]]
    >>> find_path(tt, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    def inner(tree, x):
        if label(tree) == x:
            return [label(tree)]
        elif is_leaf(tree):
            return []
        else:
            lst = [[label(tree)]+inner(b, x) for b in branches(tree)]

            for i in lst:
                if x in i:
                    return i
            return []
    lst1 = inner(tree,x)
    if lst1:
        return lst1
    else:
        return None
        



def prune(t, k):
    if k == 0:
        return [label(t)]
    else:
        return tree(label(t),[prune(b,k-1) for b in branches(t)])
