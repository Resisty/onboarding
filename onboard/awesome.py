#!/usr/bin/env python
''' awesome module
This module is totally awesome!
The only class it defines is capable of announcing it, too!

Example:
    import onboard.awesome
    awesome_object = onboard.awesome.Awesomeclass("I'm awesome!")
'''
class Awesomeclass(object):
    ''' This class is awesome.
    '''
    def __init__(self, awesome_text):
        try:
            self._tokens = awesome_text.split(' ') # of course we can split on
                                               # space, it's text!
        except AttributeError as e:
            raise TypeError('Awesome argument is wrong type, needs to \
implement .split(): %s' % e.message)
    @property
    def tokens(self):
        ''' Decorators are awesome, let's use them to expose our text
        '''
        for i in self._tokens:
            # generators are also awesome
            # Produce parts of our text back one by one
            yield i
    def announce(self):
        ''' Why settle for a decorator when we can also have a callable
            function?
        '''
        return ' '.join([i for i in self.tokens])

