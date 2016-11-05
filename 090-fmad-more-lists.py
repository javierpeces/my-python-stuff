#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Revisiting lists
#

mylist = ["canguro", 123.44176, "Ptolomeo", 100, 'more', 'language']

mylist.append("otro")
print("the original list adding 'otro' at the end....... {}".format(mylist))

mylist.remove("more")
print("remove element that contains the string 'more'... {}".format(mylist))

mylist.pop(3)
print("Take away the element in place 3. First is 0..... {}".format(mylist))

mylist.pop()
print("Pop no args removes the last element............. {}".format(mylist))

mylist.pop(-1)
print("Pop with -1 removes the last element............. {}".format(mylist))

mylist.pop(-3)
print("Pop with -3 removes the third from the end....... {}".format(mylist))

# I suppose that a negative value mean counting back from the end of the list,
# and still need a loop to add or remove multiple items. This is under heavy research by now.

for item in ("fistro", "pradera", "jander", "gromenauer"):
    mylist.append(item)

print("Add four new elements at the end of the list..... {}".format(mylist))

for index in range(-4, -2):
    print(" - removing {}".format(index))
    mylist.pop(index)

print("Pop two values starting at the fourth from end.... {}".format(mylist))

# Sample run...
#
# $ ./lists.py 
# the original list adding 'otro' at the end....... ['canguro', 123.44176, 'Ptolomeo', 100, 'more', 'language', 'otro']
# remove element that contains the string 'more'... ['canguro', 123.44176, 'Ptolomeo', 100, 'language', 'otro']
# Take away the element in place 3. First is 0..... ['canguro', 123.44176, 'Ptolomeo', 'language', 'otro']
# Pop no args removes the last element............. ['canguro', 123.44176, 'Ptolomeo', 'language']
# Pop with -1 removes the last element............. ['canguro', 123.44176, 'Ptolomeo']
# Pop with -3 removes the third from the end....... [123.44176, 'Ptolomeo']
# Add four new elements at the end of the list..... [123.44176, 'Ptolomeo', 'fistro', 'pradera', 'jander', 'gromenauer']
#  - removing -4
#  - removing -3
# Pop two values starting at the fourth from end.... [123.44176, 'Ptolomeo', 'jander', 'gromenauer']
# The End

print("The End")
