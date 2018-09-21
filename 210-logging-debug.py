#!/usr/bin/env python3
# Traducción libre de "Stop Using 'print' for Debugging: 
# A 5 Minute Quickstart Guide to Python’s logging Module", en el blog de Al Sweigart.
# 
# Indicaciones previas:
# 
# Este tutorial es corto.
# Para encontrar las miserias del código, se puede usar "print" para mostrar los valores de las variables
# durante la ejecución. No lo haga. En su lugar, use el módulo logging. Este módulo es mejor que print porque se puede:
#
# · Poner una marca de tiempo en cada mensaje.
# · Usar varios niveles de urgencia, filtrando los mensajes que interesen.
# · Quitar los mensajes de depuración cuando ya no hacen falta, sin tener que revisar todo el código, con el riesgo de confundirse y quitar llamadas "print" verdaderas.
# · Ignorar los mensajes en lugar de quitarlos.
#
# El uso de print se reserva a programadores con mucho tiempo libre.
#
# Para el resto, logging ahorra esfuerzo. También se recomienda el Python Debugger 
# y Pylint para anticiparse a los bugs y mejorar la legibilidad del código.
# Como primera prueba, un pequeño script que tira un mensaje a la consola:

import logging
logging.basicConfig( level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
logging.debug('This is a log message.')

# He guardado este código como... NO COMETA EL ERROR de llamar logging.py a su script.
# Nueve de cada diez programadores novicios usan el nombre del módulo para su propio script y, claro, les falla.
# Elija un nombre que no sea igual al del "import" del principio del código de arriba.
# Por ejemplo, loggindvs.py. Esto es lo que se muestra en la pantalla al ejecutarlo:

$ python loggindvs.py
2017-01-02 17:12:05,662 - DEBUG - This is a log message.

# Una pequeña modificación nos permite enviar los mensajes a un fichero:

import logging
logging.basicConfig( filename='logfile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
logging.debug('This is a log message.')

# Las sucesivas ejecuciones añadirán los mensajes al final del fichero en lugar de reemplazarlo.

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter( '%(asctime)s - %(levelname)s - %(message)s' )

fh = logging.FileHandler('logfile.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug('This is a test log message.')

# Asegúrese de que la variable "logger" es global, para poder usarla en las funciones. 
# No es necesario "global logger" al principio de la función, porque la variable "logger" solamente se lee y no se modifica.
# De mayor a menor urgencia, los niveles son:
# 
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
#
# La llamada a setLevel establece el mínimo nivel de los mensajes que son registrados.
# Si se llama a fh.setLevel( logging.ERROR ) no se escribirán los mensajes WARNING, INFO y DEBUG. 
# Observe que, en el ejemplo de arriba, "fh" es el manejador de los logs a fichero y "ch" el de consola.
#
# Para escribir un mensaje puede emplear:

logger.critical('This is a critical message.')
logger.error('This is an error message.')
logger.warning('This is a warning message.')
logger.info('This is an informative message.')
logger.debug('This is a low-level debug message.')

# Hay muchas más cosas, pero esto es lo necesario para abandonar con carácter definitivo la instrucción print 
# en labores de depuración.
#
# Cosas de interés:
#
# Un tutorial básico en la web oficial: http://docs.python.org/howto/logging.html#logging-basic-tutorial
# La función "pretty print" para diccionarios y listas:
# http://docs.python.org/library/pprint.html#pprint.pprint
# http://docs.python.org/library/pprint.html#pprint.pformat
# La órden "tail -f logfile.txt" muestra las líneas nuevas a medida que se incorporan al fichero
# sin necesidad de volver a abrirlo.
# Si la (mala) fortuna le ha llevado a disponer de un Windows, instale Cygwin para tener disponible 
# la instrucción tail.
