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
        mes=vector[6:8]
        sys.stdout.write("{}\n".format(mes))
