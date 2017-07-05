#!usr/bin/env python
''' This module has examples for working with functions
'''

def class_ex():
    ''' Classes in Python are a way to define a new type.
        Instantiating a member of that type produces a new object.
        Classes have attributes, chief of which are member functions, or
        methods.
    '''
    class NewClass(object):
        ''' Like functions, classes can have docstrings
        '''
        def __init__(self):
            ''' Most classes will override the basice __init__ method
                in order to exert control over the instantiation of the new
                object, mostly like by setting up internal variables.
                Note that methods always take 'self' as the first argument.
            '''
            self.value = 'Amazing value!'

        def member_func(self, value):
            ''' Methods also have docstrings.
                Override our internal value with the argument because reasons.
            '''
            self.value = value
        def get_value(self):
            ''' See below about object privacy
            '''
            return self.value
    mynewobj = NewClass() # create a new object of type NewClass
    print(mynewobj.value) # Even though this is an internal value, we can
                          # access it because Python has no object privacy
                          # This is considered rude, however.
    mynewobj.value = 'Just OK value' # This is also permitted, but also rude.
    print(mynewobj.get_value()) # This is better, but still not great. A better
                                # way will be covered under 'decorators'
    mynewobj.member_func('Even better value!')
    print(mynewobj.value)

    # In general it is best to have __init__ perform only assignment statements
    # and any actual computation in a run() method or something similar
    class RunMe(object):
        ''' Class for running computations
        '''
        def __init__(self, value=0):
            ''' Initialize custom attributes
            '''
            self._value = value # _variable syntax indicates this is a
                                # """private""" attribute
            self._run = False # we haven't run
        def run(self):
            ''' Run the computation!
            '''
            if not self._run:
                self._value *= self._value
        def value(self):
            ''' Get the value back
            '''
            if not self._run:
                self.run() # It's nice to implicitly call .run() for the end
                           # user when possible
            return self._value
    myrunner = RunMe(5)
    print(myrunner.value())

def funcs():
    ''' assemple functions for running
    '''
    return [class_ex]
