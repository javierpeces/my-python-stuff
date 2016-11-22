#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

""" MAIN
    Here it comes the very very true stuff
    String tokenized by slashes: mystring.rsplit("/", 1)
    "One" for the first word from the right end.
    
    >>> mystr = "/home/javier/data"
    
    >>> mystr.rsplit("/", 0)
     ['/home/javier/data']
     
    >>> mystr.rsplit("/", 1)
     ['/home/javier', 'data']
     
    >>> mystr.rsplit("/", 2)
     ['/home', 'javier', 'data']
     
    >>> mystr.rsplit("/", 3)
     ['', 'home', 'javier', 'data']
     
    Get the [-1] element of the list: mystring.rsplit("/", 1)[-1]
"""

if __name__ == "__main__":

    myself = sys.argv[0].rsplit("/", 1)[-1]
    print("Started {}...".format(myself))

    rc = 0

    print("Ended {} with code {}.".format(myself, rc))
    exit(rc)

# the end
