'''
You are given an array nums of positive integers. In one operation, you can choose
any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.
'''

def halveArray(self, A):
    q, s, k, i = [], sum(A), 0, 0
    for x in A:
        heappush(q, -x)
    while s - k > s / 2:
        x = -heappop(q)
        k += x / 2
        heappush(q, -x / 2)
        i += 1
    return i
  
-----------------------------------------------------------------------------------------------
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # Creating empty heap
        maxHeap = []
        heapify(maxHeap) # Creates minHeap 
        
        totalSum = 0
        for i in nums:
            # Adding items to the heap using heappush
            # for maxHeap, function by multiplying them with -1
            heappush(maxHeap, -1*i) 
            totalSum += i
        
        requiredSum = totalSum / 2
        minOps = 0
        
        while totalSum > requiredSum:
            x = -1*heappop(maxHeap) # Got negative value make it positive
            x /= 2
            totalSum -= x
            heappush(maxHeap, -1*x) 
            minOps += 1
        
        return minOps
