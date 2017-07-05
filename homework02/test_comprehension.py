#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

class CompTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_listcomp(self):
        ''' Test that we know how a comprehension works
        '''
        self.assertEquals(__, [0, 1, 2]) # __ is a placeholder
    def test_controlcomp(self):
        ''' Test that we know about expressions in comprehensions
        '''
        comp = [__]
        self.assertEquals(comp, [0, 2, 4, 8])
    def test_nest(self):
        ''' Test that we know how to nest comprehensions
        '''
        comp = [__]
        self.assertEquals(comp, [[0], [0, 1], [0, 1, 2]])
    def test_dictcomp(self):
        ''' Test that we can create a dictionary via comprehension
        '''
        comp = {__:__}
        self.assertEquals(comp, {0: 0.0, 1: .5, 2: 1.0})

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(CompTestCase)
    return the_suite
