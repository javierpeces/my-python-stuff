#!/usr/bin/env python
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

# $ ./lists.py 
# the original list adding 'otro' at the end....... ['canguro', 123.44176, 'Ptolomeo', 100, 'more', 'language', 'otro']
# remove element that contains the string 'more'... ['canguro', 123.44176, 'Ptolomeo', 100, 'language', 'otro']
# Take away the element in place 3. First is 0..... ['canguro', 123.44176, 'Ptolomeo', 'language', 'otro']
# Pop no args removes the last element............. ['canguro', 123.44176, 'Ptolomeo', 'language']
# Pop with -1 removes the last element............. ['canguro', 123.44176, 'Ptolomeo']
# The End

print("The End")
