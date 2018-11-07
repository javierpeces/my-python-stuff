#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

  #
  # Simplest oneliner
  #

  nlist = { 7, 14, 21 }
  doble = [ num * 2 for num in nlist if num > 10 ]
  print( doble )

  #
  # Classic loop moving across a list
  #
  
  slist = { 0: "a", 1: "ante", 2: "bajo", 3: "cabe", 4: "con", 5: "contra", 6: "de", 7: "desde" }
  for key, val in slist.items( ):
    print( "The key {} has value {}".format( key, val ) )
    
  #
  # Python loop doing the same
  #
  
  dummy = [ print( "Key {} Val {}".format( key, val ) ) for key, val in slist.items( ) if val != "cabe" ]
  
  #
  # That's all folks
  #
