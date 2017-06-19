#!usr/bin/env python
''' This module has examples for working with the json library
'''
import json
import requests

def read_ex():
    ''' The json module allows us to read a json string into a dict/list
    '''
    text = requests.get('https://jsonplaceholder.typicode.com/posts').text
    data = json.loads(text)
    print('Found the title for a piece of data: %s' % data[1]['title'])

def create_ex():
    ''' The json module allows us to create a json string from a dict/list
    '''
    data = {'top_key':
            {'next_level': [
                {'this is getting confusing': 'yep'},
                {'oh jeez what even is this structure': '?'},
                'This isn\'t even a dict!']},
            'another_top_key': {'same_level': 'Not a list, though?'}}
    text = json.dumps(data)
    print('Got some really ugly data:')
    print(text)


def funcs():
    ''' assemple functions for running
    '''
    return [read_ex,
            create_ex]
