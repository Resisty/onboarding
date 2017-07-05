#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None
___ = True

class LogicTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_true(self):
        ''' Test that we know how to use True
        '''
        self.assertTrue(__) # __ is a placeholder
    def test_false(self):
        ''' Test that we know how to use False
        '''
        self.assertFalse(___)
    def test_equality(self):
        ''' Test that we know what equality is
        '''
        self.assertEquals(0 and 1 or 1 and 2, __)
    def test_negation(self):
        ''' Test that we can negate truthiness
        '''
        self.assertEquals(not True, __)
    def test_identity(self):
        self.assertIs(__, True)
    def test_ternary(self):
        ''' Test that we can use the ternary notation
        '''
        value = __ # implement ternary logic here
        self.assertEquals(value, True)
    def test_switch(self):
        ''' Test that we can fake a switch statement
        '''
        case = {True: 'Yes',
                False: 'No',
                None: ''}
        self.assertEquals(case[__], __)
    def test_while(self):
        ''' Test that we can use while loops
        '''
        i = 1
        while i > 0:
            i += 1
            if i % 2:
                i = -1
        self.assertEquals(__, i)
    def test_for(self):
        ''' Test that we can use for loops
        '''
        result = 1
        for i in range(4):
            result += i
            result *= i
        self.assertEquals(__, result)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(LogicTestCase)
    return the_suite
