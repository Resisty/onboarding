#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import collections
import unittest
__ = None

class CollTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.defdict = collections.defaultdict(list)
        self.namedtuple = collections.namedtuple('Test', 'value id comment')
        self.namedtuples = [self.namedtuple('Nothing',
                                            0,
                                            'This is a named tuple'),
                            self.namedtuple('Little',
                                            1,
                                            'This is another named tuple')]
        self.ordered = collections.OrderedDict()
        for i in sorted(['buffalo',
                         'aardvark',
                         'walrus',
                         'capybara',
                         'mongoose']):
            self.ordered[i] = 'A fantastic animal!'
        self.count = collections.Counter([5,3,5,7,3,1,34,6,7,2,1,2,2,2,34])
        self.dict = {}
    def test_defdict(self):
        ''' Test that we know how defaultdicts work
        '''
        self.assertEquals(__, self.defdict['nonextant key'])
        for i in range(5):
            self.defdict[i % 2].append(i * 2)
        self.assertEquals(self.defdict[1], __)
    def test_namedtuple(self):
        ''' Test that we know how namedtuples work
        '''
        self.assertEquals(__, self.namedtuples[1].id)
        self.namedtuples.append(self.namedtuple(__, __, __))
        self.assertEquals(self.namedtuples[1], self.namedtuples[2])
    def test_ordered(self):
        ''' Test that we know how ordered dicts work
        '''
        self.assertEquals(__, 'A fantastic animal!')
        self.assertEquals(__, self.ordered.pop('mongoose'))
        # This is a list comprehension, and it simply creates a list
        # Example: [i for i in range(3)] -> [0, 1, 2]
        self.assertEquals(__, [i for i in self.ordered.keys()])
    def test_counter(self):
        ''' Test that we know how counters work
        '''
        self.assertEquals(__, self.count.most_common(6)[-1][0]))
        self.count.subtract(collections.Counter([1,1,1]))
        self.assertEquals(__, self.count[1])

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(CollTestCase)
    return the_suite
