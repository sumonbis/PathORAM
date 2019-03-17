import sys
import math
import numpy as np
import random

inFile = sys.argv[1]    # input file 'in.txt'
outFile = sys.argv[2]   # output file 'out.txt'

read_op = list()        # ['W', 'R', 'R', ...]
read_block = list()     # [ 1,   1,   4,  ...]

buffer_r = list() # buffer stores output data
buffer_w = list()

# read input file and store data on the lists
with open(inFile,'r') as f:
    N = int(f.readline().strip()) # total number of blocks
    for line in f.readlines():
        read_op.append(line.strip().split()[0])
        read_block.append(line.strip().split()[1])

L = int(math.ceil(math.log(N, 2)) - 1) # height of the tree
noOfLeafs = int(math.pow(2, L) - 1)
treeSize = int(math.pow(2, L + 1) - 1)
tree = [0] * treeSize
for i in range(1, N + 1):
    tree[i] = i
random.shuffle(tree)
#print(tree)

def readLeaf(branch):
    return int(int(math.pow(2, L)) + int(branch) - 1);

def getParent(node):
    return int(math.floor((node - 1) / 2.0))

def pathNodes(branch):
    path = list()
    for i in range(0, L + 1):
        path.append(branch)
        branch = getParent(branch)
    return list(reversed(path))

def randomPath(node):
    rand = random.randint(0, 1)
    child1 = 2 * node + 1
    child2 = 2 * node + 2
    if (child2 > (treeSize - 1)):
        return int (node - noOfLeafs)

    else:
        if(rand == 0):
            return randomPath(child1)
        else:
            return randomPath(child2)

def readBucket(block):
    buffer_r.append(['R', block])
    return data[block]

def writeBucket(block, new_data):
    buffer_w.append(['W', block])
    data[block] = new_data

posMap = dict((x, random.randint(0, noOfLeafs - 1))
               for x in range(1, N + 1))

for i in range(treeSize):
    block = tree[i]
    if(block != 0):
        posMap[block] = randomPath(i)

stash = list()
stash_data = dict()
data = dict()
for i in tree:              # block 0 has dummy data
    data[i] = random.randint(1000, 10000)

def access(op, block, new_data):
    # 1-2
    x = posMap.get(block)
    posMap[block] = np.random.randint(0, noOfLeafs - 1)

    # 3-5
    leafNode = readLeaf(x)
    path = pathNodes(leafNode)
    for node in path:
        blocks = tree[node]
        stash.append(blocks)
        stash_data[blocks] = readBucket(blocks)

    # 6-9
    if(op == 'W'):
        stash_data[block] = new_data

    # 10-15
    for node in reversed(path):
        n = tree[node]
        writeBucket(n, stash_data.get(n))
        for i in stash:
            if (i == 0):
                stash.remove(i)
                stash_data.pop(i, None)
            else:
                current_branch = posMap.get(i)
                a = pathNodes(current_branch)
                if(node in a):
                    tree[node] = i
                    stash.remove(i)
                    stash_data.pop(i, None)

def writeFile(o):
    buffer = buffer_r + list(reversed(buffer_w))
    for i in buffer:
        o.write(str(i[0]) + ' ' + str(i[1]) + '\n')

o = open(outFile, "w")
unit_test = {}
for i in range (len(read_op)):
    if(read_op[i] == 'R'):
        access(read_op[i], int(read_block[i]), None)
        writeFile(o)

    else:
        access(read_op[i], int(read_block[i]), random.randint(1000, 5000))
        writeFile(o)
    unit_test[read_block[i]] = buffer_r
    buffer = []
    buffer_r = []
    buffer_w = []
o.close()

######  Unit Test   ######
print(unit_test)
