'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
'''


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def getMedian(window):
            if k % 2 == 0:
                m1 = k // 2
                m2 = k // 2 - 1
                return (window[m1] + window[m2]) / 2
            else: return window[k // 2]

        output = []
        window = []
        l = 0
        for r in range(len(nums)):
            if r - l + 1 <= k:
                window.append(nums[r])
            if r - l + 1 >= k:
                if r - l + 1 > k:
                    # Python's bisect module
                    idx = bisect_left(window, nums[l])
                    window[idx] = nums[r]
                    l += 1
                window.sort()
                output.append(getMedian(window))

        return output
      
-----------------------------------------------------------------------------------------------

import bisect

def medianaordenada(arr):
    d = len(arr)
    pos0 = (d - 1) // 2
    if d%2 == 0:
        return (arr[pos0]+arr[pos0+1])/2
    else:
        return arr[pos0]

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) < k:
            return 0    
        cnt = 0
        roll = sorted(nums[:k])
        md = medianaordenada(roll)
        lmed = [md]

        for i,k in enumerate(nums[k:]):
            del roll[bisect.bisect_left(roll, nums[i])]
            if k >= 2*md:
                cnt+=1
            if k >= md:
                bisect.insort_right(roll, k)
            else:
                bisect.insort_left(roll, k)
            lmed.append(medianaordenada(roll))
        return lmed  
        
