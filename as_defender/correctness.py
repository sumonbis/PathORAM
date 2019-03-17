import ast

track = 'track.txt'
guessFile = 'guesses.txt'
x = list()

with open(track,'r') as f:
    for line in f.readlines():
        x.append(line.strip().split()[1])

with open(guessFile,'r') as f:
    for line in f.readlines():
        y = ast.literal_eval(line)

match = 0
mismatch = 0
o = open('result.txt', 'w')

for i in range(100):
    if(x[i] == 'Workload_A' and y[i] == 'workload_A.txt'):
        o.write(str(i + 1) + ': Workload_A   ---   matches\n')
        match += 1
    elif(x[i] == 'Workload_B' and y[i] == 'workload_B.txt'):
        o.write(str(i + 1) + ': Workload_B   ---   matches\n')
        match += 1
    else:
        o.write(str(i + 1) + ': ' + str(x[i]) + '   ---   does not match\n')
        mismatch += 1

o.write('Matches: ' + str(match) + ', Mismatches: ' + str(mismatch))
o.close()