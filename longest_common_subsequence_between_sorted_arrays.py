'''
Given an array of integer arrays arrays where each arrays[i] is sorted in strictly increasing order, return an integer array representing the longest common subsequence between all the arrays.

A subsequence is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.
'''


class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        data={}
        n=len(arrays)
        for idx in range(n):
            for ele in arrays[idx]:
                if ele not in data:
                    data[ele]=0
                data[ele]+=1
        return [i for i in data.keys() if data[i]==n]
---------------------------------------


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        
        def common(x, y):
            m, n = len(x), len(y)
            i, j = 0, 0
            res = []
            while i < m and j < n:
                if x[i] == y[j]:
                    res.append(x[i])
                    i += 1
                    j += 1
                elif x[i] > y[j]:
                    j += 1
                else:
                    i += 1
            
            return res
            
        ans = arrays[0]
        for i in range(1, len(arrays)):
            ans = common(ans, arrays[i])
        return ans
      
---------------------------------
class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        return sorted(set.intersection(*[set(num) for num in arrays]))
      
------------------------------------------------------
The logic

We count all the numbers in all the arrays and store each number's count in a hash-table. For a number to be part of the common subsequence, it has to have a count == length of the array

Why does this work?

Cause the sequence is strictly increasing; which also means there are no duplicates in any of the arrays

def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
    al = len(arrays)
    dict_c = defaultdict(int)
    for array in arrays:
        for a in array:
            dict_c[a] += 1
    op = []
    for key, value in dict_c.items():
        if value == al:
            op.append(key)
    return sorted(op)
  
---------------------------------------------------------------------
Check each element of every array to see if it is part of the ongoing set subsequence; if so, add it to a temporary set. At the end of that array, our new current set is the previous temporary set. This removes all values from the subsequence that are no longer satisfactory after looking at the previous array. Return the result of sorting the final set.

Running through each element and checking if it's part of the "ret" set is O(n*m) for n arrays of maximal length m and the final sort at the end is at worst O(log(m)), worse for longer final subsequences.

Time efficiency: O(n*m)
Space efficiency: O(m)

class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ret, tmp = set(), set()
        for i in arrays[0]:
            ret.add(i)
        for arr in arrays[1:]:
            for elem in arr:
                if elem in ret:
                    tmp.add(elem)
            ret = tmp.copy()
            tmp.clear()
        return sorted(ret)
  
      
