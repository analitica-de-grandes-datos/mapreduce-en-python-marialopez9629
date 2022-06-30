#
#! /usr/bin/python3
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    curkey = None
    total = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        letra= line.split("\n")[0]
        
        if curkey==letra:
           total+=1
        else:
        
           if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                sys.stdout.write("{},{}\n".format(curkey, total))
                
           curkey=letra
           total=1
    
    #sorted_d = dict(sorted(curkey.items(), key=operator.itemgetter(1)))
    
    #for key,val in sorted_d.items():
    sys.stdout.write("{},{}\n".format(curkey, total))
#
