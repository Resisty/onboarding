#!usr/bin/env python
''' This module has examples for working with the BeautifulSoup library
'''
import bs4
import requests

def buildsoup_ex():
    ''' BeautifulSoup can allow us to build HTML documents programmatically
    '''
    newsoup = bs4.BeautifulSoup('', 'html5lib') # Depending on what you're
                                                # doing, it might be
                                                # worthwhile to specify the
                                                # version of markup you want
    newsoup.body.attrs = {'style': 'color: pink; background-color: yellow; font-style: \
MS Comic Sans'}
    center = newsoup.new_tag('center')
    newsoup.body.append(center)
    heading = newsoup.new_tag('h1')
    heading.string = 'Here is some soothing text created with BeautifulSoup!'
    center.append(heading)
    print(newsoup)
    with open('deleteme.html', 'w') as data:
        data.write(str(newsoup)) # open() does not implicitly call __str__ or
                                 # __repr__
    print('I\'ve sent the above html to a file named "deleteme.html". Try \
opening it in your web browser!')

def readsoup_ex():
    ''' BeautifulSoup can also read HTML and build a python object out of it,
        allowing us to search and perform various operations on it.
    '''
    html = (requests
            .get('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')
            .text)
    soup = bs4.BeautifulSoup(html, 'html5lib')
    # Tags are attributes of the document object, like "len(soup.body)"
    print(len(soup.body))
    # We can see "soup.body" has a length, but is it subscriptable?
    try:
        print(soup.body[0])
    except KeyError as err:
        print('Caught KeyError! "%s" not a key in soup.body.' % str(err))
    #Tags are custom objects with a lot of custom work
    print(type(soup.body))
    print(dir(soup.body))
    print(soup.table is None)
    print(soup.a)
    print(len(soup.findAll('a')))

def funcs():
    ''' assemple functions for running
    '''
    return [buildsoup_ex,
            readsoup_ex]
