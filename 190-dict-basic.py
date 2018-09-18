#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Dictionary """

d = { 1: "feo", 3: "guapo", 2: "regular" }

for key, val in sorted( d.items( ) ):
        print( "key " + str( key ) + " has value " + val + ";" )
