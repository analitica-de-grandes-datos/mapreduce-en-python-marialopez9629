#
#! /usr/bin/python3
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    curkey = {}
    posiciones= []

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        line=line.split("\n")[0]
        clave,letras=line.split("\t")
        letras2=letras.split(',')
        longitud=len(letras2)
        
        for i in range(longitud):
           curkey[letras2[i]]=list(curkey.get(letras2[i],''))+[int(clave)]
        
    dicc=dict(sorted(curkey.items()))
    for key,value in dicc.items():
    	values=sorted(value)
    	values=[str(x) for x in values]
    	values=','.join(values)
    	sys.stdout.write("{}\t{}\n".format(key, values))

#
#
#
#
#
