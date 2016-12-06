#!/usr/bin/env python
"""Tests onboard.awesome.Awesomeclass

Example:
    import unittest
    suite = test_attdict.suite()
    unittest.TextTestRunner().run(suite)

"""
import unittest
from onboard import awesome

class AwesomeTestCase(unittest.TestCase):
    ''' Test cases for onboard.Awesomeclass
    '''
    def setUp(self):
        self.text = "Yep, I'm definitely awesome!"
        self.awesome = awesome.Awesomeclass(self.text)
    def test_constructor_requires_arg(self):
        ''' Test that the constructor fails without an argument
        '''
        # pylint: disable=no-value-for-parameter
        with self.assertRaises(TypeError):
            awesome.Awesomeclass()
    def test_constructor_with_arg(self):
        ''' Test the constructor to create an Awesomeclass object with an argument
        '''
        self.assertTrue(isinstance(awesome.Awesomeclass(self.text),
                                   awesome.Awesomeclass))
    def test_constructor_with_bad_arg(self):
        ''' Test the constructor to fail when given an incorrect argument
        '''
        with self.assertRaises(TypeError):
            awesome.Awesomeclass(None)
    def test_property_generator(self):
        ''' Test the property-decorated generator
        '''
        import types # necessary to valide generators
        self.assertTrue(isinstance(self.awesome.tokens, types.GeneratorType))
    def test_announce(self):
        ''' Test ability to announce that we're awesome
        '''
        # __ IS INVALID
        # PUT SOMETHING IN ITS PLACE TO FIX THE TEST!
        self.assertEquals(self.awesome.announce(), __)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(AwesomeTestCase)
    return the_suite
