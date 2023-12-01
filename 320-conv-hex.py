#!/usr/bin/env python3

import sys

def ruler(plen):
    rv = ""
    for i in range(0,plen):
        r = i % 10
        match r:
            case 0:
                rv += str(i)[0]
            case 5:
                rv += "+"
            case _:
                rv += "."
    return rv 

def alldigits(pstr):
    rv1 = ""
    rv2 = ""
    for c in pstr:
        x = c.encode("utf-8").hex()
        rv1 += x[0]
        rv2 += x[1]
    return rv1, rv2

if __name__ == "__main__":

    for a in sys.argv[1:]:
        print(a)
        with open(a) as f:
            lines = f.readlines()
        for l in lines:
            print(" ---------- ")
            s = len(l)
            print(ruler(s))
            print(l)
            (v1, v2) = alldigits(l)
            print(v1)
            print(v2)

    print("fine")
