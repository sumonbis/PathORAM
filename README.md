# PathORAM
Path ORAM is a simple oblivious RAM algorithm. While using cloud platform or any other insecure memory, attack can be made using the access pattern. Oblivious RAM is the way to hide the memory access pattern with some extra bandwidth and memory overhead.

## Path Oram Implementation
Path ORAM uses a binary tree to store all memory blocks. Each node of the tree is
a bucket which can contain a fixed number of block. First, we define all necessary data
structure. The depth of the tree is `ceiling(log N)`. The empty blocks are filled with dummy
data. Each leaf node is a distinct branch and each block is mapped to a random branch.
For each operation, we perform read and write through the branch. Since, the blocks
are positioned to different branches, repeated operations do not disclose any information. A
local memory is used to read and re-write the data. Path ORAM uses limited amount of
memory and bandwidth with respect to other oblivious algorithms. This is an implementation described in the following paper: https://people.csail.mit.edu/devadas/pubs/PathORam.pdf

## Security
Path ORAM changes the location of block repeatedly and accesses the whole branch for
a single block. Therefore, the pattern of access is always random. However, the security is
dependent mostly on the random branch selection of the blocks. We used python package
numpy to obtain uniformly distributed random integer.

## Performance
For each access, we go through the whole path twice, once for reading and again for writing.
So, we need to access twice the depth of the tree. Since, depth is `ceiling(log N)`, the performance
also sticks to that.

## Unit Test
The correctness holds because the path we access includes the intended block. And after
each access the block is remapped to another branch so that access to same block does not
repeat the same set of blocks.


## How to Run
### Command Line

- python `path_oram.py <input_file> <output_file>`

- Example run: `path_oram.py in.txt out.txt`
