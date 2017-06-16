#!usr/bin/env python
''' This module has examples for working with the BeautifulSoup library
'''
import bs4

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


def funcs():
    ''' assemple functions for running
    '''
    return [buildsoup_ex]
