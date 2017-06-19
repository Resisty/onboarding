#!usr/bin/env python
''' This module has examples for working with the re and regex libraries
'''
import re
import regex

def re_ex():
    ''' The re module allows us to work with (extended) regexes
    '''
    # Most regexes use a pattern and raw strings are perfect for patterns
    simple_search = re.search(r'abc', 'This is a string with abc in it')
    # The match is retrievable
    print(simple_search.group())
    # If you have matched groups, you can retrieve those
    group_search = re.search(r'(a)(b)(c)', 'This is an abc string')
    print(group_search.groups())
    # As well as the simple match
    print(group_search.group())
    # If you're going to use a pattern a log, compile it!
    # You can pass flags to a compilation for insensitivity, verbosity, etc
    reg = re.compile(r'(a)(b)(c)', re.I)
    print(re.search(reg, 'This is an abc string').group())
    # Although passing a raw string will yield a compiled pattern as well
    print(simple_search.re)

def match_ex():
    ''' Demonstrate .match() as opposed to .search()
    '''
    # Beware that .match only matches against the beginning of the string!
    pat = r'(\d{1,3}\.){3}\d{1,3}'
    msg = 'The IP address is 127.0.0.1'
    print('Found it! %s' % re.search(pat, msg, re.I).group())
    try:
        print('Found it! %s ...wait. What?'
              % re.match(pat, msg, re.I).group())
    except AttributeError:
        print('No matched IP address. What?')
    pat2 = r'The IP address is %s' % pat
    print('Found it! Kind of... %s'
          % re.match(pat2, msg, re.I).group())

def sub_ex():
    ''' Regexes are a great way to perform string substitution.
        Note that this returns a new string since Python strings are immutable.
    '''
    msg = 'Store all your stuff in the cloud!'
    re.sub(r'cloud', 'butt', msg)
    print('New message: "%s" ...wait.' % msg)
    newmsg = re.sub(r'cloud', 'butt', msg)
    print('Really new message: "%s"' % newmsg)
    pat = r'''([^aeiou\s]*)([aeiou]+)([\w']*)'''
    subpat = r'''\2\3\1ay'''
    msg = 'Let\'s use regexes to make a secret code!'
    print(re.sub(pat, subpat, msg))

def regex_ex():
    ''' The regex module is essentially a superset of the re module
    '''
    # If you can do it with re, you can do it with regex
    simple_search = regex.search(r'abc', 'This is an abc string')
    print(simple_search.group())
    # There are, however, some advanced features not included in re
    # You will, however, need to enable version1 so it doesn't mimic re
    regex.DEFAULT_VERSION = regex.VERSION1
    print(regex.split(r'\m', 'Splitting on the end of words with zero-width \
assertions isn\'t possible with "re".'))

def funcs():
    ''' assemple functions for running
    '''
    return [re_ex,
            match_ex,
            sub_ex,
            regex_ex]
