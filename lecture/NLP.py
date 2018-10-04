class Tree():
    def __init__(self, label, branches = []):
        assert len(branches) >= 1
        for b in branches:
            assert isinstance(b, (Tree, Leaf))
        self.tag = tag
        self.branches = branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.tag, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

class Leaf:
    def __init__(self, tag, word):
        self.tag = tag
        self.word = word

lexicon = {
        Leaf('N', 'buffalo'), #beasts
        Leaf('V', 'buffalo'), #intimidate
        Leaf('J', 'buffalo'), #from new york
        Leaf('R', 'that')
}

grammar = {
        'S': [['NP', 'VP']],
        'NP': [['N'], ['J', 'N'], ['NP', 'RP']],
        'VP': [['V', 'NP']],
        'RP': [['R', 'NP', 'V'], ['NP', 'V']],
}

def parse(ling):
    words = line.split()

    def expand(start, end, tag):
        """yield all trees rooted by tag."""
        if end-start == 1:
            word = words[start]
            for leaf in lexicon:
                if tag == leaf.tag and word == leaf.word:
                    yield leaf
        if tag in grammar:
            for tags in grammar[tag]:
                for branches in expand_all(start, end, tags):
                    yield Tree(tag, branches)

    def expand_all(start, end, tags):
        """yield all sequences of branches for a sequence of tags."""
        if len(tags) == 1:
            for branch in expand(start, end, tags[0]):
                yield [branch]
        else:
            first, rest = tags[0], tags[1:]
            for middle in range(start+1, end+1 - len(rest)):
                for first_branche in expand(start, middle, first):
                    for rest_branches in expand_all(middle, end, rest):
                        yield [first_branch] + rest_branches

    for tree in expand(0, len(words), 'S'):
        print_tree(tree)
