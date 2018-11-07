#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# And here it is...
#

if __name__ == "__main__":

  dict = [ 500, 600, 700, 800 ]
  
  fstr = "Hay {:d} items en {:s} y suman {:d}"
  print( fstr.format( len(dict), str(dict), sum(dict) ) )
  
  dummy = [ print( val ) for val in dict if val < 750 ]
  dummy2 = [ print( "Key {} Val {}".format( key, val ) ) for key, val in enumerate( dict ) ]
  
# 
# Output...
#
# $ chmod +x ./250-another-set-of-oneliners.py
# $ ./250-another-set-of-oneliners.py
# Hay 4 items en [500, 600, 700, 800] y suman 2600
# 500
# 600
# 700
# Key 0 Val 500
# Key 1 Val 600
# Key 2 Val 700
# Key 3 Val 800
# 

  print( "Now the same with a list instead of a dictionary" )
  alst = { 500, 600, 700, 800 }
  dummy = [ print( val ) for val in alst if val < 750 ]
  dummy2 = [ print( "Key {} Val {}".format( key, val ) ) for key, val in enumerate( alst ) ]

# 
# Funny enough, the first loop returns a non-sorted set, and the second one returns sorted. Life.
# 
# Now the same with a list instead of a dictionary
# 600
# 700
# 500
# Key 0 Val 600
# Key 1 Val 700
# Key 2 Val 800
# Key 3 Val 500
# 
