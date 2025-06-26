import sys
import numpy as np

g = open("tape20", 'r')
T = sys.argv[1]

lines = g.readlines()

num = lines[1][66:70]

f = open("input_BROADR", 'w')

f.write(f"""broadr 
22 23 21/ 
{num}/
0.001/
{T}./
0/
stop""")
