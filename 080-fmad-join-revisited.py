#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Additional explanation per reader request
# 

sourcelist = ["Humpty", "Dumpty", "sat", "on", "a", "wall"]
targetstr1 = " ".join( sourcelist )

#
# No strange things above. The sourcelist becomes a string
# that contains all the list elements separated by spaces.
# But the magic comes below: a list created with a for loop.
# Amazing:
# - Get a char c from targetstr1
# - Obtain ord( c )
# - Format the result as hex of length two 
# - Go for a new char c and repeat the process
#

separator = ":"
formatstr = "{:02x}"
newlist = [ formatstr.format( ord(c) ) for c in targetstr1 ]

targetstr2 = separator.join( newlist )

print("Joined... '" + targetstr1 + "'")
print("Xlated... '" + targetstr2 + "'")

# $ ./pyjoin.sh
# Joined... 'Humpty Dumpty sat on a wall'
# Xlated... '48:75:6d:70:74:79:20:44:75:6d:70:74:79:20:73:61:74:20:6f:6e:20:61:20:77:61:6c:6c'
