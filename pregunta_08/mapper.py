#
#
#
#
#
#! /usr/bin/python3
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
        line=line.replace('\n','')
        line=line.replace('   ','')
        vector=line.split('\t')[0]
        letra=vector[0]
        value=vector[11:15]
        sys.stdout.write("{},{}\n".format(letra,value))
#
#
#
