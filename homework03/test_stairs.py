#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

class Stairs(object):
    '''Consider a staircase of size :

           #
          ##
         ###
        ####
        Observe that its base and height are both equal to 4, and the image is
        drawn using '#' symbols and spaces (' '). The last line is not preceded
        by any spaces.

        Write a program that prints a staircase of size .
    '''
    def __init__(self, n):
        ''' Initialization method
        '''
        # Do __init__ stuff
    def run(self):
        ''' Solve the problem
        '''
        return __

class StairsTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_solver(self):
        ''' Test that we can create staircases of size n
        '''
        stairs4 = '''   #
  ##
 ###
####'''
        stairs7 = '''      #
     ##
    ###
   ####
  #####
 ######
#######'''
        stairs1 = '''#'''
        stairs0 = ''''''
        self.assertEquals(Stairs(4).run(), stairs4)
        self.assertEquals(Stairs(7).run(), stairs7)
        self.assertEquals(Stairs(1).run(), stairs1)
        self.assertEquals(Stairs(0).run(), stairs0)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(StairsTestCase)
    return the_suite
