from collections import Counter as mset

atk_file = 'enigma.txt'
out_file = open('res.txt', 'w')
o = open('formatted_access_patter.txt', 'w')
rows = []
output = []
op = []
block = []

with open(atk_file,'r') as f:
    for line in f.readlines():
        if (line[0] == '*'):
            continue
        op.append(line.strip()[0])
        block.append(line.strip()[1:])

op = op[1::2]
block = block[1::2]
print(block)
print(len(block))

j = 1
for i in range(0,50000,5):
    o.write('Access ' + str(j) + ': ' +str(block[i:i+5]) + '\n')
    j += 1
    if(j == 101):
        j = 1
        o.write('\n\n*******************************************\n\n')
o.close()

block1 = ['0', '0', '2', '5', '12']
block2 = ['0', '1', '3', '8', '17']

run = 1
for i in range(0,50000,500):
    print(block[i:i+5])
    print(block[i+495:i+500])
    temp1 = block[i:i+5]
    temp2 = block[i+495:i+500]
    print('\n')

    match1 = list((mset(temp2) & mset(block1)).elements())
    match2 = list((mset(temp2) & mset(block2)).elements())
    if(len(match1) >= len(match2)):
        out_file.write('Run ' + str(run) + ': Group A\n')
        block1 = temp2
    else:
        out_file.write('Run ' + str(run) + ': Group B\n')
        block2 = temp2
    run += 1

out_file.close()
