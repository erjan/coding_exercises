'''
You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
Return the number of pairs that satisfy the conditions.
'''

class segment_tree:
  
  def __init__(self, arr):
    self.len_ = len(arr)
    
    self.data_ = [0] * (self.len_ * 2)
    
    for t in range(self.len_, self.len_ * 2, 1):
        self.data_[t] = arr[t - self.len_]
      
    for t in range(self.len_-1, -1, -1): 
        self.data_[t] = self.data_[t * 2] + self.data_[t * 2 + 1]
  
  def update(self, index, target):
    self.data_[index + self.len_] = target
    
    start = index + self.len_
    start = start // 2
    
    while start >= 1:
        self.data_[start] = self.data_[start*2] + self.data_[start*2+1]
        start = start // 2
  
  def query(self, left, right):
    left += self.len_
    right += self.len_
    
    res = 0
    
    while left < right:
        if left & 1:
            res += self.data_[left]
            left += 1
        if right & 1:
            right -= 1
            res += self.data_[right]
        left = left // 2
        right = right //2
      
    return res

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        data = [ x-y for (x,y) in zip(nums1, nums2)]
        
        data2 = [(data[i] + diff, i) for i in range(len(data))]
         
        data2.sort(key = lambda x : x[0])
                
        st = segment_tree([1 for x in range(len(data2))])
        
        lookup = {}
        
        for t in range(len(data2)):
            lookup[data2[t][1]] = t 
            
        data3 = [x[0] for x in data2]
        
        res = 0
        
        n = len(data)
        
        for i in range(len(data)):
            element = data[i]
            index = bisect.bisect_left(data3, element)
            index2 = lookup[i]
            st.update(index2, 0)
            if index < n:
                res += st.query(index, n)
        return res
      
---------------------------------------------------------------------------------------------------------
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl, ans = SortedList(), 0
        for num1, num2 in zip(nums1, nums2):
            ans += sl.bisect_right(num1 - num2 + diff)
            sl.add(num1 - num2)
        return ans
