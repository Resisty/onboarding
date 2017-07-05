#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

class SliceTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        ''' Do this at the start of all tests
        '''
        self.iterable = [i for i in range(10)]
    def test_stop(self):
        ''' Test that we know what a single-argument slice does
        '''
        stop = slice(5)
        self.assertEquals(__, self.iterable[stop]) # __ is a placeholder
    def test_start(self):
        ''' Test that we know what a two-argument slice does
        '''
        start = slice(2, 8)
        self.assertFalse(__, self.iterable[start])
    def test_step(self):
        ''' Test that we know what a three-argument slice does
        '''
        step = slice(1, 10, 4)
        self.assertEquals(__, self.iterable[step])

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(SliceTestCase)
    return the_suite
