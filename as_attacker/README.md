# Attack 

In this section, I have generated two workloads (Workload A and Workload B) for the user and I will break the security. Each contains 100 lines of access. Workload A contains access to only block 1 repeatedly. Workload B does the same with block 2. Therefore, if not randomised properly there should be some pattern of access.

After receiveing the hundred runs (enigma.txt), First I have formatted the result and then
tried to find pattern. Path oblivious ram randomise the location of each block over the
path of the tree. So, the twist of breaking the semantic security lies in the randomisation
function (in this case Random class of Java). Rather, I tried to match the access path of
two sequential runs.

## attack.py

Since it specified 32 total blocks, the height of the tree was 5. I formatted each 5 blocks
and comared the last path accessed with the first path of the next run. Here I assumed that
the runs are sequential. So, if it is accessing the same block then the two paths should be
similar. For the first guess, I randomly choosen one workload.

If the path oblivious RAM implementation did not use the stash properly to swap elements
between the consecutive path access then there should be a similar path in the next run.
Then the correctness could be either more than 50% or near 0%. Note that either can leak
information significantly.