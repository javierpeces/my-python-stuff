#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FMAD stands for 'five-minutes-a-day' but TBH I'm dedicating more than that.
""" hit and run and return """


import subprocess

args = ["ls", "-l", "/tmp"]
p = subprocess.run(args, stdin=None, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
    shell=False, timeout=None, check=False, universal_newlines=True)

print(p)

rc = p.returncode

if rc == 0:
    print("bien. rc is {:04d}".format(rc))
    for item, line in enumerate(p.stdout.split("\n")):
        print("#{:02d}: '{}'".format(item,line))
else:
    print("male. rc is {:04d}".format(rc))
    for item, line in enumerate(p.stderr.split("\n")):
        print("#{:02d}: '{}'".format(item,line))

# Works "if not p.returncode:" as well
    
print("The end")
