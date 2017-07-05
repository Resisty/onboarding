#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

class FuncTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_func(self):
        ''' Test that we can create and use functions
        '''
        def myfunc():
            '''Docstring!'''
            return __
        self.assertEquals(myfunc(), myfunc.__doc__) # __ is a placeholder
    def test_funcargs(self):
        ''' Test that we know about positional vs keyword arguments
        '''
        def myfunc(a, b, c=1):
            '''Another docstring!'''
            return __
        self.assertEquals(myfunc(3, 4), 7)
        self.assertEquals(myfunc(4, 5, 6), 54)
        self.assertEquals(myfunc(1, 2, c=1), 3)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(FuncTestCase)
    return the_suite
