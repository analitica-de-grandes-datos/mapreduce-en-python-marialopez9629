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
        purpose=vector.split(',')[3]
        amount=vector.split(',')[4]        
        sys.stdout.write("{}\t{}\n".format(purpose,amount))
#
