#!usr/bin/env python
''' This module has examples for working with conditional logic and control
    structures
'''
def if_ex():
    ''' Python's logic should be familiar if you have worked with C, C++, Java,
        etc
    '''
    # You can evaluate the truthiness of something and proceed accordingly
    if True:
        print('If something is true, proceed!')
    # If your condition is False, you can add a backup with 'else'
    if False:
        print('This will never print!')
    else:
        print('But this will!')
    # You may add as many exclusive conditions as you like with 'elif'
    if False:
        print('This won\'t print...')
    elif 0:
        print('0 evaluates to False, so this won\'t print, either!')
    else:
        print('Default cases always print, though!')
    # Additionally, your truthiness tests can use a variety of logical
    # constructs
    if True and 1: # 1 evaluates to True, so True and True -> True
        print('Python uses \'and\' instead of \'&&\'')
    if True and not 0:  # Remember 0 is False, and negating False yields True
        print ('Python uses \'not\' instead of \'!\'')
    if True != False: # Ok, the ! symbol is still used to negate equality
        print('Brian lies sometimes.')
    # Python equality works just like in C and Java except for object equality
    # If two objects have the same value, it is evaluatable with == and !=
    # If two NAMES refer to the same OBJECT, it is evaluatable with the keyword
    # 'is'
    a = 0
    if a == 0:
        print('The variable a refers to the value 0')
    if a is 0:
        print('This will never print because the variable a is not the same \
as the integer 0')
    a = None
    if a is None: # There is only one None
        print('The \'is\' keyword implements the identity function.')
    # Logic expressions may be as complex as you like and obey parens ordering
    if True and ((not 0 and 1) or False):
        print('Express whatever conditions you want!')

def ternary_ex():
    # Python does not have a ternary operator, but you can fake it
    value = True if True else False
    if value:
        print('Yep, it\'s true!')
    value = 'Print me!' if not 0 else 'This will never print!'
    print(value)

def case_ex():
    # Python doesn't have a case or switch statement, unlike C or Java.
    # However, those concepts are really just maps from a key to a value
    case = {True: 'Print me!',
            False: 'Don\'t print me!'}
    # In another language this might look like:
    # switch case {
    #     True: 'Print me!'
    #     False: 'Don\'t print me!'
    #     default: 'Huh?'
    print(case[not 0]) # Note that the key is True, so you may use any
                       #  expression which evaluates to True
    print({0: 'Evenly divisible by 2',
           1: 'Not evenly divisible by 2'}[5 % 2])

def while_ex():
    # Python's while should look familiar, it runs as long as its logic
    # expression is true
    while True:
        print('I\'ll run forever!')
        # this could get old fast
        print('On second thought, let\'s break out of this loop jail.')
        break # The break statement forces the innermost loop to exit

def for_ex():
    # Unlike C and Java, Python's for statement simply takes an iterable
    # and stops when the iterable is exhausted
    for i in range(3): # range is a builtin generator that yields successive values
        print('Got a number: %d' % i)
    # Can we have infinite for loops?
    def yield_forever():
        # Ignore this function, we'll cover it later
        i = -1
        while True:
            i += 1
            yield i
    for i in yield_forever():
        print('Uh oh, I\'m getting another number: %d' % i)
        if i > 0 and not i % 5:
            print('Let\'s get outta here!')
            break # don't loop forever
    # What if we want to skip some items?
    for i in range(10):
        # I hate multiples of 3
        if i > 0 and not i % 3:
            print('No sir, I don\'t like it.')
            continue # the continue statement will move to the next iteration
                     # of the loop immediately
        print('A good, wholesome non-multiple of 3: %d' % i)

def funcs():
    ''' assemple functions for running
    '''
    return [if_ex,
            ternary_ex,
            case_ex,
            while_ex,
            for_ex]
