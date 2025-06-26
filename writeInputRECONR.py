import sys
import numpy as np

def writeInputRECONR():
    g = open("tape20", 'r')

    lines = g.readlines()

    num = lines[1][66:70]

    f = open("input_RECONR", 'w')

    f.write(f"""reconr
     +20 +21 /
     'generate angular distribution'/
     {num} 0 0 /
     0.01 /
     0 /
    stop""")
