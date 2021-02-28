'''
Given an array of integers nums, sort the array in increasing order based 
on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
'''


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s= collections.Counter(nums)
        
        nums.sort(key = lambda x: (s[x], -x))
        return nums

    
#2nd solution - easier to understand

import collections
def f( nums):
        
    r = collections.Counter(nums).most_common()
    print(r)
    r.sort(key = lambda x: x[0], reverse=True)
    print('after 1st sorting')
    print(r)
    r.sort(key = lambda x: x[1])
    print('after 2nd sorting')
    print(r)
        
    t = []
    for i in r:
        a, b = i
        t.extend([a]*b)
            
    return t
