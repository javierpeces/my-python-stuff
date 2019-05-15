#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, logging
from datetime import datetime as dt
from os import path as op

""" ------------------------------
    formatted date time
    ------------------------------
"""

def strNow( ):

	return f'{dt.now( ):%Y-%m-%d %H:%M:%S,%f}'

""" ------------------------------
    log ordo 
    ------------------------------
"""

if __name__ == "__main__":

	me = op.basename( sys.argv[ 0 ] )	

	logging.basicConfig( 
		level=logging.DEBUG, 
    		format=me + ': %(asctime)s - %(levelname)s - %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S' 
	)

	print( "{}: {} - Iniciando...".format( me, strNow( ) ) )

	for index, item in enumerate( sys.argv[ 0: ] ):

		logging.debug( "Arg {} contains {}".format(index, item) )

	print( "{}: {} - Terminado.".format( me, strNow( ) ) )
