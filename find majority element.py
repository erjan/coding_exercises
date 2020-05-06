#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

#You may assume that the array is non-empty and the majority element always exist in the array.

#solution 1
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
        
        
#solution 2

def majorityElement(self, nums: List[int]) -> int:
       
        d = dict()
        result = -1
        half = len(nums)/2
        for num in nums:
            if num in d.keys():
                d[num]+=1
            else:
                d[num]=1

        for k in d.keys():
            if d[k] >= half:
                result = k
                break

        print(result)
        return result   
