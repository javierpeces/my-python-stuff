#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Time for an amazing script. Every time we audit a new customer,
# we need to connect to a bunch of new hosts we never heard of. 
# Let's generate the related .ssh/config file with info about those boxes.

# For each host we'll probably find a Host entry. Example:
#     Host server1
#         Hostname 10.7.7.181
#         User root
#         Port 22

# When we connect to this host for the first time, an annoying question
# about the key and its fingerprint will disturb our work. The command:
#     ssh-keyscan -p port host
# -iterated for all those hosts- will collect keys so that no questions
# will be made in the future.

# So we'll read the .ssh/config file, gather data and generate a script
# to be run later.

import sys

if __name__ == "__main__":

        print( "#!/bin/bash" )

        #
        # Useless this time, but good to remember
        #

        # for index, parameter in enumerate( sys.argv[:] ):
        #         print( "# Arg {} is {}".format( index, parameter ) )

        #
        # Will pass the 'input' file name in the first parameter
        # On error must leave execution here
        #

        try:
                filename = sys.argv[1]

        except IndexError as err:
                print( "# Arg 1 problem. Exiting." )
                print( "# Msg: {}".format( err ) )
                exit( 1 )

        #
        # If we reached this point,
        # then the variable 'filename' has some content
        # Let's try to open the file of that name
        #
        
        with open( filename, "r" ) as f:

                #
                # read one record at a time, and count what we do
                #

                recCount = 0
                addCount = 0
                outCount = 0
                
                #
                # Amazing loop: A line from the file is placed
                # into the variable 'textline' for each iteration

                for textline in f:

                        #
                        # split the line into space delimited words
                        #

                        phrase = textline.split( )
                        wordCount = phrase.__len__( )

                        #
                        # Ignore empty lines and those with a "#"
                        #
                        
                        if wordCount < 2:
                                recCount += 1
                                continue

                        if phrase[0].startswith( "#" ):
                                recCount += 1
                                continue

                        #
                        # print( "# \tPhrase ·{}· has {} words".format( phrase, wordCount ) )
                        #
                        
                        #
                        # Store relevant information
                        #

                        if phrase[0] == "Host":
                                host = phrase[1]
                                name = False
                                user = False
                                port = False
                        elif phrase[0] == "Hostname":
                                name = phrase[1]
                        elif phrase[0] == "Port":
                                port = phrase[1]
                        elif phrase[0] == "User":
                                user = phrase[1]
                        else:
                                print( "# Internal error: {} · {} · {} · {} ·".format( host, name, user, port ) )
                                recCount += 1
                                continue

                        #
                        # Build a ssh-keyscan line with the gathered hostname and port
                        #

                        if host is not False and name is not False and user is not False and port is not False:
                                print( "# {}\nssh-keyscan -p {} {}".format( host, port, name ) )
                                outCount += 1

                        #
                        # go up for the next record
                        #

                        recCount += 1
                        addCount += 1

        #
        # Print totals and close
        #

        print( "# Records read ........: {}".format( recCount ) )
        print( "# Records processed ...: {}".format( addCount ) )
        print( "# Output lines ........: {}".format( outCount ) )

        #
        # finito
        #

        print( "# Bye" ) 
