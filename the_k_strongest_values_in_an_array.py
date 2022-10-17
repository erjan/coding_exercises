'''
Given an array of integers arr and an integer k.

A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the median of the array.
If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].

Return a list of the strongest k values in the array. return the answer in any arbitrary order.

Median is the middle value in an ordered integer list. More formally, if the length of the list is n, the median is the element in position ((n - 1) / 2) in the sorted list (0-indexed).

For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) / 2) = 2. The median is 6.
For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2) = 1. The median is 3.
'''
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        i, j = 0, len(arr) - 1
        median = arr[(len(arr) - 1) // 2]
        while len(arr) + i - j <= k:
            if median - arr[i] > arr[j] - median:
                i = i + 1
            else:
                j = j - 1
        return arr[:i] + arr[j + 1:]
      
--------------------------------------------------------------------
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = sorted(arr[(len(arr)-1)//2])
        return sorted(array, key=lambda x:(abs(x-med),x))[-k:]
      
-----------------------------------------------------------------------------
def getStrongest(self, arr: List[int], k: int) -> List[int]:
    arr.sort(reverse = True) # sort the arr in descending order, this will put the larger number at first if they have same distance to the median
    m_index = len(arr) - (len(arr)-1)//2 - 1 # median index in reversely sorted arr
    m = arr[m_index]
    arr.sort(key = lambda x: abs(x-m), reverse = True) # sorted the arr again by absolute distance 
    return arr[:k]
  
----------------------------------------------------------------------------------------------------------
# Idea- Strongest value are willing to realy on boundary either side, and then inward with decreasing intesity.
# Steps to solve
# Sort, get median, and assign lastPointer, startPointer
# compare lastPointer's element with startPointer's element, then add accordingly
# only iterate loop for k, because elements in start and last with range of k, have Strongest value

# OR
# Explaination(hindi lang.)- https://www.youtube.com/watch?v=mvbTN2I3HxY

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        lastPointer = -1
        startPointer = 0
        mInd = (len(arr)-1)//2
        m = arr[mInd]
        res = []
        for i in range(k):
            if abs(arr[lastPointer] - m) >= abs(arr[startPointer] - m):
                res.append(arr[lastPointer])
                lastPointer -= 1
            else:
                res.append(arr[startPointer])
                startPointer += 1
        return res
