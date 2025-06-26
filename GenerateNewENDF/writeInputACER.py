import sys
import numpy as np

def writeInputACER():
    g = open("tape20", 'r')

    lines = g.readlines()

    num = lines[1][66:70]

    f = open("input_ACER", 'w')

    f.write(f"""acer 
    22 21 0 31 32/ 
    1 0 1/ 
    'ENDF/B-VIII.1'/ 
    {num} 0/ 
    / 
    / 
    stop""")
