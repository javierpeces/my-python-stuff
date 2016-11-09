#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python looks like a powerful programming language. It is fully object oriented, so you may easily use 
# the notation “object.property” to access all the available features of a given thing. 
# I’m focusing on text file handling for a quick set of examples. If you have a text file named “data.txt”,
# reading it is pretty straightforward.

""" read file contents and show in standard output """

infilename = "data.txt"
infile = open(infilename, "r")

for line in infile:
    print(line.rstrip())

infile.close()

# Easy and concise. Comments are enclosed in three double quotes. Variables are created when referenced
# for the first time. The “for” loop body is not delimited but indented instead. To be honest, this way 
# of building the code is the one I dislike the most. See how the method “rstrip” of the object “line” 
# removes unconvenient characters before printing. Now for a read and write loop.

""" read file contents, show in standard output, write to new file """

infilename = "data.txt"
outfilename = "results.txt"
infile = open(infilename, "r")
outfile = open(outfilename, "w")
i = 1

for line in infile:
    outline = str(i) + ": " + line
    print(outline.rstrip())
    outfile.write(outline)
    i += 1

infile.close()
outfile.close()

# A small manipulation of the incoming string is shown inside the “for” loop, right before using the
# “write” method to dump the new string into the output file. For the next sample, let’s get the whole
# file into a list. The loop will process the list accordingly, one loop iteration for each line.
# The “readlines” method creates a list with all the file inside. Each list element contains a line from
# the file. So list[0] contains the first line, list[1] gets the second, etc.

""" all the file contents into a list"""

list = open("data.txt").readlines()

for item in list:
    print(item.rstrip())
    
# This variation will use a numeric variable as the list index. The “range” function ensures that the “i” 
# index value is incremented by one unit on each iteration. Every time that the value of “i” is increased,
# we may process the next item of the list using the expression list[i] in our code.

""" all the file contents into a list"""

list = open("data.txt").readlines()

for i in range(0, len(list)):
    print(str(i) + ": " + list[i].rstrip("\n"))

# UPDATE
# The pythonic version of this loop.

for i, item in enumerate(list):
    print("item {:2d} contains {}".format(i, item))

# That’s all by now. Hope this has been useful…
