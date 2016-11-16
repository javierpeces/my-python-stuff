#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    print("hello")
    
    for index, item in enumerate(sys.argv[1:]):
        
        print("Arg {} contains {}".format(index, item))
        scan = "nmap -sL -n " + str(item)
        print("\tScan command number {} is '{}'".format(index, scan))
    
    print("bye")
