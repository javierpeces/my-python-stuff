#!/usr/bin/env python
# FMAD stands for 'five-minutes-a-day' but TBH I'm dedicating more than that.

p = subprocess.Popen(cmdargs, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
f = "{} | {}"

for i, line in enumerate(p.stdout.readlines()):
    print(f.format(i, line.rstrip().decode("utf-8"))
    
print("The end")
