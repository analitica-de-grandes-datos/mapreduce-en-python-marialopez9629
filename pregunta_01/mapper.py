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
        cred_his=vector.split(',')[2]
        sys.stdout.write("{}\t1\n".format(cred_his))
#
