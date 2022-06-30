#
#! /usr/bin/python3
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:
        vector=line.split('\n')[0]
        datos=vector.split(',')      
        sys.stdout.write("{},{}\n".format(datos[0],datos[1]))
#
