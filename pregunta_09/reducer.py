#
#! /usr/bin/python3
import sys
import operator
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    curkey = None
    suma=0
    contador=0
    dicc={}

    for line in sys.stdin:

        line=line.split("\n")[0]
        letra,date,value=line.split(",")
        value=int(value)
        dicc[value]=[letra,date]
        resultado=dict(sorted(dicc.items()))       

    for key, value in resultado.items():
        contador+=1
        sys.stdout.write("{}\t{}\t{}\n".format(value[0],value[1],key))
        if contador==6:
           break
                
#
