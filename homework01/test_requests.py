#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
import requests
__ = None

class ReqTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.url = 'https://www.google.com'
    def test_req(self):
        ''' Test that we know how to make a request and validate it
        '''
        request = requests.get(self.url)
        self.assertEquals(__, 200)
        self.assertEquals(request.ok, __)
    def test_fail(self):
        ''' Test that we have a float
        '''
        with self.assertRaises(__):
            response = requests.post(self.url+'/api/not/implemented',
                                     json={'nonsense': 'data'})
            response.raise_for_status()
    def test_request(self):
        ''' Test that we can set headers
        '''
        response = requests.get(self.url, headers=__)
        self.assertEquals(response.request.headers['New-header'], __)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(ReqTestCase)
    return the_suite
