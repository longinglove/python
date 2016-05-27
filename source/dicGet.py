#!/usr/bin/env python

people = {}

labels = {
        'phone':'phone number',
        'addr':'address'
        }
name = raw_input('Name: ')

request = raw_input('Phone number(p) or address(a)? ')

key = request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print name + "'s " + label + ' ' + result
