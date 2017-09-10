#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" ----------------------------------------------------------------
        Browse URL
    ----------------------------------------------------------------
"""

import requests
import socket

""" ----------------------------------------------------------------
    valida( ) comprueba dirección IP válida
    ----------------------------------------------------------------
"""

def valida( a ):

    try:
        socket.inet_pton( socket.AF_INET, a )

    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton( a )
        except socket.error:
            return False
        return a.count('.') == 3

    except socket.error:  # not a valid address
        return False

    return True
    
""" ----------------------------------------------------------------
    navega( ) obtiene la IP visitando una página de comprobación
    ----------------------------------------------------------------
"""

def navega( u ):

        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        try:
                r = requests.get( u )

        except requests.exceptions.RequestException as e:
                return( e )

        i = str( r.text ).rstrip( '\n' )

        if valida( i ):
                return( i )
        else:
                return( "no válida" )

""" ----------------------------------------------------------------
        Main
    ----------------------------------------------------------------
"""

if __name__ == "__main__":

        sites = [
                'http://ident.me/raw',
                'http://tnx.nl/ip',
                'http://icanhazip.com',
                'http://ipecho.net/plain',
                'http://ip.appspot.com',
                'http://ifconfig.me/ip',
                'http://ip.appspot.com',
                'http://whatsmyip.akamai.com'
        ]

        print( "Hola" )

        for key, value in enumerate( sites ):
                print( "Item {} Site {}".format( key, value ) )
                ipaddr = navega( value )
                print( "    IP {}".format( ipaddr ) )

        print( "Adeu" )

""" ----------------------------------------------------------------
    final
    ----------------------------------------------------------------
"""                
