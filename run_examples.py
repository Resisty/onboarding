#!/usr/bin/env python
'''config module
Run unit tests

Example:
    python run_tests.py
'''
import inspect
import importlib
import re

def example_runner(funcs):
    ''' Run our examples, try to print prettily
    '''
    for func in funcs:
        print('Let\'s take a look at an example for %s\'s:'
              % re.sub(r'_ex', '', func.__name__))
        print(inspect.getsource(func))
        func()
        print('===\n')

PACKAGE = 'examples'
if __name__ == '__main__':
    PKG = importlib.import_module(PACKAGE)
    for modname in PKG.__all__:
        module = importlib.import_module('%s.%s' % (PACKAGE, modname))
        example_runner(module.funcs())
