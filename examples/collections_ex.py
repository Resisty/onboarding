#!usr/bin/env python
''' This module has examples for working with the collections library
'''
import collections

def defaultdict_ex():
    ''' Default dicts are a modification of dicts which have a default value
        This means fewer KeyError exceptions, in general
    '''
    mydict = collections.defaultdict(int) # All queries to mydict will have a
                                          # default value of 0, the 'basic' int
    mydict['first_entry'] = 3 # assignment works as usual
    print('The value for %s in mydict is %s'
          % ('first_entry', mydict['first_entry']))
    print('There is no value for %s in mydict yet... or is there? "%s"'
          % ('no_entry', mydict['no_entry']))

def namedtuple_ex():
    ''' Namedtuples are a way to build classlike objects (similar to C structs)
        for when you don't need the full object model
    '''
    jiver = collections.namedtuple('Jiver', 'name id favorite_beer')
    brian = jiver('Brian Auron', '#1', 'Deschutes Black Butte')
    sunny_d = jiver('David Sundberg', '#0', 'Angry Orchard')
    print('%s is a jiver and his favorite beer is %s'
          % (brian.name, brian.favorite_beer))
    print('%s is a jiver and his favorite beer is %s'
          % (sunny_d.name, sunny_d.favorite_beer))

def ordereddict_ex():
    ''' OrderedDicts preserve insertion order, but otherwise work like normal
        dicts. Note: this is the default behavior for dicts in python 3.6
    '''
    fuzz = collections.OrderedDict()
    batz = dict()
    for i in range(5):
        fuzz[i] = 'a'
        batz[i] = 'b'
    print('In python2.7, the order of batz is nondeterministic. However, in \
python3.6, fuzz and batz will have the same order:')
    print(fuzz, batz)

def counter_ex():
    ''' Counters are like dictionaries in that they are subscriptable, but are
        built around counting hashable items.
    '''
    count_stuff = collections.Counter([1,2,4,4,4,5,4,3,2,3,3,2,1,1])
    print('You can find the most common elements with the convenience \
function .most_common(): %s' % count_stuff.most_common())
    print('Limit the most common items with a parameter, like \
.most_common(2): %s' % count_stuff.most_common(2))
    print('You can obtain the non-unique items from a Counter again with \
.elements: %s' % count_stuff.elements())
    print('You can add and subtract counters:')
    butts = collections.Counter('butts')
    print(butts)
    butts.subtract(collections.Counter('stub'))
    print(butts)
    print(collections.Counter('abc') + collections.Counter('bcd'))
    print('Check help(collections.Counter) for all of the features!')

def funcs():
    ''' assemple functions for running
    '''
    return [defaultdict_ex,
            namedtuple_ex,
            ordereddict_ex,
            counter_ex]
