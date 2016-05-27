#!/usr/bin/env python

people = {
        'Alice':{
            'phone':'2341',
            'addr':'Foo drive 23'
            },
        'Beth':{
            'phone':'9102',
            'addr':'Bar street 42'
            },
        'Cecil':{
            'phone':'3258',
            'addr':'Baz avenue 90'
            }
        }
labels = {
        'phone':'phone number',
        'addr':'address'
        }

name = raw_input('Name: ')

request = raw_input('Phone number (p) or address (a)?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people:
    print name + "'s " + labels[key] + ' is ' + people[name][key]
