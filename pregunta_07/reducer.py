#! /usr/bin/python3
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    dicc={}
    lista=[]

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        line=line.split("\n")[0]
        letra,date,value=line.split(",")
        dicc[letra,int(value)]=date
    
    sorted_d=dict(sorted(dicc.items()))
    
    for key,date in sorted_d.items():
    	sys.stdout.write("{}   {}   {}\n".format(key[0], date,key[1]))
    	
    
