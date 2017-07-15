#!usr/bin/env python
''' This module has examples for working with algorithms
'''
import requests

def fizzbuzz_ex():
    ''' Fizzbuzz is a simple programming problem presented relatively commonly
        in coding interviews.
        The request is: given a list of N contiguous integers, represented by
        the range [a, b), for each integer i, do the following:
            If i is divisible by 3, print 'fizz'
            If i is divisible by 5, print 'buzz'
            If i is divisible by 3 and 5, print 'fizz' first, then 'buzz'
            ('fizzbuzz')
            Otherwise, print i
    '''
    def fizzbuzz(a, b):
        items = []
        for i in range(a, b):
            s = ''
            if not i % 3:
                s += 'fizz'
            if not i % 5:
                s += 'buzz'
            s = '%d' % i if not s else s
            items.append(s)
        return items
    print('Fizzbuzz from 0 to 10:')
    print('\n'.join(fizzbuzz(0, 10)))

def funcs():
    ''' assemple functions for running
    '''
    return [fizzbuzz_ex]
