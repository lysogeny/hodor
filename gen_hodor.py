#!/usr/bin/env python3

import random
import itertools
import copy
import random

#hodor = "hodor"
#
#hodors = []
#
## I need 7776 different hodors I think
#
#n = len(hodor)
#ns = list(range(n))
#print(n)
#print(ns)
#instructions = ['cap'+str(i) for i in ns]
#instructions += ['dup'+str(i) for i in ns]
#print(instructions)
#for i in ns+[n]:
#    positions = list(itertools.combinations(ns, i))
#    hodor_local = hodor
#    for j in positions:
#        hodor_local = list(hodor)
#        for i in j:
#            hodor_local[i] = hodor_local[i].capitalize()
#        hodor_local = ''.join(hodor_local)
#        print(hodor_local)

LEET_MAP = {
    'o': '0',
    'a': '4',
    'l': '1',
    'I': 'i',
    's': '$',
}

class Word:
    """A word"""
    def __init__(self, string):
        self.value = list(string)

    def __repr__(self):
        return ''.join(self.value)

    def __str__(self):
        return ''.join(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value

    def __hash__(self):
        return hash(''.join(self.value))

    @property
    def length(self):
        """The length of this object"""
        return len(self.value)

    @property
    def max_i(self):
        """The maximum position in this object"""
        return self.length - 1

    @property
    def min_i(self):
        """The minimum position in this object"""
        return 0

    @property
    def permute_methods(self):
        """Return all methods capable of returning permutations"""
        return [getattr(self, method) for method in dir(self) if method.startswith('permute')
                and method != 'permute_methods']

    def copy(self):
        """Returns a deep copy"""
        return copy.deepcopy(self)

    def capitalise(self, i: int):
        """Change capitalisation of the symbol at position i"""
        self.value[i] = self.value[i].swapcase()
        return self

    def capitalise_all(self, i: list):
        """Capitalises all values at all positions in i"""
        selfcopy = self.copy()
        for position in i:
            selfcopy.capitalise(position)
        return selfcopy

    def duplicate(self, i: int):
        """Duplicate letter at position i"""
        self.value = self.value[:i] + [self.value[i]] + self.value[i:]
        return self

    def append(self, i: int):
        """Append punctuation i"""
        self.value.append(i)
        return self

    def prepend(self, i: int):
        """Prepend puncuation i"""
        self.value = [i] + self.value
        return self

    def swap_leet(self, i: int):
        """Change symbol i to leetspeak"""
        raise NotImplementedError

    def permute_capitalise(self):
        """Returns all possible capitalisations of self"""
        positions = list(range(self.min_i, self.max_i+1))
        for position in positions:
            mutations = itertools.combinations(positions, position)
            for mutation in mutations:
                yield self.capitalise_all(mutation)

    def permute_copy(self):
        """Returns all possible duplications of self"""
        positions = list(range(self.min_i, self.max_i+1))
        for position in positions:
            yield self.copy().duplicate(position)

    def permute_append(self):
        """Returns all possible appends of self"""
        #symbols = '.,!?‽:;'
        symbols = '!?‽.'
        for symbol in symbols:
            yield self.copy().append(symbol)

    def no_permute_prepend(self):
        """Returns all possible prepends of self"""
        symbols = '¿¡'
        for symbol in symbols:
            yield self.copy().prepend(symbol)

    def permutations(self):
        for method in self.permute_methods:
            for mutation in method():
                yield mutation

word = Word('hodor')
word.capitalise_all([1,2,3])

def rprint(i=0):
    """Closure for tracking line numbers in prints."""
    def printer(word):
        nonlocal i
        i += 1
        print(f'{i} {word}', end='\r')
    return printer

printer = rprint(0)
def permute(word, depth=2) -> set:
    """Permutes word to a max depth of depth

    This search for hodor is not really tractable.
    A dynamic programming algorithm might be better.
    """
    mutations = set(word.permutations())
    if depth:
        new = list()
        for mutation in mutations:
#            printer(mutation)
            new += permute(mutation, depth-1)
            #new += novel
        return new
    return [word]

words = permute(word, 3)
words = set(words)
#print(len(words))
nums = [''.join(num) for num in itertools.product('123456', repeat=5)]
words = random.sample(words, len(nums))
tab = [nums, [word.__str__() for word in words]]
for row in zip(*tab):
    print('\t'.join(row))


#new = set('a')
#while new:
#    words = set()
#    mutations = set(word.permutations())
#    new = mutations.difference(words)
#    for mutation in mutations:
#        words.add(mutation)
#    print(new)
#
# The goal is to create a bunch of variatons of the word "hodor". I estimate
# that I need at least about 6**4 hodors (1296).
# I think that a recursive algorithm should work best.
# Start out with the word, and add permutations until sufficient amounts of
# hodor are created.
# Permutations may include:
# - Duplicate letter
# - Capitalise letter
# - Append punctuation
# - Prepend spanish punctuation
# - Replace letter with leetspeak version

# hodor will have all possible duplications, capitalisations, and such be done
# to it. Every successive word will recieve the same treatment until enough
# unique words are created.

# This will be used to create an absolutely unusable diceware list.
