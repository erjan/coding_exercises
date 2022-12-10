'''
Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.
'''

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.cnt = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, val):
        cur = self.root
        for i in reversed(range(15)):
            bit = val >> i & 1
            cur.nodes[bit].cnt += 1
            cur = cur.nodes[bit]
    
    def count(self, val, high):
        res = 0
        cur = self.root
        for i in reversed(range(15)):
            if not cur:
                break
            bit = val >> i & 1
            cmp = high >> i & 1
            if cmp:
                res += cur.nodes[bit].cnt
                cur = cur.nodes[1^bit]
            else:
                cur = cur.nodes[bit]
        return res
    
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        res = 0
        for num in nums:
            res += trie.count(num, high + 1) - trie.count(num, low)
            trie.insert(num)
        
        return res
      
-------------------------------------------------------------------------------------------------------
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
        
        
class Trie:
    def __init__(self, maxbits=None):
        self.root = TrieNode()
        self.maxbits = maxbits
        
    def add(self, v):
        n = self.root
        # build the trie from the left-most bit
        for i in reversed(range(self.maxbits)):
            node_value = (v >> i) & 1
            n.children[node_value].count += 1
            n = n.children[node_value]
            
    def count(self, v, high):
        cnt = 0
        n = self.root
        for i in reversed(range(self.maxbits)):
            if not n: break
                
            high_at_bit_i = (high >> i) & 1
            v_at_bit_i = (v >> i) & 1
            if high_at_bit_i:  # x could be v_at_bit_i, and possibly 1-v_at_bit_i
                if v_at_bit_i in n.children:
                    cnt += n.children[v_at_bit_i].count
                n = n.children.get(1 - v_at_bit_i, None)
            else:  # x must be v_at_bit_i
                n = n.children.get(v_at_bit_i, None)
                
        return cnt
                

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # determine the max number of bits needed in our trie,
        #    the # of bits for the largest number in nums and high+1, whichever is the greatest
        max_bits = len(bin(max(nums + [high+1]))) - 2
        
        ans = 0
        trie = Trie(max_bits)
        for num in nums:
            ans += trie.count(num, high+1) - trie.count(num, low)  # due to `low <= (nums[i] XOR nums[j]) <= high`
            trie.add(num)
                        
        return ans
