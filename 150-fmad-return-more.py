#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

""" calculate how many words contain a given letter """

def myfunction(haystack, needle):
    
    print("Looking for this needle: {} in this haystack: {}".format(needle, haystack))

    rc = 0
    rv = []

    for word in haystack:
        if(needle in word):
            rc += 1
            rv.append(word)

    return rc, rv


""" the true stuff """

if __name__ == "__main__":
    
    myself = sys.argv[0]
    print("Started {}".format(myself))
    
    universe = ["madrid", "toledo", "ciudad real", "cuenca", "guadalajara"]
    lookfor = "a"
    retcode, retvalue = myfunction(universe, lookfor)

    print("Ended {} with code {} and contents: {}".format(myself, retcode, retvalue))

# the end
