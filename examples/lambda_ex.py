#!usr/bin/env python
''' This module has examples for working with unnamed functions, or lambdas
'''

def lambda_ex():
    ''' Lambdas are a simpler version of functions: they are still callable but
        have no name, no docstrings, and can only execute one statement
    '''
    squares = lambda x: x * x
    print('The square of 5 is: %d' % squares(5))
    # Lambdas are useful either when you do not need a fully-featured function
    # or when a class or another function accepts a function as an argument
    # Ex: sorted accepts a 'key' argument which applies the function to each
    # element before sorting
    backwards = sorted(range(10), key=lambda x: -x)
    print(backwards)

def funcs():
    ''' assemple functions for running
    '''
    return [lambda_ex]
