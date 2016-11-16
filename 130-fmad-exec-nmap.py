#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    The final goal is finding free addresses in a network range
    Not finished but you may see how it looks like
"""

import sys
import subprocess

"""
    execthis()
    a function that runs an arbitrary command with its args
    and returns the contents of the standard output in case of success
    or the error text in case of disaster
"""

def execthis(cmdargs, pattern):

    """ create a subprocess "p" and pipe stdout and stderr
    """

    p = subprocess.run(scan, stdin=None, input=None,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
        shell=False, timeout=None, check=False, universal_newlines=True)

    """ get the result of the execution (much like "$?" in bash) and add it to the "output" list
    """

    rc = p.returncode
    output = []
    output.append(rc)

    """ in case of success, the subprocess returns zero, so "not rc" is true 
        and flow goes thru the "if"; in case of error will go thru the "else"
    """

    if not rc:
        for item, line in enumerate(p.stdout.split("\n")):           
            if(pattern in line):
                words = line.split(" ")
                output.append(words[len(words) - 1])
    else:
        for item, line in enumerate(p.stderr.split("\n")):
            output.append(line)

    return output


""" 
    HERE it comes the very very true stuff 
"""

if __name__ == "__main__":

    print("Started " + sys.argv[0] + "...")
    
    for index, item in enumerate(sys.argv[1:]):
        
        """ we plan to execute nmap to build the range of addresses. 
            check it's installed in your system
        """
        
        scan = ["nmap", "-sL", "-n", str(item)]
        # print("Scan command {} is '{}'".format(index, scan))
        thisproc = execthis(scan,"Nmap scan report for") 
        retcode = thisproc[0]
        
        """ now check nmap's return code
        """
        
        if not retcode:
            print("GOOD! Rc is {:04d}".format(retcode))
        else:
            print("ARGH! Rc is {:04d}".format(retcode))
            
        """ print the address list in case of success, or the stderr contents if something goes wrong
        """

        for outitem, outline in enumerate(thisproc[1:]):
        
            """ a new nmap WILL test each address for presence or absence of a system
                but BY NOW we are printing each
            """
            print("\tItem #{:02d} contains '{}'".format(outitem, outline))

    print("Ended {} with code {}".format(sys.argv[0], retcode))

""" THE END
"""
