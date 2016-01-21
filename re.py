# -*- coding: utf-8 -*-

import re

a = re.compile(r"""\d +
                   \.
                   \d*""", re.X)

b = re.compile(r"\d+\.\d*")

match11 = a.match('33.1415')
match12 = a.match('33')
match21 = b.match('33.1415')
match22 = b.match('33')

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world')
print m.group()
print "m.string:", m.string
print m.group(1, 2)

pattern = re.compile(r'longing')
match = pattern.search('hello longing')

if match:
    print match.group()

if match11:
    print match11.group()
else:
    print 'Fail'

if match12:
    print match12.group()
else:
    print 'Fail'

if match21:
    print match21.group()
else:
    print 'Fail'

if match22:
    print match22.group()
else:
    print 'Fail'
