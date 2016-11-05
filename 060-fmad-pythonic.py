#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Looks like this is not pythonic:
#

my_container = ['Larry', 'Moe', 'Curly']
index = 0
for element in my_container:
    print ('{} {}'.format(index, element))
    index += 1
    
#
# and this IS:
#

my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
    print ('{} {}'.format(index, element))
    
#
# source: https://jeffknupp.com/writing-idiomatic-python-ebook/
#
