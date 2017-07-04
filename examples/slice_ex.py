#!usr/bin/env python
''' This module has examples for working with comprehensions and slices
'''
def comprehension_ex():
    ''' A comprehennsion is a shorthand for constructing lists. It can also
        create dictionaries.
    '''
    # Basic numerical list
    basic = [i for i in range(10)]
    # This is the same as:
    # basic = []
    # for i in range(10):
    #    basic.append(i)
    # Comprehensions can use logic, just like for loops
    odds = [i for i in range(10) if not i % 2]
    # Comprehensions can be composed like for loops
    repetition = [j for i in range(11) for j in range(i)]
    # Comprehensions can also be nexted
    # Why do we need to specify range(1, 11) instead of range(11)?
    nested = [[i for i in range(j)] for j in range(1, 11)]
    print(basic)
    print(odds)
    print(repetition)
    print(nested)

def slice_ex():
    ''' A slice is an object which partitions sequences (e.g. list, tuples) but not
        dicts
    '''
    iterlist = [i for i in range(10)]
    itertuple = tuple(iterlist)
    itergen = range(10)
    stop = slice(5) # Take only the first five items
    startstop = slice(1, 6) # Take only the items indexed at 1 to 5, inclusive
    startstopstep = slice(2, 8, 3) # Take only every index divisible by 3 of
                                   # the items indexed at 2 to 7, inclusive
    print(iterlist[stop])
    print(itertuple[startstop])
    print([i for i in itergen[startstopstep]])


def funcs():
    ''' assemple functions for running
    '''
    return [comprehension_ex,
            slice_ex]
