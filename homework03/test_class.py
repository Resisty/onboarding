#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
__ = None

class DiagDiff(object):
    '''Given a square matrix of size NxN, calculate the absolute difference
       between the sums of its diagonals.
       Sample Input:
           [[11, 2,  4],
            [4,  5,  6],
            [10, 8,  -12]]
       Sample Output:
           15
   '''
   def __init__(self, matrix):
       ''' Initialization method
       '''
       # Do __init__ stuff
   def run(self):
       ''' Solve the problem
       '''
       return __

class DiagTestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def test_solver(self):
        ''' Test that we can solve for the absolute difference of diagonals in
        a square matrix
        '''
        mat1 = [[4, -2, 8], [5, 1, 1], [3, 11, 9]]
        mat2 = [[2, -7], [6, 4]]
        mat3 = [[1, -1, 1, -1], [1, -1, 1, -1], [1, -1, 1, -1], [1, -1, 1, -1]]
        self.assertEquals(DiagDiff(mat1).run(), 2)
        self.assertEquals(DiagDiff(mat2).run(), 7) # __ is a placeholder
        self.assertEquals(DiagDiff(mat3).run(), 0) # __ is a placeholder

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(DiagTestCase)
    return the_suite
