#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

""" calculate how many words contain a given letter """

def myfunction(haystack, needle):

    print("looking for this needle: {} in this stack: {}")

    rc = 0
    rv = []

    for word in haystack:
        if(needle in word):
            rc += 1
            rv.append(word)

    return rc, rv


""" the true stuff """

if __name__ == "__main__":
    print("Started " + sys.argv[0] + "...")
    
    universe = ["madrid", "toledo", "ciudad real", "cuenca", "guadalajara"]
    lookfor = "a"
    retcode, retvalue = myfunction(universe, lookfor)

    print("Ended {} with code {} and contents: {}".format(sys.argv[0], retcode, retvalue))

# the end
