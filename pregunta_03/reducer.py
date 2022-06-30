#
#! /usr/bin/python3
import sys
import operator
from functools import reduce
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    curkey = {}
    maximo = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split(",")
        val = int(val)
        curkey[key]=val
    
    sorted_d = dict(sorted(curkey.items(), key=operator.itemgetter(1)))
    
    for key,val in sorted_d.items():
        sys.stdout.write("{},{}\n".format(key, val))
#
