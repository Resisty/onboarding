#!/usr/bin/env python
''' Serves as an introduction to tests

Example:
    import unittest
    suite = test_tests.suite()
    unittest.TestTestRunner().run(suite)
'''
import unittest
import bs4
__ = None
SOUP = '''!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>'''

class Bs4TestCase(unittest.TestCase):
    ''' Test some stuff!
    '''
    def setUp(self):
        self.soup = bs4.BeautifulSoup(SOUP, 'html5lib')
    def test_tag(self):
        ''' Test that we know what a tag is
        '''
        self.assertEquals(bs4.element.Tag, __) # __ is a placeholder
    def test_attribute(self):
        ''' Test that we know how to use tag attributes
        '''
        self.assertEquals(__, 'My first paragraph.')
    def test_insert(self):
        ''' Test that we can manipulate the document
        '''
        newtag = self.soup.new_tag('p')
        newtag.string = 'More html!'
        ###
        # self.soup <- Do smething to the soup!
        ###
        self.assertEquals('More html!',
                          self.soup.findAll('p')[1].string)

def suite():
    ''' Create a suite of tests
    '''
    the_suite = unittest.TestLoader().loadTestsFromTestCase(Bs4TestCase)
    return the_suite
