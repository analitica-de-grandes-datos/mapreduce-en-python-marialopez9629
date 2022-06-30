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
        letra=vector[0]     
        sys.stdout.write("{}\n".format(letra))
#
