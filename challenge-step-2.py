#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

if __name__ == "__main__":
    print("Starting...")
    
    if len(sys.argv) < 2:
        print("ERROR: no file name specified.")   
        exit(1)

    infile = sys.argv[1]
    if os.path.isfile(infile) == False:
        print("ERROR: input file does not exist.") 
        exit(1)

    if os.access(infile, os.R_OK) == False:
        print("ERROR: input file is not readable.") 
        exit(1)

    if len(sys.argv) < 3:
        print("ERROR: no num of top results specified.")   
        exit(1)

    maxnotr = int(sys.argv[2])
    if maxnotr <= 0:
        print("ERROR: num of top results must be bigger than 0.")   
        exit(1)

    if maxnotr > 30000000:
        print("ERROR: num of top results must be less than 30000000.")   
        exit(1)

    f = open(infile, "r")
    lines = f.readlines()
    f.close()

    lines[:] = [line.strip("\n ") for line in lines]
    ranking = [ int(l) for l in lines if l.isnumeric() ]
    item = 1

    for line in sorted(ranking, reverse=True):
        print("FINAL: {:5d} ·{}·".format(item, line))
        item = item + 1
        if item > maxnotr:
            break

    print("Done.")
