#!usr/bin/env python
''' This module has examples for working with functions
'''

def function_ex():
    ''' Functions are first-class citizens in Python, meaning they are actually
        objects. However, they are unlike other objects in that they invariably
        have a .__call__ method which implements the () syntax, e.g.:
        return_value = func()
        Functions are created with the def keyword
    '''
    def randominteger():
        ''' Superior random int function implementation
        '''
        return 4 # Chosen by fair dice roll
    print('I rolled a die and got %d' % randominteger())
    # Since functions are first-class citizens, we can assign them to names
    myawesomeinteger = randominteger # note the lack of ()
    print('I rolled another die and got %d' % myawesomeinteger())
    # Functions have attributes
    print(dir(myawesomeinteger))
    # You can use them in or out of the function
    def printdocs():
        ''' This is a useful docstring!
        '''
        print(printdocs.__doc__)
    print('Once more with feeling:')
    print(printdocs.__doc__)
    otherdocs = printdocs
    # Note that this does not work if 'printdocs' is ever assigned anything
    # else
    printdocs = None
    otherdocs() # Nothing happens
    # functions can accept positional and keyword arguments
    def two_arg_func(first, second):
        ''' Gimme two args or else!
        '''
        print('First I got %s, then I got %s' % (first, second))
    def keyword_func(first='something', second='else'):
        ''' I could use two arguments if you have them, but if not it's fine
        '''
        print('First I got %s, then I got %s' % (first, second))
    # Positional arguments are REQUIRED. Keyword arguments are optional as they
    # obviously have a default value
    two_arg_func(4, 5)
    # Keyword arguments can appear in any order and can be partially passed
    keyword_func()
    # If keywords are not specified, they are parsed in the order of the
    # function's definition
    keyword_func('things', 'stuff')
    keyword_func(second='things')
    keyword_func(second='things', first='stuff')

def funcs():
    ''' assemple functions for running
    '''
    return [function_ex]
