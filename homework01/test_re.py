#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import re
import unittest
__ = None

class ReTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.anything = r'.*'
        self.numbers = r'\d+'
        self.space_for_butts = r'\s+butts\s+'
    def test_search(self):
        ''' Test that we know how to search
        '''
        self.assertEquals('I wonder...', re.search(self.anything, __).group())
        self.assertEquals('01189998819991197253',
                          re.search(self.numbers, __).group())
        self.assertEquals(__,
                          re.search(self.space_for_butts,
                                    'This is a string with butts and stuff'))
    def test_match(self):
        ''' Test that we how to match
        '''
        self.assertEquals(__,
                          re.match(self.anything, 'This is trivial').group())
        # Why does this succeed?
        self.assertEquals(__,
                          re.match(self.numbers, 'There are definitely \
numbers: 135'))
        self.assertEquals(__,
                          re.match(self.space_for_butts,
                                   '         butts ?').group())
    def test_sub(self):
        ''' Test that we know how to substitute
        '''
        do_over = re.sub(self.anything,
                         'Literally anything else',
                         'From what we start with')
        self.assertEquals(__, do_over)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(ReTestCase)
    return the_suite
