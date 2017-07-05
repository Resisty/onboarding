#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None
___ = 0

class LambdaTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_lambda(self):
        ''' Test that we can create and use lambdas
        '''
        func = lambda: __
        self.assertEquals(func(), 'Return value!') # __ is a placeholder
    def test_lambdaargs(self):
        ''' Test that we know about lambda arguments
        '''
        func = lambda x, y: __
        self.assertEquals(func(5, 10), '10 over 5 is 2!')
    def test_practical(self):
        ''' Test that we know how to use lambdas as args in other functions
        '''
        iterable = sorted(range(5), key=lambda x: ___)
        self.assertEquals(iterable, [4, 3, 2, 1, 0])
    def test_dictcomp(self):
        ''' Test that we can create a dictionary via comprehension
        '''
        comp = {__:__}
        self.assertEquals(comp, {0: 0.0, 1: .5, 2: 1.0})

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(LambdaTestCase)
    return the_suite
