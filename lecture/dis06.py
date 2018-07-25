
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [lst[i] * i for i in range(0,len(lst),2)]

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) == 0 or len(lst) == 1:
        return lst
    pivot = lst[0]
    less = quicksort_list([i for i in lst if i < pivot])
    greater = quicksort_list([i for i in lst if i > pivot])
    return less + [pivot] + greater

def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    total = 1
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        cache = []
        for i in range(len(lst)):
            for j in range(i+2, len(lst)+1):
                cache.append(lst[i] * max_product(lst[j:]))
        if cache:
            return max(cache)
        else:
            return 1



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

def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if is_leaf(tree):
        return label(tree)
    else:
        if label(tree) == '*':
            total = 1
            for i in [eval_tree(b) for b in branches(tree)]:
                total *= i
            return total
        elif label(tree) == '+':
            total = 0
            for i in [eval_tree(b) for b in branches(tree)]:
                total += i
            return total


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

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    >>> tree.label
    2
    >>> tree.branches[0].label
    4
    >>> tree.branches[1].branches[0].label
    8

    """
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(b, new_f) for b in t.branches]
    return t
