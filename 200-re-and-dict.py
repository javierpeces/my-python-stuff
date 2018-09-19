#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
    Integrate simple regexp stuff and dictionaries.
    Analyze a text file with this content...
    $ cat samp.zone.db
    www IN A 192.168.100.3
    ; not to be IN my Area
    smtp 	IN A	192.168.100.100
    print	IN	A	192.168.100.70
    www		IN	A	192.168.100.2
  	; tampoco es IN ni A
    	truco	IN A
    	data IN	A 192.168.100.6
"""

import re
f = re.compile( '.*IN.*A.*' )
g = re.compile( '^.*;' )

""" Read file into a list  """

file = open( "samp.zone.db" ).readlines( )
dict = { }

""" Loop thru lines """

for i, line in enumerate( file ):

        """ remove trailing newline character """
        
        line = line.rstrip( "\n" )
        
        """ 
            discard lines beginning with ";" 
            and those not like 'xxx IN A yyy' 
        """
        
        if not g.match( line ) and f.match( line ):
                # print( "l {:2d} = {}".format( i, line ) )
                
                """ 
                    split the line in words 
                    and put them into the 'cols' list
                    set empty key by now, and use the first word as value
                """
                
                cols = line.split( )
                dkey = ""
                dval = cols[ 0 ]
                
                """
                    analyze each word 
                    trying to find what comes next to the "A" token
                """

                for j, word in enumerate( cols ):
                        # print( "\tw {:2d} = {}".format( j, word ) )
                        if word == "A":
                                next = j + 1
                                if next < len( cols ):
                                        dkey = cols[ next ]

                """
                    if a non empty word was found after the "A"
                    use it as a key for the current pair
                """
                
                if dkey != "":
                        dict[ dkey ] = dval

""" Print the obtained dictionary """

for key, val in sorted( dict.items( ) ):
        print( "Key '" + str( key ) + "', Val '" + val + "'" )                        
                        
""" That's all folks """                        
