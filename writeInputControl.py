import sys
import numpy as np

g = open("tape20", 'r')

lines = g.readlines()

num = lines[1][66:70]

f = open("input_CONTROL", 'w')

f.write(f"""reconr
 +20 +21 /
 'generate angular distribution'/
 {num} 0 0 /
 0.01 /
 0 /\n""")

f.write(f"""acer 
20 21 0 31 32/ 
1 0 1/ 
'ENDF/B-VIII.1'/ 
{num} 0/ 
/ 
/ 
stop""")
