#
#
#
#
#! /usr/bin/python3
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    curkey = None
    suma=0
    registros=0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        line=line.split("\n")[0]
        letra,value=line.split(",")
        value=float(value)
        
        if curkey==letra:
           suma+=value
           registros+=1
           promedio=suma/registros
        else:
        
           if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma,promedio))
                
           curkey=letra
           suma=value
           registros=1
           promedio=suma/registros
    
   
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma,promedio))
#
#
#
#
