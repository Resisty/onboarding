#!/usr/bin/env python
'''config module
Run unit tests

Example:
    python run_tests.py
'''
import argparse
import inspect
import importlib
import re

PACKAGE = 'examples'

def example_runner(funcs):
    ''' Run our examples, try to print prettily
    '''
    for func in funcs:
        print('===\nLet\'s take a look at an example for %s:\n===\n'
              % re.sub(r'_ex', '', func.__name__))
        print(inspect.getsource(func))
        print('===\nExecuting...\n===')
        func()
        print('===\n')

def main():
    ''' Main entry function
    '''
    pkg = importlib.import_module(PACKAGE)
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--examples',
                        type=str,
                        nargs='*',
                        choices=pkg.__all__,
                        default=pkg.__all__)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

def run(args):
    ''' Run the examples from arguments
    '''
    for modname in args.examples:
        module = importlib.import_module('%s.%s' % (PACKAGE, modname))
        example_runner(module.funcs())

if __name__ == '__main__':
    main()
