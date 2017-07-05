#!/usr/bin/env python
'''config module
Run unit tests

Example:
    python run_tests.py
'''
import argparse
import importlib
import sys
import unittest

PACKAGE = 'homework02'
PACKAGES = ['homework02']

def main():
    ''' Main entry function
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--package',
                        type=str,
                        choices=PACKAGES,
                        default=PACKAGE)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

def run(args):
    ''' Run the package tests from arguments
    '''
    exit_code = 0
    pkg = importlib.import_module(args.package)
    for modname in pkg.__all__:
        module = importlib.import_module('%s.%s' % (args.package, modname))
        suite = module.suite()
        exit_code |= not unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
