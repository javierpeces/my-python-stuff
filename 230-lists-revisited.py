#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import os.path
import struct
import logging

#
# render a list
#

def renderList( al ):

    logging.debug( "Printing the full list with {:d} items...".format( len( al ) ) )

    for index, item in al.items( ):
        print( "Item {:d} has <{}>".format( index, item ) )

    logging.debug( "Done rendering." )

#
# search a list of needles in a list of haystacks
#

def searchInList( needle, haystack ):

    logging.debug( "Searching needles in the haystack" )

    fl = { }
    i = 0
    for needleIndex, needleItem in needle.items( ):
        needleItem = "^" + needleItem.strip("\n" ) + "$"
        searchExpr = re.compile( needleItem )
        logging.debug( "Search needle <{}> which is: <{}>".format( needleIndex, needleItem ) )
        for hayIndex, hayItem in haystack.items( ):
            if searchExpr.match( hayItem ):
                print( "Found {:d} containing <{}>".format( hayIndex, hayItem ) )
                fl[ i ] = hayItem
                i += 1

    logging.debug( "Done searching." )
    logging.debug( "Found list: <{}>".format( fl ) )

    return fl

#
# read a file and drop its lines into a list (removing the final newline char)
#

def createListFromFile( filename ):

    logging.debug( "Creating list from file <{}>".format( filename ) )

    if not os.path.exists( filename ):
        print( "Check that {:s} is a valid file".format( filename ) )
        exit( 2 )
    try:
        commentExpr = re.compile( '^.*;' )
        aFile = open( filename ).readlines( )
        returnList = {}
        i = 0
        for key, val in enumerate( aFile ):
            item = val.rstrip( "\n" )
            print( "Val obtained is {}".format( item ) )
            if not commentExpr.match( item ):
                returnList[ i ] = item
                i += 1

        logging.debug( "Created list of {:d} items from file <{}>".format( len( returnList ), filename ) )
        logging.debug( returnList )

        return returnList
    except IOError as e:
        print( "; An i/o error occurred opening {}. Exiting.".format( filename ) )
        errno, strerror = e.args
        print( "Error {:d} > {:s}".format( errno, strerror ) )
        exit( errno )

#
# And here it is...
#

if __name__ == "__main__":

    logging.basicConfig( level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
    logging.debug('This is a log message.')

    # haystackList = { "a", "ante", "bajo", "cabe" }  # this is the list we have to search in
    # needleList   = { "ante", "cabe" }               # these are the items we are looking for

    needleList = createListFromFile( "needle.txt" )
    haystackList = createListFromFile( "haystack.txt" )
    renderList( needleList )
    renderList( haystackList )
    foundList = searchInList( needleList, haystackList )
    renderList( foundList )
