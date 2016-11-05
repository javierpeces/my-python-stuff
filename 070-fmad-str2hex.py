#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Remember the shell script fight to convert a string to its hex equivalent?
# Let's see how to manage the same in Python.
# The short story for busy people: Turn a string into hex...
#

s = "Th1515TheP455w0rd0fMyR0ut3r"
x = ":".join("{:02x}".format(ord(c)) for c in s)
print(x)

#
# And now for the details.
# First of all, process command line args.
#

#!/usr/bin/env python
import sys
for index, item in enumerate(sys.argv):
    print("Arg {} contains {}".format(index, item))
    
#
# The arg 0 is the script name as usual. Remove it. 
# Put everything else in a string.
#

#!/usr/bin/env python
import sys
args = "".join(sys.argv[1:])
print("Args received: {}".format(args))

#
# Once we have a string,
# translate each char to hex.
#

#!/usr/bin/env python
import sys

args = "".join(sys.argv[1:])
print("Args received: {}".format(args))

hexs = ":".join("{:02x}".format(ord(c)) for c in args)
print("And now in hex: {}".format(hexs))

#
# Highlights:
# - Get args from sys.argv
# - Discard the 'zero' arg as it is the script name
# - Put all the rest in a string with... list[1:]
# - Turn each char in the string into its 'two chars long' hex equivalence
# - See... format(xxx(c) for c in string)
# - Join all the hex values obtained in a new string, using ":" as the separator
# - Like this: separator.join( formatstring.format( string ) )
#

#
# Saved as argtohex.py, chmod +x, executed. The output...
#
# ./argtohex.py abcd1234
# Args received: abcd1234
# And now in hex: 61:62:63:64:31:32:33:34
#
# It seemed to be simpler than the shell script version, but I'm starting to change my mind...
#

print("The End")
