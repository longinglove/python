#!/usr/bin/env python

import types

def displayNumType(num):
    print num, 'is',
    if type(num) == types.IntType:
        print 'a number of type integer'
    elif type(num) == types.LongType:
        print 'a number of type long'
    elif type(num) == types.FloatType:
        print 'a number of type float'
    elif type(num) == types.ComplexType:
        print 'a number of type complex'
    else:
        print 'not a number at all'


displayNumType(-1)
displayNumType(9999999999999999999999999999999999999999999L)
displayNumType(3.1415)
displayNumType(-1+2j)
displayNumType('xxx')
