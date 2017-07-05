#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

# IMPLEMENT CORE FEATURES OF THESE CLASSES
class SpecialClass(object):
    '''A very special class'''
    def __init__(self):
        '''Initialize'''
        pass # REPLACE ME
    def run(self):
        '''Run it'''
        return __
    def getstuff(self):
        '''Return it'''
        return __
class SpecialerClass(object):
    '''A very more special class'''
    def __init__(self, first, second='butts'):
        '''Initialize'''
        pass # REPLACE ME
    def run(self):
        '''Run it'''
        return __
    def getstuff(self):
        '''Return it'''
        return __

class ClassTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.special = SpecialClass()
        self.specialer = SpecialerClass('SOME', 'BODY ONCE TOLD ME')
    def test_class(self):
        ''' Test that we can create and use classes
        '''
        self.assertEquals(self.special.getstuff(), 'Stuff!') # __ is a placeholder
    def test_classargs(self):
        ''' Test that we know about positional vs keyword arguments
        '''
        self.assertEquals(self.specialer.getstuff(), 'SOMEBODY ONCE TOLD ME')

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(ClassTestCase)
    return the_suite
