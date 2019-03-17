import os
from numpy import random

o = open('track.txt', 'w')
p = 0
q = 0
for i in range(100):
    coin = random.choice(['head', 'tail'])
    if coin == 'head':
        os.system("python path_oram.py Maddy_workload_A.txt Output_" + str(i + 1) + ".txt")
        o.write(str(i + 1) + ': Workload_A\n')
        p += 1
    else:
        os.system("python path_oram.py Maddy_workload_B.txt Output_" + str(i + 1) + ".txt")
        o.write(str(i + 1) + ': Workload_B\n')
        q += 1

print(p)
print(q)

o.close()


