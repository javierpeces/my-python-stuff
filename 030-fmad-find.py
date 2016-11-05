#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Yesterday's research showed the way to split a phrase in words, generating an easily usable list.
# Before yesterday we read lines from a text file. Combining both samples we get lines one by one, 
# and we split each line in words. This way we easily seek a word inside the file.
#

""" read data file and tokenize it """

infilename = "data.txt"
infile = open(infilename, "r")

for line in infile:
    print("line # contents: '" + line.rstrip() + "'")
    words = line.split()
    i = 1
    for word in words:
        print("    word # " + str(i) + " is '" + word + "'")
        i += 1

infile.close()

# 
# The real version of this script adds a comparison to find the word we are looking for...
# We will remove the "print" statements to let you focus in the search action.
#

""" read data file, tokenize it and search for something """

infilename = "data.txt"
infile = open(infilename, "r")
seek = "esta"
l = 1

for line in infile:
    # print("line # contents: '" + line.rstrip() + "'")
    words = line.split()
    i = 1
    for word in words:
        # print("    word # " + str(i) + " is '" + word + "'")
        if word == seek:
            print("at line #" + str(l) + " found word #" + str(i) + ": " + word)
        i += 1
    l += 1

infile.close()

#
# That's all folks
#
