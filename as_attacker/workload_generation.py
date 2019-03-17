import sys
import math
import random

file = sys.argv[1]
o = open(file, "w")

o.write('32\n')

for i in range(50):
    o.write('R' + ' ' + '2' + '\n')

for i in range(50):
    o.write('W' + ' ' + '2' + '\n')

o.close()