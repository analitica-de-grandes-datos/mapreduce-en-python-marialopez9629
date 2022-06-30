#
#! /usr/bin/python3
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        line=line.replace('\n','')
        vector=line.split('\t')
        clave=vector[0]
        letras=vector[1]
        sys.stdout.write("{}\t{}\n".format(clave,letras))
#
#
