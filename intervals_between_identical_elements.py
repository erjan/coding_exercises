'''
You are given a 0-indexed array of n integers arr.

The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].

Note: |x| is the absolute value of x.
'''

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
        # make a dict to save indices
        idces = collections.defaultdict(list)
        
        # search for all common numbers and make the computations
        for idx, num in enumerate(arr):
            
            # check whether we already found one
            idces[num].append(idx)
        
        # go through all of the numbers and calculate the sums
        for ls in idces.values():
            
            # make the prefix sum
            prefix = [ls[0] for _ in ls]
            n = len(ls)
            for idx, num in enumerate(ls[1:], 1):
                prefix[idx] = prefix[idx-1] + num
            
            # calculate the result
            for idx, num in enumerate(ls):
                
                # get the left part (current index - sum before the index)
                left = 0
                if idx > 0:
                    left = idx*num - prefix[idx-1]
                
                # get the right part (sum after the index, minus current index)
                right = 0
                if idx < n-1:
                    right = prefix[-1] - prefix[idx] - (n-1-idx)*num
                    
                arr[num] = left + right
        return arr
