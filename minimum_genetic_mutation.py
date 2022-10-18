'''
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
'''

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(start, 0)])
        
        while q:
            curr_gene, mutations = q.popleft()
            
            if curr_gene == end:
                return mutations
            
            for i in range(8):
                for ch in "ACGT":
                    next_gene = curr_gene[:i] + ch + curr_gene[i+1:]
                    
                    if next_gene in bank:
                        bank.remove(next_gene)
                        q.append((next_gene, mutations + 1))    
        
        return -1
      
--------------------------------------------------------------------------------------
'''
Here we will use BFS.

Firstly insert the starting string in queue.

Check that end string is in bank or not. If not directly return -1.

Go through all the words in bank and check for exactly one dissimilar indeces in bank and append that in queue with the cost+1 (here, limit+1).

If you are not able to reach end string and queue becomes empty then return -1 in Last.

'''
