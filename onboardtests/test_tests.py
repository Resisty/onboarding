#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest

class TestTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.int = 0
        self.float = 0.0
        self.string = 'This is a string!'
        self.list = []
        self.dict = {}
    def test_int(self):
        ''' Test that we have an integer
        '''
        self.assertEquals(__, 0) # __ is a placeholder
    def test_float(self):
        ''' Test that we have a float
        '''
        self.assertEquals(__, 0.0)
    def test_string(self):
        ''' Test that we have a string
        '''
        self.assertEquals(__, str) # What is the bareword 'str'?
    def test_list(self):
        ''' Test that we have a list
        '''
        self.assertTrue(isinstance(__, list)) # Another way of thinking about
                                              # type comparison
    def test_dict(self):
        ''' Test that we have a dict
        '''
        with self.assertRaises(KeyError):
            __.pop(1) # What happens when we call pop(1) on a dict?

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(TestTestCase)
    return the_suite
