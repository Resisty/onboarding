#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import json
import unittest
__ = None

class JSONTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.data = {'stuff': {'things': [0, 1, 2],
                               'hello': 'ohai'},
                     'peanut butter': 'jelly time'}
        self.stringdata = json.dumps(self.data)
    def test_data(self):
        ''' Test that we know how data works
        '''
        self.assertEquals(__, json.loads(self.stringdata)['stuff']['hello']) # __ is a placeholder
    def test_string(self):
        ''' Test that we know how json strings work
        '''
                                                  # Starting at index 0,
                                                  # return characters 12
                                                  # through 17 but not 18
        self.assertEquals(__, json.dumps(self.data[12:18]))
    def test_createstr(self):
        ''' Test that we can create json strings
        '''
        self.assertEquals(__, '{"key": "value"}')
    def test_createdata(self):
        ''' Test that we can create data
        '''
        self.assertTrue(json.loads(__), {'key': 'value'})

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(JSONTestCase)
    return the_suite
