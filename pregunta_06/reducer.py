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
    maxi = 0
    mini = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        line=line.split("\n")[0]
        letra,value=line.split(",")
        value=float(value)
        
        if curkey==letra:
           if value>maxi:
              maxi=value
           elif value<mini:
              mini=value
        else:
        
           if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi,mini))
                
           curkey=letra
           mini=value
           maxi=value
    
   
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maxi,mini))
#
#
#
