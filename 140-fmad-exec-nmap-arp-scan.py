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

    p = subprocess.run(cmdargs, stdin=None, stdout=subprocess.PIPE,
                       input=None, stderr=subprocess.PIPE,
                       shell=False, timeout=None, check=False, universal_newlines=True)

    """ get the result of the execution (much like "$?" in bash) and add it to the "output" list
    """

    rc = p.returncode
    rv = []

    """ in case of success, the subprocess returns zero, so "not rc" is true
        and flow goes through the "if"; in case of error will run the "else"
    """

    if not rc:
        for item, line in enumerate(p.stdout.split("\n")):
            if pattern in line:
                words = line.split(" ")
                rv.append(words[len(words) - 1])
    else:
        for item, line in enumerate(p.stderr.split("\n")):
            rv.append(line)

    return rc, rv


"""
    HERE it comes the very very true stuff
"""

if __name__ == "__main__":

    myself = sys.argv[0]
    print("Started {}...".format(myself))
    rc = 0

    for index, item in enumerate(sys.argv[1:]):

        """ we plan to execute nmap to build the range of addresses.
            check it's installed in your system
        """

        cmdargs = ["nmap", "-sL", "-n", str(item)]
        rc, rv = execthis(cmdargs, "Nmap scan report for")

        """ now check nmap's return code
        """

        if rc:
            print("ARGH! Rc is {:04d}".format(rc))

        """ print the address list in case of success, or the stderr contents if something goes wrong
        """

        for outline in enumerate(rv):

            """ arp-scan tests each address for presence or absence of a system
                again, check it's installed
            """
            print(outline)
            ipaddress = outline[1]
            cmdargs2 = ["sudo", "arp-scan", ipaddress]
            rc2, rv2 = execthis(cmdargs2, ipaddress)

            if not rc2:
                if len(arpproc) > 1:
                    print("USED... ", end="")
                else:
                    print("FREE... {}".format(outline))
            else:
                print("ARGH! Rc is {:04d}".format(rc2))

    print("Ended {} with code {}".format(myself, rc2))

""" THE END
"""
