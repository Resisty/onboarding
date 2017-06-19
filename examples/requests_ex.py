#!usr/bin/env python
''' This module has examples for working with the re and regex libraries
'''
import requests

def request_ex():
    ''' The requests module allows us to make HTTP requests
    '''
    # Note that requests addresses require the protocol to be explicit
    url = 'https://www.google.com'
    response = requests.get(url)
    print('We are able to resolve %s with status %s'
          % (url, response.status_code))
    print('The page at %s has A LOT of content: %s characters'
          % (url, len(response.text)))
    # Requests also natively support JSON format
    data = requests.get('https://jsonplaceholder.typicode.com/posts')
    # JSON data is returned as a Python dict or list
    print('The first JSON item in returned data: %s' % data.json()[0])

def post_ex():
    ''' The HTTP verbs are supported as functions, so you can GET, POST, PUT,
        etc
    '''
    url = 'https://httpbin.org'
    uri = '/post'
    data = {'some_key': 'some_value'}
    # We can post a JSON payload with correct headers using the json keyword
    # argument
    response = requests.post(url+uri, json=data)
    print('We managed to post something!')
    print('Status: %s' % response.status_code)
    print('Text: %s' % response.text)
    # Optionally, we can define custom headers and include the raw data
    headers = {'Content-type': 'application/json'}
    response = requests.post(url+uri, headers=headers, data=data)
    print('We managed to post something again!')
    print('Status: %s' % response.status_code)
    print('Text: %s' % response.text)

def fail_ex():
    ''' Requests make it easy to fail, or rather, to know why you failed.
    '''
    url = 'https://brewspace.jiveland.com/api/v3/places/1'
    data = {'nonsense': 'there\'s a lot of it'}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        # This shouldn't happen, but...
        print('How the hell did we manage that?')
    try:
        response.raise_for_status()
    except requests.HTTPError as err:
        print('Woops! We goofed on our request. Error: %s' % str(err))

def funcs():
    ''' assemple functions for running
    '''
    return [request_ex,
            post_ex,
            fail_ex]
