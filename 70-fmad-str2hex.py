#!/usr/bin/env python
#
# ¿Se acuerdan de la que tuvimos que formar para convertir a hex en bash?
#

s = "esternocleidomastoideo"

#
# en python es sencillamente brillante
#

x = ":".join("{:02x}".format(ord(c)) for c in s)

#
# pues ya
#

print(x)
